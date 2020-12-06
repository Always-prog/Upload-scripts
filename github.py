import json


class GitHub():
    def __init__(self, token, user_name: str):
        import requests
        self.requests = requests
        self.__USER__ = {
            "name":user_name
        }
        self.__URLS__ = {
            "repos":"https://api.github.com/user/repos",
            "repos_list":f"https://api.github.com/users/{self.__USER__['name']}/repos",
        }
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
    def post(self, url, **data):
        return self.requests.post(url, data, headers=self.__AUTHORIZE__["request"]["headers"])
    def get(self, url, **data):
        return self.requests.get(url, data, headers=self.__AUTHORIZE__["request"]["headers"])

    def get_repositories(self, **data):
        return self.get(url=self.__URLS__["repos"], **data)

    def get_repo(self, name: str):
        repos = self.get_repositories(json={"sort":name})
        for r in repos.json():
            if "name" in r:
                if r["name"] == name:
                    return r
