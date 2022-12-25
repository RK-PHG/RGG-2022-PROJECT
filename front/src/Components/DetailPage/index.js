import { List,Space,Image} from "antd";
import React, { useEffect, useState } from "react";
import attrName from "../Controler/attrName";
import {TagOutlined} from "@ant-design/icons"
import "./DetailPage.css"
import { handleGetDetail } from "../Controler";

const testJson = {
      "name":"铧头草",        
      "allNames":["青地黄瓜","地黄瓜","烙铁草","犁头草"],     
      "source":"为堇菜科植物白花地丁、长萼堇菜或尼泊尔堇菜的全草或带根全草。2～7月有花果时采收。",        
      "natural":"辛微苦，寒。",        
      "process":0,     
      "shape":"叶片三角状卵形或舌状三角形，基部宽心形，稍下延于叶柄，有两垂片，有的两面皆可见少数短毛。花距短囊形，长约2.5cm。",      
      "usage":"为堇菜科植物白花地丁、长萼堇菜或尼泊尔堇菜的全草或带根全草。主治肠痈，疔疮，红肿疮毒，黄疸，淋浊，目赤生翳。",       
      "jingMai":"大肠，心，肝经。",     
      "mainUse":"清热解毒，散瘀消肿。主治肠痈，疔疮，红肿疮毒，黄疸，淋浊，目赤生翳。",    
      "dosage":"内服：煎汤，9-15g；鲜品30-60g。外用：适量，捣敷",      
      "attention":"《南宁市药物志》：虚寒者忌服。",     
      "prescription":"①治肠痈：铧头草、红藤煎汤服。（《四川中药志》）②治恶疮疔毒，红肿疼痛：鲜铧头草，捣烂外敷。（成都《常用草药治疗手册》）",    
}

/** Detail Page */
const Detail = (props)=>{
    
    
   
    const ToHTML = (info_) => {
       if(props.KeyWords == undefined)
           return info_

        var info = info_;
        for(let i=0;i<props.KeyWords.length;i++){
            for(let j=0;j<info.length;j++){
                if(props.KeyWords[i]===info[j]){
                    if(j==0){
                        info='<span style="color: #f73131">'+info[j]+'</span>'+info.slice(j+1, info.length-1)
                        j+='<span style="color: #f73131"></span>'.length
                    }else if(j==info.length-1){
                        info=info.slice(0,j-1)+'<span style="color: #f73131">'+info[j]+'</span>'
                        j+='<span style="color: #f73131"></span>'.length
                    }else{
                        info=info.slice(0,j-1)+'<span style="color: #f73131">'+info[j]+'</span>'+info.slice(j+1, info.length-1)
                        j+='<span style="color: #f73131"></span>'.length
                    }                    
                }
            }
        }
        return info;
    }
    
 
    const getItems = ()=>{
        var ListItems = [];
        for(var key in props.Json){
            if(key=="Image"){
                ListItems.push({"title":"图片","value":<img className="image" width={"50%"} src={"data:;base64,"+props.Json[key]}/>})
                continue;
            }
           
            if(props.Json[key]!=0){

                if(key=="allNames"){
                    var value = "";
                    for(var s in props.Json[key]){
                        value += (props.Json[key][s]+" ");
                    }
                    ListItems.push({"title":attrName[key],"value":value});
                    continue
                }
                var value_html = ""            
                var Ts = []
                if(props.Tags!=undefined)
                     Ts = props.Tags
                if(props.KeyWords&&props.Tags&&Ts.indexOf(key)!==-1){
                    value_html = ToHTML(props.Json[key])
                }else{
                    value_html = props.Json[key]
                }
                ListItems.push({"title":attrName[key],"value":value_html});
            }
        }
        return ListItems;
    }

    return(<div>
             <List header={<div className="header"><Space size={10}>
                               <span className="title"><TagOutlined/></span>
                               <span className="title">{props.Json.name}</span></Space>
                           </div> }
                   dataSource={getItems()}
                   bordered={false}
                   className="detail"
                   itemLayout="vertical"
                   size="large"
                   split={false}
                   renderItem={(item)=>(
                      <List.Item 
                        style={{textAlign:"left"}}
                        >
                        <List.Item.Meta
                          title={<h3 className="attr">{item.title}</h3>}
                        ></List.Item.Meta>
                        <div className="info">
                             {
                                item.title=="图片"?(item.value):
                              <div dangerouslySetInnerHTML={{__html:item.value}}/>
                             }
                            </div>
                      </List.Item>                   
    )}
                   >               
             </List>
           </div>);
}

export default Detail;

