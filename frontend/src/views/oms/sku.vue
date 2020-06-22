<!-- 商品管理-> 查看&&修改 测试环境订单信息 -->
<template>
    <div>
        <h1>修改sku的库存数量</h1>
            <select v-model="selected1" @change="changeType1($event)">
                <option value="2">contract_no</option>
                <option selected value="1">trade_no</option>
            </select>
            <input type="text" v-model="input1" placeholder="请输入订单号"/>
            <a href="javascript:void(0)" v-on:click="getTradeinfo">查询</a><br />
            <span v-if="Tinfos!='' && Tinfos!='None' && Tinfos['err']==undefinded">
                当前订单状态为：{{Tinfos['order_status']}},订单的合约号是：cont_no={{Tinfos['cont_no']}},<br />
                订单的tradeid是{{Tinfos['tradeid']}},用户的userid是：{{Tinfos['userid']}}、分表是{{Tinfos['fenbiao_num']}},<br />
            </span>
            <span v-else-if="Tinfos=='None'">查询不到该订单，请确认订单号是否正确</span>
            <span v-else-if="Tinfos['err']!=undefinded">接口返回错误信息：{{Tinfos['err']}},<br/>请确认订单号、页面选择条件等是否正确</span>
        <br />
        <hr />
        <h1>修改sku库存</h1>
        <h1>一键捡货</h1>
        <h1>一键退货</h1>
        
    </div>
</template>

<style>

</style>

<script>
export default {
    name:"myorderinfo",
    props:{
       
    },

    data() {
        return {
            input1:'',
            selected1:1,
            selected2:1,
            Tinfos:'',
            results:'',
            prourl:'http://192.168.1.43:8000',
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

