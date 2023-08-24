from fastapi import APIRouter
from typing import List
import model
from model import hpps_township_info_array
from send_email import send_mail
import access_hpps_jsonfile

hpps_router = APIRouter()

hpps_repair_infos = []
hpps_repair_records = []


@hpps_router.get("/hpps_users")
def get_hpps_user():
    return hpps_township_info_array


@hpps_router.get("/hpps_users/{township}")
def get_hpps_user_from_township(
        township: str
):
    school_array = []
    for hpps_township_info in hpps_township_info_array:
        if hpps_township_info.township == township:
            school_array.append(hpps_township_info.school)

    if school_array:
        return school_array
    else:
        return "請選擇正確的鄉鎮市區"


@hpps_router.get("/hpps_members")
def get_hpps_members():
    return access_hpps_jsonfile.load_hpps_members_jsonfile()


@hpps_router.post("/hpps_repair_infos/hpps_change_password")
def post_hpps_change_password(
        account: str,
        password: str,
        new_password: str
):
    member_list = access_hpps_jsonfile.load_hpps_members_jsonfile()
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
        access_hpps_jsonfile.put_hpps_members_jsonfile(member_register["id"], new_password)
        return {'message': 'Put has been updated successfully'}


@hpps_router.post("/hpps_login")
def post_hpps_login(
        login: model.Login
):
    token = ''

    username = login.username
    password = login.password

    member_list = access_hpps_jsonfile.load_hpps_members_jsonfile()
    for member in member_list:
        if username == member['account'] and password == member['password']:
            return {'account': member['account'], 'alias': member['alias'], 'priority': member['priority']}
        else:
            token = "未取得 token"
    return token


@hpps_router.get("/hpps_repair_infos")
async def get_hpps_repair_infos():
    return access_hpps_jsonfile.load_hpps_jsonfile()


@hpps_router.get("/hpps_repair_infos/{selected_id}")
def get_hpps_selected_info(
        selected_id: int
):
    access_hpps_jsonfile.load_hpps_jsonfile()
    for data in access_hpps_jsonfile.load_hpps_jsonfile():
        if data['id'] == selected_id:
            return data
    return None


@hpps_router.post("/hpps_repair_infos")
async def post_hpps_repair_info(
        repair_info: model.RepairInfo
):
    repair_info_dict = repair_info.dict()
    global hpps_repair_infos
    repair_infos_len: int
    if access_hpps_jsonfile.load_hpps_jsonfile() is None:
        repair_infos_len = 0
    else:
        repair_infos_len = len(access_hpps_jsonfile.load_hpps_jsonfile())
    repair_info_dict['id'] = repair_infos_len + 1
    hpps_repair_infos.append(repair_info_dict)
    access_hpps_jsonfile.write_hpps_jsonfile(repair_info_dict)
    send_mail(
        "ruruwu1127@gmail.com",
        "yuxp0130@gmail.com, fish33@swell.com.tw",
        repair_info_dict['school'],
        "申告學校：" + str(repair_info_dict['school']) + "\n申告內容：" + str(
            repair_info_dict['repair_description']) + "\n聯絡電話：" + str(repair_info_dict['tel'] + "\n\n\n和平國小案報修系統郵件通知")
    )
    return access_hpps_jsonfile.load_hpps_jsonfile()


@hpps_router.put("/hpps_repair_infos/{selected_id}")
def put_hpps_repair_info(
        selected_id: int,
        repair_record: model.RepairRecord
):
    global hpps_repair_infos
    hpps_repair_infos = access_hpps_jsonfile.load_hpps_jsonfile()
    repair_record_dict = repair_record.dict()
    access_hpps_jsonfile.put_hpps_jsonfile(selected_id, repair_record_dict)
    return {'message': 'Put has been updated successfully'}


@hpps_router.put("/hpps_repair_infos/{selected_id}/detail")
def put_hpps_repair_info(
        selected_id: int,
        repair_status: str
):
    access_hpps_jsonfile.put_hpps_status_jsonfile(selected_id, repair_status)
    return {'message': 'Put has been updated successfully'}


@hpps_router.put("/hpps_repair_infos/{selected_id}/end_time")
def put_hpps_repair_info_end_time(
        selected_id: int,
        end_time: str
):
    access_hpps_jsonfile.put_hpps_end_time_jsonfile(selected_id, end_time)
    return {'message': 'Put has been updated successfully'}


@hpps_router.post("/hpps_write_default_members")
def hpps_write_default_members(
    member_model_list: List[model.Member]
):
    return access_hpps_jsonfile.write_hpps_members_jsonfile(member_model_list)


@hpps_router.post("/hpps_write_default_repair_infos")
def hpps_write_default_members(
    repair_info_list: List[model.RepairInfo]
):
    return access_hpps_jsonfile.write_hpps_repair_info_jsonfile(repair_info_list)
