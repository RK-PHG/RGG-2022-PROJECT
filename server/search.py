# 负责完成搜索逻辑
from collections import Counter
def search(index,attr,key,mode):
#  实现单个属性值索引的搜索
#  parma: index--该属性对应的索引
#         attr--该属性的标签
#         key--索引关键词
#         mode--1为并集模式，2为交集模式
#  return：按顺序，返回该属性对应搜索结果的列表
  #  这个错误指的是在这个索引之中并没有这个标签（当然这种可能性为0，只是以防万一）
  if attr not in index:
    return -1  # 这个之后再补充 反正就是返回一个错误的信息
  #  现在要做的是取出这个单个属性对应的字典
  #  如果搜索内容为空的话，直接return
  if key == "":
    return -1
  AttrMode1 = []
  AttrMode2 = []
  if mode == 1:
    flag = 0
    number = 0
    TheAttr = index.get(attr, "NULL")
    for i in range(len(key)):
      KeyAttr = TheAttr.get(key[i], "NULL")
      if KeyAttr != "NULL":
        number = number + 1
        flag = 1
        AttrMode1.append(KeyAttr)
    if flag == 1:  # 如果flag==1的话，说明你输入的key之中至少有一个字能搜索到，那么我们对结果进行处理
      Answer = {}
      for i in range(number):
        Answer = dict(Counter(Answer) + Counter(AttrMode1[i]))
      AnswerAfterSort = sorted(Answer.items(), key=lambda x: -x[1])
      AnswerAfterSort_dic = {k: v for k, v in AnswerAfterSort}

      return (AnswerAfterSort_dic)
    if flag != 1:  # 如果flag！=1的话，说明key中没有1个字能搜索到，返回错误信息，
      return -1

  if mode == 2:
    TheAttr = index.get(attr, "NULL")
    for i in range(len(key)):
      KeyAttr = TheAttr.get(key[i], "NULL")
      if KeyAttr == "NULL":
        return -1
      if KeyAttr != "NULL":
        AttrMode2.append(KeyAttr)
    # 现在如果所有的字都能找到 我们已经完成了数据的收集，现在要求交集
    Answer_key = AttrMode2[0]
    for i in range(len(key)):
      key1 = Answer_key.keys()
      key2 = AttrMode2[i].keys()
      key3 = key1 & key2
      if len(key3) == 0:
        return -1
      if i != 0:
        dic_tmp = {}
        for k in key3:
          num1 = Answer_key.get(k)
          num2 = AttrMode2[i].get(k)
          num3 = num1 + num2
          # print(k)
          # print(num3)
          dic_tmp[k] = num3
        #  (dic_tmp)
        Answer_key = dic_tmp
    # 在得到answer之后 我们给answer进行排序之后就可以输出了
    AnswerAfterSort = sorted(Answer_key.items(), key=lambda x: -x[1])
    AnswerAfterSort_dic = {k: v for k, v in AnswerAfterSort}
    #  print(AnswerAfterSort_dic)

    return (AnswerAfterSort_dic)

def searchAll(index,attrs,key,mode):
#  实现多个属性值搜索的逻辑
#  parma: index -- 该属性对应的索引
#         attrs -- 属性的标签列表
#         return -- 相关度排序后的结果
  AttrsAnswer = []
  n = 0
  # 我们现在得到的是一个包含字典的一个列表，现在要做的就是处理数据
  if mode == 1:
    Flag = 0
    for attr in attrs:
      if (search(index, attr, key, mode) != -1):
        Flag = 1
        AttrsAnswer.append(search(index, attr, key, mode))
        n = n + 1
    if Flag == 0:
      #  print("就算大模式是并集模式你也依然没有搜到哦")
      return -1
    #  if Flag == 1:
    #  print(AttrsAnswer)
    #  现在我我们获得列一个装有n个字典的列表
    #  我们需要对这个列表中的字典进行合并，其中采用并集模式
    Answers = {}
    for i in range(n):
      Answers = dict(Counter(Answers) + Counter(AttrsAnswer[i]))
    #  print(Answers)
    AnswersAfterSort = sorted(Answers.items(), key=lambda x: -x[1])
    AnswersAfterSort_dic = {k: v for k, v in AnswersAfterSort}
    #  print(AnswersAfterSort_dic)
    AnswerList = []
    AnswerList = list(AnswersAfterSort_dic.keys())
    return AnswerList

  if mode == 2:
    for attr in attrs:
      if (search(index, attr, key, mode) == -1):
        #  print("大模式是交集找不到")
        return -1
      AttrsAnswer.append(search(index, attr, key, mode))
      n = n + 1
    #  print(AttrsAnswer)
    #  现在我我们获得列一个装有n个字典的列表
    #  我们需要对这个列表中的字典进行合并，其中采用交集模式
    Answer_tmp = AttrsAnswer[0]
    for i in range(n):
      key1 = Answer_tmp.keys()
      key2 = AttrsAnswer[i].keys()
      key3 = key1 & key2
      if len(key3) == 0:
        #  print("大模式是交集的时候 找到的结果没交集")
        return -1
      if i != 0:
        dic_tmp = {}
        for k in key3:
          num1 = Answer_tmp.get(k)
          num2 = AttrsAnswer[i].get(k)
          num3 = num1 + num2
          dic_tmp[k] = num3
        Answer_tmp = dic_tmp
    AnswersAfterSort = sorted(Answer_tmp.items(), key=lambda x: -x[1])
    AnswersAfterSort_dic = {k: v for k, v in AnswersAfterSort}
    AnswerList = []
    AnswerList = list(AnswersAfterSort_dic.keys())
    return AnswerList

