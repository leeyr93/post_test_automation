import uuid

def generate_random_user_id():
    return f"user{uuid.uuid4().hex[:8]}"   # 언더스코어 제거