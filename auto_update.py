import json
import os
from os import listdir
from os import system as cmd
from sys import exit
from sys import path;
from time import sleep
import subprocess
from github import GitHub

MY_PATH = path[0]

ROOT = None
REPOSITORY = None
USERNAME = None
TOKEN = None
START = []
with open("config.txt", "r") as f:
    for line in f:
        if "ROOT" in line:
            ROOT = line.split("==")[1].replace("\n","")
        elif "REPOSITORY" in line:
            REPOSITORY = line.split("==")[1].replace("\n","")
        elif "START" in line:
            START = line.split("==")[1].replace("\n","")
        elif "USERNAME" in line:
            USERNAME = line.split("==")[1].replace("\n","")
        elif "TOKEN" in line:
            TOKEN = line.split("==")[1].replace("\n", "")
if not START:
    print("Not found START, this is path where is you repository")
    print("Please, set ROOT in config file.")
    exit()
if not ROOT:
    print("Not found ROOT, this is path where is you repository")
    print("Please, set ROOT in config file.")
    exit()
if not REPOSITORY:
    print("Not found REPOSITORY, this is name of your repository")
    print("Please, set REPOSITORY into config file.")
    exit()
if not USERNAME:
    print("Not found USERNAME, this is name of account where is your repository")
    print("Please, set USERNAME into config file.")
    exit()
if not TOKEN:
    print("Not found TOKEN, this is token of account")
    print("Please, set TOKEN into config file.")
    exit()

git = GitHub(TOKEN, user_name=USERNAME)
process = None

if not "history.json" in listdir():
    print("No such history file")
    with open("history.json", "w") as f:
        f.write(json.dumps({"last": None}))
    print("Create history file")


def save(data: dict, path="history.json"):
    with open(path, "w") as f:
        f.write(json.dumps(data))

def stop_program():
    global process
    if process:
        process.kill()
def found_new_changes():
    os.chdir(ROOT)
    print("have changes!")
    print("update repository...")
    cmd(f"git pull")
    stop_program()
    start_program()
    print("successfully update")
    os.chdir(MY_PATH)

def start_program():
    global START
    global ROOT
    global process
    os.chdir(ROOT)
    process = subprocess.Popen(START.split(" "))

while True:
    repository = git.get_repo(REPOSITORY)
    if not repository:
        print("Repository has no found!")
        continue
    history = json.load(open("history.json", "r"))
    last_update = history.get("last", None)
    if last_update:
        if last_update != repository["pushed_at"]:
            found_new_changes()
        save({"last": repository["pushed_at"]})
    else:
        last_update = repository["pushed_at"]
        save({"last": last_update})

        print("Not have last data")

    sleep(10)
