# ---------------------- 案例1: 窗口函数(M有SQL8.X 新特性) ----------------------
/*
窗口函数解释:
    概述:
        它是MySQL8.x的新特性, 主要用于 给表新增1列, 至于新增的内容是什么, 取决于你用什么 窗口函数.
    格式:
        窗口函数 over([partition by 分组字段 order by 排序字段 asc | desc])
    常用的窗口函数:
        row_number():   做行号标记的, 即: 1, 2, 3, 4...
        rank():         做稀疏排名的.
        dense_rank():   做密集排名的.
    大白话解释:
        假设数据集是 100, 90, 90, 60, 则三个函数的排名结果分别是:
             row_number():  1, 2, 3, 4
             rank():        1, 2, 2, 4
             dense_rank():  1, 2, 2, 3
    细节:
        1. 窗口函数 = 给表新增1列, 至于新增的是什么, 取决于和什么函数一起用.
        2. 如果不写partition by, 则统计的是全表数据, 如果写了, 则统计的是组内的数据.
        3. 如果不写order by, 则统计的是组内所有的数据, 如果写了, 则统计的是组内从第一行, 截止到当前行的数据.
        4. 如果你感兴趣, 你可以尝试玩意儿下其它的窗口函数结合over()一起用,
            例如: count(), max(), min(), sum(), avg(), ntile(n), lag(), lead(), first_value(), last_value()...
    总结: 关于窗口函数, 我只希望大家掌握两点:
        1. 分组排名.
        2. 分组排名求TopN
*/
# 准备数据 -> 建库, 切库, 查表
# drop database day03;
create database day03;
use day03;
show tables;

# 准备数据 -> 建表, 添加数据.
create table employee (empid int,ename varchar(20) ,deptid int ,salary decimal(10,2));

insert into employee values(1,'刘备',10,5500.00);
insert into employee values(2,'赵云',10,4500.00);
insert into employee values(2,'张飞',10,3500.00);
insert into employee values(2,'关羽',10,4500.00);

insert into employee values(3,'曹操',20,1900.00);
insert into employee values(4,'许褚',20,4800.00);
insert into employee values(5,'张辽',20,6500.00);
insert into employee values(6,'徐晃',20,14500.00);

insert into employee values(7,'孙权',30,44500.00);
insert into employee values(8,'周瑜',30,6500.00);
insert into employee values(9,'陆逊',30,7500.00);

# 查看数据.
select * from employee;

# 案例1: 分组排名,  需求: 按照部门id(deptid)分组, 按照工资(salary)降序排名.
# 场景1: 如何给表新增1列.
select *, '夯哥' from employee;
select *, 10 / 3 from employee;
select *, deptid + 100 from employee;

# 场景2: 引入 窗口函数.
select
    *,
    # sum(salary) over () as total_sum                                          # 没写partition by, 统计全表
    # sum(salary) over (partition by deptid) as total_sum                       # 写了partition by, 统计全组
    sum(salary) over (partition by deptid order by salary desc) as total_sum    # 写了order by, 统计全组
from
    employee;

# 场景3: 分组排名:  按照部门id(deptid)分组, 按照工资(salary)降序排名.
select
    *,
    row_number() over(partition by deptid order by salary desc) as rn,
    rank() over(partition by deptid order by salary desc) as rk,
    dense_rank() over(partition by deptid order by salary desc) as dr
from
    employee;

# 场景4: 分组排名求TopN,  需求: 找出每组工资最高的2人的信息(考虑并列).
# 如下代码, 思路没问题, 但是语法格式有问题, 因为where后边的字段必须是表中 已有的字段.
select
    *,
    rank() over(partition by deptid order by salary desc) rk
from
    employee
where
    rk <= 2;

# 解决方案如下
# 思路1: 用 子查询 解决.
select * from (
    select
        *,
        rank() over(partition by deptid order by salary desc) rk
    from
        employee
) t1 where rk <= 2;

# 思路2: 用CTE 公共表表达式, 可以把常用的数据集封装成新表, 方便操作.
/*
格式:
    with 表名1 as (select .....),
         表名2 as (select ....),
         表名3 as ....
    select * from t1 ....;          # 这里正常写SQL, 使用上述的 表名即可.
 */
with t1 as (select *, rank() over(partition by deptid order by salary desc) rk from employee)
select * from t1 where rk <= 2;

# 扩展: 1个需求表示 CTE表达式的强大之处.
with t1 as (select * from employee),
     t2 as (select * from employee where deptid=10),
     t3 as (select * from employee where deptid=20),
     t4 as (select * from employee where deptid=30),
     t5 as (select *, sum(salary) over() as total_salary from employee)
select * from t5;


# ---------------------- 案例2: 自关联(自连接)查询 ----------------------
/*
解释:
    表自己和自己做 关联查询 -> 自关联, 自连接查询.
应用场景:
    省市区(行政区域表) 信息查询.
如果不考虑 自连接查询, 让你设计 行政区域表, 要求有 行政区域的id 和 行政区域名, 例如: 410000 -> 河南省, 你如何设计?
    大概率你会设计成 3 张表, 分别对应 省, 市, 区 的信息, 但是这样做太繁琐了, 我们可以考虑把 省市区合并到一张表, 然后做 自关联查询即可.
合并之后, 表中有三个字段, 分别是:
    区域自身id      区域名     区域的父级id
    410000         河南省         0

    410100         郑州市         410000
    410200         开封市         410000

    410101         二七区         410100
    410102         金水区         410200
    ......
 */
# 查表.
show tables;
# 查看表数据
select * from areas;

# 1. 查看河南省的信息
select * from areas where title = '河南省';

# 2. 查看河南省所有的市.
select * from areas where pid = '410000';

# 3. 查看新乡市所有的县区.
select * from areas where pid = '410700';

# 4. 查看所有省, 所有市, 所有县区的信息.
select
    province.id, province.title,        # 省级的id, 名字
    city.id, city.title,                # 市级的id, 名字
    county.id, county.title             # 县区级的id, 名字
from
    areas as county         # 县区表
join
    areas as city on county.pid = city.id       # 市级表
join
    areas as province on city.pid = province.id # 省级表
;


# 5. 精准查找信息.
select
    province.id, province.title,        # 省级的id, 名字
    city.id, city.title,                # 市级的id, 名字
    county.id, county.title             # 县区级的id, 名字
from
    areas as county         # 县区表
join
    areas as city on county.pid = city.id       # 市级表
join
    areas as province on city.pid = province.id # 省级表
where
    county.id = '230221';         # 身份证号前6位