from math import floor


def ns_to_human(i):
    milliseconds = i % 1000000000
    x = floor(i / 1000000000)
    seconds = x % 60
    x = floor(x / 60)
    minutes = x % 60
    x = floor(x / 60)
    hours = x % 24
    x = floor(x / 24)
    days = floor(x)
    print(str(days) + " days, " + str(hours) + ":" + str(minutes) + ":" + str(seconds) + "." + str(milliseconds))


ns_to_human(299077863923)
ns_to_human(184195016134)
