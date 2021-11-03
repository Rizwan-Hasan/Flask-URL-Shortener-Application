import logging

import redis

from rediscache import host, port, password, dbNo


# Redis Connector ↓
class RedisConnect:
    def __init__(self, counterName: str, counter: int):
        try:
            self.__pool = redis.ConnectionPool(
                decode_responses=True, host=host, port=port, password=password, db=dbNo
            )
            self.__counterName: str = counterName
            self.__counter: int = counter
            self.__urltable = None
        except Exception as e:
            logging.error(e)

    def __getConnection(self):
        return redis.Redis(connection_pool=self.__pool)

    def setUrlTableObject(self, urltable):
        self.__urltable = urltable

    def getNewCounter(self):
        while True:
            try:
                conn = self.__getConnection()
                counter = conn.get(self.__counterName)
                if counter is None:
                    conn.set(
                        self.__counterName,
                        self.__counter + self.__urltable.getRowCount(),
                    )
                counter = conn.incr(self.__counterName)
                conn.close()
                return counter
            except Exception as e:
                logging.error(e)

    def storeURL(self, url: str, short_url: str, expire: int):
        while True:
            try:
                conn = self.__getConnection()
                conn.set(f"{short_url}", f"{url}", ex=expire)
                conn.close()
                return True
            except Exception as e:
                logging.error(e)

    def getLongUrl(self, short_url: str):
        while True:
            try:
                conn = self.__getConnection()
                tmp = conn.get(f"{short_url}")
                conn.close()
                if tmp is not None:
                    return tmp
                else:
                    return None
            except Exception as e:
                logging.error(e)


if __name__ == "__main__":
    print("Hello World")
