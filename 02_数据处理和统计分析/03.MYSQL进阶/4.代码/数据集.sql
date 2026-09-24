# 1. 创建商品表.
create table product
(
    pid         int primary key auto_increment, # 商品id, 主键
    pname       varchar(20),    # 商品名
    price       double,         # 商品单价
    category_id varchar(32)     # 商品的分类id
);

# 2. 添加表数据.
INSERT INTO product(pid,pname,price,category_id) VALUES(null,'联想',5000,'c001');
INSERT INTO product(pid,pname,price,category_id) VALUES(null,'海尔',3000,'c001');
INSERT INTO product(pid,pname,price,category_id) VALUES(null,'雷神',5000,'c001');
INSERT INTO product(pid,pname,price,category_id) VALUES(null,'杰克琼斯',800,'c002');
INSERT INTO product(pid,pname,price,category_id) VALUES(null,'真维斯',200, null);
INSERT INTO product(pid,pname,price,category_id) VALUES(null,'花花公子',440,'c002');
INSERT INTO product(pid,pname,price,category_id) VALUES(null,'劲霸',2000,'c002');
INSERT INTO product(pid,pname,price,category_id) VALUES(null,'香奈儿',800,'c003');
INSERT INTO product(pid,pname,price,category_id) VALUES(null,'相宜本草',200, null);
INSERT INTO product(pid,pname,price,category_id) VALUES(null,'面霸',5,'c003');
INSERT INTO product(pid,pname,price,category_id) VALUES(null,'好想你枣',56,'c004');
INSERT INTO product(pid,pname,price,category_id) VALUES(null,'香飘飘奶茶',1,'c005');
INSERT INTO product(pid,pname,price,category_id) VALUES(null,'海澜之家',1,'c002');






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







# 2. 创建数据表.
create table employee (
    id int,                 # 员工id
    ename varchar(20),      # 员工名
    deptid int,             # 部门id
    salary decimal(10,2)    # 工资
);
# 3. 添加表数据.
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
# 4. 查看表数据.
select * from employee;






