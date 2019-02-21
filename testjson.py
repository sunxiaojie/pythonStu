#coding=utf-8
import json
import requests





# def getjson(file):
#     f = open(file, encoding='UTF-8')
#     setting = json.load(f)
#     for a in setting:
#         bb = dict.values(a)
#         print(bb)
#         for (k,v) in dict.items(a):
#             print(k,str(v))
#
#
# files = "D:/1.封装包2个-出入参json(1)/1.封装包2个/vehicle_dispatch_拼车/in/vehicle_name_json.json"
# getjson(files)

# 读取json文件
# with open('E:/pythonCode/data/param.json', 'r', encoding='utf-8') as json_str:
#     a = json_str.read()
#     print(json.dumps(json.loads(a), sort_keys=True, indent=2))

# json_file = open('E:/pythonCode/data/param.json', encoding='utf-8')
# setting = json.load(json_file)
# print(json.dumps(setting, sort_keys=True, indent=2, ensure_ascii=False))
read = json.load(open('D:/1.封装包2个-出入参json(1)/1.封装包2个/vehicle_dispatch_拼车/in/vehicle_name_json.json', 'r', encoding='utf-8'))
print(read)
bb = {}
for a in read:
    bb[str(a['vehicle_type']+''+a['vehicle_volume'])]=a['vehicle_type']

print(bb)