import json
def loop(a,c):
    dict = {}
    for x in range(a, c):
        if "11" in str(bin(x).replace("0b", "")) :
            dict[x] = True
        else :
            dict[x] = False
    return json.dumps(dict)