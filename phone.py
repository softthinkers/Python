import phonenumbers
x = phonenumbers.parse("+442083661177", None)
G=phonenumbers.example_number("+442083661177")
print(G)
type(x)

y = phonenumbers.parse("020 8366 1177", "GB")
print("h",y)
print(x == y)

# as dialed from GB, not a GB number
z = phonenumbers.parse("00 1 650 253 2222", "GB")
print(z)


z = phonenumbers.parse("+120012301", None)
phonenumbers.is_valid_number(z)