from typing import Optional, List
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from pydantic import BaseModel
import datetime
import access_jsonfile
from fastapi.encoders import jsonable_encoder


app = FastAPI()

app.debug = True
# origins = [
#     "http://localhost",
#     "http://localhost:8080",
#     "http://103.3.63.116"
# ]
origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class TownshipInfo:
    def __init__(self, id, township, school):
        self.id = id
        self.township = township
        self.school = school


class Login(BaseModel):
    username: str
    password: str


class RepairRecord(BaseModel):
    id: int
    record_time: str
    record_info: str
    record_user: str


class RepairInfo(BaseModel):
    id: int
    school: str
    name: str
    tel: str
    device_type: str
    repair_description: str
    start_time: str
    end_time: Optional[str]
    status: str = '未接案'
    repair_record: Optional[List[RepairRecord]]


member_array = [
    {'id': 1, 'account': 'admin', 'alias': '駐點工程師', 'password': 'admin', 'priority': 0},
    {'id': 2, 'account': 'hjps', 'alias': '後庄國小', 'password': 'hjps', 'priority': 1},
    {'id': 3, 'account': 'hnps', 'alias': '惠農國小', 'password': 'hnps', 'priority': 1},
    {'id': 4, 'account': 'ssps', 'alias': '新生國小', 'password': 'ssps', 'priority': 1},
    {'id': 5, 'account': 'rhes', 'alias': '榮華國小', 'password': 'rhes', 'priority': 1},
    {'id': 6, 'account': 'ftps', 'alias': '富田國小', 'password': 'ftps', 'priority': 1},
    {'id': 7, 'account': 'jyps', 'alias': '佳義國小', 'password': 'jyps', 'priority': 1},
    {'id': 8, 'account': 'mdps', 'alias': '牡丹國小', 'password': 'mdps', 'priority': 1},
    {'id': 9, 'account': 'gses', 'alias': '高士國小', 'password': 'gses', 'priority': 1},
    {'id': 10, 'account': 'mlbh', 'alias': '牡林分校', 'password': 'mlbh', 'priority': 1},
    {'id': 11, 'account': 'ccjhs', 'alias': '車城國中', 'password': 'ccjhs', 'priority': 1},
    {'id': 12, 'account': 'cces', 'alias': '車城國小', 'password': 'cces', 'priority': 1},
    {'id': 13, 'account': 'lgps', 'alias': '里港國小', 'password': 'lgps', 'priority': 1},
    {'id': 14, 'account': 'tkps', 'alias': '土庫國小', 'password': 'tkps', 'priority': 1},
    {'id': 15, 'account': 'ytes', 'alias': '玉田國小', 'password': 'ytes', 'priority': 1},
    {'id': 16, 'account': 'jdjh', 'alias': '佳冬國中', 'password': 'jdjh', 'priority': 1},
    {'id': 17, 'account': 'cyps', 'alias': '羌園國小', 'password': 'cyps', 'priority': 1},
    {'id': 18, 'account': 'yges', 'alias': '玉光國小', 'password': 'yges', 'priority': 1},
    {'id': 19, 'account': 'welps', 'alias': '文樂國小', 'password': 'welps', 'priority': 1},
    {'id': 20, 'account': 'dkjh', 'alias': '東港國中', 'password': 'dkjh', 'priority': 1},
    {'id': 21, 'account': 'hbps', 'alias': '海濱國小', 'password': 'hbps', 'priority': 1},
    {'id': 22, 'account': 'dtes', 'alias': '大潭國小', 'password': 'dtes', 'priority': 1},
    {'id': 23, 'account': 'fkps', 'alias': '楓港國小', 'password': 'fkps', 'priority': 1},
    {'id': 24, 'account': 'flhs', 'alias': '枋寮高中', 'password': 'flhs', 'priority': 1},
    {'id': 25, 'account': 'jsps', 'alias': '建興國小', 'password': 'jsps', 'priority': 1},
    {'id': 26, 'account': 'dhps', 'alias': '東海國小', 'password': 'dhps', 'priority': 1},
    {'id': 27, 'account': 'lpjh', 'alias': '林邊國中', 'password': 'lpjh', 'priority': 1},
    {'id': 28, 'account': 'rhps', 'alias': '仁和國小', 'password': 'rhps', 'priority': 1},
    {'id': 29, 'account': 'cfps', 'alias': '崎峰國小', 'password': 'cfps', 'priority': 1},
    {'id': 30, 'account': 'sulps', 'alias': '水利國小', 'password': 'sulps', 'priority': 1},
    {'id': 31, 'account': 'csps', 'alias': '長興國小', 'password': 'csps', 'priority': 1},
    {'id': 32, 'account': 'njjh', 'alias': '南州國中', 'password': 'njjh', 'priority': 1},
    {'id': 33, 'account': 'njps', 'alias': '南州國小', 'password': 'njps', 'priority': 1},
    {'id': 34, 'account': 'dtjh', 'alias': '大同高中', 'password': 'dtjh', 'priority': 1},
    {'id': 35, 'account': 'hsps', 'alias': '鶴聲國小', 'password': 'hsps', 'priority': 1},
    {'id': 36, 'account': 'hcjh', 'alias': '恆春國中', 'password': 'hcjh', 'priority': 1},
    {'id': 37, 'account': 'chyps', 'alias': '僑勇國小', 'password': 'chyps', 'priority': 1},
    {'id': 38, 'account': 'dpps', 'alias': '大平國小', 'password': 'dpps', 'priority': 1},
    {'id': 39, 'account': 'kdes', 'alias': '崁頂國小', 'password': 'kdes', 'priority': 1},
    {'id': 40, 'account': 'kdps', 'alias': '港東國小', 'password': 'kdps', 'priority': 1},
    {'id': 41, 'account': 'snps', 'alias': '新南國小', 'password': 'snps', 'priority': 1},
    {'id': 42, 'account': 'spjh', 'alias': '新埤國中', 'password': 'spjh', 'priority': 1},
    {'id': 43, 'account': 'spes', 'alias': '新埤國小', 'password': 'spes', 'priority': 1},
    {'id': 44, 'account': 'dcps', 'alias': '大成國小', 'password': 'dcps', 'priority': 1},
    {'id': 45, 'account': 'syjh', 'alias': '新園國中', 'password': 'syjh', 'priority': 1},
    {'id': 46, 'account': 'sjes', 'alias': '仙吉國小', 'password': 'sjes', 'priority': 1},
    {'id': 47, 'account': 'wyps', 'alias': '瓦磘國小', 'password': 'wyps', 'priority': 1},
    {'id': 48, 'account': 'dles', 'alias': '丹路國小', 'password': 'dles', 'priority': 1},
    {'id': 49, 'account': 'nses', 'alias': '內獅國小', 'password': 'nses', 'priority': 1},
    {'id': 50, 'account': 'sjps', 'alias': '新庄國小', 'password': 'sjps', 'priority': 1},
    {'id': 51, 'account': 'sses', 'alias': '新興國小', 'password': 'sses', 'priority': 1},
    {'id': 52, 'account': 'shes', 'alias': '興化國小', 'password': 'shes', 'priority': 1},
    {'id': 53, 'account': 'jlps', 'alias': '竹林國小', 'password': 'jlps', 'priority': 1},
    {'id': 54, 'account': 'chsps', 'alias': '赤山國小', 'password': 'chsps', 'priority': 1},
    {'id': 55, 'account': 'mjjhs', 'alias': '滿州國中', 'password': 'mjjhs', 'priority': 1},
    {'id': 56, 'account': 'kcjhs', 'alias': '光春國中', 'password': 'kcjhs', 'priority': 1},
    {'id': 57, 'account': 'wutps', 'alias': '霧臺國小', 'password': 'wutps', 'priority': 1},
    {'id': 58, 'account': 'lgbn', 'alias': '勵古百合分校', 'password': 'lgbn', 'priority': 1},
]

township_info_array = [
    TownshipInfo(1, "九如鄉", "後庄國小"),
    TownshipInfo(2, "九如鄉", "惠農國小"),
    TownshipInfo(3, "內埔鄉", "新生國小"),
    TownshipInfo(4, "內埔鄉", "榮華國小"),
    TownshipInfo(5, "內埔鄉", "富田國小"),
    TownshipInfo(6, "內埔鄉", "佳義國小"),
    TownshipInfo(7, "牡丹鄉", "牡丹國小"),
    TownshipInfo(8, "牡丹鄉", "高士國小"),
    TownshipInfo(9, "牡丹鄉", "牡林分校"),
    TownshipInfo(10, "車城鄉", "車城國中"),
    TownshipInfo(11, "車城鄉", "車城國小"),
    TownshipInfo(12, "里港鄉", "里港國小"),
    TownshipInfo(13, "里港鄉", "土庫國小"),
    TownshipInfo(14, "里港鄉", "玉田國小"),
    TownshipInfo(15, "佳冬鄉", "佳冬國中"),
    TownshipInfo(16, "佳冬鄉", "羌園國小"),
    TownshipInfo(17, "佳冬鄉", "玉光國小"),
    TownshipInfo(18, "來義鄉", "文樂國小"),
    TownshipInfo(19, "東港鎮", "東港國中"),
    TownshipInfo(20, "東港鎮", "海濱國小"),
    TownshipInfo(21, "東港鎮", "大潭國小"),
    TownshipInfo(22, "枋山鄉", "楓港國小"),
    TownshipInfo(23, "枋寮鄉", "枋寮高中"),
    TownshipInfo(24, "枋寮鄉", "建興國小"),
    TownshipInfo(25, "枋寮鄉", "東海國小"),
    TownshipInfo(26, "林邊鄉", "林邊國中"),
    TownshipInfo(27, "林邊鄉", "仁和國小"),
    TownshipInfo(28, "林邊鄉", "崎峰國小"),
    TownshipInfo(29, "林邊鄉", "水利國小"),
    TownshipInfo(30, "長治鄉", "長興國小"),
    TownshipInfo(31, "南州鄉", "南州國中"),
    TownshipInfo(32, "南州鄉", "南州國小"),
    TownshipInfo(33, "屏東市", "大同高中"),
    TownshipInfo(34, "屏東市", "鶴聲國小"),
    TownshipInfo(35, "恆春鎮", "恆春國中"),
    TownshipInfo(36, "恆春鎮", "僑勇國小"),
    TownshipInfo(37, "恆春鎮", "大平國小"),
    TownshipInfo(38, "崁頂鄉", "崁頂國小"),
    TownshipInfo(39, "崁頂鄉", "港東國小"),
    TownshipInfo(40, "高樹鄉", "新南國小"),
    TownshipInfo(41, "新埤鄉", "新埤國中"),
    TownshipInfo(42, "新埤鄉", "新埤國小"),
    TownshipInfo(43, "新埤鄉", "大成國小"),
    TownshipInfo(44, "新園鄉", "新園國中"),
    TownshipInfo(45, "新園鄉", "仙吉國小"),
    TownshipInfo(46, "新園鄉", "瓦磘國小"),
    TownshipInfo(47, "獅子鄉", "丹路國小"),
    TownshipInfo(48, "獅子鄉", "內獅國小"),
    TownshipInfo(49, "萬丹鄉", "新庄國小"),
    TownshipInfo(50, "萬丹鄉", "新興國小"),
    TownshipInfo(51, "萬丹鄉", "興化國小"),
    TownshipInfo(52, "萬丹鄉", "竹林國小"),
    TownshipInfo(53, "萬巒鄉", "赤山國小"),
    TownshipInfo(54, "滿州鄉", "滿州國中"),
    TownshipInfo(55, "潮州鎮", "光春國中"),
    TownshipInfo(56, "霧台鄉", "霧臺國小"),
    TownshipInfo(57, "霧台鄉", "勵古百合分校")
]

datetime_dt = datetime.datetime.today()  # 獲得當地時間
dt = datetime_dt.date()  # 最小單位為日
format_dt = dt.strftime("%Y%m%d")  #


@app.get("/users")
def get_user():
    return township_info_array


@app.get("/users/{township}")
def get_user_from_township(
        township: str
):
    school_array = []
    for township_info in township_info_array:
        if township_info.township == township:
            school_array.append(township_info.school)

    if school_array:
        return school_array
    else:
        return "請選擇正確的鄉鎮市區"


# repair_id = 4
# repair_record_id = 1
repair_infos = []
repair_records = []


# repair_infos.append(
#     RepairInfo(
#         id=1,
#         school='楓港國小',
#         name='網管',
#         tel='08-7654321#12',
#         device_type='宏碁老師端電腦',
#         repair_description='office 無法使用',
#         start_time='2021/7/28 上午8:21:56',
#         end_time=None,
#         status='未接案',
#         repair_record=None
#     )
# )
# repair_infos.append(
#     RepairInfo(
#         id=2,
#         school='枋寮高中',
#         name='設備組長',
#         tel='08-7654321#12',
#         device_type='宏碁螢幕顯示器',
#         repair_description='螢幕時好時壞',
#         start_time='2021/7/29 上午10:43:50',
#         end_time=None,
#         status='未接案',
#         repair_record=None
#     )
# )
# repair_infos.append(
#     RepairInfo(
#         id=3,
#         school='丹路國小',
#         name='黃老師',
#         tel='0922222222',
#         device_type='宏碁學生端電腦',
#         repair_description='疑似中毒',
#         start_time='2021/7/30 上午7:30:30',
#         end_time=None,
#         status='未接案',
#         repair_record=None
#     )
# )


@app.post("/login")
def post_login(
        login: Login
):
    # global user_account_array
    token = ''

    username = login.username
    password = login.password

    for member in member_array:
        if username == member['account'] and password == member['password']:
            return {'alias': member['alias'], 'priority': member['priority']}
            break
        else:
            token = "未取得 token"
    return {'token: ': token}


@app.get("/repair_infos")
async def get_repair_infos():
    # return crud.crud_get_repair_info_db()
    # json_string = json.dumps([ob.__dict__ for ob in repair_infos])
    # return json_string
    return access_jsonfile.load_jsonfile()


@app.get("/repair_infos/{selected_id}")
def get_selected_info(
        selected_id: int
):
    access_jsonfile.load_jsonfile()
    for data in access_jsonfile.load_jsonfile():
        if data['id'] == selected_id:
            return data
    return None


@app.post("/repair_infos")
async def post_repair_info(
        repair_info: RepairInfo
):
    repair_info_dict = repair_info.dict()
    global repair_infos
    repair_infos_len: int
    if access_jsonfile.load_jsonfile() is None:
        repair_infos_len = 0
    else:
        repair_infos_len = len(access_jsonfile.load_jsonfile())
    repair_info_dict['id'] = repair_infos_len + 1
    repair_infos.append(repair_info_dict)
    access_jsonfile.write_jsonfile(repair_info_dict)
    # return repair_info_dict
    return access_jsonfile.load_jsonfile()

repair_record_dict_list = []


@app.put("/repair_infos/{selected_id}")
def put_repair_info(
        selected_id: int,
        repair_record: RepairRecord
):
    global repair_infos
    repair_infos = access_jsonfile.load_jsonfile()
    repair_record_dict = repair_record.dict()

    access_jsonfile.put_jsonfile(selected_id, repair_record_dict)
    return {'message': 'Put has been updated successfully'}


@app.put("/repair_infos/{selected_id}/detail")
def put_repair_info(
        selected_id: int,
        repair_status: str
):
    access_jsonfile.put_status_jsonfile(selected_id, repair_status)
    return {'message': 'Put has been updated successfully'}


@app.put("/repair_infos/{selected_id}/end_time")
def put_repair_info_end_time(
        selected_id: int,
        end_time: str
):
    access_jsonfile.put_end_time_jsonfile(selected_id, end_time)
    return {'message': 'Put has been updated successfully'}


@app.post("/repair_infos/change_password")
def post_change_password(
        account: str,
        password: str,
        new_password: str
):
    for member in member_array:
        if member["account"] == account and member["password"] == password:
            member["password"] == new_password
    return {'message': '成功變更'}


if __name__ == '__main__':
    uvicorn.run('main:app', host="0.0.0.0", port=5000, log_level="info", reload=True, debug=True, workers=1)
