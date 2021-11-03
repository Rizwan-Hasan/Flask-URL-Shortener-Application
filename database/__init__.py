import json

# Database Information ↓

with open("database-redis-config.json", "r", encoding="utf-8") as file:
    config: dict = json.load(file)["database"]
    host: str = config["host"]
    dbname: str = config["dbname"]
    user: str = config["user"]
    password: str = config["password"]
    del config
