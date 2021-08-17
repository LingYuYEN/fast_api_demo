import json
import os

dict_list = []


def write_jsonfile(dic):
    if os.path.exists('jsonfile.json'):
        with open('jsonfile.json', 'r+') as jsonfile_list:  # 如果 json 檔案存在，就載入
            dic_list = json.load(jsonfile_list)  # 並轉換成 dic_list
            dic_list.append(dic)  # 將 dic append 到 dic_list
            jsonfile_list.seek(0)  # 指定光標位置，避免將 list 加到原本 jsonfile_list 後
            json_obj_list = json.dumps(dic_list, indent=4)  # 再將 dic_list 轉成 json
            print(json_obj_list)
            jsonfile_list.write(json_obj_list)
            jsonfile_list.close()
    else:
        with open('jsonfile.json', 'w') as jsonfile:  # 如果沒有 json 檔案，就新增
            dict_list.append(dic)  # 先將 dict 加入陣列
            json_object_list = json.dumps(dict_list, indent=4)  # 再將 dict_list 轉成 json
            jsonfile.write(json_object_list)  # 並寫入
            jsonfile.close()


def load_jsonfile():
    with open('jsonfile.json', 'r') as jsonfile_list:
        dict_data_list = json.load(jsonfile_list)
        return dict_data_list


def delete_jsonfile():
    if os.path.exists('jsonfile.json'):
        os.remove('jsonfile.json')
    else:
        print('The file does not exist.')
