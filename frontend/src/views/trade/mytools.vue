<template>
    <div>
        <h1>测试辅助小工具</h1><hr />
            <table id="get_V2">
                <tr><th>获取user_id_V2:<input type="text" v-model="input1" placeholder="user_id" /></th><th><a href="javascript:void(0)" v-on:click="getTradeinfo">submit</a></th><th><input type="text" v-model="input1" placeholder="请输入订单号" /></th></tr>
                <tr></tr>
                
            </table>
    </div>
</template>

<style>

</style>

<script>
export default {
    name:"tardetool",
    props:{
       
    },

    data() {
        return {
            input1:'',
            input2:'',
            input3:'',
            selected1:1,
            selected2:1,
            selected3:1,
            selected4:1,
            selected5:1,
            Tinfos:'',
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
                this.axios.get('http:///api/getTrade?trade_no='+this.input1+'&type='+this.selected1).then((response)=>{
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
            this.axios.get('http:///api/changeTrade?trade_no='+this.input2+'&type='+this.selected2+'&stat='+this.selected3).then((response)=>{
                console.log(response);
                // this.Tinfos=response.data;
            }).catch((response)=>{
                console.log(response);
            })
        },
        // 更改订单的risk_channel
        ChangeRiskiskChanel(){
            this.axios.get('http://47.96.91.99:8000/api/changeTrade?trade_no='+this.input2+'&type='+this.selected4+'&stat='+this.selected5).then((response)=>{
                console.log(response);
                // this.Tinfos=response.data;
            }).catch((response)=>{
                console.log(response);
            })
        },

        test(){
            this.axios.get('http:///api/index').then((response)=>{
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
            console.log('changeType3 choosed selected is'+this.selected3)
        },
        changeType5(event){
            this.selected5 = event.target.value;
            console.log('changeType3 choosed selected is'+this.selected3)
        },

    },
}
</script>

