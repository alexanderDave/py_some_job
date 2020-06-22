<template>
  <div id="main_ts_page">
    测试环境 查看订单信息：
    <div class="info_square">
        <div class="context">
            <input type="text" v-model="input1" :placeholder="Plcontext"/>
            <button @click="getTrade(1)">提交</button>
        </div>
    <!-- --------------------------------------------------------- -->
        <div class="show_square_else" v-if="getTradeResult == ''">当前查询结果为空，请确认订单号是否正确</div>
        <div v-else class="show_square">
          <!-- 获取的订单信息展示 -->
          <div class="show_info" v-for="(value,key,index) in getTradeResult" :key="index">
              <div class="info_index">{{ key }}:</div>
              <div class="info_key">{{ value }}</div>
              
          </div>
          
        </div>
    </div>







    <br />
    测试环境 修改订单信息：
    <div class="change_func">

      <div id="func_square">
        <div id="func_name">快速创建订单：</div>
        <input type="text" v-model="input2" placeholder="请输入测试环境号和手机号：/* e.g.: test99,18612340001 */"/>
        <em>tips:1.默认银联乐百分订单 2.默认使用华为P30商品 3.请按提示格式输入测试环境跟手机号</em>
        <button @click="changeTrade(10)">提交</button>
      </div>
      <!-- --------------------------------------------------------- -->

      <div id="func_square">
        <div id="func_name">修改订单状态:</div>
        <input type="text" v-model="input2" :placeholder="Plcontext"/>
          <select v-model="selectNum" @change="changeType1($event)">
                <option value = "5">已发货:5</option>
                <option selected value = "10">已签收:10</option>
                <option value = "27">已买断:27</option>
                <option value = "28">已还机:28</option>
                <option value = "8">已退货:8</option>
            </select>
        <button @click="changeTrade(1)">提交</button>
      </div>
      <!-- --------------------------------------------------------- -->
      <div id="func_square">
        <div id="func_name">修改订单下单时间：</div>
        <input type="text" v-model="input2" :placeholder="Plcontext"/>
        <input type=text v-model="mTime" placeholder="0000-00-00 00:00:00"/>
        <button @click="changeTrade(2)">提交</button>
      </div>
      <!-- --------------------------------------------------------- -->
      <div id="func_square">
        <div id="func_name">修改订单签收时间：</div>
        <input type="text" v-model="input2" :placeholder="Plcontext"/>
        <input type=text v-model="mTime" placeholder="0000-00-00 00:00:00"/>
        <button @click="changeTrade(3)">提交</button>
      </div>
      <!-- --------------------------------------------------------- -->
      <div id="func_square">
        <div id="func_name">修改订单到期时间：</div>
        <input type="text" v-model="input2" :placeholder="Plcontext"/>
        <input type=text v-model="mTime" placeholder="0000-00-00 00:00:00"/>
        <button @click="changeTrade(4)">提交</button>
      </div>
      <!-- --------------------------------------------------------------- -->
      <div id="func_square">
        <div id="func_name">修改订单资金方：</div>
        <input type="text" v-model="input2" :placeholder="Plcontext"/>
            <select v-model="selectNum" @change="changeType1($event)">
                <option selected value = "1">享换机:1</option>
                <option value = "2">光大银行:2</option>
                <option value = "3">众安:3</option>
                <option value = "4">北文投:4</option>
                <option value = "5">江南:5</option>
                <option value = "6">湖北消金:6</option>
            </select>
        <button @click="changeTrade(5)">提交</button>
      </div>
      <!-- --------------------------------------------------------- -->
      <div id="func_square">
        <div id="func_name">修改订单担保方：</div>
        <input type="text" v-model="input2" :placeholder="Plcontext"/>
            <select v-model="selectNum" @change="changeType1($event)">
              <option value = "2">江南:2</option>
                <option value = "2">挖财:2</option>
                <option value = "4">享换机:4</option>
                <option selected value = "1">银联:1</option>
            </select>
        <button @click="changeTrade(6)">提交</button>
      </div>
      <!-- --------------------------------------------------------- -->
      <div id="func_square">
        <div id="func_name">订单打开\关闭续租：</div>
        <input type="text" v-model="input2" :placeholder="Plcontext"/>
        <select v-model="selectNum" @change="changeType1($event)">
                <option selected value = "1">开启续租</option>
                <option value = "0" selected>关闭续租</option>
            </select>
        <button @click="changeTrade(7)">提交</button>
      </div>
      <!-- --------------------------------------------------------- -->
      <div id="func_square">
        <div id="func_name">修改江南人脸识别成功：</div>
        <input type="text" v-model="input2" :placeholder="Plcontext"/>

        <button @click="changeTrade(8)">提交</button>
      </div>
      <!-- --------------------------------------------------------- -->
      <div id="func_square">
        <div id="func_name">取消订单的买断状态：</div>
        <input type="text" v-model="input2" :placeholder="Plcontext"/>
        <button @click="changeTrade(10)">提交</button>
      </div>
      <!-- --------------------------------------------------------- -->
      <div id="func_square">
        <div id="func_name">线上用户token获取：</div>
        <input type="text" v-model="input2" placeholder="/**请输入用户的 UserId **/"/>
        <em class="user_token" v-if="usertoken != ''">{{usertoken}}</em>  <!--这里有一个坑点：如果这一行用div标签的话，会自动换行-->
        <button @click="changeTrade(9)">提交</button>
      </div>
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
