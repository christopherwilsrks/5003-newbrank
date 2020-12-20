import axios from 'axios'
import Vue from 'vue'
import store from '@/store'
import { Message, MessageBox } from 'element-ui'
import { ip } from '@/statics/config'

// 创建axios实例
const service = axios.create({
    // baseURL: process.env.BASE_API, // api的base_url
    baseURL: '/newbrank/api',
    // baseURL: '/api',
    withCredentials: true,
    // timeout: 15000                  // 请求超时时间
});

// request interceptor
service.interceptors.request.use(
    config => {
        // do something before request is sent
        // if (store.getters.token) {
        //     config.headers['Authorization'] = getToken()
        // }
        return config
    },
    error => {
        // do something with request error
        console.log(error) // for debug
        return Promise.reject(error)
    }
)

// respone拦截器
service.interceptors.response.use(
    response => {
        /**
         * code为非200是抛错 可结合自己业务进行修改
         */
        return response.data
        // const res = response.data;
        // if (res.error_code !== 0) {
        //     Message({
        //         message: res.data,
        //         type: 'error',
        //         duration: 3 * 1000
        //     })
        //     return Promise.reject(res.data)
        // } else {
        //     return res.data
        // }
    },
    error => {
        Message({
            message: error.message,
            type: 'error',
            duration: 5 * 1000
        });
        return Promise.reject(error)
    }
)

export default service