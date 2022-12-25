import React, { useEffect,useState } from "react";
import "./HomeRight.css";
import { Divider,List,Typography,Popover,Image,Space,Spin } from "antd";
import  {RedoOutlined} from "@ant-design/icons"
import { unstable_renderSubtreeIntoContainer } from "react-dom";
import {getRandom} from "../Controler";


/** Pover Card */
const PopoverContent = (props)=>{
   return(<div className="popover_content">     
           <div className="popover_img" ><img src={"data:;base64,"+props.src} ></img></div>
           <div className="popover_info"  >{props.disp}</div>
         </div>);
};    

/** Random Bar */
const HomeRight = (props)=>{

   const[isLoading,setIsLoading] = useState(false)
   
   /** Home List */
   const[MList,setHomeList] = useState([]);


   /** refresh after a piece of time*/
   useEffect(()=>{
       refresh();
       setInterval(()=>{refresh();},1000000);
   },[])
   
   /** refresh */
   const refresh = (props)=>{
       getRandom().then(
         res=>{
            setHomeList(res)
            setIsLoading(false)
         }).catch(err=>{
         setHomeList([{"src":"","allNames":[],"name":"","natural":""}]);
         setIsLoading(false)
       })
   }

    return(<div className="home_page_right">
                 <List 
                    style={{backgroundColor:"white",textAlign:"center"}}
                    
                    header={<div className="sider_header">
                                 <Space size={10}>
                                    <span className="sider_title_font">{"可能感兴趣的"}</span>
                                    <span className="sieder_title_font"
                                       >{ isLoading?<Spin/>:
                                           <RedoOutlined onClick={()=>{refresh();setIsLoading(true)}} className="refresh_icon"/>
                                        }
                                    </span>
                                 </Space>
                                 <Divider className="divider"></Divider>
                              </div>}
                    footer={<span className="footer">查看更多</span>}
                    size="large"
                    itemLayout="horizontal"
                    bordered={false}
                    split={false}
                    dataSource={MList}

                    renderItem={(item,index) => (
                     <List.Item style={{backgroundColor:"white"}} key={item.name} onClick={()=>{props.handleSelect(item.name);}}>
                        <Popover placement="left" 
                                 content={<PopoverContent 
                                               src={item.src} 
                                               disp={item.natural!=="0"?(item.name+","+item.natural):item.name}
                                               onClick={()=>{props.handleSelect(item.name);}}
                                               >
                                          </PopoverContent>}>
                                          <a href="javascript:void(0)">
                                          <span>{(index+1)+". "}</span>{item.name}</a>
                        </Popover>
                     </List.Item>
                  )}/>
           </div>);
}

 

export default HomeRight;
