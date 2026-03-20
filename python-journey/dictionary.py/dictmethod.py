student ={
    "name":"harshal wath",
    "subject" : {
        "phy": 98,
        "chem": 97,
        "math": 99 ,

    }
}

print(student.keys()) # key method

print(len(student)) # for finding length

print(list(student.values())) #value() method 

print(student.items()) # it return all value in pair

print(student.get("name"))
 
new_dict = {"surname" : "wath"}
student.update(new_dict)
print(student)