import React, { useState } from "react";
import { AutoComplete, Input, Popover, Select, InputNumber, Calendar } from "antd";
import PopoverContent from "../PopoverCentent";


/** the search input*/
const SearchInput = (props) => {
   console.log(props.medicineOptions)
   return (<>
      <Input.Group compact>
         <Select style={{ width: "80px" }} 
                 size="large"
                 defaultValue={"or"}
                 defaultActiveFirstOption={"或"} 
                 onChange={(value)=>{props.handleSetLogic(value)}}>
            <Select.Option value="and">与</Select.Option>
            <Select.Option value="or">或</Select.Option>
         </Select>
         <AutoComplete style={{ width: "400px" }} 
         onChange={(value)=>{props.handleChange(value)}}
         onSelect={(value)=>{props.handleDetail(value)}}
         options={
         props.medicineOptions!="no_data"?(
          props.medicineOptions.map((m) =>
         ({
            value: m.name,
            label: (<PopoverContent name={m.name} src={m.src} disp={m.natural!=="0"?(m.name + "," + m.natural):m.name}></PopoverContent>)
         }))):""
      }>

            <Input.Search size="large"  onSearch={(value)=>{ props.handleSearch(value)}}></Input.Search>
         </AutoComplete>
      </Input.Group>
   </>);
}

export default SearchInput;

