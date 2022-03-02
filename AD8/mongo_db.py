import pymongo

mydict = {
  "12125454" : {
    "name" : "Hilda",
    "major" : "App Dev"
  },
  "54009323" : {
    "name" : "Tony",
    "major" : "CS"
  },
  "37882108" : {
    "name" : "Louise",
    "major" : "IT"
  }
}

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"]

print(myclient.list_database_names())

mycol = mydb["students"]

x = mycol.insert_many([mydict])

print(x)

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"]

mycol = mydb["students"]

myquery = {"12125454" : {"major" : "App Dev"}}

print(mycol.find(myquery))
