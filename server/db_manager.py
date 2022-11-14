# 对数据库进行操作，实现输入药材名称和标签名称需要能够直接进行查询
# 数据库结构
#
# create table medicines(
#    id int,
#    source varchar(1023),
#    natural varchar(1023),
#    process varchar(1023),
#    shape varchar(1023),
#    usage varchar(1023),
#    jingMai varchar(1023),
#    mainUse varchar(1023),
#    dosage varchar(1023),
#    attention varchar(1023),
#    Image blob,
#    prescription varchar(2047),
#    primary key(name),
# );
#
#create table names(
#    name varchar(15),
#    id int,
#    primary key(name),
#    foreign key(keyname) references medicines(name)    
# );
#
#create table indexs(
#  
#   source blob,
#   natural blob,
#   process blob,
#   shape blob,
#   usage blob,
#   jingMai blob,
#   mainUse blob,
#   dosage blob,
#   attention blob,
#   prescription varchar(2047),
#   primary key(name),
# )

import pymysql

def saveMedicine(path):

# 该函数属于前期数据集处理函数,实现药材入库，通过读取json文件，来将所有药材导入数据库
# param: path--要导入的药材信息json文件的地址
# return: "success"/"error"
   pass

def getMedicine(name,tags):

# 根据给定的药材名字和药材的属性，来返回相应的值
# param: name--药材名字，根据此可以唯一确定该种药材
#        tags--属性列表，包含需要查询的字段名称，如果为空则返回药材全部信息
# return: 字典类型，包括了tags中所有要求的字段的实际内容，没查询到的变量值为0： 比如{"source":"云南,大理...","jingMai":"胃肠经","shape":0}
#         如果数据库中根本没有这味药，直接返回"not found"
       pass

def saveIndex(attrs):

# 将索引类型存到数据库中
# prama：attrs--一个列表，包含了所有索引结构的集合
#return: "success"/"error"
       pass

def getIndex():

# 从数据库中拿到索引
# parma：无
# return：从数据库中拿到索引，并返回所有类型的索引列表，的二进制字节流
      attrs = { "source":"",
                "natural": "",
                "process":"",
                "shape": "",
                "usage": "",
                "jingMai": "",
                "mainUse": "",
                "dosage": "",
                "attention": "",
              }
      pass
      return attrs
      
def getAllMedicines():
# 将药材除了名称之外的所有属性，都提取出来，存放到列表里面
# 列表中每一条的格式为：
    attrs = {  "source":"",
                "allNames":[],
                "natural": "",
                "process":"",
                "shape": "",
                "usage": "",
                "jingMai": "",
                "mainUse": "",
                "dosage": "",
                "attention": "",
              }
    pass
    return attrs
