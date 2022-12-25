import { useState } from "react";
import SearchInput from "../SearchInput";
import TagArea from "../TagArea";
import React from "react";
import { autoComplete } from "../Controler";


const SearchArea = (props) => {


   const [medicineOptions, setMedicitionOptions] = useState("no_data");

   const [tagSelected, setTagSelected] = useState([]);

   const [logic, setLogic] = useState("and");

   const change = (value) => {

      autoComplete(value, tagSelected, logic).then(
         (resp) => {
            if (resp.data.length != 0)
               setMedicitionOptions(resp.data)
            else
               setMedicitionOptions("no_data");
         }
      ).catch(err => {
         setMedicitionOptions("no_data");
      })

   }

   const search = (value) => {

      var value_ = value.trim(); 
      props.handleSearch(value_, tagSelected, logic);
   }

   const handleSetLogic = (value) => {
      setLogic(value)
   }


   const handleSelectTags = (tag, checked) => {

      const newList = checked ? [...tagSelected, tag] : tagSelected.filter((t) => t !== tag);

      setTagSelected(newList);
   }

   return (<>
      <TagArea selectedKeys={tagSelected} handleChecked={handleSelectTags}></TagArea>
      <div className="search_input">
         <SearchInput
            handleSetLogic={handleSetLogic}
            handleSearch={search}
            handleChange={change}
            handleDetail={props.handleDetail}
            medicineOptions={medicineOptions}></SearchInput></div>
   </>)
}

export default SearchArea;