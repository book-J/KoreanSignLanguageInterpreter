from typing import Optional
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
import pymongo
import json
import yaml
app = FastAPI()
myclient = pymongo.MongoClient("mongodb://mongo-server:27017")
mydb = myclient["mydatabase"]
bookcol=mydb["books"]
usercol = mydb["users"]


@app.post("/v1/books/{bid}")
async def post_book(bid: str, publisher: str, author: str):
    chk=bookcol.find_one({"bid":bid})
    if(chk is None):
        bookcol.insert_one({"bid":bid, "pid":publisher, "aid":author})
        return {"result":"SUCCESS"}
    else:
        return {"result":"FAILED"}

@app.get("/v1/books/{bid}")
async def get_book(bid:str):
    chk = bookcol.find_one({"bid":bid})
    if(chk is not None):
        result ={"BID":chk["bid"], "PID":chk["pid"], "AID":chk["aid"]}
        return result
    else:
        return {"result":"FAILED"}
@app.delete("/v1/books/{bid}")
async def del_book(bid:str):
    chk = bookcol.find_one({"bid":bid})
    if(chk is not None):
        bookcol.delete_one({"bid":bid})
        return {"result":"SUCCESS"}
    else:
        return {"result":"FAILED"}
@app.get("/v1/books")
async def get_books(publisher="", author=""):
    if(publisher=="" or author==""):
        return {"result":"FAILED"}
    else:
        booklist = []
        iterfind = bookcol.find({"pid":publisher, "aid":author},{"_id":0})
        for x in iterfind:
            booklist.append({"BID":x["bid"], "PID":x["pid"], "AID":x["aid"]})
        return booklist


@app.post("/v1/users/{uid}")
async def post_user(uid: str, name: str, age:int=0):
    chk=usercol.find_one({"uid":uid})
    if((chk is None) and (age>=0) and (age<=200)):
        usercol.insert_one({"uid":uid, "name":name, "age":age})
        return {"result":"SUCCESS"}
    else:
        return {"result":"FAILED"}

@app.get("/v1/users/{uid}")
async def get_user(uid:str):
    chk = usercol.find_one({"uid":uid})
    if(chk is not None):
        result ={"UID":chk["uid"], "Name":chk["name"], "Age":chk["age"]}
        return result
    else:
        return {"result":"FAILED"}
@app.delete("/v1/users/{uid}")
async def del_user(uid:str):
    chk = usercol.find_one({"uid":uid})
    if(chk is not None):
        usercol.delete_one({"uid":uid})
        return {"result":"SUCCESS"}
    else:
        return {"result":"FAILED"}

@app.get("/v1/")
async def get_manual():
    with open("api_manual.yaml") as f:
        api_manual=yaml.load(f)
        return api_manual