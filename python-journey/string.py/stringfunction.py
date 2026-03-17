##endswith() in string
str = "i am the student of bncoe"
print(str.endswith("coe")) 

#capitalize() 
# by using this function the first letter of string we get capital

str = "harshal"
print(str.capitalize())

# replace()
# it replace old value with new one 

str = " i am the student of bncoe"
print(str.replace("t", "r" )) # here t will be replace with r

#find()
str = "i am the student of bncoe"
print(str.find("s")) # here we get the index no. of s 
# if we find a letter which not present in given string then we get output -1

#count()

str = "i am student of am bncoe"
print(str.count("am")) #here count() count the am word from given string