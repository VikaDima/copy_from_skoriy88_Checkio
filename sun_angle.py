tm = "5:00"

def sun_angle(time):
    res = "I don't see the sun!"
    minutes = int(time.split(':')[0]) * 60 + int(time.split(':')[1])
    #print(minutes)
    if minutes < 360 or minutes > 1080:
        #print(res)
        return res
    else:
        res = minutes * 0.25 - 90
        #print(res)
        return res

sun_angle(tm)