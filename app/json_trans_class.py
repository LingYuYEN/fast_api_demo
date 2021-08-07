from typing import List
from pydantic import BaseModel


class MemberModel(BaseModel):
    id: int
    account: str
    password: str
    priority: int


user_a = MemberModel(id=1, account='aaps', password='aaps', priority=1)
# user_b = MemberModel(2, 'bbps', 'bbps', 1)
# user_c = MemberModel(3, 'ccps', 'ccps', 1)
# user_d = MemberModel(4, 'ddps', 'ddps', 1)

# user_a = {'id': 1, 'account': 'aaps', 'password': 'aaps', 'priority': 1}
user_array = [user_a]

print(user_array)
