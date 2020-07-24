'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    if "0" in word:
        return word.count("0")
    elif "th" in word:
        return count_th(word.replace("th", "0"))
    elif "th" not in word:
        return 0

    # substring = "th"
    # if substring in word:
    #     return count_th(word.replace(substring, '0'))

    # else:
    #     return 0


# print(count_th("ththththth"))


# def count_th(word):
#     substring = "th"
#     if substring in word:
#         return word.count(substring)

#     else:
#         return 0


# print(count_th("ththththth"))
