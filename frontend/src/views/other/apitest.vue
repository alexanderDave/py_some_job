<!-- 工具分析->接口测试  -->
<template>
    <div class="apitest">
        接口测试:( **注意：** 接口测试用例请用excel编写，<a href = "http://47.96.91.99:8000/api/downloads/excel">测试用例模板请点击下载</a>)
        <div class="update_square">
                <p><strong>用例导入：</strong><a  class="btn" @click="chooseFile"> 点此选择文件 </a></p>
            <div class="filecommit">
                <em>已选择文件：<em style="color:red; font-style:normal;">{{attence}}</em></em>
                <input type="file" style="display:none" name="attence"  @change="changeFile($event)" ref="attenceInput" />
                <button type="button" class="btn" @click="upFile" >确认导入</button>
            </div>
       </div>
        <hr/>
        用例展示:
        <div class="case_square">
            <div class="show_square_else" v-if="getCaseResult == ''">db conn 错误</div>
                <div v-else class="show_square">
                    <div class="show_tc1">
                        <!-- <em>caseid</em><em>casename</em><em>model</em><em>url</em><em>method</em><em>params</em><em>except</em><em>infos</em><em>auth</em><em>dates</em> -->
                        <em class="em2">用例名称</em><em class="em3">用例模块</em><em class="em4">接口</em><em class="em6">infos</em><em class="em7">auth</em>
                    </div>
                    <div class="show_tc1" v-for="(val,key, index) in getCaseResult" :key="index">
                        <!-- <em>{{val.caseid}}</em><em>{{val.casename}}</em><em>{{val.model}}</em><em>{{val.url}}</em><em>{{val.method}}</em><em>{{val.params}}</em><em>{{val.except}}</em><em>{{val.infos}}</em><em>{{val.auth}}</em><em>{{val.dates}}</em> -->
                        <em class="em2">{{val.casename}}</em><em class="em3">{{val.model}}</em><em class="em4">{{val.url}}</em><em class="em6">{{val.infos}}</em><em class="em7">{{val.auth}}</em>
                    </div>
                </div>
        </div>
        <hr />
        历史操作记录:
        <div class="history_square">
            <div class="show_square_else" v-if="getOperResult == ''">暂无操作信息</div>
            <div v-else class="show_square">
            <!-- 获取的订单信息展示 -->
                <div class="show_info" v-for="(value,key,index) in getOperResult" :key="index">
                <div class="info_index">{{ key }}:</div>
                <div class="info_key">{{ value }}</div>  
                </div>
            </div>
        </div>

        

    </div>
</template>

<script>
export default {
    name:"apitests",

    data() {
        return {
            csrfToken:'',                           //csrf token
            attence:'',
            attenceFile:{},                         //数据库获取的用例数据
            dates:{},                               //接口测试结果数据
            backendurl:'http://47.96.91.99:8000',

            getCaseResult:'',
            getOperResult:'',
        }
    },

    mounted() {
        this.getTestcases();
    
    },

    methods: {

        // https://blog.csdn.net/qq_35465132/article/details/78687350?locationNum=4&fps=1 see it
        chooseFile(){
            this.$refs.attenceInput.click();
        },
        changeFile(e){
            this.attenceFile = e.target.files[0];
            this.attence = this.attenceFile.name;
        },

        upFile(){

            let filename = this.attence;
            console.log(filename)
            if (filename === '') {
                this.$alert('请先选择要上传的文件！');
                return;
            }
            let arr = filename.split('.');
            console.log(arr[1])
            if (arr[1] !== 'xls' && arr[1] !== 'xlsx') {
                this.$alert('请确认上传的文件是 excel 文件!');
                return;
            }

            let fileDate = new window.FormData();
            fileDate.append('file',this.attenceFile)
            

            let xhr = new window.XMLHttpRequest();
            xhr.open('post',this.backendurl+'/api/apitest',true);
            this.axios.get(this.backendurl+'/api/otherapis?type=2').then((response)=>{
                console.log(response.data);
                this.csrfToken = response.data
            }).catch((response)=>{
                console.log(response);
            })
            xhr.setRequestHeader('X-CSRFToken',this.csrfToken)            //设置csrf的token 防止被django拦截
            xhr.send(fileDate)

            xhr.onreadystatechange = () =>{
                if (xhr.readyState === 4) {
                    if (xhr.status === 200) {
                        let response = JSON.parse(xhr.response)
                        this.$alert(response.message)
                    } else {
                        let error = this.$emit('upload-error', xhr)
                        if (err !== false) {
                            this.$alert(xhr.statusText)

                        }
                    }
                }
            }
        },
        



        // 获取数据库中的接口用例，并分页展示
        getTestcases(){
        this.axios.get('http://47.96.91.99:8000/api/gettscases').then((response)=>{
                console.log(response.data);
                this.getCaseResult = response.data;
            }).catch((response)=>{
                console.log(response);
            })            
        },

    },
}
</script>

<style>

.apitest{
  width: 100%;
  height: 100%;
  margin: 0px;
}
.update_square {
  width: 100%;
  /* background: red; */
}
.history_square {
  width: 100%;
  height: 30px;
  overflow: scroll;
}
.case_square {
  width: 100%;
  height: 60%;
  overflow: scroll;
}
.show_tc1 em{
    display: inline-block;
    width: 20%;
    font-size: 12px;
}
.em7 {
    display: block;
    float: right;
    margin-right: 0px;

}

.update_square a{
    color:rgb(71, 129, 204);
}
.update_square a:hover{
    background: rgb(89, 159, 224);
    cursor:pointer;
}

button{
  background-color: rgb(71, 129, 204);
  color: white;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 10px;
  margin-right: 50%;
  cursor: pointer;
  float: right;
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

.show_square {
    font-family: 8px;
}

</style>
