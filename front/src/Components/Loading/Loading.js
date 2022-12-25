import React from "react";
import { LoadingOutlined } from "@ant-design/icons";
import { Spin } from "antd";
import "./Loading.css"
 
const Loading = ()=>{
    return (
        <div className="load">
           <Spin
            indicator={
              <LoadingOutlined
              style={{
                fontSize: 100,
              }}
              spin
            />
            } 
            className="spi"/>
        </div>
      )
}

export default Loading;