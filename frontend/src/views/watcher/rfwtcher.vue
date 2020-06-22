<template>
  <div id="main_page">
      watcher
  </div>

  
</template>

<script>
export default {
    name:"rfwtcher",
    props:{
       test:String,
       Plcontext:String,
    },

    mounted() {
      // init context.
      this.Plcontext = "请输入订单的trade_no";
      this.Plcontext2 = "请输入要修改的时间";
      this.err_1 = "没有查到对应的token，请确认user_id是否正确";
      this.err_2 = "没有查到对应的订单，请确认trade_no是否正确";
      

      // init func.
    },

    data() {
        return {
          prourl:'',//后端接口的ip；
          input1:'',                        //测试环境需要查询的trade_no；
          input2:'',                        //测试环境需要修改的trade_no；
          selectNum:'',                     //select字段选择数据的传值
          mTime:'',                         //需要修改时间的传值
          getTradeResult:'',                //查询的接口返回值
          usertoken:'',                     //userToken
          backup:'',                        //备用参数字段
        }
    },

    methods: {
        getTrade:function(arg){
          if (this.input1 == '') {
            alert(this.Plcontext);          //非空判断
            return -1;
          }
          // 测试环境获取订单接口
          this.axios.get(this.prourl+'/api/getV2?mtradeno='+this.input1).then((response)=>{
                console.log(response);
                if (response.data == 'err2') {
                  alert(this.err_2);
                  return -1
                }
                this.getTradeResult=response.data;
                
                }).catch((response)=>{
                console.log(response);
                })
        },

        changeTrade:function(arg){
          if (this.input2 == '') {
            alert(this.Plcontext);          //非空判断
            return -1;
          }
          
          console.log(arg); 
          if (((arg == '2')|| (arg == '3') || (arg== '4')) && (this.mTime == '')) {
            alert(this.Plcontext2);
            return -1;
          }
          this.query = 'mselect='+this.selectNum+'&mtradeno='+this.input2+'&mtype='+arg+'&mtime='+this.mTime;
          console.log(this.query);
          this.axios.get(this.prourl+'/api/changeV2?'+this.query).then((response)=>{
                console.log(response.data);
                // 判断是否有usertoken字段
                if (response.data.search('XHJ') != -1) {
                  this.usertoken = response.data;
                }
                if (response.data.search('errtoken') != -1) {
                  alert(this.err_1);
                }
            }).catch((response)=>{
                console.log(response);
            })
            
        },

        // select 触发修改选择数值：一次性修改全部
        changeType1(event){
            this.selectNum = event.target.value;
            console.log('selectNum  selected is '+this.selectNum)
        },

    },
}
</script>

<style type="text/css">
#main_ts_page{
  width: 100%;
  height: 100%;
  margin: 0px;
}
.info_square {
  width: 100%;
  height: 30%;
  /* background: red; */
}

.info_square .show_square{
  /* background: rgb(221, 226, 207); */
  width: 100%;
  height: 80%;
}

.show_square .show_info{
  /* background: rgb(232, 83, 120); */
  display: inline-block;
  float: left;
  width: 30%;
  height: 20px;
}


.show_info .info_index{
  display: inline-block;
}

.show_info .info_key{
  display: inline-block;
}


.info_square .context {
  /* background: rgb(109, 47, 223); */
  height: 30px;
  width: 40%;
}
.info_square input{
  display: inline-block;
  vertical-align: middle;
  width: 35%;
  margin: 5px;
}

.change_func #func_square{
  width: 100%;
  height: 30px;
  line-height: 30px;
  background: rgb(233, 226, 226);
  display: inline-block;
  border-bottom: 1px solid;
  margin-top: 5px;
}
#func_name{
  text-align: center;
  display: inline-block;
  width: 20%;
  vertical-align: middle;
}

#func_square input{
  display: inline-block;
  vertical-align: middle;
  width: 15%;
}

#func_square select{
  width: 10%;
}

button{
  vertical-align: middle;
  background-color: rgb(71, 129, 204);
  color: white;
  padding: 3px 5px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 10px;
  margin: 2px 1px;
  cursor: pointer;
  float: right;
  margin: 2px 20px 0 0;
}


</style>
