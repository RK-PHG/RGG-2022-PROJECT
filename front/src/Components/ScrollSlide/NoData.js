import React from "react"
import { Spin } from "antd"
import "./ScrollSlide.css"
import { LoadingOutlined } from "@ant-design/icons"

const NoData = ()=>{
    return (
      <div className="loading">
         <Spin
          indicator={
            <LoadingOutlined
            style={{
              fontSize: 100,
            }}
            spin
          />
          } 
          className="Spin"/>
      </div>
    )
}

export default NoData;
