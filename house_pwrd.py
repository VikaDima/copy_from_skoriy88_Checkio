def checkio(data):
    if len(data) < 10:
        return False
    else:
        digit = []
        upper = []
        lower = []
        for x in data:
            digit.append(x.isdigit())
            upper.append(x.isupper())
            lower.append(x.islower())
        if True in digit and True in upper and True in lower:
            return True
        else:
            return False









