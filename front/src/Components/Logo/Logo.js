import { Space } from "antd";
import React from "react";
import { SearchOutlined } from "@ant-design/icons";
import "./Logo.css"

const Logo = (props)=>{
    return  <div className="Logo" onClick={()=>props.onClick()}>
               <Space direction="horizontal" size={10}>
                  <span className="title_logo"><b><i>CMS</i></b></span>
                  <span className="icon_"><SearchOutlined /></span>
                </Space>
            </div>
}

export default Logo;