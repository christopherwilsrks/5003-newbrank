import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

import Layout from '@/layout'

export default new Router({
    mode: 'history',
    routes: [
        {
            path: '/',
            component: Layout,
            children: [
                {
                    path: '/',
                    component: () => import('@/views/homepage'),
                    name: 'Homepage'
                }
            ]
        }
    ]
})