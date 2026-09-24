/*
SQL语句介绍:
    概述:
        全称叫 Structured Query Language, 结构化查询语言, 主要是实现 用户(程序员) 和 数据库软件(例如: MySQL, Oracle)之间交互用的.
    分类:
        DDL: 数据定义语言, 主要是操作 数据库, 数据表, 字段, 进行: 增删改查(CURD)
            涉及到的关键字: create, drop, alter, show
        DML: 数据操作语言, 主要是操作 表数据, 进行: 增删改(CDU) -> 统称为 更新语句.
            涉及到的关键字: insert, delete, update
        DQL: 数据查询语言, 主要是操作 表数据, 进行: 查询操作(R)
            涉及到的关键字: select, from, where
        DCL: 数据控制语言, 主要是 创建用户, 设置权限, 隔离级别等.
    通用语法:
        1. SQL语句可以写一行, 也可以写多行, 最后用 分号 结尾.
        2. SQL语句不区分大小写, 为了阅读方便, 建议关键字大写, 其它都小写.
        3. 注释写法:
                /星  多行注释的文本 星/
                # 单行注释
                -- 单行注释

数据类型:
    概述:
        就是用来限定某列值的范围的, 必须是: 整数, 小数, 字符串, 日期等...
    常用的数据类型:
        整型:       int
        浮点型:     float, double, decimal
        日期型:     datetime
        字符串型:   varchar(长度)

约束:
    概述:
        在数据类型的基础上, 进一步对该列值做 限定.
    (常用的)分类:
        单表约束:
            primary key 主键约束, 特点: 非空, 唯一, 一般结合 auto_increment(自动增长, 自增)一起使用.
            not null    非空约束, 即: 该列值不能为null, 但是可以 重复.
            unique      唯一约束, 即: 该列值必须不重复, 但是可以 为空.
            default     默认约束, 等价于Python的 缺省参数.
        多表约束:
            foreign key 外键约束

*/
# 单行注释
# 我是单行注释

-- 单行注释
-- 我也是单行注释


# --------------------------------- 案例1: DDL语句(数据定义语言) 操作 数据库(DataBase) ---------------------------------
# 1. 查看(已创建的)所有数据库.
show databases ;

# 2. 创建数据库.
create database day01;                          # 以默认码表(这里是: UTF8)
create database day02 character set 'gbk';      # 以GBK码表, 创建数据表.
# create database day01;            # 会报错, 因为数据库存在.
create database if not exists day01;            # 数据库day01不存在, 就创建, 存在就: 什么都不做.

# 完整建库格式.
create database if not exists day03 charset 'utf8';          # 采用utf8码表, 创建day03数据库, 如果存在就什么都不做.

# 3. 修改数据库 -> 码表, 把day02数据库的码表从 gbk -> utf8
alter database day02 charset 'utf8';


# 4. 删除数据库.
drop database day01;
drop database day02;
drop database day03;

# 5. 查看当前用的是哪个数据库.
select database();

# 6. 切换数据库.
use day02;

# 7. 查看某个指定数据库的数据库的码表.
show create database day01;     # 默认: utf-8码表
show create database day02;     # 默认: gbk码表


# --------------------------------- 案例2: DDL语句(数据定义语言) 操作 数据表(Table) ---------------------------------
# 1. 切库.
use day01;
# 2. 查看(当前数据库中)所有的数据表.
show tables;
# 3. 创建数据表, 学生表: student, 字段为: sid, 学生id    name, 学生姓名,   age, 学生年龄
/*
格式:
    create table [if not exists] 数据表名(
        字段名 数据类型 [约束],
        字段名 数据类型 [约束],
        字段名 数据类型 [约束],
        ......
    );
*/
create table if not exists student(
    sid int,            # 学生学号
    name varchar(20),   # 学生姓名
    age int             # 学生年龄
);

# 4.修改数据表(名), 从 student -> stu
# 格式: rename table 旧表名 to 新表名;
rename table student to stu;

# 5. 删除数据表.
# 格式: drop table [if exists] 数据表名;
drop table if exists stu;

# 6. 如何查看表结构.
# 格式: desc 数据表名
# show create table student;
desc student;



# --------------------------------- 案例3: DDL语句(数据定义语言) 操作 字段(Field) ---------------------------------
# 细节: 实际开发中, 建表时一般都会多预留2 ~ 7个字段, 当做扩展字段, 将来业务扩展变更等, 可以启用新的字段.
# 1. 切库, 查表.
use day01;
show tables;

# 2. 查看表结构.
desc student;

# 3.给 student表添加字段 address varchar(20)v
# 格式: alter table 表名 add 新列名 数据类型 [约束];
alter table student add address varchar(20) not null;

# 4.修改字段
# 场景1: 只修改数据类型 和 约束.
# 格式: alter table 表名 modify 旧列名 新的数据类型 [新的约束];
alter table student modify address int;

# 场景2: 即修改数据类型 和 约束, 还修改 字段名.  address -> addr, varchar(10)
# 格式: alter table 表名 change 旧列名 新列名 新的数据类型 [新的约束];
alter table student change address addr varchar(10) not null;

# 5. 删除字段.
# 格式: alter table 表名 drop 旧列名;
alter table student drop addr;

desc student;

alter table student add `desc` varchar(20) not null;


