import json
import os
global DB
global DataBase
DB = ""


class PolyMathDB:
    global DB,DataBase
    with open(f"{DB}.json", "w") as file:
        DataBase = file.read()
    
    def createDB(self,name):
        global DB
        DB = name
        os.system(f"touch {DB}.json")
        

    def add(self, key, value):
        global DB,DataBase
        data = {key:value}
        DataBase.update(data)
        print(DataBase)
        # with open(f"{DB}.json", "w") as file:
        #     json.dump(data, file)
        # Content = json.load(open(f"{DB}.json"))
        # DataBase.update(Content) 
        # DataBase.update(data)
        # print(DataBase)
        