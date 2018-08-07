# -*- coding: utf-8 -*-
from pyecharts import Map


def readProvince(filename):
    with open(filename, 'r') as f:
        lines = [line.split(' ')[0] for line in f.readlines()]
        ulines = list(set(lines))
        return ulines

provinceList = readProvince("data/visited.txt")
valueList = [1 for i in range(len(provinceList))]


attr =["安徽", "北京", "福建", "广东", "贵州", "海南", "河北", "河南", "黑龙江",
       "湖北", "湖南", "吉林", "江苏", "辽宁", "山东", "山西", "陕西", "上海",
       "四川", "天津", "云南", "浙江", "重庆"]

# value = [1 for i in range(len(attr))]

map=Map("去过的地方", width=1200, height=600)
map.add("", provinceList, valueList, maptype='china', is_visualmap=True, visual_text_color='#000')
# map.add("", [], [], maptype=u'china', is_visualmap=True, visual_text_color='#000')
map.show_config()
map.render()