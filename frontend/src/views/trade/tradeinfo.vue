<!-- 废弃页面 -->
<template>
    <div>
        <h1>1.测试环境查看订单信息</h1>
            <select v-model="selected1" @change="changeType1($event)">
                <option value="2">contract_no</option>
                <option selected value="1">trade_no</option>
            </select>
            <input type="text" v-model="input1" placeholder="请输入订单号"/>
            <a href="javascript:void(0)">查询</a><br />
            <span v-if="Tinfos!='' && Tinfos!='None' && Tinfos['err']==undefinded">
                当前订单状态为：{{Tinfos['order_status']}},订单的合约号是：cont_no={{Tinfos['cont_no']}},<br />
                订单的tradeid是{{Tinfos['tradeid']}},用户的userid是：{{Tinfos['userid']}}、分表是{{Tinfos['fenbiao_num']}},<br />
            </span>
            <span v-else-if="Tinfos=='None'">查询不到该订单，请确认订单号是否正确</span>
            <span v-else-if="Tinfos['err']!=undefinded">接口返回错误信息：{{Tinfos['err']}},<br/>请确认订单号、页面选择条件等是否正确</span>
        <br /><br />
        <h1>2.修改订单的状态</h1>
            1.修改订单状态：<select v-model="selected2" @change="changeType2($event)">
                <option value="2">contract_no</option>
                <option selected value="1">trade_no</option>
            </select>
            <input type="text" v-model="input2" placeholder="请输入订单号"/>
            <select v-model="selected3" @change="changeType3($event)">
                <option value = "5">已发货:5</option>
                <option selected value = "10">已签收:10</option>
                <option value = "27">已买断:27</option>
                <option value = "28">已还机:28</option>
                <option value = "8">已退货:8</option>
            </select>
            <a href="javascript:void(0)" v-on:click="changeTradeinfo">提交</a><br/>
            
            2.修改订单修改订单的配置项：<select v-model="selected4" @change="changeType4($event)">
                <option value="2">contract_no</option>
                <option selected value="1">trade_no</option>
            </select>
            修改资方、担保方、续租开关等（具有一定的可扩展性）
            <input type="text" v-model="input3" placeholder="请输入订单号"/>
            <select v-model="selected5" @change="changeType5($event)">
                <option value = "2">挖财订单:2</option>
                <option value = "0">银联:0</option>
                <option value = "3">开启续租</option>
                <option value = "4" selected>关闭续租</option>
            </select>
            <a href="javascript:void(0)" v-on:click="ChangeRiskiskChanel">提交</a><br />
            
            3.修改订单的到期时间：<select v-model="selected6" @change="changeType6($event)">
                <option value="2">contract_no</option>
                <option selected value="1">trade_no</option>
            </select>
            <input type="text" v-model="input4" placeholder="请输入订单号"/>
            <input type=text v-model="input5" placeholder="0000-00-00 00:00:00"/>
            <a href="javascript:void(0)" v-on:click="ChangeDuedate">提交</a><br />

            4.修改订单的下单时间：<select v-model="selected7" @change="changeType7($event)">
                <option value="2">contract_no</option>
                <option selected value="1">trade_no</option>
            </select>
            <input type="text" v-model="input6" placeholder="请输入订单号"/>
            <input type=text v-model="input7" placeholder="0000-00-00 00:00:00"/>
            <a href="javascript:void(0)" v-on:click="ChangeCreated">提交</a><br />

            5.自动捡货：<select v-model="selected7" @change="changeType7($event)">
                <option value="2">contract_no</option>
                <option selected value="1">trade_no</option>
            </select><input type="text" v-model="input8"/>
            <input type="text" v-model="input6" placeholder="请输入订单号"/>
            <input type=text v-model="input7" placeholder="0000-00-00 00:00:00"/>
            <a href="javascript:void(0)" v-on:click="getSku">提交</a><br />

            6.修改订单的
            <hr />
            <br />{{results}}
    </div>
</template>

<style>
h1 {
    font: 1em sans-serif;
}


</style>

<script>
export default {
    name:"myorderinfo",
    props:{
       
    },

    data() {
        return {
            input1:'',
            input2:'',
            input3:'',
            input4:'',
            input4:'',
            input5:'',
            input6:'',
            input7:'',
            input8:'test8',
            selected1:1,
            selected2:1,
            selected3:10,
            selected4:1,
            selected5:0,
            selected6:1,
            selected7:1,
            Tinfos:'',
            results:'',
            prourl:'http://localhost:8000',  //open4test
        }
    },

    methods: {
        // 获取订单的信息
        getTradeinfo(){
            console.log(this.input1, 'input1')
            if (this.input1 == '') {
                this.Tinfos = 'None'
            }
            else{
                this.axios.get(this.prourl+'/api/getTrade?trade_no='+this.input1+'&type='+this.selected1).then((response)=>{
                console.log(response);
                this.Tinfos=response.data;
                this.input2 = this.input1;
                }).catch((response)=>{
                console.log(response);
                })
            } 
        },
        // 更改订单的状态
        changeTradeinfo(){
            this.axios.get(this.prourl+'/api/changeTrade?change=1&trade_no='+this.input2+'&type='+this.selected2+'&stat='+this.selected3).then((response)=>{
                console.log(response);
                this.results=response.data;
            }).catch((response)=>{
                console.log(response);
            })
        },
        // 更改订单的risk_channel or 是续租开关
        ChangeRiskiskChanel(){
            if (this.selected5==3 || this.selected5==4) {
                this.axios.get(this.prourl+'/api/changeTrade?change=3&trade_no='+this.input3+'&type='+this.selected4+'&stat='+this.selected5%2).then((response)=>{
                console.log(response);
                this.results=response.data;
                }).catch((response)=>{
                console.log(response);
                })
            } else {
                this.axios.get(this.prourl+'/api/changeTrade?change=2&trade_no='+this.input3+'&type='+this.selected4+'&stat='+this.selected5).then((response)=>{
                console.log(response);
                this.results=response.data;
                }).catch((response)=>{
                console.log(response);
                })
            }
        },
        // 更改订单的到期时间
        ChangeDuedate(){
            this.duetime = this.input5.replace(/^\s*|\s*$/g,"")
            this.axios.get(this.prourl+'/api/changeTrade?trade_no='+this.input4+'&change=4&dates='+this.duetime+'&type='+this.selected6).then((response)=>{
                console.log(response);
                this.results=response.data;
            }).catch((response)=>{
                console.log(response);
            })
        },

        ChangeCreated(){
            this.createtime = this.input7.replace(/^\s*|\s*$/g,"")
            this.axios.get(this.prourl+'/api/changeTrade?trade_no='+this.input6+'&change=6&dates='+this.createtime+'&type='+this.selected6).then((response)=>{
                console.log(response);
                this.results=response.data;
            }).catch((response)=>{
                console.log(response);
            })
        },
        
        // 自动检货
        getSku(){
            this.axios.get(this.prourl+'/api/changeTrade?change=5&trade_no='+this.input6+'&evn='+this.input8+'&type='+this.selected7+'&dates='+this.input7).then((response)=>{
                this.newsList=response.data.data;
            }).catch((response)=>{
                console.log(response);
            })
        },


        test(){
            this.axios.get(this.prourl+'/api/index').then((response)=>{
                this.newsList=response.data.data;
            }).catch((response)=>{
                console.log(response);
            })
        },

        changeType1(event){
            this.selected1 = event.target.value;
            console.log('changeType1 choosed selected is'+this.selected1)
        },
        changeType2(event){
            this.selected2 = event.target.value;
            console.log('changeType2 choosed selected is'+this.selected2)
        },
        changeType3(event){
            this.selected3 = event.target.value;
            console.log('changeType3 choosed selected is'+this.selected3)
        },
        changeType4(event){
            this.selected4 = event.target.value;
            console.log('changeType3 choosed selected is'+this.selected4)
        },
        changeType5(event){
            this.selected5 = event.target.value;
            console.log('changeType3 choosed selected is'+this.selected5)
        },
        changeType6(event){
            this.selected6 = event.target.value;
            console.log('changeType3 choosed selected is'+this.selected6)
        },
        changeType7(event){
            this.selected7 = event.target.value;
            console.log('changeType3 choosed selected is'+this.selected7)
        },

    },
}
</script>

