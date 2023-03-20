from typing import Optional, List
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from pydantic import BaseModel
import datetime
import access_jsonfile
import access_dl_jsonfile
import access_aa_jsonfile
from model import township_info_array
from model import dl_township_info_array
from model import aa_township_info_array
from send_email import send_mail


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


class Member(BaseModel):
    id: int
    account: str
    password: str
    alias: str
    priority: int


datetime_dt = datetime.datetime.today()  # 獲得當地時間
dt = datetime_dt.date()  # 最小單位為日
format_dt = dt.strftime("%Y%m%d")  #

repair_infos = []
repair_records = []


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


@app.get("/members")
def get_members():
    return access_jsonfile.load_members_jsonfile()


@app.post("/repair_infos/change_password")
def post_change_password(
        account: str,
        password: str,
        new_password: str
):
    member_list = access_jsonfile.load_members_jsonfile()
    member_register = {}
    for member in member_list:
        if member["account"] == account and member["password"] == password:
            member_register = member
            break
        else:
            member_register = None
            # return {'message': 'Put has been updated successfully'}

    if member_register is None:
        return None
    else:
        access_jsonfile.put_members_jsonfile(member_register["id"], new_password)
        return {'message': 'Put has been updated successfully'}


@app.post("/login")
def post_login(
        login: Login
):
    # global user_account_array
    token = ''

    username = login.username
    password = login.password

    member_list = access_jsonfile.load_members_jsonfile()
    for member in member_list:
        if username == member['account'] and password == member['password']:
            return {'account': member['account'], 'alias': member['alias'], 'priority': member['priority']}
            break
        else:
            token = "未取得 token"
    return token


@app.get("/repair_infos")
async def get_repair_infos():
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
    send_mail(
        "ruruwu1127@gmail.com",
        "yuxp0130@gmail.com, fish33@swell.com.tw",
        repair_info_dict['school'],
        "申告學校：" + str(repair_info_dict['school']) + "\n申告內容：" + str(
            repair_info_dict['repair_description']) + "\n聯絡電話：" + str(repair_info_dict['tel'] + "\n\n\n鶴小案報修系統郵件通知")
    )
    return access_jsonfile.load_jsonfile()

# repair_record_dict_list = []


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


@app.post("/write_default_members")
def write_default_members(
    member_model_list: List[Member]
):
    return access_jsonfile.write_members_jsonfile(member_model_list)


@app.post("/write_default_repair_infos")
def write_default_members(
    repair_info_list: List[RepairInfo]
):
    return access_jsonfile.write_repair_info_jsonfile(repair_info_list)


@app.get("/====================================================================")
def 分隔線():
    return ""
# =========================================================================================================


dl_repair_infos = []
dl_repair_records = []


@app.get("/dl_users")
def get_dl_user():
    return dl_township_info_array


@app.get("/dl_users/{township}")
def get_dl_user_from_township(
        township: str
):
    school_array = []
    for dl_township_info in dl_township_info_array:
        if dl_township_info.township == township:
            school_array.append(dl_township_info.school)

    if school_array:
        return school_array
    else:
        return "請選擇正確的鄉鎮市區"


@app.get("/dl_members")
def get_dl_members():
    return access_dl_jsonfile.load_dl_members_jsonfile()


@app.post("/dl_repair_infos/dl_change_password")
def post_dl_change_password(
        account: str,
        password: str,
        new_password: str
):
    member_list = access_dl_jsonfile.load_dl_members_jsonfile()
    member_register = {}
    for member in member_list:
        if member["account"] == account and member["password"] == password:
            member_register = member
            break
        else:
            member_register = None

    if member_register is None:
        return None
    else:
        access_dl_jsonfile.put_dl_members_jsonfile(member_register["id"], new_password)
        return {'message': 'Put has been updated successfully'}


@app.post("/dl_login")
def post_dl_login(
        login: Login
):
    token = ''

    username = login.username
    password = login.password

    member_list = access_dl_jsonfile.load_dl_members_jsonfile()
    for member in member_list:
        if username == member['account'] and password == member['password']:
            return {'account': member['account'], 'alias': member['alias'], 'priority': member['priority']}
            break
        else:
            token = "未取得 token"
    return token


@app.get("/dl_repair_infos")
async def get_dl_repair_infos():
    return access_dl_jsonfile.load_dl_jsonfile()


@app.get("/dl_repair_infos/{selected_id}")
def get_dl_selected_info(
        selected_id: int
):
    access_dl_jsonfile.load_dl_jsonfile()
    for data in access_dl_jsonfile.load_dl_jsonfile():
        if data['id'] == selected_id:
            return data
    return None


@app.post("/dl_repair_infos")
async def post_dl_repair_info(
        repair_info: RepairInfo
):
    repair_info_dict = repair_info.dict()
    global repair_infos
    repair_infos_len: int
    if access_dl_jsonfile.load_dl_jsonfile() is None:
        repair_infos_len = 0
    else:
        repair_infos_len = len(access_dl_jsonfile.load_dl_jsonfile())
    repair_info_dict['id'] = repair_infos_len + 1
    repair_infos.append(repair_info_dict)
    access_dl_jsonfile.write_dl_jsonfile(repair_info_dict)
    send_mail(
        "ruruwu1127@gmail.com",
        "yuxp0130@gmail.com, fish33@swell.com.tw",
        repair_info_dict['school'],
        "申告學校：" + str(repair_info_dict['school']) + "\n申告內容：" + str(
            repair_info_dict['repair_description']) + "\n聯絡電話：" + str(repair_info_dict['tel'] + "\n\n\n校園智慧網路優化案報修系統郵件通知")
    )
    return access_dl_jsonfile.load_dl_jsonfile()


@app.put("/dl_repair_infos/{selected_id}")
def put_dl_repair_info(
        selected_id: int,
        repair_record: RepairRecord
):
    global repair_infos
    repair_infos = access_dl_jsonfile.load_dl_jsonfile()
    repair_record_dict = repair_record.dict()
    access_dl_jsonfile.put_dl_jsonfile(selected_id, repair_record_dict)
    return {'message': 'Put has been updated successfully'}


@app.put("/dl_repair_infos/{selected_id}/detail")
def put_dl_repair_info(
        selected_id: int,
        repair_status: str
):
    access_dl_jsonfile.put_dl_status_jsonfile(selected_id, repair_status)
    return {'message': 'Put has been updated successfully'}


@app.put("/dl_repair_infos/{selected_id}/end_time")
def put_dl_repair_info_end_time(
        selected_id: int,
        end_time: str
):
    access_dl_jsonfile.put_dl_end_time_jsonfile(selected_id, end_time)
    return {'message': 'Put has been updated successfully'}


@app.post("/dl_write_default_members")
def dl_write_default_members(
    member_model_list: List[Member]
):
    return access_dl_jsonfile.write_dl_members_jsonfile(member_model_list)


@app.post("/dl_write_default_repair_infos")
def dl_write_default_members(
    repair_info_list: List[RepairInfo]
):
    return access_dl_jsonfile.write_dl_repair_info_jsonfile(repair_info_list)


@app.get("/dl====================================================================")
def dl_分隔線():
    return ""


aa_repair_infos = []
aa_repair_records = []


@app.get("/aa_users")
def get_aa_user():
    return aa_township_info_array


@app.get("/aa_users/{township}")
def get_aa_user_from_township(
        township: str
):
    school_array = []
    for aa_township_info in aa_township_info_array:
        if aa_township_info.township == township:
            school_array.append(aa_township_info.school)

    if school_array:
        return school_array
    else:
        return "請選擇正確的鄉鎮市區"


@app.get("/aa_members")
def get_aa_members():
    return access_aa_jsonfile.load_aa_members_jsonfile()


@app.post("/aa_repair_infos/aa_change_password")
def post_aa_change_password(
        account: str,
        password: str,
        new_password: str
):
    member_list = access_aa_jsonfile.load_aa_members_jsonfile()
    member_register = {}
    for member in member_list:
        if member["account"] == account and member["password"] == password:
            member_register = member
            break
        else:
            member_register = None

    if member_register is None:
        return None
    else:
        access_aa_jsonfile.put_aa_members_jsonfile(member_register["id"], new_password)
        return {'message': 'Put has been updated successfully'}


@app.post("/aa_login")
def post_aa_login(
        login: Login
):
    token = ''

    username = login.username
    password = login.password

    member_list = access_aa_jsonfile.load_aa_members_jsonfile()
    for member in member_list:
        if username == member['account'] and password == member['password']:
            return {'account': member['account'], 'alias': member['alias'], 'priority': member['priority']}
            break
        else:
            token = "未取得 token"
    return token


@app.get("/aa_repair_infos")
async def get_aa_repair_infos():
    return access_aa_jsonfile.load_aa_jsonfile()


@app.get("/aa_repair_infos/{selected_id}")
def get_aa_selected_info(
        selected_id: int
):
    access_aa_jsonfile.load_aa_jsonfile()
    for data in access_aa_jsonfile.load_aa_jsonfile():
        if data['id'] == selected_id:
            return data
    return None


@app.post("/aa_repair_infos")
async def post_aa_repair_info(
        repair_info: RepairInfo
):
    repair_info_dict = repair_info.dict()
    global repair_infos
    repair_infos_len: int
    if access_aa_jsonfile.load_aa_jsonfile() is None:
        repair_infos_len = 0
    else:
        repair_infos_len = len(access_aa_jsonfile.load_aa_jsonfile())
    repair_info_dict['id'] = repair_infos_len + 1
    repair_infos.append(repair_info_dict)
    access_aa_jsonfile.write_aa_jsonfile(repair_info_dict)
    send_mail(
        "ruruwu1127@gmail.com",
        "yuxp0130@gmail.com, fish33@swell.com.tw",
        repair_info_dict['school'],
        "申告學校：" + str(repair_info_dict['school']) + "\n申告內容：" + str(
            repair_info_dict['repair_description']) + "\n聯絡電話：" + str(repair_info_dict['tel'] + "\n\n\nAP新增汰換案報修系統郵件通知")
    )
    return access_aa_jsonfile.load_aa_jsonfile()


@app.put("/aa_repair_infos/{selected_id}")
def put_aa_repair_info(
        selected_id: int,
        repair_record: RepairRecord
):
    global repair_infos
    repair_infos = access_aa_jsonfile.load_aa_jsonfile()
    repair_record_dict = repair_record.dict()
    access_aa_jsonfile.put_aa_jsonfile(selected_id, repair_record_dict)
    return {'message': 'Put has been updated successfully'}


@app.put("/aa_repair_infos/{selected_id}/detail")
def put_aa_repair_info(
        selected_id: int,
        repair_status: str
):
    access_aa_jsonfile.put_aa_status_jsonfile(selected_id, repair_status)
    return {'message': 'Put has been updated successfully'}


@app.put("/aa_repair_infos/{selected_id}/end_time")
def put_aa_repair_info_end_time(
        selected_id: int,
        end_time: str
):
    access_aa_jsonfile.put_aa_end_time_jsonfile(selected_id, end_time)
    return {'message': 'Put has been updated successfully'}


@app.post("/aa_write_default_members")
def aa_write_default_members(
    member_model_list: List[Member]
):
    return access_aa_jsonfile.write_aa_members_jsonfile(member_model_list)


@app.post("/aa_write_default_repair_infos")
def aa_write_default_members(
    repair_info_list: List[RepairInfo]
):
    return access_aa_jsonfile.write_aa_repair_info_jsonfile(repair_info_list)


if __name__ == '__main__':
    uvicorn.run('main:app', host="0.0.0.0", port=5000, log_level="info", reload=True, debug=True, workers=1)
