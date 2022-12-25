import React from "react";
import { Menu } from "antd";
import "./MenuBar.css"

const MenuItemsHome = [
    {label:"首页",key:"home"},
    {label:"药材大全",key:"AllMedicines"}
]
const MenuItemsResult = [
    {label:"首页",key:"home"},
    {label:"搜索结果",key:"result"},
    {label:"药材大全",key:"AllMedicines"}
]
const MenuItemsDetail = [
    {label:"首页",key:"home"},
    {label:"详情页",key:"detail"},
    {label:"药材大全",key:"AllMedicines"}
]

const menus = [MenuItemsHome,MenuItemsResult,MenuItemsDetail];
const selected = ["home","result","detail"];

const MenuBar = (props)=>{
    
    const handleClick = (key)=>{
        switch(key.key){
            case "home":
                props.toHome();
                break;
            default:
                break;            
        }
    }

    return( 
            <Menu selectedKeys={[selected[props.mId],]} items={menus[props.mId]} mode="horizontal" className="menu" onSelect={(key)=>{handleClick(key)}}></Menu>
        )
}

export default MenuBar;