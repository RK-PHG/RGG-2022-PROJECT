from lxml import etree
import requests
import re

with requests.get("https://zhongyibaike.com/wiki/%E8%91%B1%E9%A1%BB") as resp:
    tree = etree.HTML(resp.text)
    allContents =  tree.xpath("string(/html/body/main/article/section/div/div[2])")
    allContents += tree.xpath("string(/html/body/main/article/section/div/div[3])")
    allContents += tree.xpath("string(/html/body/main/article/section/div/div[4])")
    con = str(allContents).replace(" ",'')
    con = re.sub("\n+",'\n',con)
    
    splitIndex = []
    arrtList = {
        "source":"来源",
        "natural":"性味",
        "process":"炮制",
        "shape":"性状",
        "usage":"功效",
        "jingMai":"经脉",
        "mainUsage":"主治",
        "dosage":"用法用量",
        "attention":"注意禁忌"
    }

    for key in arrtList:
        index = con.find(f'\n{arrtList[key]}\n') 
        if index != -1:
            splitIndex.append([key,index])
    splitIndex.append(['',len(con)])        
    k = len(splitIndex)
    for i in range(0,k-1):
        print(i)
        thiss = con[splitIndex[i][1]:splitIndex[i+1][1]].lstrip(f"\n")
        thiss = thiss.replace(f'{arrtList[splitIndex[i][0]]}\n','')
        print(thiss)
        print("")


    print(splitIndex)
    
    with open('test.txt',"a+") as f:
        f.write(con)
    

   