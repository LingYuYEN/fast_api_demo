import json
import os

jsonfile_name = "./root/fast_api_demo/jsonfile.json"
# jsonfile_name = "jsonfile_test.json"


json_str = '{"a": "a"}'


def creat_jsonfile():
    with open(jsonfile_name, 'w') as jsonfile:
        jsonfile.write(json_str)
        print(jsonfile)
        jsonfile.close()


creat_jsonfile()
