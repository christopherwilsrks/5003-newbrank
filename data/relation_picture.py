'''
这个是用来生成关系图代码的代码，然后用生成的关系图代码和库就可以生成关系图
'''

import numpy as np
import pandas as pd
import os

channels = ['健身', '动物', '动画', '娱乐', '影视', '手工绘画', '搞笑', '数码', '时尚', '服饰', '汽车', '游戏', '生活', '知识', '科学科普', '美妆', '美食', '职场', '舞蹈', '财经', '资讯', '运动', '音乐', '鬼畜']

for channel in channels:
    # 先提取出所有的up的uid放进up_list
    up_list = []
    with open('./2_待爬up主/{}.csv'.format(channel), 'rb') as csv:
        data = pd.read_csv(csv)
        for uid in data.Uid:
            up_list.append(uid)

    # 提取出所有的up的描述放进nodes，并根据已有的up_list提取出有用的关系组放进relation
    relations = {}
    nodes = []
    for npy_file_name in os.listdir('./4_npyFile/{}'.format(channel)):
        npy = np.load('./4_npyFile/{}/{}'.format(channel, npy_file_name), allow_pickle=True).item()
        user_info = npy['user_info']
        up = {"role_id": user_info['mid'], "name": user_info['name'], "group": 0, "avatar": user_info['face']}
        nodes.append(up)

        followings = npy['followings']
        follow_list = []
        for following in followings:
            if following['mid'] in up_list:
                follow_list.append(following['mid'])

        up_uid = user_info['mid']
        relations[up_uid] = follow_list

    links = []
    for up in relations:
        followings = relations[up]
        if followings != []:
            for following in followings:
                link = {"source": up_list.index(up), "target": up_list.index(following), "relation": "关注", "color": "734646"}
                links.append(link)

    data = {"nodes": nodes, "links": links}
    print("let {} = {};".format(channel, data))


