import React, { useEffect, useState } from "react";
import { PageHeader, PageFooter, Loading,HomeRight, ScrollSlides, HomeLeft, MenuBar, SearchList, Detail, SearchArea, Logo } from "../../Components";
import 'antd/dist/reset.css';
import './home.css'
import { Divider, Layout, Skeleton, Space } from "antd";
import { Content } from "antd/es/layout/layout";
import { handleGetDetail, handleSearch } from "../../Components/Controler";
import { message } from "antd";
import a1 from "../../imgbk.webp"
import a2 from "../../imgbk3.webp"


const HomePage = (props) => {
   return (<>
      <Content className="scroll_slides"><ScrollSlides  handleDetail={props.handleDetail}></ScrollSlides></Content>
      <Layout.Sider className="page_right"> <HomeLeft Search={props.Search}></HomeLeft></Layout.Sider>
   </>);
}

const ResultPage = (props) => {
   console.log(props.KeyWords);
   return (<SearchList data={props.list} useTime={props.useTime} Tags={props.Tags} handleDetail={props.handleDetail} KeyWords={props.KeyWords}></SearchList>);
}

const DetailPage = (props) => {
   console.log("sdfs")
   console.log(props.Tags)
   return (<Detail Json={props.Json} Tags={props.Tags} KeyWords={props.KeyWords}></Detail>);
}


/** Main Page */
const Home = (props) => {


   const [pageId, setPageId] = useState(0)
   const [page, setPage] = useState(<HomePage></HomePage>)
   const [resultList, setRList] = useState({})
   const [color,setColor] = useState("rgba(140, 246, 197, 0.2)");
   const [img,setImg] = useState(a1);

   useEffect(
      ()=>{
         const colors = ["rgba(247, 226, 40, 0.4)","rgba(140, 246, 197, 0.4)",]
         const imgs = [a2,a1]
         var index = 0;            
         setInterval(
            ()=>{
               index = (index+1)%2;
               document.getElementById("main").style.backgroundImage =  "url("+imgs[index]+")"
               document.getElementById("center_img").style.backgroundImage = "url("+imgs[index]+")"
               document.getElementById("info_area_scroll").style.backgroundColor = colors[index]               
               document.getElementById("page_footer").style.backgroundColor = colors[index]               
               document.getElementById("page_header").style.backgroundColor = colors[index]  
               setColor(colors[index])           
               setImg(imgs[index])  

            },10000
         )
         setPage(<HomePage handleDetail={toDetail} Search={toResult} bk_color={color}></HomePage>)
      },[]
   )

   /** drump to the detail index */
   const toDetail = (name,KeyWords,tags) => {
      document.title=name
      var lastPage = page;
      // setPage(<Skeleton active style={{ height: "100%" }} />);
      setPage(<Loading></Loading>);
      handleGetDetail(name).then(res => {
         setPage(<DetailPage Json={res.data} KeyWords={KeyWords} Tags={tags}></DetailPage>)
         setPageId(2);
         message.success("加载成功")
      }).catch(() => {
         setPage(lastPage);
      })
   }


   /** drump to the result page */
   const toResult = (key, tags, logic) => {
      document.title="搜索结果"
      key = key.replaceAll(" ","");
      var lastPage = page;
      // setPage(<Skeleton active style={{ height: "100%" }} />);
      setPage(<Loading></Loading>);
      handleSearch(key, tags, logic).then(res => {
         message.success("搜索成功, 耗时"+res.data["time"]+"s")
         setPage(<ResultPage list={res.data["mList"]} useTime={res.data["time"]} handleDetail={toDetail} Tags={tags} KeyWords={key}></ResultPage>)
         setPageId(1);
      }).catch(() => {
         setPage(lastPage);
      })

   }


   /** drump to Home Page */
   const toHome = (props) => {
      document.title="CMSS-首页"
      setPage(<Skeleton active style={{ height: "100%" }} />);
      setPage(<HomePage handleDetail={toDetail} Search={toResult} bk_color={color}></HomePage>);
      setPageId(0);
   }


   return (<div className="home_root">
      <PageHeader><Logo onClick={toHome}></Logo></PageHeader>
      <div className="search_area">
         <SearchArea handleSearch={toResult} handleDetail={toDetail}></SearchArea>
         <Divider className="main_divider"></Divider>
         <div id="main">
         <MenuBar toHome={toHome} mId={pageId}></MenuBar>
            <Layout className="main_context_area" >
               <Layout.Sider className="page_left"> <HomeRight handleSelect={toDetail}></HomeRight></Layout.Sider>
               {page}
            </Layout>
         </div>
      </div>
      <PageFooter>
           <Space direction="vertical" size={10}>
             <div>Developed by Team 14, 2022 Software Engneering Management, 浙江大学.</div>
             <div>黄可欣, 李毅桐, 张天涵, 李裕辰, 米恩京</div>
            </Space>
      </PageFooter>
   </div>
   );
}

export default Home;