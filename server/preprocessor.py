#建立索引，完成索引的序列化
import mindex
import db_manager

def preProcess():
  attrInex =  mindex.createIndex()  # 建立索引  
  bIndex = mindex.indexDeserialize(attrInex)  # 索引序列化
  db_manager.saveIndex(bIndex)  #保存索引

if __name__ == "__main__":
    preProcess()