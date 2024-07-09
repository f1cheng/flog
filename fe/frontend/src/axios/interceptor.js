// axios拦截器
import axios from "axios";
import router from "@/router";
import Vue from 'vue';
const request = axios.create({
    //headers: {'content-type': 'application/x-www-form-urlencoded'}
    headers: {'content-type': 'application/json'}
})
request.interceptors.request.use(
    config => {
        //const token =localStorage.getItem('token')
        const token =sessionStorage.getItem('token')
        if (token){
             // DRF认证 token格式为Token 2a1sdwadadwdff
             config.headers.authorization = 'Token ' + token
        }
        return config
    },
    err => {
    return Promise.reject(err)
    }
)

request.interceptors.response.use(
   res => {
    return res
   },
   (error) => {
     // 针对特定的http状态码进行处理
     if (error.response && error.response.status === 401) {
        Vue.prototype.$message({
          showClose: true,
          message: 'Token过期请重新登录',
          type: 'warning',
          center: true,
        });
       router.push({ name: 'Login' }).then()
       return new Promise(() => {}) // pending的promise，中止promise链
     }
   }
)

export default request
