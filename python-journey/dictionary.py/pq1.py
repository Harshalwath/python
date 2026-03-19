info = {
    "name" : "harshal",
    "subject" : ["math","marathi"],
    "age" : "21",
    12.99 : 94.4

}

info["name"] = "rahul"
info["surname"] = "wath"
print(info)

#dict. inside dict (nested dictionary)

student ={
    "name":"harshal wath",
    "subject" : {
        "phy": 98,
        "chem": 97,
        "math": 99 ,

    }
}
#here if we want to print only chem marks then use
print(student["subject"]["chem"])