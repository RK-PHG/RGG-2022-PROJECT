import React, { useEffect } from "react";
import { Image, Space } from "antd";
import "./ScrollSlide.css"
import { Content } from "antd/es/layout/layout";
import { TagOutlined } from "@ant-design/icons";

const SlidePage = (props) => {
  return (<div className='slides_page' >
    <Content>
      <div className='slides_img_area'>
        <div id="center_img">
          <a><img className='slides_img' onClick={() => { props.handleDetail(props.name) }} src={"data:;base64," + props.imgSrc} fallback={""}></img></a>
        </div>
      </div>
    </Content>
    <div id='info_area_scroll' style={{backgroundColor:props.bk_color}}>
      <Space size={8}>
        <a style={{color:"green"}}><div className='info_line' onClick={() => { props.handleDetail(props.name)}} ><Space size={5}><span><TagOutlined/></span><span><span>{"名称:   "}</span>{props.name}</span></Space></div></a>
      </Space>
    </div>
  </div>);
}
export default SlidePage;