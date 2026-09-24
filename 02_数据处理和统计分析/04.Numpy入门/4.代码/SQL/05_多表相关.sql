# ------------------------ 案例1: 多表建表之 一对多(理解即可) ------------------------
# 需求: 新建部门表(dept, department) 和 员工表(emp), 他们之间是 一对多的关系, 请用外键约束, 完成限定.
# 细节: 实际开发中, 外键约束相对用的少一点, 而是通过 代码层面, 对表数据做限定.
# 记忆: 多表关系中, 有外键列的表 -> 外表(从表), 有主键列的表 -> 主表,  外表的外键列 不能出现 主表的主键列 没有的数据.
# 回顾: 一对多建表原则, 在多的一方新建1列, 充当外键列, 去关联一的一方的主键列.

# 1. 切库, 查表.
use day02;
show tables;

# 2. 创建 主表 -> 部门表.
create table dept(
    id int primary key auto_increment,  # 部门id
    name varchar(10)                    # 部门名
);

# 3. 创建 外表 -> 员工表.
create table emp(
    id int primary key auto_increment,  # 员工id
    name varchar(10),       # 员工姓名
    salary double,          # 员工工资
    dept_id int             # 员工所属的部门id
    # 设置外键约束的方式1: 建表时添加 外键约束, 注意: 写到 外表中.
    # 格式: [constraint 外键约束名] foreign key(外键列名) references 主表名(主键列名)
    , constraint fk_dept_emp foreign key(dept_id) references dept(id)
);

# 4. 给部门表添加数据.
insert into dept values(null, '人事部'), (null, '财务部'), (null, '研发部'), (null, '行政部');

# 5. 给员工表添加数据.
insert into emp values(null, '胡歌', 33333, 1);   # 可以
insert into emp values(null, '刘亦菲', 22222, 2); # 可以
insert into emp values(null, '迪丽热巴', 11111, 2); # 可以
insert into emp values(null, '水冷哥', 11.1, 3);    # 可以
insert into emp values(null, '坤哥', 66666, 10);    # 不可以, 外表的外键列不能出现主表的主键列没有的数据.

# 6. 查看表数据.
select * from dept;
select * from emp;

# 7. 删除外键约束.
# 格式: alter table 外表名 drop foreign key 外键约束名;
alter table emp drop foreign key fk_dept_emp;

# 8. 建表后, 添加外键约束, 前提: 表数据之间必须是合法的.
# 格式: alter table 外表名 add [constraint 外键约束名] foreign key(外键列名) references 主表名(主键列名);
alter table emp add foreign key(dept_id) references dept(id);



# ---------------------- 案例2: 多表查询 准备数据 ----------------------
# 1. 创建hero表
create table hero (
    hid   int primary key auto_increment,   # 英雄id
    hname varchar(255),                     # 英雄名
    kongfu_id int                           # 功夫id
);
# 2. 创建kongfu表
create table kongfu (
    kid     int primary key auto_increment, # 功夫id
    kname   varchar(255)                    # 功夫名
);
# 3. 添加表数据.
# 插入hero数据
insert into hero values(1, '鸠摩智', 9),(3, '乔峰', 1),(4, '虚竹', 4),(5, '段誉', 12);
# 插入kongfu数据
insert into kongfu values(1, '降龙十八掌'),(2, '乾坤大挪移'),(3, '猴子偷桃'),(4, '天山折梅手');
# 4. 查看表数据.
select * from hero;
select * from kongfu;


# ---------------------- 案例3: 多表查询 交叉连接(cross join) ----------------------
# 格式1: select * from 表名1, 表名2;
# 格式2: select * from 表名1 join 表名2;
# 查询结果 = 两张表的笛卡尔积, 即: 表A的总条数 * 表B的总条数, 会产生大量的脏数据, 实际开发一般不用.
select * from hero, kongfu;
select * from hero join kongfu;



# ---------------------- 案例4: 多表查询 内连接(inner join) ----------------------
# 查询结果: 表的交集.
# 隐式内连接.
# 格式1: select * from 表1, 表2 where 关联条件;
select * from hero as h, kongfu as kf where h.kongfu_id = kf.kid;   # 标准写法.
select * from hero, kongfu where kongfu_id = kid;                   # as可以省略, 因为没有重名字段, 数据表.字段名 可以直接写为 字段名

# 显式内连接(推荐使用, 效率高)
# 格式2: select * from 表1 inner join 表2 on 关联条件;      # 细节: inner可以省略不写.
select * from hero as h inner join kongfu as kf on h.kongfu_id = kf.kid;
select * from hero as h join kongfu as kf on h.kongfu_id = kf.kid;



# ---------------------- 案例5: 多表查询 外连接(outer join) ----------------------
# 场景1: 左外连接, 查询结果 = 左表的全集 + 交集.
# 格式: select * from 表1 left outer join 表2 on 关联条件;      # outer可以省略不写.
select * from hero h left outer join kongfu kf on h.kongfu_id = kf.kid;
select * from hero h left join kongfu kf on h.kongfu_id = kf.kid;       # 效果同上, outer可以省略不写.

# 场景2: 右外连接, 查询结果 = 右表的全集 + 交集.
# 格式: select * from 表1 right outer join 表2 on 关联条件;      # outer可以省略不写.
select * from hero h right outer join kongfu kf on h.kongfu_id = kf.kid;
select * from hero h right join kongfu kf on h.kongfu_id = kf.kid;      # 效果同上, outer可以省略不写.

# 场景3: 满外连接(全连接), 查询结果 = 左外链接 + 右外连接的结果.
# 格式: select * from 表1 full outer join 表2 on 关联条件;      # outer可以省略不写.    格式如此, 但是MySQL不支持full outer join写法
# select * from hero h full outer join kongfu kf on h.kongfu_id = kf.kid;

# 我们可以用 union 关键字 把 左外连接 和 右外连接的结果 合并到一起, 形成 满外连接的效果.
select * from hero h left join kongfu kf on h.kongfu_id = kf.kid        # 左外连接
# union distinct  # 合并, 并去重, 细节: distinct可以省略不写.
# union
union all         # 合并, 不去重.
select * from hero h right join kongfu kf on h.kongfu_id = kf.kid;      # 右外连接


# ---------------------- 案例6: 多表查询 子查询 ----------------------
/*
概述:
    一个SQL语句的查询条件, 需要依赖另1个SQL语句的查询结果, 这种写法就叫: 子查询.
    外表的查询叫: 父查询(主查询), 里边的查询叫: 子查询.
写法:
    select * from 表名 where 字段 = (select 字段 from 表名 where ...);
*/
# 需求: 查询价格最高的商品的信息, 只要 商品名, 价格, 分类id即可.
# step1: 查找商品最高的 单价.
select max(price) from product;

# step2: 查找单价最高的 商品信息.
# select * from product where price = 5000;
select * from product where price = 5000;

# 合并版: 子查询.
#             主查询(父查询)                        子查询
select * from product where price = (select max(price) from product);

# 实际开发写法, 连接查询.
select
    *
from
    product p
join
    (select max(price) price from product) t1
on
    p.price = t1.price;


# 自关联查询
# 窗口函数



# SQL练习题-北风34



# case when语法
select * from product;

/*
格式1: 通用写法.
    case
        when 条件1 then 结果1
        when 条件2 then 结果2
        ...
        else 结果n
    end [as 别名]

格式2: 针对于格式1的语法糖, 要满足两点 -> 1.都是操作同1个字段.  2.都是等于的判断.
    case 字段名
        when 值1 then 结果1
        when 值2 then 结果2
        ...
        else 结果n
    end [as 别名]
 */
# 需求: c001 -> 电脑, c002 -> 服装, c003 -> 化妆品, c004 -> 零食, c005 -> 饮料, null -> 未知类别
select
    *,
    case
        when category_id = 'c001' then '电脑'
        when category_id = 'c002' then '服装'
        when category_id = 'c003' then '化妆品'
        when category_id = 'c004' then '零食'
        when category_id = 'c005' then '饮料'
        else '未知类别'
    end as category_name
from
    product;

# 上述格式可以简化为
select
    *,
    case category_id
        when 'c001' then '电脑'
        when 'c002' then '服装'
        when 'c003' then '化妆品'
        when 'c004' then '零食'
        when 'c005' then '饮料'
        else '未知类别'
    end as category_name
from
    product;
