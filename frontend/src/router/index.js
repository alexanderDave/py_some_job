import Main from '../views/index.vue'
import Abstract from '../views/layout/abstract.vue'
import Home from '../views/home/home.vue'
import Login from '../views/login.vue'
import Table from '../views/oms/table.vue'
import Sku from '../views/oms/sku.vue'                        //商品后台页面
import Dloads from '../views/other/download.vue'              //app包下载地址页面
import deploye from '../views/other/deploye.vue'              //deploye
import jira from '../views/other/jira.vue'                    //jira
import jve from '../views/other/jarvas.vue'                    //jira
import gongdan from '../views/other/gongdan.vue'              //gongdan
import Apitests from '../views/other/apitest.vue'             //接口测试页面
import Tradei3 from '../views/trade/MainPage.vue'          //获取线上订单数据
import Tradei from '../views/trade/tradeinfo.vue'             //获取&&修改测试环境订单数据
import Tradei2 from '../views/trade/onlineTrade.vue'          //获取线上订单数据
import mytools1 from '../views/trade/mytools.vue'             //todo 小工具
import flowreview from '../views/other/flowreview.vue'        //流程回归
import ckreview from '../views/other/ckreview.vue'        //仓库回归

export const loginRouter = {
  path: '/login',
  name: 'login',
  meta: {
    title: '登录'
  },
  component: Login
}

export const appRouter = [
  {
    title: '首页',
    path: '/home',
    name: 'home',
    icon: 'fa fa-home fa-lg',
    component: Home
  },
  {
    title: '项目流程',
    path: '/pm',
    name: 'pm',
    icon: 'fa fa-home fa-lg',
    component: Abstract,
    children: [
      {
        title: '项目管理(待开发)',
        name: 'manager',
        path: 'manager',
        icon: 'ios-paper',
        component: Dloads
      },
    ]
  },
  {
    title: '订单管理',
    path: '/content',
    name: 'content',
    icon: 'fa fa-home fa-lg',
    component: Abstract,
    children: [
      {
        title: '测试环境订单',
        name: 'orderinfo',
        path: 'orderinfo',
        icon: 'ios-paper',
        component: Tradei3
      },
      {
        title: '线上环境订单',
        name: 'onlineOrder',
        path: 'onlineOrder',
        icon: 'images',
        component: Tradei2
      },
    ]

  },
  {
    title: '发布系统',
    path: '/deployes',
    name: 'deployes',
    icon: 'fa fa-home fa-lg',
    component: Abstract,
    children: [
      {
        title: 'XHJ App',
        name: 'app',
        path: 'app',
        icon: 'fa fa-home fa-lg',
        component: Dloads
      },
      {
        title: 'Jira系统',
        name: 'jira',
        path: 'jira',
        icon: 'fa fa-home fa-lg',
        component: jira
      },
      {
        title: '工单系统',
        name: 'gongdan',
        path: 'gongdan',
        icon: 'fa fa-home fa-lg',
        component: gongdan
      },
      {
        title: 'deploye系统',
        name: 'deploye',
        path: 'deploye',
        icon: 'fa fa-home fa-lg',
        component: deploye
      },
      {
        title: 'JARVIS排期',
        name: 'jve',
        path: 'jve',
        icon: 'fa fa-home fa-lg',
        component: jve
      },
    ]
  },
  {
    title: '测试工具',
    path: '/mytools',
    name: 'mytools',
    icon: 'fa fa-home fa-lg',
    component: Abstract,
    children: [
      {
        title: '接口测试',
        name: 'api_test',
        path: 'api_test',
        icon: 'fa fa-home fa-lg',
        component: Apitests
      },
      {
        title: '流程回归',
        name: 'retest',
        path: 'retest',
        icon: 'fa fa-home fa-lg',
        component: flowreview
      },
      {
        title: '仓库回归',
        name: 'sync_info',
        path: 'sync_info',
        icon: 'fa fa-home fa-lg',
        component: ckreview
      },
    ]

  },
  {
    title: '监控管理',
    path: '/watcher',
    name: 'watcher',
    icon: 'fa fa-home fa-lg',
    component: Abstract,
    children: [
      {
        title: '还机监控',
        name: 'returnflow',
        path: 'returnflow',
        icon: 'ios-paper',
        component: Tradei
      },
      {
        title: '买断监控',
        name: 'buyout_Order',
        path: 'buyout_Order',
        icon: 'images',
        component: Tradei2
      },
      {
        title: '其他监控',
        name: 'other_watcher',
        path: 'other_watcher',
        icon: 'images',
        component: Sku
      }
    ]
  }

]

export const mainRouter = {
  path: '/',
  redirect: '/home',
  name: 'index',
  component: Main,
  children: appRouter
}

export const routers = [
  loginRouter,
  mainRouter,
  // catch all redirect
  {path: '*', redirect: '/home'}

]

