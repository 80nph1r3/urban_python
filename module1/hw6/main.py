my_dict = {
    "Viktor": 1998,
    "Maria": 2002,
    "Elizabeth": 2005,
    "Igor": 1977,
}
print(my_dict)
print(my_dict["Igor"])
print(my_dict.get("Nikita"))
my_dict["Anna"] = 1975
del my_dict["Maria"]
print(my_dict)

my_set = {1, 1, "a", "a"}
print(my_set)
my_set.update((2, "b"))
my_set.discard("a")
print(my_set)
