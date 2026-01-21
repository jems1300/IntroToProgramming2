# dictionary thing that we will sort through
# We will use years as keys
# and courses as values
def main():
    # dictionary = [("blah", 12),
    #               ("asdf", 13),
    #               ("blegh", 14)]

    # thisdict = {
    #     "brand": "Ford",
    #     "model": "Mustang",
    #     "year": 1964
    # }
    #
    # print(thisdict["year"])

    curriculum: dict[int, str] = {2026: "Software Engineering",
                                  2024: "Programming Fundamentals II",
                                  2025: "Data Structures"}

    print(curriculum)
    # Saw an online guide showing how to do this, key lambda let's me access the index element of the
    # the dict and then sort it from that index alone.
    print(dict(sorted(curriculum.items(), key=lambda x: x[0])))
    # dict puts it back in it's dictionary form

    print(len(curriculum))
main()
