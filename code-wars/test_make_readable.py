def make_readable(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60

    return "%0d:%02d:%02d" % (hour, minutes, seconds)


print(make_readable(60))
print(make_readable(86399))

