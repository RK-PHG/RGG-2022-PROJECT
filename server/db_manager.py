# 该文件只有1处涉及到跟文件配置有关的操作，所以若报错，则先检查文件路径是否正确
# 涉及到文件路径的函数有getAllMedicines()若报错，则先检查这个函数
# 这个函数只是把json文件里面的数据存到列表中，为创建倒排索引做准备，若无法解决可以先注释掉它

import json
from sqlalchemy import Column, Integer, String, LargeBinary

# constants里面储存着DR_URI这个配置
from constants import DB_URI
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import ForeignKey
import random

engine = create_engine(DB_URI, echo=False)

# 所有的类都要继承自`declarative_base`这个函数生成的基类
Base = declarative_base(engine)


# 创建数据库操作的对象类
class oneMedicine(Base):
    __tablename__ = "medicines"
    id = Column(Integer, primary_key=True, autoincrement=True)
    source = Column(String(2047))
    natural = Column(String(1023))
    process = Column(String(1023))
    shape = Column(String(2047))
    usage = Column(String(1023))
    jingMai = Column(String(1023))
    mainUse = Column(String(1023))
    dosage = Column(String(2047))
    attention = Column(String(2047))
    Image = Column(LargeBinary(16777216))
    prescription = Column(String(2047))


class oneName(Base):
    __tablename__ = "names"
    id = Column(Integer, ForeignKey('medicines.id'), primary_key=True, autoincrement=True)
    name = Column(String(30))


class Alias(Base):
    __tablename__ = "Alias"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30))
    alias = Column(String(30))


class Index(Base):
    __tablename__ = "Index"
    id = Column(Integer, primary_key=True, autoincrement=True)
    source = Column(LargeBinary(16777216))
    natural = Column(LargeBinary(16777216))
    process = Column(LargeBinary(16777216))
    shape = Column(LargeBinary(16777216))
    usage = Column(LargeBinary(16777216))
    jingMai = Column(LargeBinary(16777216))
    mainUse = Column(LargeBinary(16777216))
    dosage = Column(LargeBinary(16777216))
    attention = Column(LargeBinary(16777216))


# 创建数据库
def createDatabase():
    Base.metadata.create_all()


# 用于事务提交


# 根据给定的药材名字和药材的属性，来返回相应的值
# param: name--药材名字，根据此可以唯一确定该种药材
#        tags--属性列表，包含需要查询的字段名称，如果为空则返回药材全部信息
# return: 字典类型，包括了tags中所有要求的字段的实际内容，没查询到的变量值为0： 比如{"source":"云南,大理...","jingMai":"胃肠经","shape":0}
#         如果数据库中根本没有这味药，直接返回"not found"
# 此函数为主要搜索函数
def getMedicine(temp_name, tags):
    try:
        Session = sessionmaker()
        session = Session()
        idName = session.query(oneName).filter(oneName.name == temp_name)
        idName = idName.all()
        if len(idName) == 0:
            return "not found"
        else:
            medicionResult = session.query(oneMedicine).filter(oneMedicine.id == idName[0].id)
            medicionResult = medicionResult.all()
            dict = {"name": temp_name}

            if len(tags) == 0:
                tags = ["source", "allNames", "natural", "process", "shape", "usage", "jingMai", "mainUse", \
                        "dosage", "attention", "prescription", "Image"]
            for tag in tags:
                if tag == "source":
                    dict["source"] = medicionResult[0].source
                elif tag == "natural":
                    dict["natural"] = medicionResult[0].natural
                elif tag == "allNames":
                    dict["allNames"] = []
                    allNames = session.query(Alias).filter(Alias.name == temp_name).all()
                    for otherName in allNames:
                        dict["allNames"].append(otherName.alias)
                elif tag == "process":
                    dict["process"] = medicionResult[0].process
                elif tag == "shape":
                    dict["shape"] = medicionResult[0].shape
                elif tag == "usage":
                    dict["usage"] = medicionResult[0].usage
                elif tag == "jingMai":
                    dict["jingMai"] = medicionResult[0].jingMai
                elif tag == "mainUse":
                    dict["mainUse"] = medicionResult[0].mainUse
                elif tag == "dosage":
                    dict["dosage"] = medicionResult[0].dosage
                elif tag == "attention":
                    dict["attention"] = medicionResult[0].attention
                elif tag == "prescription":
                    dict["prescription"] = medicionResult[0].prescription
                elif tag == "Image":
                    dict["Image"] = medicionResult[0].Image
                else:
                    pass
    except:
        session.rollback()
    session.close()

    return dict


# 随机生成一个药材的名字，并调用getMedicine返回一个药材的所有信息
def randomName():
    dict = {}
    try:
        randNum = random.randint(1, 1343)
        Session = sessionmaker()
        session = Session()
        idName = session.query(oneName).filter(oneName.id == randNum)
        idName = idName.all()
        dict = getMedicine(idName[0].name, [])
    except:
        session.rollback()

    session.close()

    return dict


def getMedicineById(id, tags):
    try:
        Session = sessionmaker()
        session = Session()
        idName = session.query(oneName).filter(oneName.id == id)
        idName = idName.all()
        dict = getMedicine(idName[0].name, tags)

    except:
        session.rollback()
    session.close()
    return dict


# 以下三个函数与倒排索引相关
def getIndex():
    # 从数据库中拿到索引
    # parma：无
    # return：从数据库中拿到索引，并返回所有类型的索引列表，的二进制字节流
    attrs = {"source": "",
             "natural": "",
             "process": "",
             "shape": "",
             "usage": "",
             "jingMai": "",
             "mainUse": "",
             "dosage": "",
             "attention": "",
             }
    Session = sessionmaker()
    session = Session()
    tempIndex = session.query(Index).filter(Index.id == 1).all()
    attrs["source"] = tempIndex[0].source
    attrs["natural"] = tempIndex[0].natural
    attrs["process"] = tempIndex[0].process
    attrs["shape"] = tempIndex[0].shape
    attrs["usage"] = tempIndex[0].usage
    attrs["jingMai"] = tempIndex[0].jingMai
    attrs["mainUse"] = tempIndex[0].mainUse
    attrs["dosage"] = tempIndex[0].dosage
    attrs["attention"] = tempIndex[0].attention
    return attrs


def saveIndex(attrs):
    Session = sessionmaker()
    session = Session()
    temp_index = Index(source=attrs['source'], natural=attrs['natural'],
                       process=attrs['process'], shape=attrs['shape'], usage=attrs['usage'],
                       jingMai=attrs['jingMai'], mainUse=attrs['mainUse'], dosage=attrs['dosage'],
                       attention=attrs['attention'])
    session.add(temp_index)
    session.commit()
    session.close


#
def getAllMedicines():
    # 将药材除了名称之外的所有属性，都提取出来，存放到列表里面
    # 列表中每一条的格式为：

    attrs = []
    f = open('./server/filename.txt', 'r', encoding='UTF-8')
    lines = f.readlines()
    temp_len = len(lines)
    for i in range(0, temp_len):
        temp_path = './data/data-pure-context/'
        temp_path = temp_path + lines[i]
        temp_path = temp_path.replace('\n', '')
        fp = open(temp_path, 'r', encoding='utf8')
        json_data = json.load(fp)
        # 属性字段为空的用0替代
        temp_name = json_data.get("name", 0)
        temp_allNames = json_data.get("allNames", [])
        temp_source = json_data.get("source", 0)
        temp_natural = json_data.get("natural", 0)
        temp_process = json_data.get("process", 0)
        temp_shape = json_data.get("shape", 0)
        temp_jingMai = json_data.get("jingMai", 0)
        temp_usage = json_data.get("usage", 0)
        temp_dosage = json_data.get("dosage", 0)
        temp_mainUse = json_data.get("mainUsage", 0)
        temp_attention = json_data.get("attention", 0)
        if temp_mainUse == 0:
            temp_mainUse = json_data.get("mainUse", 0)

        dict = {}
        dict["name"] = temp_name
        dict["allNames"] = temp_allNames
        dict["source"] = temp_source
        dict["natural"] = temp_natural
        dict["process"] = temp_process
        dict["shape"] = temp_shape
        dict["usage"] = temp_usage
        dict["jingMai"] = temp_jingMai
        dict["mainUse"] = temp_mainUse
        dict["dosage"] = temp_dosage
        dict["attention"] = temp_attention
        attrs.append(dict)
    return attrs






