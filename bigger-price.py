begin = [{"name": "bread", "price": 100},
         {"name": "wine", "price": 138},
         {"name": "meat", "price": 15},
         {"name": "water", "price": 1}]



def bigger_price(num, lst):
    res = []
    new_lst = []
    for dic in lst:
        #new_lst.append([dic['name'], dic['price']])
        new_lst.append([dic['price'], dic['name']])

    for item in (sorted(new_lst)[-1:-num-1:-1]):
        res.append({"name":item[1], "price":item[0]})
    return res


bigger_price(1, begin)

