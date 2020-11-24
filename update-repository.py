import json


class GitHub():
    def __init__(self, token):
        import requests
        self.requests = requests
        self.__TOKEN__ = token
        self.__AUTHORIZE__ = {
            "data":{
                "token":self.__TOKEN__
            },
            "request":{
                "headers":{
                    "Authorization": "token " + token
                }
            }

        }
    def get_repositories(self, **data):
        return self.requests.get("https://api.github.com/user/repos", data,headers=self.__AUTHORIZE__["request"]["headers"])

token = json.load(open("keys.json","r"))["token"]
git = GitHub(token)
print(git.get_repositories().json())