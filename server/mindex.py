# 该文件实现索引的构建，序列化与反序列化
import db_manager
import pickle

def createIndex():
# 这个函数是数据的预处理函数，功能是根据原始数据建立一次索引，但是因为我们的索引只需要建一次
# 所以这个函数只需要在预处理函数中调用一次即可，以后每次系统启动时均直接向程序请求索引
 allMedicines = db_manager.getAllMedicines()  #得到所有药材的列
 attrs = { "source":{},
                "natural": {},
                "process":{},
                "shape": {},
                "usage": {},
                "jingMai": {},
                "mainUse": {},
                "dosage": {},
                "attention": {},
              }
 # 建立索引，并将索引转化为二进制字节流，保存在attrs的对应字段中
 all_num = len(allMedicines)            # 获取药品数量
 
 for i in range(all_num):
   if (type(allMedicines[i]["source"]) == str) == False: # 如果这个字段为空（也就是设为0），那么跳过它
    continue
   str_len = len(allMedicines[i]["source"]) # 确定这个药品的该字段有多少个字
   for j in range(str_len):
    if (allMedicines[i]["source"][j] in attrs["source"]) == False: # 如果这个字是第一次出现在该字段中，那么给这个字建一个新字典，然后字典内药品编号key对应的value设为1
      attrs["source"][allMedicines[i]["source"][j]] = {}
      attrs["source"][allMedicines[i]["source"][j]][i] = 1
    else:
      if(i in attrs["source"][allMedicines[i]["source"][j]]) == False: # 如果这个字已经出现在该字段中过，但在该药品的该字段中第一次出现，那么给该药品编号对应的value设为1
        attrs["source"][allMedicines[i]["source"][j]][i] = 1
      else:                                                            # 否则value直接加1，之后的所有字段都一样
        attrs["source"][allMedicines[i]["source"][j]]
        attrs["source"][allMedicines[i]["source"][j]][i] += 1

 for i in range(all_num):
   if (type(allMedicines[i]["natural"]) == str) == False:
    continue
   str_len = len(allMedicines[i]["natural"])
   for j in range(str_len):
    if (allMedicines[i]["natural"][j] in attrs["natural"]) == False:
      attrs["natural"][allMedicines[i]["natural"][j]] = {}
      attrs["natural"][allMedicines[i]["natural"][j]][i] = 1
    else:
      if(i in attrs["natural"][allMedicines[i]["natural"][j]]) == False:
        attrs["natural"][allMedicines[i]["natural"][j]][i] = 1
      else:
        attrs["natural"][allMedicines[i]["natural"][j]]
        attrs["natural"][allMedicines[i]["natural"][j]][i] += 1
      
 for i in range(all_num):
   if (type(allMedicines[i]["process"]) == str) == False:
    continue
   str_len = len(allMedicines[i]["process"])
   for j in range(str_len):
    if (allMedicines[i]["process"][j] in attrs["process"]) == False:
      attrs["process"][allMedicines[i]["process"][j]] = {}
      attrs["process"][allMedicines[i]["process"][j]][i] = 1
    else:
      if(i in attrs["process"][allMedicines[i]["process"][j]]) == False:
        attrs["process"][allMedicines[i]["process"][j]][i] = 1
      else:
        attrs["process"][allMedicines[i]["process"][j]]
        attrs["process"][allMedicines[i]["process"][j]][i] += 1

 for i in range(all_num):
   if (type(allMedicines[i]["shape"]) == str) == False:
    continue
   str_len = len(allMedicines[i]["shape"])
   for j in range(str_len):
    if (allMedicines[i]["shape"][j] in attrs["shape"]) == False:
      attrs["shape"][allMedicines[i]["shape"][j]] = {}
      attrs["shape"][allMedicines[i]["shape"][j]][i] = 1
    else:
      if(i in attrs["shape"][allMedicines[i]["shape"][j]]) == False:
        attrs["shape"][allMedicines[i]["shape"][j]][i] = 1
      else:
        attrs["shape"][allMedicines[i]["shape"][j]]
        attrs["shape"][allMedicines[i]["shape"][j]][i] += 1
  
 for i in range(all_num):
   if (type(allMedicines[i]["usage"]) == str) == False:
    continue
   str_len = len(allMedicines[i]["usage"])
   for j in range(str_len):
    if (allMedicines[i]["usage"][j] in attrs["usage"]) == False:
      attrs["usage"][allMedicines[i]["usage"][j]] = {}
      attrs["usage"][allMedicines[i]["usage"][j]][i] = 1
    else:
      if(i in attrs["usage"][allMedicines[i]["usage"][j]]) == False:
        attrs["usage"][allMedicines[i]["usage"][j]][i] = 1
      else:
        attrs["usage"][allMedicines[i]["usage"][j]]
        attrs["usage"][allMedicines[i]["usage"][j]][i] += 1

 for i in range(all_num):
   if (type(allMedicines[i]["jingMai"]) == str) == False:
    continue
   str_len = len(allMedicines[i]["jingMai"])
   for j in range(str_len):
    if (allMedicines[i]["jingMai"][j] in attrs["jingMai"]) == False:
      attrs["jingMai"][allMedicines[i]["jingMai"][j]] = {}
      attrs["jingMai"][allMedicines[i]["jingMai"][j]][i] = 1
    else:
      if(i in attrs["jingMai"][allMedicines[i]["jingMai"][j]]) == False:
        attrs["jingMai"][allMedicines[i]["jingMai"][j]][i] = 1
      else:
        attrs["jingMai"][allMedicines[i]["jingMai"][j]]
        attrs["jingMai"][allMedicines[i]["jingMai"][j]][i] += 1

 for i in range(all_num):
   if (type(allMedicines[i]["mainUse"]) == str) == False:
    continue
   str_len = len(allMedicines[i]["mainUse"])
   for j in range(str_len):
    if (allMedicines[i]["mainUse"][j] in attrs["mainUse"]) == False:
      attrs["mainUse"][allMedicines[i]["mainUse"][j]] = {}
      attrs["mainUse"][allMedicines[i]["mainUse"][j]][i] = 1
    else:
      if(i in attrs["mainUse"][allMedicines[i]["mainUse"][j]]) == False:
        attrs["mainUse"][allMedicines[i]["mainUse"][j]][i] = 1
      else:
        attrs["mainUse"][allMedicines[i]["mainUse"][j]]
        attrs["mainUse"][allMedicines[i]["mainUse"][j]][i] += 1

 for i in range(all_num):
   if (type(allMedicines[i]["dosage"]) == str) == False:
    continue
   str_len = len(allMedicines[i]["dosage"])
   for j in range(str_len):
    if (allMedicines[i]["dosage"][j] in attrs["dosage"]) == False:
      attrs["dosage"][allMedicines[i]["dosage"][j]] = {}
      attrs["dosage"][allMedicines[i]["dosage"][j]][i] = 1
    else:
      if(i in attrs["dosage"][allMedicines[i]["dosage"][j]]) == False:
        attrs["dosage"][allMedicines[i]["dosage"][j]][i] = 1
      else:
        attrs["dosage"][allMedicines[i]["dosage"][j]]
        attrs["dosage"][allMedicines[i]["dosage"][j]][i] += 1

 for i in range(all_num):
   if (type(allMedicines[i]["attention"]) == str) == False:
    continue
   str_len = len(allMedicines[i]["attention"])
   for j in range(str_len):
    if (allMedicines[i]["attention"][j] in attrs["attention"]) == False:
      attrs["attention"][allMedicines[i]["attention"][j]] = {}
      attrs["attention"][allMedicines[i]["attention"][j]][i] = 1
    else:
      if(i in attrs["attention"][allMedicines[i]["attention"][j]]) == False:
        attrs["attention"][allMedicines[i]["attention"][j]][i] = 1
      else:
        attrs["attention"][allMedicines[i]["attention"][j]]
        attrs["attention"][allMedicines[i]["attention"][j]][i] += 1

 return attrs #返回的attrs包括了各种字段的索引


def indexSerialize(attrs):
# 这个函数也可以说是预处理函数，因为建好的索引只需要序列化一次，存到库中，之后都可以直接拿
# params: attrs--包含了所有的索引类型的字典
# return: attrIndexs--包含了所有索引序列化之后的字典
# 注意：该函数的返回结果是要写到数据库中，但是最好在这个函数中也直接产生一个中间文件，以便直接观察
  attrIndexs = {"source":"",
                "natural": "",
                "process":"",
                "shape": "",
                "usage": "",
                "jingMai": "",
                "mainUse": "",
                "dosage": "",
                "attention": "",}
 # 用pickle模块的dumps方法将各字段key对应的value，也就是次级字典变为二进制字符串
  attrIndexs["source"] = pickle.dumps(attrs["source"])
  attrIndexs["natural"] = pickle.dumps(attrs["natural"])
  attrIndexs["process"] = pickle.dumps(attrs["process"])
  attrIndexs["shape"] = pickle.dumps(attrs["shape"])
  attrIndexs["usage"] = pickle.dumps(attrs["usage"])
  attrIndexs["jingMai"] = pickle.dumps(attrs["jingMai"])
  attrIndexs["mainUse"] = pickle.dumps(attrs["mainUse"])
  attrIndexs["dosage"] = pickle.dumps(attrs["dosage"])
  attrIndexs["attention"] = pickle.dumps(attrs["attention"])

  # 生成一些存储二进制字符流的中间文件
  filename = 'source.pickle'
  with open(filename,'wb') as f:
    pickle.dump(attrIndexs["source"],f)
  
  filename = 'natural.pickle'
  with open(filename,'wb') as f:
    pickle.dump(attrIndexs["natural"],f)

  filename = 'process.pickle'
  with open(filename,'wb') as f:
    pickle.dump(attrIndexs["process"],f)
  
  filename = 'shape.pickle'
  with open(filename,'wb') as f:
    pickle.dump(attrIndexs["shape"],f)

  filename = 'usage.pickle'
  with open(filename,'wb') as f:
    pickle.dump(attrIndexs["usage"],f)
  
  filename = 'jingMai.pickle'
  with open(filename,'wb') as f:
    pickle.dump(attrIndexs["jingMai"],f)

  filename = 'mainUse.pickle'
  with open(filename,'wb') as f:
    pickle.dump(attrIndexs["mainUse"],f)
  
  filename = 'dosage.pickle'
  with open(filename,'wb') as f:
    pickle.dump(attrIndexs["dosage"],f)

  filename = 'attention.pickle'
  with open(filename,'wb') as f:
    pickle.dump(attrIndexs["attention"],f)

  return attrIndexs 
    
def indexDeserialize():
# 将二进制字节流反序列化称为索引结构
# params:
# return: 包含了所有字段索引结构的字典类型
  attrIndex = db_manager.getIndex()
  attrs = { "source":{},
                "natural": {},
                "process":{},
                "shape": {},
                "usage": {},
                "jingMai": {},
                "mainUse": {},
                "dosage": {},
                "attention": {},
              }
  # 用pickle模块的loads方法将二进制字符流转换回原本的字典类型
  attrs["source"] = pickle.loads(attrIndex["source"])
  attrs["natural"] = pickle.loads(attrIndex["natural"])
  attrs["process"] = pickle.loads(attrIndex["process"])
  attrs["shape"] = pickle.loads(attrIndex["shape"])
  attrs["usage"] = pickle.loads(attrIndex["usage"])
  attrs["jingMai"] = pickle.loads(attrIndex["jingMai"])
  attrs["mainUse"] = pickle.loads(attrIndex["mainUse"])
  attrs["dosage"] = pickle.loads(attrIndex["dosage"])
  attrs["attention"] = pickle.loads(attrIndex["attention"])

  return attrs
