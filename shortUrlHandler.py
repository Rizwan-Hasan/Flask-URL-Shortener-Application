from app import cache
from base26 import Base26Converter
from database import urltable


class ShortURL:
    def __init__(self):
        self.__cacheUrlExpireTimeout: int = 300
        self.__base26 = Base26Converter()
        cache.setUrlTableObject(urltable=urltable)

    def getShortURL(self, longURL: str):
        longURL: str = longURL.strip()
        shortURL = urltable.getShortURL(long_url=longURL)
        if shortURL is None:
            uid: int = cache.getNewCounter()
            shortURL: str = self.__base26.encode(uid)
            longURL: str = longURL.strip()
            urltable.insertURL(uid=uid, long_url=longURL, short_url=shortURL)
        cache.storeURL(
            url=longURL, short_url=shortURL, expire=self.__cacheUrlExpireTimeout
        )
        return shortURL

    def getLongURL(self, short_url: str):
        short_url = short_url.strip()
        longURL: str = cache.getLongUrl(short_url=short_url)
        if longURL is None:
            longURL = urltable.getLongURL(short_url=short_url)
            if longURL is None:
                return None
        cache.storeURL(
            url=longURL, short_url=short_url, expire=self.__cacheUrlExpireTimeout
        )
        return longURL


if __name__ == "__main__":
    print("Hello World")
