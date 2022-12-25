import axios from "axios";
import server_config from "../../network-config";

//handle the search
async function handleSearch(words, tags, logics){
    
    var response = null;
    try{
       const resp =  axios.get(server_config.server_ip+"/search",
        {  
           params:{ 
              "words":words,
              "tags":JSON.stringify(tags),
              "logic":logics
           }
        });
        
        response = resp;
 
    }catch(err){
 
    } 
    return response;
}


export default handleSearch;