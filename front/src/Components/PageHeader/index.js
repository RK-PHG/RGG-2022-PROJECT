import React, { useEffect, useRef } from 'react';
import './PageHeader.css';
import B1 from "./Image/partten1.jpg"
import B2 from "./Image/Pattern2.webp"


/** Page's header */
const backgroundImages = [];
const PageHeader = (props)=>{
    
    const headerRef = useRef();  //header

    /** set the bacground switch effect */
    useEffect(()=>{
        var index = 0;
        setInterval(()=>{
            //set the header's background image
            // headerRef.current.style.backgroundImg = "url("+backgroundImages[(index++)%2]+")";  
        },40000)
    });

    return(<div id='page_header' ref={headerRef}>{props.children}</div>)
}

export default PageHeader;

