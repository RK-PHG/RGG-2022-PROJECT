# 文件说明： 这是一个数据爬虫，为满足软件工程管理课程设计
# 需要，爬取中医药数据，作为自建网站数据源。爬取网站为： 
# https://zhongyibaike.com/  中医百科网

# 创建于2022年10月22日

from contextlib import nullcontext
from imp import reload
from time import sleep
from xml.dom.minidom import AttributeList
import aiofiles
import aiohttp
import asyncio
from lxml import etree
import requests


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
  
  # 访问单味药材主页, 获取图片url

  try:
      async with session.get(url) as resp:
        
          tree = etree.HTML(await resp.text())  # 获取网页所有内容
          #获取药材图片
          imageURLs = tree.xpath("/html/body/main/article/section/div/div[1]//img/@src")
          
          if len(imageURLs)!=0: 
             async with aiofiles.open("list.txt","a+",encoding="utf-8") as f:
                await f.write(imageURLs[0]+'\n')
                print("Save href successfully")
          
  except Exception as e:
     print(e)
     aioDownLoad(url)
    


async def main():

  # 主函数，通过调用getHrefs生成Url列表，创建任务列表
  # 然后异步完成任务

  tasks = []  # 任务列表
  hrefs = getHrefs()  #获取所有药材对应的url
  session = aiohttp.ClientSession()
  for h in hrefs:
      tasks.append(asyncio.create_task(aioDownLoad(h,session)))  #向任务列表中添加元素
      await asyncio.wait(tasks)



if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
        


  
  
    

 


