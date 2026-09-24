## RFM案例

* 导包

  ```python
  # 导包
  import time
  import numpy as np 
  import pandas as pd
  from sqlalchemy import create_engine
  from pyecharts.charts import Bar3D              # 需要安装下, 即: pip install pyecharts
  from pyecharts.commons.utils import JsCode
  import pyecharts.options as opts
  
  # 改变相对路径. 
  import os
  os.chdir(r'D:\workspace\ai_22_work_bj\pandasProject\day05')
  ```

* 读取数据

  ```python
  # 1. 定义变量, 记录表名. 
  sheet_names = ['2015', '2016', '2017', '2018', '会员等级']
  
  # 2. 读取上述的excel表, 获取到数据, 结果是: 字典类型,  键: Excel表名, 值: 该表的数据封装成的DataFrame对象.
  sheet_dict = pd.read_excel('./data/sales.xlsx', sheet_name=sheet_names)
  sheet_dict      # {'2015': df对象, '2016': df对象, '2017': df对象, '2018': df对象, '会员等级': df对象, }
  
  # 3. 查看上述数据的 类型.
  print(type(sheet_dict))     # <class 'dict'>
  
  # 4. 从字典中 获取 2015表 的数据.
  sheet_dict['2015']
  
  # 5. 查看 2015表数据的 详细信息. 
  sheet_dict['2015'].info()
  
  # 6. 查看 2015表数据的 统计信息.
  sheet_dict['2015'].describe()
  
  # 7. 查看 2016表数据的 详细信息. 
  sheet_dict['2016'].info()
  
  # 8. 查看 各表的 详细信息, 统计信息. 
  for i in sheet_names:
      print(sheet_dict[i])
      sheet_dict[i].info()
      sheet_dict[i].describe()
  ```

* 数据的预处理

  ```python
  # 1. 处理缺失值, 过滤掉不合法的数据, 新增: max_year_date列
  # 1.1 遍历, 获取到前4张表, 即: 2015 ~ 2018年的所有表数据.
  for i in sheet_names[:-1]:
      # 1.2 处理缺失值, 方案: 删除.
      sheet_dict[i] = sheet_dict[i].dropna()
      # 1.3 过滤出合法值, 即: 金额在1元以上的订单.
      sheet_dict[i] = sheet_dict[i][sheet_dict[i]['订单金额'] > 1]
      # 1.4 新增1列, 用于表示: 固定时间(统计时间)
      sheet_dict[i]['max_year_date'] = sheet_dict[i]['提交日期'].max()
      
      
  # 2 查看处理后的数据信息. 
  for i in sheet_names:
      print(sheet_dict[i].info())        # 表的详细信息
      print(sheet_dict[i].describe())    # 表的统计信息
      
      
  # 3. 合并数据集, 获取到最终的处理后的 DataFrame对象.
  # 3.1 获取到前4张表的数据, 拼接成新的DataFrame对象.
  data_merge = pd.concat(list(sheet_dict.values())[:-1], ignore_index=True)
  
  # 3.2 给表新增1列: 年.
  data_merge['year'] = data_merge['max_year_date'].dt.year
  
  # 3.3 给表新增1列 date_interval, 表示: 购买商品的间隔时间, 即: max_year_date - 提交日期
  data_merge['date_interval'] = data_merge['max_year_date'] - data_merge['提交日期']
  # 3.4 把上述的时间间隔, 转成对应的 天数(数值)
  data_merge['date_interval'] = data_merge['date_interval'].dt.days
  # 3.5 查看最终合并后的结果.
  data_merge
  ```

* 数据统计->分析

  ```python
  # 1. 按照 year, 会员ID分组, 分别计算: r(最近购买时间), f(频次), m(金额)三项的 原始数据.
  rfm_gb = data_merge.groupby(['year', '会员ID'], as_index=False).agg({
      'date_interval': 'min',         # 间隔时间的最小值 -> r(recency)
      '订单号': 'count',               # 购买频次的数量 -> f(frequency)
      '订单金额': 'sum'                # 购买金额的和 -> m(monetary)
  })
  
  # 2. 修改列名.
  rfm_gb.columns = ['year', '会员ID', 'r', 'f', 'm']
  rfm_gb
  
  
  # 3. 因为使用的是三分法, 所以需要确定4个值, 才能划分: 3个区间. 自定义区间即可.
  # 3.1 查看 r, f, m的 分位数. 
  rfm_gb.iloc[:, 2:].describe().T
  
  # 3.2 自定义区间.
  r_bins = [-1, 79, 255, 365]
  f_bins = [0, 2, 5, 130]
  m_bins = [0, 69, 1199, 206252]
  
  
  # 4. 具体的划分区间的动作, 获取 r, f, m三项的 具体评分. 
  # 场景1: 演示 自动划分区间, 即: 给定区间数, 由Pandas自动划分区间.
  pd.cut(rfm_gb['r'], bins=3).unique()        # Categories类型: [(-0.365, 121.667], (121.667, 243.333], (243.333, 365.0]]
  
  # 场景2: 演示 自定义区间, 即: 我们给定数字, 由Pandas进行具体的划分.
  pd.cut(rfm_gb['r'], bins=r_bins).unique()   # Categories类型: [(-1, 79], (79, 255], (255, 365]]
  
  # 场景3: 自定义区间 + 评分.
  pd.cut(rfm_gb['r'], bins=r_bins, labels=[3, 2, 1])      # 可以, 但是不推荐, 因为值写死了. 
  pd.cut(rfm_gb['f'], bins=f_bins, labels=[1, 2, 3])      # 可以, 但是不推荐, 因为值写死了. 
  pd.cut(rfm_gb['m'], bins=m_bins, labels=[1, 2, 3])      # 可以, 但是不推荐, 因为值写死了. 
  
  # 场景4: 最终版, 自定义区间 + 评分(结合区间值 列表的长度获取)
  # r(Recency): 最后一次购买的时间, 越小越好, 评分是: 3, 2, 1
  rfm_gb['r_label'] = pd.cut(rfm_gb['r'], bins=r_bins, labels=[i for i in range(len(r_bins) - 1, 0, -1)]) # range(3, 0, -1) -> [3, 2, 1]    
  # f(Frequency): 购买频次, 越大越好, 评分是: 1, 2, 3
  rfm_gb['f_label'] = pd.cut(rfm_gb['f'], bins=f_bins, labels=[i for i in range(1, len(f_bins))]) # range(1, 4) -> [1, 2, 3]    
  # m(Monetary): 购买金额, 越大越好, 评分是: 1, 2, 3
  rfm_gb['m_label'] = pd.cut(rfm_gb['m'], bins=m_bins, labels=[i for i in range(1, len(m_bins))]) # range(1, 4) -> [1, 2, 3]    
  rfm_gb
  
  
  # 5. 获取具体的 用户分群结果值. 
  # 思路1: 加权, r_lable * 权重 + f_label * 权重 + m_label * 权重
  # 例如: r_label * 0.2 + f_label * 0.3 + m_label * 0.5
  
  # 思路2: 拼接思路 即: r_label + f_label + m_label -> 字符串类型. 
  rfm_gb['r_label'] = rfm_gb['r_label'].astype(str)
  rfm_gb['f_label'] = rfm_gb['f_label'].astype(str)
  rfm_gb['m_label'] = rfm_gb['m_label'].astype(str)
  
  rfm_gb['rfm_group'] = rfm_gb['r_label'] + rfm_gb['f_label'] + rfm_gb['m_label']
  rfm_gb
  ```

* 保存分析结果

  ```python
  # 1. 保存结果到 -> Excel表.
  rfm_gb.to_excel('./data/sale_rfm_group.xlsx', index=False)
  print('导出信息到Excel表 成功!')
  
  
  # 2. 保存结果到 -> Excel表, 例如: rfm_db数据库,  rfm_score 表.
  # 2.1 创建引擎对象.
  engine = create_engine('mysql+pymysql://root:123456@localhost:3306/rfm_db?charset=utf8')
  engine
  
  
  # 2.2 导出数据到MySQL表中.
  # 场景1: 导出指定字段.
  # rfm_gb[['year', '会员ID', 'rfm_group']].to_sql('rfm_score', engine, index=False, if_exists='replace')
  
  # 场景2: 导出所有字段. 
  rfm_gb.to_sql('rfm_score', engine, index=False, if_exists='replace')
  print('导出数据到MySQL表 成功!')
  
  
  # 2.3 查看导出后的结果, 即: 从SQL表中读取数据.
  pd.read_sql('select * from rfm_score limit 100;', engine)
  pd.read_sql('select count(1) from rfm_score;', engine)
  ```

* 数据可视化

  ```python
  # 1. 按照 用户分群类型(rfm_group), 年份分组, 统计会员总数. 
  # 思路1: value_counts()
  # rfm_gb.groupby(['rfm_group', 'year'])['会员ID'].value_counts()
  
  # 思路2: groupby() + 聚合函数.
  display_data = rfm_gb.groupby(['rfm_group', 'year'], as_index=False).agg({'会员ID': 'count'})
  # 修改列名.
  display_data.columns = ['rfm_group', 'year', 'number']
  # 修改 rfm_group的类型为 int类型.
  display_data['rfm_group'] = display_data['rfm_group'].astype(int)
  # 查看最终结果.
  display_data
  
  
  
  # 2. 可视化, 显示图形
  
  # 颜色池
  range_color = ['#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf',
                 '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']
  
  range_max = int(display_data['number'].max())
  c = (
      Bar3D()#设置了一个3D柱形图对象
      .add(
          "",#图例
          [d.tolist() for d in display_data.values],#数据
          xaxis3d_opts=opts.Axis3DOpts(type_="category", name='分组名称'),#x轴数据类型，名称，rfm_group
          yaxis3d_opts=opts.Axis3DOpts(type_="category", name='年份'),#y轴数据类型，名称，year
          zaxis3d_opts=opts.Axis3DOpts(type_="value", name='会员数量'),#z轴数据类型，名称，number
      )
      .set_global_opts( # 全局设置
          visualmap_opts=opts.VisualMapOpts(max_=range_max, range_color=range_color), #设置颜色，及不同取值对应的颜色
          title_opts=opts.TitleOpts(title="RFM分组结果"),#设置标题
      )
  )
  c.render() 		      # 数据保存到本地的网页中.
  # c.render_notebook() #在notebook中显示
  ```



## 扩展_Pandas绘图

* 需求1

  ```python
  import pandas as pd
  import seaborn as sns               # 底层依赖 Matplotlib 
  import matplotlib.pyplot as plt
  
  plt.rcParams['font.sans-serif'] = ['SimHei']
  plt.rcParams['axes.unicode_minus'] = False
  
  
  # 1. 加载数据源, 获取到 df对象.
  df = pd.read_csv('./data/winemag-data_first150k.csv', index_col=0)
  df
  
  
  # 需求1: 绘制图形, 展示 产葡萄酒最多的10个产地的信息. 
  # 方式1: 使用 groupby()方法.
  df.groupby('province')['province'].count().sort_values(ascending=False).head(10)
  
  # 方式2: value_counts()  统计每个值的次数, 等价于: groupby()方法 + 聚合count() + 排序(默认: 降序)
  df['province'].value_counts().head(10)
  
  # 对上述结果进行可视化, 采用 Pandas自带的 绘图方式. 
  # df['province'].value_counts().head(10).plot()                 # 折线图.
  
  # 柱状图
  text_kwargs = dict(fontsize=15, figsize=(10, 6), color=['r', 'g', 'b', 'y', 'c', 'm', 'k', 'pink', 'gray', 'orange'])
  # print(text_kwargs)      # {'fontsize': 15, 'figsize': (10, 6), 'color': ['r', 'g', 'b', 'y', 'c', 'm', 'k', 'pink', 'gray', 'orange']}
  
  df['province'].value_counts().head(10).plot.bar(**text_kwargs)
  ```

* 需求2

  ```python
  # 需求2: 展示 产葡萄酒最多的10个产地的 占比.
  (df['province'].value_counts().head(10) / len(df)).plot.bar(**text_kwargs)
  ```

* 需求3

  ```python
  # 需求3: 展示 每个评分的葡萄酒种类(个数) 
  # df['points'].value_counts().sort_index().plot.bar(**text_kwargs)          # 柱状图
  
  # 如果是固定值的数据, 不是分类性的, 可以直接使用: 折线图显示. 
  # df['points'].value_counts().sort_index().plot.line(**text_kwargs)          # 折线图
  df['points'].value_counts().sort_index().plot.area(**text_kwargs)            # 面积图 = 把折线图的空白填充成颜色即可.
  ```



## 扩展_Seaborn绘图

* 读取数据

  ```python
  # 1. 读取数据, 获取df对象. 
  # df = pd.read_csv('./data/tips.csv')
  df = sns.load_dataset('tips')       # 加载Seaborn包自带的 内置数据集, 前提: 电脑要联网.
  df
  ```

* 直方图

  ```python
  # seaborn的绘图, 基本上都是:  图形名 + plot()即可.
  # 例如: Pandas中 直方图叫 hist(), seaborn中 直方图叫 histplot()
  # 2. 绘制图形, 展示 每天 男女 总账单的情况.
  # 计数柱状图, data: 要操作的df对象, x: 绘制的列名, hue: 分组列名.
  # sns.countplot(data=df, x='day', hue='sex')
  
  # 3. 绘制图形, 展示 男女 总账单的情况.
  fig, ax = plt.subplots(figsize=(10, 6))
  
  # 直方图, data: 要操作的df对象, x: 绘制的列名, hue: 分组列名.
  sns.histplot(data=df, x='total_bill', hue='sex')
  
  ax.set_title('男女总账单分布情况', fontsize=20)
  plt.show()
  ```

* 散点图

  ```python
  # 需求: 描述 总账单金额 和 小费的分布情况(关系图) -> 散点图
  # x轴 -> 总账单金额, y轴 -> 小费金额.
  fig, ax = plt.subplots(figsize=(10, 6))
  # 参1: 要操作的df对象, x: 总账单金额, y: 小费金额.
  sns.scatterplot(data=df, x='total_bill', y='tip', hue='sex')
  ax.set_title('总账单金额 和 小费金额 的关系图', fontsize=20)
  plt.show()
  ```

  ```python
  fig, ax = plt.subplots(figsize=(10, 6))
  # 参1: 要操作的df对象, x: 总账单金额, y: 小费金额.
  sns.regplot(data=df, x='total_bill', y='tip')       # 会绘制1条拟合回归线, 默认是线性回归.
  ax.set_title('总账单金额 和 小费金额 的关系图', fontsize=20)
  plt.show()
  ```

  ```python
  # 参1: 要操作的df对象, x: 总账单金额, y: 小费金额.
  # sns.jointplot(data=df, x='total_bill', y='tip', kind='reg')       # 会绘制1条拟合回归线, 默认是线性回归.
  sns.jointplot(data=df, x='total_bill', y='tip', kind='hex')         # kind='hex' -> 蜂巢图
  ax.set_title('总账单金额 和 小费金额 的关系图', fontsize=20)
  plt.show()
  ```

* 箱线图

  ![1743521875833](assets/1743521875833.png)

  ```python
  # 参1: 要操作的df对象, x: 时间(午餐, 晚餐), y: 账单总金额.
  # 箱线图.
  sns.boxplot(data=df, x='time', y='total_bill')         # kind='hex' -> 蜂巢图
  plt.show()
  ```

* 小提琴图

  ```python
  # 参1: 要操作的df对象, x: 时间(午餐, 晚餐), y: 账单总金额.
  # 小提琴图.
  sns.violinplot(data=df, x='time', y='total_bill', hue='sex', split=True)         # kind='hex' -> 蜂巢图
  plt.show()
  ```



