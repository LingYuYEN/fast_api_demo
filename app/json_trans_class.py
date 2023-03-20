import json
from pydantic import BaseModel
import os


class MemberModel(BaseModel):
    id: int
    account: str
    password: str
    priority: int


data = {
    "name": "Louis",
    "phone": "0988888888"
}


def write_jsonfile(json_str):
    ret = json.dumps(json_str)
    with open('jsonfile.json', 'w') as fp:
        fp.write(ret)


def load_jsonfile():
    with open('jsonfile.json', 'r') as fp:
        dict_data = json.load(fp)
        print(dict_data)
        print(type(dict_data))
        return dict_data


def delete_jsonfile():
    if os.path.exists('jsonfile.json'):
        os.remove('jsonfile.json')
    else:
        print('The file does not exist.')


write_jsonfile(data)
load_jsonfile()
delete_jsonfile()
