import json
import os

jsonfile_name = "./root/fast_api_demo/jsonfile.json"


def creat_jsonfile():
    with open(jsonfile_name, 'w') as jsonfile:
        print(jsonfile)
        return "成功新增 jsonfile"

