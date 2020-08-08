import json

# Redis Server Information ↓

with open('database-redis-config.json', 'r', encoding='utf-8') as file:
    config: dict = json.load(file)['redis']
    host: str = config['host']
    port: int = config['port']
    password: str = config['password']
    dbNo: int = config['dbNo']
    sslStatus: bool = config['sslStatus']
    del config
