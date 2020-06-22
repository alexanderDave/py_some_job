<template>
  <div>
    <el-row>
      <el-col :span="6" style="padding-right: 5px">
      <info-card
        iconType="android-person-add"
        color="#2d8cf0"
        :count = "newbug"
        message="昨日新增bug数"></info-card>
      </el-col>
      <el-col :span="6" style="padding-right: 5px">
      <info-card
        iconType="android-person-add"
        color="#64d572"
        :count="allbug"
        message="bug总数"></info-card>
      </el-col>
      <el-col :span="6" style="padding-right: 5px">
      <info-card
        iconType="android-person-add"
        color="#ffd572"
        :count="newissue"
        message="昨日新增工单数量"></info-card>
      </el-col>
      <el-col :span="6" >
      <info-card
        iconType="android-person-add"
        color="#f25e43"
        :count="allissue"
        message="总报工单数量"></info-card>
      </el-col>

    </el-row>
    <el-row style="padding-top: 10px">
      <el-col :span="24">
      <el-card>
        <p slot="title" class="card-title">
          <i type="ios-shuffle-strong"></i>
          广告投放分析
        </p>
        <div class="line-chart-con">
          <line-chart></line-chart>
        </div>
      </el-card>
      </el-col>

    </el-row>
    <el-row style="padding-top: 10px">
      <el-col :span="8" style="padding-right: 5px">
      <el-card>
        <p slot="title" class="card-title">
          <i type="android-wifi"></i>
          各类用户服务调用变化统计

        </p>
        <div style="height: 200px">
          <gauge-chart></gauge-chart>
        </div>
      </el-card>
      </el-col>
      <el-col :span="8" style="padding-right: 5px">
      <el-card>
        <p slot="title" class="card-title">
          <i type="android-wifi"></i>
          用户访问来源

        </p>
        <div style="height: 200px">
          <pie-chart></pie-chart>
        </div>
      </el-card>
      </el-col>
      <el-col :span="8" >
      <el-card>
        <p slot="title" class="card-title">
          <i type="android-wifi"></i>
          上周每日服务调用量

        </p>
        <div style="height: 200px">
          <shadow-chart></shadow-chart>
        </div>
      </el-card>
      </el-col>

    </el-row>

  </div>
</template>

<script>
  import infoCard from '../../components/info-card/infoCard.vue'
  import lineChart from '../../components/echarts/lineChart.vue'
  import gaugeChart from '../../components/echarts/gaugeChart.vue'
  import pieChart from '../../components/echarts/pieChart.vue'
  import shadowChart from '../../components/echarts/shadowChart.vue'
  export default {
    // 加载的时候执行js 刷新页面数据
    mounted() {
      this.getInfos()
    },

    components: {
      infoCard,
      lineChart,
      gaugeChart,
      pieChart,
      shadowChart
    },

    data() {
        return {
            
            allbug:'112',
            newbug:'12',
            allissue:'1',
            newissue:'1',
            
        }
    },

    methods: {
      // 更改订单的状态
        getInfos(){
            this.axios.get('/api/otherapis?type=1').then((response)=>{
                console.log(response.data);
                this.allissue = response.data['gall'];
                this.allbug = response.data['jall'];
                this.newbug = response.data['jadd'];
                this.newissue = response.data['gadd'];
            }).catch((response)=>{
                console.log(response);
            })
        },
    },
  }
</script>

<style>
  .line-chart-con{
    height: 200px;
  }
</style>
