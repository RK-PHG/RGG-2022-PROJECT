import React from 'react'
import { SetStateAction, useEffect, useState } from 'react';
import axios from 'axios'
import { Link, useNavigate, useParams } from 'react-router-dom'
import { FrownOutlined, MehOutlined, SmileOutlined, BarsOutlined, TagOutlined, FileTextOutlined, CaretRightOutlined } from '@ant-design/icons';
import { Rate, Divider, List } from 'antd'
import './singleinfo.css'
import Item from 'antd/es/list/Item';

const SingleInfo = () => {
    // const Navigate = useNavigate()
    const [smile_disable, setSmile] = useState(false)
    const [rd_data, setrddata] = useState([{
        title: '',
        description: '',
        content: '',
        usage: '',
        info: '',
    }])

    const [herb_info, setherbinfo] = useState({
        name: '',
        allname: [''],
    })


    useEffect(() => {
        const initdata = async () => {
            axios
                .get('/test/2.json')
                .then(response => {
                    let temp = response.data
                    temp = [...temp]
                    setrddata(temp)
                });
            axios
                .get('/test/ex.json')
                .then(response => {
                    let temp = herb_info
                    temp.name = response.data.name
                    temp.allname = response.data.allNames
                    temp.info = response.data.attention
                    temp.usage = response.data.usage
                    temp = [...temp]
                    setherbinfo(temp)
                });
        }

        initdata();
    }, [])

    const tospecific = (id) => {
        // Navigate('/single/' + id)
    }

    const customIcons = {
        1: <FrownOutlined rotate={330} />,
        2: <FrownOutlined rotate={350} />,
        3: <MehOutlined />,
        4: <SmileOutlined rotate={10} />,
        5: <SmileOutlined rotate={30} />,
    };

    return (
        <div className='singlecard'>
            <div className='under_right_single'>
                <div className='main_info_single'>
                    <div className='info_left'>
                        <h1><TagOutlined style={{ fontSize: '28px' }} /> {herb_info.name} </h1>

                        <div className='main_info_down'>
                            <p style={{ fontSize: '16px' }}><CaretRightOutlined /> <strong>别名：</strong>付致胶，阿胶珠，蛤粉炒阿胶，傅致胶，盆覆胶，驴皮胶，东阿胶，陈阿胶，覆盆胶 </p>
                            <p style={{ fontSize: '16px' }}><strong>产地：</strong>山东东阿</p>
                            <p style={{ fontSize: '16px' }}><strong>形状：</strong>呈整齐的长方形块状，通常长约8.5厘米，宽约3.7厘米，厚约0.7或1.5厘米。表面棕黑色或乌黑色，平滑，有光泽。对光照视略透明。质坚脆易碎，断面棕黑色或乌黑色，平滑，有光泽。气微弱，味微甜。以色乌黑、光亮、透明、无腥臭气、经夏不软者为佳。 </p>
                            <p style={{ fontSize: '16px' }}><strong>治疗疾病：</strong>{herb_info.usage}</p>
                        </div>
                    </div>
                    <div className='info_right'>
                        <img
                            width={350}
                            alt="logo"
                            src="https://gw.alipayobjects.com/zos/rmsportal/mqaQswcyDLcXyDKnZfES.png"
                        />
                    </div>
                    <div className='clear' />
                </div>

                <div className='specific_single'>
                    <div className='specific_info'>
                        <h2><FileTextOutlined /> 详细信息</h2>
                        <p>{herb_info.info}</p>
                    </div>
                </div>

                <div className='evaluate_single'>
                    <div className='evaluate_title'><div className='evaluate_title_text'>您愿意向朋友推荐本条目吗？</div></div>
                    <div className='evaluate_icon'>
                        <Rate id='smile_icon'
                            defaultValue={0}
                            character={({ index }) => customIcons[index + 1]}
                            style={{ fontSize: 32 }}
                            disabled={smile_disable}
                            onChange={() => { setSmile(true); alert('感谢您的评价') }} />
                    </div>

                </div>


            </div>

        </div>

    )
}

export default SingleInfo;