import React from "react";
import CheckableTag from "antd/es/tag/CheckableTag";
import { attrName } from "../Controler";


const Tags = [ "source","shape","usage","natural","process","jingMai","mainUse","dosage","attention","prescription"];  

const TagArea = (props)=>{

   return(  <div className="tag_area">
                    <CheckableTag key={"name"} checked className="tag">{attrName["name"]}</CheckableTag>
                    {
                      Tags.map((tag=>(
                       <CheckableTag key={tag} checked={props.selectedKeys.indexOf(tag)>-1} onChange={(checked)=>{props.handleChecked(tag,checked)}} className="tag">{attrName[tag]}</CheckableTag>      
                    )))}
            </div> )
        ;

}

export default TagArea;