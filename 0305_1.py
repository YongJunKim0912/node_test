person = {
    "이름": "나귀욤",
    "나이": "10"
}


person["나이"] = 8
print(person["나이"])

person.update({"나이":20, "이름":"용준"})
print(person)

print(person.keys())    #키만 출력
print(person.values())  #밸류만 출력
print(person.items())   #키,밸류 출력