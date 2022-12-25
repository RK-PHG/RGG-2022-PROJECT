import axios from "axios";
import server_config from "../../network-config";
 

/* return a 10 pieces of data */
async function getRandom (){
   
  var mList =null;
  try{
     const response = await axios.get(server_config.server_ip+'/random');
     mList = response.data;
     mList = mList.filter(m=> m.src!==0)
      
  }catch(err){
     mList = null;
  }
  return mList; 

}

export default getRandom;


