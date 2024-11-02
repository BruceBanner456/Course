def test_fruits(fruits):
    for i in range(len(fruits)):
        if "berry" in fruits[i]:
            fruits[i] = fruits[i].replace("berry", "berries")
        else:
            fruits[i] = fruits[i] + "s"

# name = input("What's your name: ")
#
#
# if name == "bob":
#     print("You are not allowed in the club")
# elif name.count("b") >= 2:
#     print("You're allowed bin the club")
