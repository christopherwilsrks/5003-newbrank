import request from '@/utils/request'

export function getVideosByUid(data) {
    return request({
        url: `/videos/up/${data['uid']}/size/${data['size']}/page/${data['page']}`,
        method: 'get',
    })
}