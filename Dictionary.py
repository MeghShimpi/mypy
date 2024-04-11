detail = {
    "name":"megh",
    "Age":21,
    "City":"jalgaon",
}
print(detail)
print(detail["name"])
print(detail["Age"])
print(detail["City"])
print(detail["name"],detail["Age"],detail["City"])
detail["Age"] = 22
print(detail["Age"])
detail.update({"Age": 23})
print(detail["Age"])

print(detail.items())

print(detail.keys())
print(detail.get('name'))
