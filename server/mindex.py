# 该文件实现索引的构建，序列化与反序列化
import db_manager

def createIndex():

# 这个函数是数据的预处理函数，功能是根据原始数据建立一次索引，但是因为我们的索引只需要建一次
# 所以这个函数只需要在预处理函数中调用一次即可，以后每次系统启动时均直接向程序请求索引
 allMedicines = db_manager.getAllMedicines()  #得到所有药材的列
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
 pass #建立索引，并将索引转化为二进制字节流，保存在attrs的对应字段中
 return attrs #返回的attrs包括了各种字段的索引


def indexSerialize(attrs):

# 这个函数也可以说是预处理函数，因为建好的索引只需要序列化一次，存到库中，之后都可以直接拿
# params: attrs--包含了所有的索引类型的字典
# return: attrIndexs--包含了所有索引序列化之后的字典
# 注意：该函数的返回结果是要写到数据库中，但是最好在这个函数中也直接产生一个中间文件，以便直接观察
  attrIndexs = {}
  return attrIndexs 
    
def indexDeserialize():

# 将二进制字节流反序列化称为索引结构
# params:
# return: 包含了所有字段索引结构的字典类型
  attrIndex = db_manager.getIndex()
  pass
  return attrIndex