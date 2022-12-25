import React from 'react'
import { useEffect, useState } from 'react';
import axios from 'axios'
import './Searchlist.css'
import { Divider, List, Tag} from 'antd'
import { SearchOutlined } from '@ant-design/icons';
import { handleSearch } from '../Controler';
import {attrName} from '../Controler';

const Searchlist = (props) => {
    const ToHTML = (info_) => {
        var info = info_;
        for(let i=0;i<props.KeyWords.length;i++){
            for(let j=0;j<info.length;j++){
                if(props.KeyWords[i]===info[j]){
                    if(j==0){
                        info='<span style="color: #f73131">'+info[j]+'</span>'+info.slice(j+1, info.length-1)
                        j+='<span style="color: #f73131"></span>'.length
                    }else if(j==info.length-1){
                        info=info.slice(0,j-1)+'<span style="color: #f73131">'+info[j]+'</span>'
                        j+='<span style="color: #f73131"></span>'.length
                    }else{
                        info=info.slice(0,j-1)+'<span style="color: #f73131">'+info[j]+'</span>'+info.slice(j+1, info.length-1)
                        j+='<span style="color: #f73131"></span>'.length
                    }                    
                }
            }
        }
        return info;
    }

    return (
                <div className='under_left_search'>
                    <div className='tags_area'>
                       <div className='tags'><span className='tags_title'>已选标签：</span><Tag className='tag_below'>名称</Tag>{props.Tags.map(tag=>(<Tag className='tag_below'>{attrName[tag]}</Tag>))}</div>
                    </div>
                    <div className='under_list'>
                        <List
                            header={
                                <div style={{textAlign:"left"}}>
                                    <h3><SearchOutlined style={{ fontSize: '15px' }} /> 搜索到 <span className='cue'>{props.data.length}</span > 条数据, 用时 <span className='cue'>{props.useTime}</span> s</h3>
                                    <Divider className='divider' />
                                </div>
                            }
                            itemLayout="vertical"
                            size="large"
                            // split={false}
                            pagination={{ pageSize: 4 }}
                            dataSource={props.data}
                            renderItem={(item,index) => (
                                <List.Item
                                    style={{textAlign:"left"}}
                                    key={item.name}
                                    extra={
                                        <div>
                                            <div><br /></div>
                                            <img
                                                className='result_picture'
                                                onClick={()=>{ props.handleDetail(item.name,props.KeyWords,props.Tags);}}
                                                width={200}
                                                alt="logo"
                                                src={"data:;base64,"+item.src}
                                            />
                                        </div>
                                    }
                                >
                                    <List.Item.Meta
                                        title={<a onClick={() => { props.handleDetail(item.name,props.KeyWords,props.Tags);  }}>{item.name}</a>}
                                        description={<div dangerouslySetInnerHTML={{__html:ToHTML(item.name+item.natural)}}/>}
                                    />
                                    <div className='info_area'><div dangerouslySetInnerHTML={{__html:ToHTML(item.source)}}/></div>
                                </List.Item>
                            )}
                        />
                    </div>
                </div>
    )
}

export default Searchlist
