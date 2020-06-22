<!-- 工具分析->接口测试  -->
<template>
  <div id="main_ts_page">
        测试环境仓库接口回归：
            <div class="change_func">
                    <div id="func_square">
                        <div id="func_name">BFA仓库接口回归：</div>
                        <!-- <input type="text" v-model="input1" :placeholder="Plcontext2"/> -->
                        <input type="text" v-model="input2" :placeholder="Plcontext"/>
                        <button @click="runflow(1)">提交</button>
                    </div>
                    <!-- --------------------------------------------------------- -->
                    <div id="func_square">
                        <div id="func_name">BizContract仓库接口回归:</div>
                        <!-- <input type="text" v-model="input1" :placeholder="Plcontext2"/> -->
                        <input type="text" v-model="input2" :placeholder="Plcontext"/>
                        <button @click="runflow(2)">提交</button>
                    </div>
                    <!-- --------------------------------------------------------- -->
                    <div id="func_square">
                        <div id="func_name">BizSettlemnt仓库接口回归：</div>
                        <!-- <input type="text" v-model="input1" :placeholder="Plcontext2"/> -->
                        <input type="text" v-model="input2" :placeholder="Plcontext"/>
                        <button @click="runflow(3)">提交</button>
                    </div>
                    <!-- --------------------------------------------------------- -->
                    <div id="func_square">
                        <div id="func_name">ServiceUser仓库接口回归：</div>
                        <!-- <input type="text" v-model="input1" :placeholder="Plcontext2"/> -->
                        <input type="text" v-model="input2" :placeholder="Plcontext"/>
                        <button @click="runflow(4)">提交</button>
                    </div>
                    <!-- --------------------------------------------------------- -->
                    <div id="func_square">
                        <div id="func_name">BizPrice仓库接口回归：</div>
                        <!-- <input type="text" v-model="input1" :placeholder="Plcontext2"/> -->
                        <input type="text" v-model="input2" :placeholder="Plcontext"/>
                        <button @click="runflow(5)">提交</button>
                    </div>
                    <!-- --------------------------------------------------------- -->
                    <div id="func_square">
                        <div id="func_name">ServiceTrade仓库接口回归：</div>
                        <!-- <input type="text" v-model="input1" :placeholder="Plcontext2"/> -->
                        <input type="text" v-model="input2" :placeholder="Plcontext"/>
                        <button @click="runflow(6)">提交</button>
                    </div>
                    <!-- --------------------------------------------------------- -->
                    <div id="func_square">
                        <div id="func_name">ServiceTrade仓库接口回归：</div>
                        <!-- <input type="text" v-model="input1" :placeholder="Plcontext2"/> -->
                        <input type="text" v-model="input2" :placeholder="Plcontext"/>
                        <button @click="runflow(7)">提交</button>
                    </div>
                    <!-- --------------------------------------------------------- -->
                    <div id="func_square">
                        <div id="func_name">ServicePay仓库接口回归：</div>
                        <!-- <input type="text" v-model="input1" :placeholder="Plcontext2"/> -->
                        <input type="text" v-model="input2" :placeholder="Plcontext"/>
                        <button @click="runflow(8)">提交</button>
                    </div>
                    <!-- --------------------------------------------------------- -->
                    <div id="func_square">
                        <div id="func_name">ServiceDlivery仓库接口回归：</div>
                        <!-- <input type="text" v-model="input1" :placeholder="Plcontext2"/> -->
                        <input type="text" v-model="input2" :placeholder="Plcontext"/>
                        <button @click="runflow(9)">提交</button>
                    </div>
                    <!-- --------------------------------------------------------- -->
                    <div id="func_square">
                        <div id="func_name">ServiceAftersale仓库接口回归：</div>
                        <!-- <input type="text" v-model="input1" :placeholder="Plcontext2"/> -->
                        <input type="text" v-model="input2" :placeholder="Plcontext"/>
                        <button @click="runflow(10)">提交</button>
                    </div>
                    <!-- --------------------------------------------------------- -->
                    <div id="func_square">
                        <div id="func_name">BizAftersale仓库接口回归：</div>
                        <!-- <input type="text" v-model="input1" :placeholder="Plcontext2"/> -->
                        <input type="text" v-model="input2" :placeholder="Plcontext"/>
                        <button @click="runflow(11)">提交</button>
                    </div>
                    <!-- --------------------------------------------------------- -->
                    <div id="func_square">
                        <div id="func_name">ServiceFunding仓库接口回归：</div>
                        <!-- <input type="text" v-model="input1" :placeholder="Plcontext2"/> -->
                        <input type="text" v-model="input2" :placeholder="Plcontext"/>
                        <button @click="runflow(12)">提交</button>
                    </div>
            </div><br />
        流程回归结果：
            <div class="result">

            </div>
  </div>


    
</template>

<script>
export default {
    name:"main_ts_page",
    props:{
       test:String,
       Plcontext:String,
    },

    mounted() {
      // init context.
      this.Plcontext = "请输入测试环境号：/* test99 */";
      // this.Plcontext2 = "请输入手机号";
      this.err_1 = "请输入测试环境号或用户手机号";
      this.err_2 = "没有查到对应的订单，请确认trade_no是否正确";
      

      // init func.
    },

    data() {
        return {
          prourl:'http://47.96.91.99:8000',//后端接口的ip；
          input1:'',                        //备用参数字段
          input2:'',                        //流程回归的测试环境号
          
          usertoken:'',                     //userToken
          backup:'',                        //备用参数字段
        }
    },

    methods: {
        runflow:function(arg){
          if (this.input2 == '') {
            alert(this.err_1);          //非空判断
            return -1;
          }
          // TODO
          this.axios.get(this.prourl+'/api/runflow?testevn='+this.input2+'&mphone='+this.input1+'&mtype='+arg).then((response)=>{
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

        

    },
}
</script>

<style>
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
  width: 35%;
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
