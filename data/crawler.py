from bs4 import BeautifulSoup
import re
import pandas as pd
import numpy as np
from bilibili_api import user
from bilibili_api import video
import requests
import random
import os

channels = ['健身', '动物', '动画', '娱乐', '影视', '手工绘画', '搞笑', '数码', '时尚', '服饰', '汽车', '游戏', '生活', '知识', '科学科普', '美妆', '美食', '职场', '舞蹈', '财经', '资讯', '运动', '音乐', '鬼畜']


def html2csv():
    '''第一阶段，先把保存的html爬出up的名字和uid'''
    for channel in channels:
        path = 'E:\BDC\待处理的html\{}.html'.format(channel)
        print(channel)
        with open(path, 'rb') as web:
            soup = BeautifulSoup(web, 'html.parser')
            temp1 = soup.find_all(attrs={'class': '_1uibWbuI'})
            temp2 = soup.find_all(attrs={'class': '_3EjpTMJY'})
            lis1 = []
            lis2 = []
            for i in range(50):
                lis1.append(temp1[i].text)
                lis2.append(re.split(':', temp2[i].text)[-1])
            dataframe = pd.DataFrame({'用户名': lis1, 'Uid': lis2})
            dataframe.to_csv("./userinfo/{}.csv".format(channel), encoding='utf_8_sig', index=False)


def csv2simpleinfo():
    '''第二阶段，按照uid爬出一个基本的userinfo'''
    for channel in channels:
        path = 'E:\BDC\待爬up主\{}.csv'.format(channel)
        print(channel)
        mid, name, sex, video, following, follower, sign, face = [], [], [], [], [], [], [], []
        with open(path, 'rb') as csv:
            data = pd.read_csv(csv)
            i = 1
            for uid in data.Uid:
                print('正在爬取：{}/50'.format(i), uid)
                i += 1
                overview = user.get_overview(uid=uid)
                user_info = user.get_user_info(uid=uid)
                relation_info = user.get_relation_info(uid=uid)
                # liveinfo = user.get_live_info(uid=uid)
                # videos = user.get_videos(uid=uid)

                mid.append(user_info['mid'])
                name.append(user_info['name'])
                sex.append(user_info['sex'])
                video.append(overview['video'])
                following.append(relation_info['following'])
                follower.append(relation_info['follower'])
                sign.append(user_info['sign'])
                face.append(user_info['face'])

            df = pd.DataFrame({'Uid': mid, '用户名': name, '性别': sex, '视频数': video, '关注数': following, '粉丝数': follower, '个性签名': sign, '头像链接': face})
            df.to_csv("./userinfo/{}.csv".format(channel), encoding='utf_8_sig', index=False)


def crawl_to_npy():
    '''第三阶段，按照up主名单爬成npy文件保存以供之后读取'''
    for channel in channels:
        csv_file = 'E:\BDC\\2_待爬up主\{}.csv'.format(channel)
        file_path = './npyFile/{}'.format(channel)
        if not os.path.exists(file_path):
            os.mkdir(file_path)
        with open(csv_file, 'rb') as csv:
            datas = pd.read_csv(csv)
            for i in range(50):
                if channel in ['健身', '动物', '动画', '娱乐']:
                    break
                if channel == '娱乐' and i < 33:  # 少两个差不多
                    continue
                uid = datas['Uid'][i]
                user_name = datas['用户名'][i]
                # bilibili_api.request_settings["proxies"] = get_proxy()
                print('{}/50 | 正在爬{}'.format(i + 1, user_name))
                overview = user.get_overview(uid=uid)
                user_info = user.get_user_info(uid=uid)
                relation_info = user.get_relation_info(uid=uid)
                followings = user.get_followings_g(uid=uid)
                videos = user.get_videos_g(uid=uid)
                npy = {}
                npy['overview'] = overview
                npy['user_info'] = user_info
                npy['relation_info'] = relation_info
                npy['followings'] = list(followings)
                npy['videos'] = list(videos)
                np.save('{}/{}.npy'.format(file_path, user_name), dict(npy), allow_pickle=True)


def npy2csv_all5():
    '''第四阶段，把npy保存成csv格式，这是原版的5个文件版'''
    for channel in channels:
        csv_channel_path = './24x50up/{}'.format(channel)
        if not os.path.exists(csv_channel_path):
            os.mkdir(csv_channel_path)
        npy_channel_path = './npyFile/{}'.format(channel)
        for npy_name in os.listdir(npy_channel_path):
            npy = np.load('{}/{}'.format(npy_channel_path, npy_name), allow_pickle=True).item()
            up_name = npy_name[:-4]
            csv_up_path = '{}/{}'.format(csv_channel_path, up_name)
            if not os.path.exists(csv_up_path):
                os.mkdir(csv_up_path)
            print('准备存{}'.format(csv_up_path))

            overview = npy['overview']
            overview['channel'] = str(overview['channel'])
            overview['favourite'] = str(overview['favourite'])
            df = pd.DataFrame(overview, index=[0])
            df.to_csv('{}/overview.csv'.format(csv_up_path), encoding='utf_8_sig', index=False)

            user_info = npy['user_info']
            user_info['official'] = str(user_info['official'])
            user_info['vip'] = str(user_info['vip'])
            user_info['pendant'] = str(user_info['pendant'])
            user_info['nameplate'] = str(user_info['nameplate'])
            user_info['theme'] = str(user_info['theme'])
            user_info['sys_notice'] = str(user_info['sys_notice'])
            user_info['live_room'] = str(user_info['live_room'])
            df = pd.DataFrame(user_info, index=[0])
            df.to_csv('{}/user_info.csv'.format(csv_up_path), encoding='utf_8_sig', index=False)

            relation_info = npy['relation_info']
            df = pd.DataFrame(relation_info, index=[0])
            df.to_csv('{}/relation_info.csv'.format(csv_up_path), encoding='utf_8_sig', index=False)

            followings = npy['followings']
            df = pd.DataFrame(followings)
            df.to_csv('{}/followings.csv'.format(csv_up_path), encoding='utf_8_sig', index=False)

            videos = npy['videos']
            df = pd.DataFrame(videos)
            df.to_csv('{}/videos.csv'.format(csv_up_path), encoding='utf_8_sig', index=False)


def npy2scv_simple3():
    '''第四阶段，把npy保存成csv格式，这是简化版的3个文件版'''
    for channel in channels:
        csv_channel_path = './24x50up/{}'.format(channel)
        if not os.path.exists(csv_channel_path):
            os.mkdir(csv_channel_path)
        npy_channel_path = './npyFile/{}'.format(channel)
        for npy_name in os.listdir(npy_channel_path):
            npy = np.load('{}/{}'.format(npy_channel_path, npy_name), allow_pickle=True).item()
            up_name = npy_name[:-4]
            csv_up_path = '{}/{}'.format(csv_channel_path, up_name)
            if not os.path.exists(csv_up_path):
                os.mkdir(csv_up_path)
            print('准备存{}'.format(csv_up_path))

            overview = npy['overview']
            relation_info = npy['relation_info']
            user_info = npy['user_info']

            user_info['official'] = str(user_info['official'])
            user_info['vip'] = str(user_info['vip'])
            user_info['pendant'] = str(user_info['pendant'])
            user_info['nameplate'] = str(user_info['nameplate'])
            user_info['theme'] = str(user_info['theme'])
            user_info['sys_notice'] = str(user_info['sys_notice'])
            user_info['live_room'] = str(user_info['live_room'])
            #
            user_info['video'] = overview['video']
            user_info['following'] = relation_info['following']
            user_info['follower'] = relation_info['follower']
            #
            df = pd.DataFrame(user_info, index=[0])
            df.to_csv('{}/user_info.csv'.format(csv_up_path), encoding='utf_8_sig', index=False)

            followings = npy['followings']
            df = pd.DataFrame(followings)
            df.to_csv('{}/followings.csv'.format(csv_up_path), encoding='utf_8_sig', index=False)

            videos = npy['videos']
            df = pd.DataFrame(videos)
            df.to_csv('{}/videos.csv'.format(csv_up_path), encoding='utf_8_sig', index=False)


if __name__ == '__main__':
    uid = 1016258630
    overview = user.get_overview(uid)
    print(overview)
    user_info = user.get_user_info(uid)
    print(user_info)
