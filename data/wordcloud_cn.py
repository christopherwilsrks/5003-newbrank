# -*- coding: UTF-8 -*-

import os
import numpy as np
import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud

channels = ['健身', '动物', '动画', '娱乐', '影视', '手工绘画', '搞笑', '数码', '时尚', '服饰', '汽车', '游戏', '生活', '知识', '科学科普', '美妆', '美食', '职场', '舞蹈', '财经', '资讯', '运动', '音乐', '鬼畜']

stopword = open('stopwords.txt', 'r', encoding='utf-8').read().splitlines()


def generate_wordcloud(words, cloudpath, up_name):
    print(up_name)
    words_g = jieba.cut(words, cut_all=False)
    words_str = ''
    for word in words_g:
        if len(word) > 1 and not (word in stopword):
            words_str = words_str + word + ' '

    if words_str != '':
        wc = WordCloud(font_path='simhei.ttf', background_color="white", collocations=False, random_state=42, width=1000, height=860)
        wc.generate(words_str)
        wc.to_file('{}/{}.png'.format(cloudpath, up_name))


if __name__ == '__main__':
    for channel in channels:
        print(channel)
        cloudpath = 'clouds/{}'.format(channel)
        if not os.path.exists(cloudpath):
            os.mkdir(cloudpath)
        for up_npy_name in os.listdir("../4_npyFile/{}".format(channel)):
            up_npy = np.load('../4_npyFile/{}/{}'.format(channel, up_npy_name), allow_pickle=True).item()
            videos = up_npy['videos']

            words = ''
            for video in videos:
                words = words + video['title'] + '\n' + video['description'] + '\n'

            generate_wordcloud(words, cloudpath, up_npy_name[:-4])
