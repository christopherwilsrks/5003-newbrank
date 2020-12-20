'''
这个是主文件，主要的功能都写在这里了
'''

import os
import re
import numpy as np
from utils import Sql


channels = {'健身': 'aerobics', '动物': 'animal', '动画': 'douga', '娱乐': 'ent', '影视': 'cinephile', '手工绘画': 'handmake_painting', '搞笑': 'funny', '数码': 'digital', '时尚': 'fashion', '服饰': 'clothing',
            '汽车': 'automobile', '游戏': 'game', '生活': 'life', '知识': 'technology', '科学科普': 'science', '美妆': 'makeup', '美食': 'food', '职场': 'career', '舞蹈': 'dance', '财经': 'finance', '资讯': 'information',
            '运动': 'sports', '音乐': 'music', '鬼畜': 'kichiku'}


def npy2sql_up_info():
    bdc = Sql("localhost", "root", "ubuntu", "bdc")
    for channel in os.listdir('4_npyFile'):
        channel_name = channels[channel]
        field = '(uid, name, channel, sex, face, sign, level, birthday, fans_badge, official, vip, nameplate, top_photo, live_room, following, follower, video)'
        for up_npy_name in os.listdir("4_npyFile/{}".format(channel)):
            up_npy = np.load('4_npyFile/{}/{}'.format(channel, up_npy_name), allow_pickle=True).item()

            user_info = up_npy['user_info']
            uid = user_info['mid']
            name = user_info['name']
            sex = user_info['sex']
            face = user_info['face']
            face = re.sub('http://i', 'https://rks.cool/newbrank-img/i', face)
            sign = user_info['sign']
            level = user_info['level']
            birthday = user_info['birthday']
            fans_badge = user_info['fans_badge']
            official = str(user_info['official'])
            vip = str(user_info['vip'])
            nameplate = str(user_info['nameplate'])
            nameplate = re.sub('http://i', 'https://rks.cool/newbrank-img/i', nameplate)
            top_photo = user_info['top_photo']
            top_photo = re.sub('http://i', 'https://rks.cool/newbrank-img/i', top_photo)
            live_room = str(user_info['live_room'])
            live_room = re.sub('http://i', 'https://rks.cool/newbrank-img/i', live_room)

            relation_info = up_npy['relation_info']
            following = relation_info['following']
            follower = relation_info['follower']

            overview = up_npy['overview']
            video = overview['video']

            values = [uid, name, channel_name, sex, face, sign, level, birthday, fans_badge, official, vip, nameplate, top_photo, live_room, following, follower, video]
            command = "insert into up_info {} value {};".format(field, tuple(values))
            print(command)
            print(bdc.execute(command))


def npy2sql_videos():
    bdc = Sql("localhost", "root", "ubuntu", "bdc")
    for channel in os.listdir('4_npyFile'):
        field = '(uid, title, subtitle, description, pic, author, mid, created, length, aid, bvid, play, comment, video_review, typeid, review)'
        for up_npy_name in os.listdir("4_npyFile/{}".format(channel)):
            up_npy = np.load('4_npyFile/{}/{}'.format(channel, up_npy_name), allow_pickle=True).item()

            user_info = up_npy['user_info']
            uid = user_info['mid']

            videos = up_npy['videos']
            for video in videos:
                title = video['title']
                subtitle = video['subtitle']
                description = video['description']
                pic = video['pic']
                pic = re.sub('//i', 'https://rks.cool/newbrank-img/i', pic)
                author = video['author']
                mid = video['mid']
                created = video['created']
                length = video['length']
                aid = video['aid']
                bvid = video['bvid']
                play = video['play']
                if not isinstance(play, int):
                    play = 0
                comment = video['comment']
                video_review = video['video_review']
                typeid = video['typeid']
                review = video['review']

                values = [uid, title, subtitle, description, pic, author, mid, created, length, aid, bvid, play, comment, video_review, typeid, review]
                command = "insert into videos {} value {};".format(field, tuple(values))
                print(command)
                print(bdc.execute(command))


if __name__ == '__main__':
    npy2sql_up_info()
    npy2sql_videos()
