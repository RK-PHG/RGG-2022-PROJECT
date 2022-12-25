import React from "react";
import "./poverinfo.css"

const PopoverContent = (props)=>{
    
    return(<div className="popover_content">     
            <div className="popover_img"><img src={"data:;base64,"+props.src}></img></div>
            <div className="popover_info_t" style={{widht:"300px"}}>{props.disp}</div>
          </div>);
 };    
 

export default PopoverContent;

