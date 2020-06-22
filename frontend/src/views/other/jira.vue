<!-- jira跳转页面 -->
<template>
    <div class="dloads">
        jira跳转页面,将在新页面中打开……
    </div>
</template>

<script>
export default {
    name:"jira",
    data() {
        return {
        }
    },
    mounted() {
        // window.location.href="http://47.96.91.99:8080/projects/XHJ/issues";
        window.open("http://47.96.91.99:8080/projects/XHJ/issues");
    },
}
</script>

<style>
 .dloads{
     height: 100%;
 }

 .dep {
     height: 100%;
     width: 100%;
 }
</style>
