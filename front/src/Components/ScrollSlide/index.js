import React,{useState,useEffect} from "react"
import { Carousel } from "antd"
import SlidePage from "./SlidePage"
import { getRandom } from "../Controler"
import NoData from "./NoData"

const testMedicine = [
  {
    "src":"",
    "allName":[],
    "name":"",
    "natural":""
  }
]


/** scroll slides */
const ScrollSlides = (props)=>{
  /** Home List */
  const[MList,setMList] = useState([]);

  /** refresh after a piece of time*/
  useEffect(()=>{
      refresh();
  },[])

  /** refresh */
  const refresh = (props)=>{
      getRandom().then(
        res=>{
           setMList(res)
           console.log(res);
        }).catch(err=>{
        setMList([])
      })
  }


    return(<Carousel 
              effect="fade"
    
              >{
              MList.length!==0?(
              MList.map((m)=>(
                <SlidePage bk_color = {props.bk_color} handleDetail={props.handleDetail} imgSrc={m.src} allNames={m.allNames} name={m.name} natural={m.natural} ></SlidePage>
              ))):(<NoData></NoData>)
              }
           </Carousel>)
}

export default ScrollSlides;
