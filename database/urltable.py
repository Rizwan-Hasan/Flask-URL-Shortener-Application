import logging

from app import db


# UrlTable Table Model ↓
class UrlTable(db.getBase()):
    __tablename__ = "URLTABLE"
    __table_args__ = {"autoload": True, "autoload_with": db.getEngine()}


# Table Queries ↓


def getRowCount():
    dbSession = db.getSession()
    count: int = dbSession.query(UrlTable).count()
    dbSession.close()
    return count


def getLongURL(short_url: str):
    dbSession = db.getSession()
    longURL: list = (
        dbSession.query(UrlTable.URL).filter(UrlTable.SHORT_URL == short_url).all()
    )
    dbSession.close()
    if longURL:
        return longURL[0][0]
    else:
        return None


def getShortURL(long_url: str):
    dbSession = db.getSession()
    shortURL: list = (
        dbSession.query(UrlTable.SHORT_URL).filter(UrlTable.URL == long_url).all()
    )
    dbSession.close()
    if shortURL:
        return shortURL[0][0]
    else:
        return None


def insertURL(uid: int, long_url: str, short_url: str):
    try:
        dbSession = db.getSession()
        newRow = UrlTable(ID=uid, URL=long_url, SHORT_URL=short_url)
        dbSession.add(newRow)
        dbSession.commit()
        dbSession.close()
    except Exception as e:
        logging.error(str(e.__dict__["orig"]))
        return False
    return True


if __name__ == "__main__":
    print("Hello World")
