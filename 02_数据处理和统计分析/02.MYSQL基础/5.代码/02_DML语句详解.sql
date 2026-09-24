/*
DML语句详解:
    概述:
        它叫数据操作语言, 主要是 操作 表数据, 进行 增删改操作的.
        实际开发中, 增删改统称为 -> 更新语句.
    细节:
        进行删除, 修改前, 一定一定一定要备份(或者加where条件), 一个过来人的含泪忠告!
    添加数据:
        格式:
            insert into 数据表名(列名1, 列名2...) values(值1, 值2...);
            insert into 数据表名 values(值1, 值2...);

            insert into 数据表名 values(值1, 值2...), (值1, 值2..)...;
        细节:
            1. 要添加的值的个数, 必须和 列名及其类型对应.
            2. 如果不写列名, 默认是: 全列名.

    修改数据:
        格式:
            update 数据表名 set 字段名=值, 字段名=值... where 条件;

    删除数据:
        格式:
            delete from 数据表名 where 条件;         不会重置主键id.
            truncate table 数据表名;                相当于把表摧毁了, 然后再创建一张一模一样的表, 即: 会重置主键id
 */

# --------------------------------- 案例1: DML语句(数据操作语言) 操作 表数据(data) 增 ---------------------------------
# 1. 切库, 查表.
use day01;
show tables;

# 2.创建分类表, 分类id, 分类名, 描述信息.
create table category(
    cid int,                # 分类id
    cname varchar(20),      # 分类名
    info varchar(100)       # 描述信息
);

# 3. 往表中添加数据.
insert into category(cid, cname) values(1, '电脑');
# insert into category(cid, cname) values(1, '电脑', 3);    # 报错, 列的个数 和 值的个数不匹配

# insert into category values(2, '手机');       # 报错, 列的个数 和 值的个数不匹配
# insert into category values(3, '拉杆箱');       # 报错, 列的个数 和 值的个数不匹配
insert into category values(2, '手机', '华为手机666');

# 4. 查看表数据.
insert into
    category
values
    (3, '汽车', '小米'),
    (4, '平板', '华为');

# 5. 如何查看全表数据.
select * from category;     # * 代表表中 所有的列(列名)


# --------------------------------- 案例2: DML语句(数据操作语言) 操作 表数据(data) 改 ---------------------------------
# 1. 查看表数据.
select * from category;


# 2. 修改cname='空调', info='格力', cid=3
update category set cname='空调', info='格力';      # 危险, 一次性改所有
update category set cname='汽车', info=null where cid = 1;


# --------------------------------- 案例3: DML语句(数据操作语言) 操作 表数据(data) 删 ---------------------------------
# 演示 delete from
delete from category where cid = 4;
delete from category;           # 一次性删除所有, 不会重置主键id


# 演示 truncate table
truncate table category;       # 依次删除所有, 会重置主键id(明天讲解, 目前先了解)


# --------------------------------- 案例4: 扩展_如何备份数据表 ---------------------------------
# 0. 查看数据表.
show tables;

# 1. 原表
select * from category;

# 2. 场景1: 备份表不存在.
# 格式: create table 备份表名 select * from 原表名 where ...;
create table category_tmp select * from category;

# 3. 场景2: 备份表存在.
# 格式: insert into 备份表名 select * from 原表名 where ...;
insert into category_tmp select * from category where cid <= 3;

# 4. 查看备份表数据.
select * from category_tmp;

# 5. 清空备份表.
delete from category_tmp;