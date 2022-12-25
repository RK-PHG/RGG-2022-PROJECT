import React from "react";
import "./HomeLeft.css";
import { Card, List,Tag} from "antd";

const Tags = [{"attr":"natural","title":"性味","tags":["寒","温热","辛辣","甜","苦","清火","解毒"]},
              {"attr":"jingMai","title":"归经","tags":["胃","头经","大肠经","脾经","肝经"]},]
          
const HomeLeft = (props)=>{
    
    return(<div className="home_page_right">
                 <List
                    header={<div>{"标签"}</div>}
                    size="large"
                    bordered
                    dataSource={Tags}
                    renderItem={(item) => (
                     <List.Item>
                        <Card title={item.title}>
                        {item.tags.map((tag)=>(
                           <Tag.CheckableTag style={{margin:"7px"}} onClick={()=>{props.Search(tag,[item.attr,],"or");}}>{tag}</Tag.CheckableTag>
                        ))}</Card>
                     </List.Item>
                  )}/>
           </div>);
}

export default HomeLeft;
