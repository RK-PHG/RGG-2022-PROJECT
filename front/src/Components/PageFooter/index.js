import React from "react";
import './PageFooter.css';

const PageFooter = (props)=>{
    
    return(<div id="page_footer">{props.children}</div>);
}

export default PageFooter;