user = {"first_name":"Ada"}
print(user)

user = {"first_name":"Ada"}
print(user["first_name"])

user["family_name"] = "Byron"
print(user)

user["family_name"] = "Lovelace"
print(user)

del user["family_name"]
print(user)