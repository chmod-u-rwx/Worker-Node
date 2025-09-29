import uuid
from datetime import datetime

def add_local_fields(user_dict: dict) -> dict:


    user_dict["join_date"] = datetime.now().strftime("%m/%d/%Y")
    user_dict["worker_id"] = str(uuid.uuid4())
    return user_dict
