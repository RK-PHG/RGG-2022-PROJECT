#该文件用于实现路由，请求的响应等
import mindex
from flask import Flask

app = Flask(__name__)

index = mindex.indexDeserialize() #得到药材的索引

#主界面
@app.route("/")
def index():
    pass

#搜索结果界面
@app.route("/search/")
def result():
    pass

#详情界面
@app.route("/details/<medicine_name>")
def details(medicine_name):
    pass

#请求图片
@app.route("/pictures/<medicine_name>")
def getImage(medicine_name):
    pass

#随机返回
@app.route("/radom/")
def radomMessage():
    pass

#处理搜索
@app.route("/search/")
def search():
    pass

#处理返回单味药材的信息
@app.route("/medicines/<medicine_name")
def getMedicines():
    pass

