import os

# Redis Server Information ↓
host: str = os.environ["REDIS_HOST"]
port: int = int(os.environ["REDIS_PORT"])
password: str = os.environ["REDIS_PASSWD"]
dbNo: int = int(os.environ["REDIS_DB_NO"])
