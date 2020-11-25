import json
from github import GitHub
from time import sleep
from os import listdir
from os import system as cmd
import os
from sys import exit
from sys import path;MY_PATH = path[0]

ROOT = None
REPOSITORY = None
with open("config.txt", "r") as f:
    for line in f:
        if "ROOT" in line:
            ROOT = line.split("==")[1]
        elif "REPOSITORY" in line:
            REPOSITORY = line.split("==")[1]

if not ROOT:
    print("Not found ROOT, this is path where is you repository")
    print("Please, set ROOT in config file.")
    exit()
elif not REPOSITORY:
    print("Not found REPOSITORY, this is name of your repository")
    print("Please, set REPOSITORY into config file.")
    exit()





token = json.load(open("keys.json","r"))["token"]
git = GitHub(token, user_name="Always-prog")

if not "history.json" in listdir():
    print("No such history file")
    with open("history.json","w") as f:
        f.write(json.dumps({"last":None}))
    print("Create history file")

def save(data: dict,path="history.json"):
    with open(path,"w") as f:
        f.write(json.dumps(data))

while True:
    repository = git.get_repo(REPOSITORY)
    if not repository:
        print("Repository has no found!")
        continue
    history = json.load(open("./history.json","r"))
    last_update = history.get("last",None)
    if last_update:
        if last_update != repository["pushed_at"]:
            os.chdir(ROOT)
            print("have changes!")
            print("update repository...")
            cmd(f"git pull")
            print("successfully update")
            os.chdir(MY_PATH)

        save({"last": repository["pushed_at"]})
    else:
        last_update = repository["pushed_at"]
        save({"last":last_update})

        print("Not have last data")

    sleep(2)