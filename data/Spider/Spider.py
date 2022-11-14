# 文件说明： 这是一个数据爬虫，为满足软件工程管理课程设计
# 需要，爬取中医药数据，作为自建网站数据源。爬取网站为： 
# https://zhongyibaike.com/  中医百科网

# 创建于2022年10月22日

from contextlib import nullcontext
from xml.dom.minidom import AttributeList
import aiofiles
import aiohttp
import asyncio
from lxml import etree
import requests
import re
import json

baseURL = "https://zhongyibaike.com"

def getHrefs():
  
  # 从基础页获取所有中药的分页链接，然后对所有Url进行异步请求
  # 获取中药信息，再异步存到文本文件中
  
  # 中药目录界面URL，这个网站做的非常和谐，就把所有链接直接放在一个页面中了
  menuURL = "https://zhongyibaike.com/wiki/%E4%B8%AD%E8%8D%AF%E5%A4%A7%E5%85%A8"
 
  with requests.get(menuURL) as resp:
      tree = etree.HTML(resp.text)
      aList = tree.xpath("/html/body/main/article/section/div//a/@href")  # 得到所有中药的链接
      hrefs = list(map(lambda href: baseURL+href, aList))  # 转化为完整的链接, 此时hrefs中存储了所有中药信息界面的完整信息
      # 异步获取所有界面并将他们的信息记录在本地
      return hrefs
  

async def aioDownLoad(url,session):
  
  # 异步获取网页内容，提取出相关信息，信息界面做的一团糟，
  # 只保证了视觉上的逻辑关系，html文档逻辑关系没有对应上，
  # 所以只能自己去提取，最后结果保存为json文件，每一味中药
  # 对应一个json文件，直接在这里就存了
  try:
      async with session.get(url) as resp:
          tree = etree.HTML(await resp.text())  # 获取网页所有内容
        
          Medicine = {
            "name":0,            # 名称
            "allNames":0,        # 所有别名
            "source":0,          # 来源
            "natural":0,         # 性味
            "process":0,         # 炮制
            "shape":0,           # 性状
            "usage":0,             # 功效
            "jingMai":0,         # 经脉
            "mainUse":0,         # 主治
            "dosage":0,          # 用法用量
            "attention":0,       # 注意禁忌
            "prescription":0,    # 药方
            "image":0            # 表示图片的二进制字节流
          }
          
          # 提取药材名称和药材别名
          Medicine["name"] = str(url).rsplit('/')[-1]
          Medicine["allNames"] = tree.xpath("/html/body/main/article/section/div/div[1]/ol/li/a/text()")  ##获取药材所有的别名 

          # #获取药材图片
          # imageURLs = tree.xpath("/html/body/main/article/section/div/div[1]//img/@src")
   
          # if len(imageURLs)!=0:
          #   async with aiohttp.ClientSession() as session:
          #     async with session.get(imageURLs[0]) as iRe: 
          #        async with aiofiles.open(f"{Medicine['name']}.jpg","w") as f:
          #            f.write(await iRe.content.read())  #保存二进制字节流

          # 这些标签在html中没有内在的逻辑联系，所以直接获取所有文本内容进行筛选
          content = str(tree.xpath("string(/html/body/main/article/section/div/div[2])"))
          content += str(tree.xpath("string(/html/body/main/article/section/div/div[3])"))
          content += str(tree.xpath("string(/html/body/main/article/section/div/div[4])"))
          
          content = str(content).replace(" ",'')  # 去除空格
          content = re.sub("\n+",'\n',content)  # 去除空行

          #在字符串中查询关键字，根据关键字将字符串分割
          attrs = { "source":"来源", "natural":"性味","process":"炮制","shape":"性状","usage":"功效","jingMai":"经脉","mainUsage":"主治","dosage":"用法用量",  "attention":"注意禁忌" }
          splitIndex = []
          #遍历标签，查找对应的关键字
          for key in attrs:
            index = content.find(f'\n{attrs[key]}\n')  
            if index != -1:
               splitIndex.append([key,index])
          splitIndex.append(['',len(content)])        
         
          for i in range(0,len(splitIndex)-1):
            Medicine[splitIndex[i][0]] = content[splitIndex[i][1]:splitIndex[i+1][1]].lstrip(f"\n{attrs[splitIndex[i][0]]}\n")

          #药方独占最后一块，单独拿出来
          Medicine["prescription"] = str(tree.xpath("string(/html/body/main/article/section/div/div[40])"))         
          Medicine["prescription"]  = 0 if len(Medicine["prescription"]) == 0 else Medicine["prescription"]

          #写入文件
          async with aiofiles.open(f"./data-pure-context2/{Medicine['name']}.json","w") as f:
            await f.write(json.dumps(Medicine))
            print("Save successfully")
  
  except Exception as e:
    print(e)
    aioDownLoad(url)
    


async def main():

  # 主函数，通过调用getHrefs生成Url列表，创建任务列表
  # 然后异步完成任务

  tasks = []  # 任务列表
  hrefs = getHrefs()  #获取所有药材对应的url
  print(len(hrefs))
  session = aiohttp.ClientSession()
  for h in hrefs:
    tasks.append(asyncio.create_task(aioDownLoad(h,session)))  #向任务列表中添加元素
  
  await asyncio.wait(tasks)



if __name__ == "__main__":
   asyncio.run(main())
        


  
  
    

 


