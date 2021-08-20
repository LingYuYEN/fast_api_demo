import json
import os

dict_list = []
repair_record_dict_list = []
# jsonfile_name = "/root/fast_api_demo/jsonfile.json"
jsonfile_name = "jsonfile.json"

exe = 'jsonfile.json'
# if the exe just in current dir
print(os.path.abspath(exe))
# output
# D:\python\note\something.exe
# if we need find it first
for root, dirs, files in os.walk(r'D:\python'):
    for name in files:
        if name == exe:
            print(os.path.abspath(os.path.join(root, name)))


def write_jsonfile(dic):
    global dict_list
    if os.path.exists(jsonfile_name):
        with open(jsonfile_name, 'r+') as jsonfile_list:  # 如果 json 檔案存在，就載入
            dict_list = json.load(jsonfile_list)  # 並轉換成 dic_list
            dict_list.append(dic)  # 將 dic append 到 dic_list
            jsonfile_list.seek(0)  # 指定光標位置，避免將 list 加到原本 jsonfile_list 後
            json_obj_list = json.dumps(dict_list, indent=4)  # 再將 dic_list 轉成 json
            jsonfile_list.write(json_obj_list)
            jsonfile_list.close()
    else:
        with open(jsonfile_name, 'w') as jsonfile:  # 如果沒有 json 檔案，就新增
            dict_list.append(dic)  # 先將 dict 加入陣列
            json_object_list = json.dumps(dict_list, indent=4)  # 再將 dict_list 轉成 json
            jsonfile.write(json_object_list)  # 並寫入
            jsonfile.close()


def load_jsonfile():
    if os.path.exists(jsonfile_name):
        with open(jsonfile_name, 'r') as jsonfile_list:
            dict_data_list = json.load(jsonfile_list)  # 轉換成 dic_list
            return dict_data_list
    else:
        return []


def put_jsonfile(index, dic):
    global dict_list
    global repair_record_dict_list
    with open(jsonfile_name, 'r+') as jsonfile:  # 如果 json 檔案存在，就載入
        dict_list = json.load(jsonfile)
        if dict_list[index]['repair_record'] is None:
            dict_list[index]['repair_record'] = repair_record_dict_list.append(dic)
            json_obj_list = json.dumps(dict_list, indent=4)
            jsonfile.write(json_obj_list)  # 並寫入
            jsonfile.close()
        else:
            repair_record_dict_list = dict_list[index]['repair_record']
            repair_record_dict_list.append(dic)
            json_obj_list = json.dumps(dict_list, indent=4)
            jsonfile.write(json_obj_list)  # 並寫入
            jsonfile.close()


def delete_jsonfile():
    if os.path.exists('jsonfile.json'):
        os.remove('jsonfile.json')
    else:
        print('The file does not exist.')
