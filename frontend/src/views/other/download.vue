<!-- 工具分析->app包下载 -->
<template>
    <div class="dloads">
        <iframe class="ios" src="https://www.pgyer.com/9qZz" />
        <iframe class="android" src="http://118.31.223.114:8686/app/home" />
    </div>
</template>

<script>
export default {
    name:"downloadspage",
    data() {
        return {
        }
    },
}
</script>

<style>
 .dloads{
     height: 100%;
     width: 100%;
 }

 .android {
     width: 51%;
     height: 100%
 }

 .ios {
     width: 45%;
     height: 100%;
 }

</style>
