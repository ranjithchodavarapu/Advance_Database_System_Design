import pymongo
import datetime

client = pymongo.MongoClient("mongodb+srv://.....:.....@employee.m35ak.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

db = client.sample_restaurants

restaurants = db.restaurants


# question 1 "display all the documents in the collection restaurants"
for i in restaurants.find():
    print(i)


# question 2 "display the fields restaurant_id, name, borough and cuisine"
for i in restaurants.find({},{"restaurant_id" : 1,"name":1,"borough":1,"cuisine" :1}):
    print(i)


# question 3 "display the fields restaurant_id, name, borough and cuisine, but exclude the field _id "
for i in restaurants.find({},{"restaurant_id" : 1,"name":1,"borough":1,"cuisine" :1,"_id":0}):
    print(i)


#question 4 "display the fields restaurant_id, name, borough and zip code, but exclude the field _id"
for i in restaurants.find({},{"restaurant_id" : 1,"name":1,"borough":1,"address.zipcode" :1,"_id":0}):
    print(i)


#question 5 " display all the restaurant which is in the borough Bronx"
for i in restaurants.find({"borough": "Bronx"}):
    print(i)


# question 6 " display the first 5 restaurant which is in the borough Bronx"
for i in restaurants.find({"borough": "Bronx"})[:5]:
    print(i)


#question 7 "display the next 5 restaurants after skipping first 5 which are in the borough Bronx"
for i in restaurants.find({"borough": "Bronx"}).skip(5).limit(5):
    print(i)


#question 8 " find the restaurants who achieved a score more than 90"
for i in restaurants.find({"grades" : { "$elemMatch":{"score":{"$gt" : 90}}}}):
    print(i)


#question 9 " restaurants that achieved a score is more than 80 but less than 100"
for i in restaurants.find({"grades" : { "$elemMatch":{"score":{"$gt" : 80 , "$lt" :100}}}}):
    print(i)


#question 10 "  the restaurants which locate in latitude value less than -95.754168"
for i in restaurants.find({"address.coord" : {"$lt" : -95.754168}}):
    print(i)
    

#question 11 " restaurants that do not prepare any cuisine of 'American' and their grade score more than 70 and latitude less than -65.754168"
for i in restaurants.find({"$and":[{"cuisine" : {"$ne" :"American "}},{"grades.score" : {"$gt" : 70}},{"address.coord" : {"$lt" : -65.754168}}]}):
    print(i)


#question 12 "restaurants that do not prepare any cuisine of 'American' and their grade score more than 70 and latitude less than -65.754168 without and operator"
for i in restaurants.find({ "cuisine" : {"$ne" : "American "},"grades.score" :{"$gt": 70},"address.coord" : {"$lt" : -65.754168}}):
    print(i)


# question 14 "restaurant Id, name, borough and cuisine for those restaurants which contain 'Wil' as first three letters for its name"
for i in restaurants.find({ "name" : { "$regex": '^Wil',"$options":"$i"} }, { "name":1,  "borough":1, "restaurant_id":1, "cuisine" :1}):
    print(i)


#question 13 " restaurants which do not prepare any cuisine of American and achieved a grade point A not belongs to the borough Brooklyn"
for i in restaurants.find( {"cuisine" : {"$ne": "American "},"grades.grade" :"A","borough": {"$ne" : "Brooklyn"}}).sort("cuisine",-1):
    print(i)



# question 15 "restaurant Id, name, borough and cuisine for those restaurants which contain ces as last three letters for its name"
for i in restaurants.find({ "name" : { "$regex": 'ces$',"$options":"$i"} }, { "name":1,  "borough":1, "restaurant_id":1, "cuisine" :1}):
    print(i)


#question 16 " restaurant Id, name, borough and cuisine for those restaurants which contain Reg as three letters somewhere in its name"
for i in restaurants.find({ "name" : { "$regex": 'Reg.*',"$options":"$i"} }, { "name":1,  "borough":1, "restaurant_id":1, "cuisine" :1}):
    print(i)


#question 17 " find the restaurants which belong to the borough Bronx and prepared either American or Chinese dish"
for i in restaurants.find({ "borough": "Bronx" , "$or" : [{ "cuisine" : "American " },{ "cuisine" : "Chinese" }] }):
    print(i)



#question 18 "restaurant Id, name, borough and cuisine for those restaurants which belong to the borough Staten Island or Queens or Bronxor Brooklyn"
for i in restaurants.find({"borough" :{"$in" :["Staten Island","Queens","Bronx","Brooklyn"]}},{"restaurant_id" : 1,"name":1,"borough":1,"cuisine" :1}):
    print(i)


#question 19 " restaurant Id, name, borough and cuisine for those restaurants which are not belonging to the borough Staten Island or Queens or Bronxor Brooklyn"
for i in restaurants.find({"borough" :{"$nin" :["Staten Island","Queens","Bronx","Brooklyn"]}},{"restaurant_id" : 1,"name":1,"borough":1,"cuisine" :1}):
    print(i)


#question 20 " restaurant Id, name, borough and cuisine for those restaurants which achieved a score which is not more than 10"
for i in restaurants.find({"grades.score" : { "$not": {"$gt" : 10}}},{"restaurant_id" : 1,"name":1,"borough":1,"cuisine" :1}):
    print(i)


#question 21 "restaurant Id, name, borough and cuisine prepare specific dish except restaurant name begins with letter Wil"
for i in restaurants.find({"$or": [{ "name" : { "$regex": '^Wil',"$options":"$i"} }, {"$and": [{"cuisine" : {"$ne" :"American "}},  {"cuisine" : {"$ne" :"Chinees"}}]}]},{"restaurant_id" : 1,"name":1,"borough":1,"cuisine" :1}):
    print(i)


#question 22 " MongoDB query to find the restaurant Id, name, and grades for those restaurants which achieved a grade of "A" and scored 11 on an ISODate "2014-08-11T00:00:00Z" among many of survey dates."
for i in restaurants.find({ "grades.date":datetime.datetime(2014, 8, 11, 0 ,0), "grades.grade":"A" , "grades.score" : 11}, {"restaurant_id" : 1,"name":1,"grades":1}):
    print(i)

#question 23 " restaurant Id, name, and grades where the 2nd element of grades array contains a grade of A and score 9 on a specific date"
for i in restaurants.find({ "grades.1.date": datetime.datetime(2014, 8, 11, 0 ,0), "grades.1.grade":"A" , "grades.1.score" : 9}, {"restaurant_id" : 1,"name":1,"grades":1}):
    print(i)



#question 24 "restaurant Id, name, address and geographical location of the restaurants where 2nd element contains a value between 42 and 52"
for i in restaurants.find({ "address.coord.1": {"$gt" : 42, "$lte" : 52}}, {"restaurant_id" : 1,"name":1,"address":1,"coord":1}):
    print(i)


#question 25 "name of the restaurants in ascending order along with all the columns"
for i in restaurants.find({}).sort("name",1):
    print(i)


#question 26 "name of the restaurants in descending along with all the columns"
for i in restaurants.find({}).sort("name",-1):
    print(i)


#question 27 "the name of the cuisine in ascending order and for that same cuisine borough should be in descending order"
for i in restaurants.find({}).sort([("cuisine",1),("borough",-1 )]):
    print(i)


# question 28  "addresses contains the street or not"
for i in restaurants.find({"address.street" : { "$exists" : True }}):
    print(i)


# question 29 "coord field value is Double"
for i in restaurants.find({"address.coord":{"$type": 1}}):
    print(i)


# question 30 "dividing the score by 7"
for i in restaurants.find({"grades.score" :{"$mod" : [7,0]}}, {"restaurant_id" : 1,"name":1,"grades":1})[0:100]:
    print(i)


#question 31  "mon somewhere in name"
for i in restaurants.find({ "name" : { "$regex": 'mon.*',"$options":"$i"} }, { "name":1,  "borough":1, "address.coord":1, "cuisine" :1}):
    print(i)


# question 32 "Mad as first three letter in name"
for i in restaurants.find({ "name" : { "$regex": '^Mad',"$options":"$i"} }, { "name":1,  "borough":1, "address.coord":1, "cuisine" :1}):
    print(i)
