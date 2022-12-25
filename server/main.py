# 对前端的细节比较不熟悉，所以没有写处理搜索和处理搜索框
# 如果是单纯的根据药名和属性名搜索，直接调用getMedicine这个函数
# 如果要实现模糊搜索，应该是先使用倒排索引返回一个id列表，再根据getMedicineById这个函数进行搜索

from flask import Flask, jsonify, request,render_template
from db_manager import getMedicine
from db_manager import randomName
import db_manager
from flask_cors import *
from mindex import indexDeserialize
from search import searchAll
import json
import time
app = Flask(__name__)
CORS(app, supports_credentials=True)

mIndex = 0


# 引入“暂无图片“这张图片的base64编码
from no_image import noImage
app.config['JSON_AS_ASCII'] = False


@app.route("/medicines/<medicine_name>")
def getMedicines(medicine_name):
    tags = []
    # 属性为空表示返回所有属性
    medicine = getMedicine(medicine_name, tags)
    if medicine['Image'] is not None:
        img_stream = medicine['Image'].decode('ascii')
        medicine['Image'] = img_stream

    return jsonify(medicine)


@app.route("/random/")
def randomMessage():
    # medicine是一个字典，里面有除了image之外的药材所有属性
    # medicine_dict是一个字典，只有一个key值，每个key值对应一种药材的信息
    name_list = []
    mList = []
    try:
        # 此处可以设置返回药材的数目
        for i in range(0,13):
            medicine = randomName()
            while medicine['name'] in name_list:
                medicine = randomName()
            name_list.append(medicine['name'])
            if medicine['Image'] is not None:
                img_stream = medicine['Image'].decode('ascii')
                medicine['Image'] = img_stream
            else:
                medicine['Image'] = 0
            mList.append({
               "src":medicine['Image'],
               "natural": medicine["natural"],
               "name":medicine["name"],
               "allNames":medicine["allNames"]  
            })
    except Exception as e:
        print(e)
    return mList


@app.route("/pictures/<medicine_name>")
def getPicture(medicine_name):
    tags = ['Image']
    # 属性为空表示返回所有属性
    medicine = getMedicine(medicine_name, tags)
    if medicine['Image'] is not None:
        img_stream = medicine['Image'].decode('ascii')
        medicine['Image'] = img_stream
    else:
        medicine['Image'] = noImage
    return medicine["Image"]

#处理输入框
@app.route("/preProcess/")
def preProcess():
    words = request.args.get("words") # the search words
    tags =  request.args.get("tags")  # the tags
    tags = json.loads(tags)  #the loads
    if(tags.count("name")!=0):
       tags.remove("name")
    if len(tags)!=0:
     idList = searchAll(mIndex,tags,words,1)
    else:
        idList = []
    names = []
    if(idList==-1):
        idList=[]
    mList = []
    m = db_manager.getMedicine(words,["name","natural","allNames",'Image'])
    if m!= "not found":
         if m['Image'] is not None:
            img_stream = m['Image'].decode('ascii')
            m['Image'] = img_stream
         else:
            m['Image'] = noImage
         names.append(m["name"])
         mList.append({"name":m["name"],'src':m["Image"],'natural':m["natural"],'allNames':m["allNames"]})
    for i in range(min(len(idList),10)):
       m = db_manager.getMedicineById(idList[i]+1,["name","natural","allNames",'Image']);
       if m['Image'] is not None:
            img_stream = m['Image'].decode('ascii')
            m['Image'] = img_stream
       else:
            m['Image'] = noImage
       if len(m)!=0 and names.count(m["name"])==0:
          mList.append({"name":m["name"],'src':m["Image"],'natural':m["natural"],'allNames':m["allNames"]})

    if(len(mList)==0):
        mList=[]
    return mList



#处理搜索
@app.route("/search/")
def search():
    time_S = time.time()
    words = request.args.get("words") # the search words
    tags =  request.args.get("tags")  # the tags
    logic = request.args.get("logic")
    if logic=="or":
        logic = 1
    else:
        logic = 2
    tags = json.loads(tags)  #the loads
    if tags.count("name")!=0:
      tags.remove("name")
    if len(tags)!=0:
       idList = searchAll(mIndex,tags,words,logic)
    else:
       idList = []
    if(idList==-1):
        idList=[]
    mList = []
    names = []
    m = db_manager.getMedicine(words,["name","natural","source",'Image'])
    if m!= "not found":
         if m['Image'] is not None:
            img_stream = m['Image'].decode('ascii')
            m['Image'] = img_stream
         else:
            m['Image'] = noImage
         names.append(m["name"])
         mList.append({"name":m["name"],'src':m["Image"],'natural':m["natural"],'source':m["source"]})
    for i in range(len(idList)):
       m = db_manager.getMedicineById(idList[i]+1,["name","natural","source",'Image']);
       if m['Image'] is not None:
            img_stream = m['Image'].decode('ascii')
            m['Image'] = img_stream
       else:
            m['Image'] = noImage
       if len(m)!=0 and names.count(m["name"])==0:
          mList.append({"name":m["name"],'src':m["Image"],'natural':m["natural"],'source':m["source"]})

    if(len(mList)==0):
        mList=[]
    time_E = time.time()
    return {
             "mList":mList,
             "time":round(time_E-time_S,3)
           }


@app.route("/")
def index():
    medicine = randomName()
    if medicine['Image'] is not None:
        img_stream = medicine['Image'].decode('ascii')
        medicine['Image'] = img_stream
    else:
        medicine['Image'] = noImage

    # 以下是flask使用的jinja2模板的写法，
    # return render_template('index.html', medicine=medicine)
 
if __name__ == "__main__":
    mIndex =  indexDeserialize()
    app.run()
