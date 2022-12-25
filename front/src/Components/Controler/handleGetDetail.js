import axios from "axios";
import server_config from "../../network-config";

/** handle get detail */
async function handleGetDetail(key){
    var response = null;
    try{
    
       const resp =  axios.get(server_config.server_ip+"/medicines/"+key);
        response = resp;
 
    }catch(err){
 
    } 
    return response;
}

export default handleGetDetail;
