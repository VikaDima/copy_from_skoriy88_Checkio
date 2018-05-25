tm = "7:00"

def sun_angle(time):
    res = 0
    minutes = int(time.split(':')[0]) * 60 + int(time.split(':')[1])
    print(minutes)
    if minutes < 360 or minutes > 1080:
        res = "I don't see the sun!"
        print(res)
        return res
    else:
        res = minutes * 0.25 - 90
        print(res)
        return res




sun_angle(tm)