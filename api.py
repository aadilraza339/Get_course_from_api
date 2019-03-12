import json
import requests
import os.path
from os import path




if path.exists("courses.json"):
    with open("courses.json","r+") as count:
        data=json.load(count)
else:
    url="http://saral.navgurukul.org/api/courses"
    w = requests.get(url).text
    # print (w)
    with open("cours.json","w+") as count:
        count.write(w)
        data = json.loads(w)

print (data)



a=1 
courses=[]
ids =[]
for i in data["availableCourses"]:
    courses.append(i["name"])
    ids.append(i['id'])
    dic=a,i["name"]
    a=a+1
    print(dic)
user = int(input("enter what you went"))
print(courses[user-1])
var=(ids[user-1])




new_url = 'http://saral.navgurukul.org/api/courses/'+str(ids[user-1])+'/exercises'
page = requests.get(new_url).text
war=json.loads(page)
b=war["data"]
num=1
for j in b:
    dr=(num,j["name"])
    print (dr)
    num=num+1   
print(j["slug"])
user1=int(input("enter your slugs"))
f=(war["data"])
slug1 = f[user1-1]["slug"]
slug_url='http://saral.navgurukul.org/api/courses/{}/exercise/getBySlug?slug={}'.format(var,slug1)
page1=requests.get(slug_url)
loads=page1.json()
reads=loads["content"]
print(reads)




