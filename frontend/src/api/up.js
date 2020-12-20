import request from '@/utils/request'

export function getUpListByChannel(data) {
    return request({
        url: '/up/list/' + data,
        method: 'get',
    })
}

export function getUpByUid(data) {
    return request({
        url: '/up/' + data,
        method: 'get',
    })
}