import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

import Layout from '@/layout'

export default new Router({
    mode: 'hash',
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
        },
        {
            path: '/uper/:id/',
            component: Layout,
            children: [
                {
                    path: '',
                    redirect: 'trend',
                    component: () => import('@/views/uper'),
                    name: 'Uper',
                    children: [
                        {
                            path: 'trend',
                            component: () => import('@/views/uper/components/TrendAnalyze'),
                            // name: 'TrendAnalyze'
                        },
                        {
                            path: 'work',
                            component: () => import('@/views/uper/components/WorkAnalyze'),
                            // name: 'WorkAnalyze'
                        },
                        {
                            path: 'fan',
                            component: () => import('@/views/uper/components/FanAnalyze'),
                            // name: 'FanAnalyze'
                        },
                        {
                            path: 'word',
                            component: () => import('@/views/uper/components/WordAnalyze')
                        }
                    ]
                }
            ]
        },
        {
            path: '/relation',
            component: Layout,
            children: [
                {
                    path: ':tag',
                    component: () => import('@/views/relation'),
                    name: 'RelationChart',
                }
            ],
        }
    ]
})