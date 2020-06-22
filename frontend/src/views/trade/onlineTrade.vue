<!-- 订单管理->线上环境订单 ：查看线上环境订单信息 -->
<template>
    <div>
        <h1>查看线上订单的状态</h1>
            <input type="text" v-model="input1" placeholder="请输入订单号"/>
            <select v-model="selected1" @change="changeType1($event)">
                <option value="4">contract_no</option>
                <option selected value="3">trade_no</option>
            </select>
            <select v-model="selected2" @change="changeType2($event)">
                <option value="3">小程序订单</option>
                <option value="2">主渠道序买断</option>
                <option selected value="1">主渠道序还机</option>
            </select>
            <a href="javascript:void(0)" v-on:click="getProinfo">查询订单状态</a><br />
            <!--debug info: {{Tinfos['trade_info']}}<br /> -->
            <span v-if="Tinfos!='' && Tinfos['trade_info']!=undefinded">
                <!--//TODO:文案内容需要修改-->
                现在查询的这笔订单是：&nbsp;{{Tinfos['trade_info']['user_name']}}(userid:{{Tinfos['trade_info']['id_user']}})&nbsp;在{{Tinfos['trade_info']['dt_created']}}下的订单,订单号是：{{Tinfos['trade_info']['trade_no']}}，合约号：{{Tinfos['trade_info']['contract_no']}},trade_id：{{Tinfos['trade_info']['id']}}<br />
    该笔订单的utm_source为：{{Tinfos['trade_info']['utm_source']}}，下单的channel_id：{{Tinfos['trade_info']['channel_id']}}&nbsp;此时订单的状态为：{{Tinfos['trade_info']['status']}}，订单的到期时间为：{{Tinfos['trade_info']['dt_end_date']}}
    该订单的合约租赁期数：{{Tinfos['trade_info']['choose_installments_num']}}期,实际使用了：{{Tinfos['trade_info']['total_installments_number']}}期<br />
                <span v-if="Tinfos['err']!=undefinded">
                    <br />{{Tinfos['err']}}<br />
                </span>
                <span v-if="Tinfos['subTrade']!=undefinded">
                    <hr />该笔订单的还机单信息如下：<br />
                    <span   v-for="(item, index) in Tinfos['subTrade']" :key="index">
                        <!--//TODO:e_sub_trade 信息--><br />
                        还机单顺序_{{index}}："id": {{item['id']}}, "main_trade_no":{{item['main_trade_no']}}, "sub_trade_no":{{item['sub_trade_no']}}, "sub_trade_type":{{item['sub_trade_type']}}, "status":{{item['status']}}, "dt_created":{{item['dt_created']}}, "dt_updated":{{item['dt_updated']}}, "pay_code":{{item['pay_code']}},<br />
                    </span>
                    <hr />
                </span>
                <span v-if="Tinfos['settlement']!=undefinded">
                    <!--//TODO:结算信息的展示-->settlement 信息如下：<br />
                    <!-- <li><span   v-for="(item, index) in Tinfos['settlement']" :key="index">
                        {{index}}:{{item}},
                        </span>
                    </li> -->
                    
                    订单于{{Tinfos['settlement']['dt_created']}}创建了结算单，单号biz_no为{{Tinfos['settlement']['biz_no']}}<br />
                    结算单的状态为：{{Tinfos['settlement']['status']}}，执行了{{Tinfos['settlement']['execute_num']}}次，上次执行时间是：{{Tinfos['settlement']['finished_time']}}，下次执行时间为：{{Tinfos['settlement']['next_finished_time']}};<br />
                </span>
                <span v-if="Tinfos['sharding']!=undefinded">
                    <hr/>结算步骤明细如下：<br />
                    <!-- {{Tinfos['step']}} -->
                    <span   v-for="(item, index) in Tinfos['sharding']" :key="index">
                        <li> "step":{{item['step']}}: "id":{{item['id']}}, "trade_no":{{item['trade_no']}}, "biz_no":{{item['biz_no']}}, "bill_no":{{item['bill_no']}}, "结算类型":{{item['settlement_category']}},"金额":{{item['amount']}},"当前状态":{{item['status']}}, "执行次数":{{item['execute_num']}}, "is_active":{{item['is_active']}}, "创建时间":{{item['dt_created']}}, "更新时间":{{item['dt_updated']}}, "freeze_no":{{item['freeze_no']}}</li>
                    </span>
                </span>


                <span v-if="Tinfos['status']!=undefinded">
                    <!--//TODO:结算明细的展示-->
                    <hr />Tips：目前该订单处于 {{Tinfos['status']}} 状态.
                </span>
                
            </span>
            <span v-else-if="Tinfos=='None'">
                查询不到该订单，请确认订单号是否正确
            </span>
            <span v-else-if="Tinfos['err']!=undefinded">
                接口返回错误信息：{{Tinfos['err']}} <br/>
                <span v-if="Tinfos['debug']!=undefinded">
                    <!--//TODO:结算明细的展示-->
                    <br />debug info：{{Tinfos['debug']}}
                </span>
            </span>
    <hr />
    
        <a href="javascript:void(0)" v-on:click="test">//打开F12-network，可以查看更加详细的json结果
        </a>
    </div>
</template>

<style>

</style>

<script>
export default {
    name:"onlineorderinfo",
    props:{
       
    },

    data() {
        return {
            prourl:'http://localhost:8000',      //open4test
            selected1:3,
            selected2:1,
            input1:'',
            input2:'',
            Tinfos:'',
            tradeinfo:'',
        }
    },

    methods: {
        getProinfo(){
            console.log(this.input1, 'input1')
            if (this.input1 == '') {
                this.Tinfos = ''
            }
            else{
                this.tradeno = this.input1.replace(/^\s*|\s*$/g,"")
                this.axios.get(this.prourl+'/api/getTrade?trade_no='+this.tradeno+'&type='+this.selected1+'&pro='+this.selected2).then((response)=>{
                console.log(response);
                this.Tinfos=response.data;
                }).catch((response)=>{
                console.log(response);
                })
            } 
        },

        getTradeinfo2(){
            console.log(this.input2, 'input2')
            if (this.input2 == '') {
                this.Tinfos = 'None'
            }
            else{
                tradeno = str.replace(/^\s*|\s*$/g,"")
                this.axios.get(this.prourl+'/api/getTrade?trade_no='+this.input2+'&type=4').then((response)=>{
                    console.log(response);
                    // this.Tinfos=response.data;
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


    },
}
</script>

