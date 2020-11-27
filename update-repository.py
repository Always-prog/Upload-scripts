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
START = []
with open("config.txt", "r") as f:
    for line in f:
        if "ROOT" in line:
            ROOT = line.split("==")[1][:-1]
        elif "REPOSITORY" in line:
            REPOSITORY = line.split("==")[1][:-1]
        if "START" in line:
            START = str(line.split("==")[1][:-1]).split(";")
if not START:
    print("Not found START, this is path where is you repository")
    print("Please, set ROOT in config file.")
    exit()
if not ROOT:
    print("Not found ROOT, this is path where is you repository")
    print("Please, set ROOT in config file.")
    exit()
elif not REPOSITORY:
    print("Not found REPOSITORY, this is name of your repository")
    print("Please, set REPOSITORY into config file.")
    exit()

token = json.load(open("keys.json", "r"))["token"]
git = GitHub(token, user_name="Always-prog")
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
    for command in START:
        process = subprocess.Popen(command.split(" "))

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

    sleep(2)
