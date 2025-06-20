import redis
import os
import json
from dotenv import load_dotenv

load_dotenv()

r = redis.Redis(
    host=os.getenv("REDIS_HOST"),
    port=int(os.getenv("REDIS_PORT")),
    decode_responses=True
)

def cache_message(user_id, question, answer):
    key = f"chat:{user_id}"
    msg = json.dumps({"question": question, "answer": answer})
    r.lpush(key, msg)
    r.ltrim(key, 0, 19)  # Keep only the latest 20 messages

def get_cached_messages(user_id):
    key = f"chat:{user_id}"
    messages = r.lrange(key, 0, -1)
    return [json.loads(m) for m in messages]
