def sorting(some_list, key_num):
    if key_num == 1:
        return sorted(some_list)
    elif key_num == -1:
        return sorted(some_list, reverse=True)
    else:
        return "Incorrect key_num"
    
def deepSorting(list_dict, string):
    new_list = sorted(list_dict, key = lambda d: d[string])
    return new_list

def getNumbers(some_list):
    result_list = []
    for i in some_list:
        if type(i) is int or type(i) is float:
            result_list.append(i)
    return result_list

def Min(some_list):
    a = min(some_list)
    new_mas = []
    new_mas.append(a)
    return new_mas

def getSet(some_list):
    unique_list = set(some_list)
    return unique_list

def findTheMostReapetedEls(list):
    dict = {}
    for item in list:
        if item in dict:
            dict[item]+=1
        else:
            dict[item]=1
    list_get = []
    for key in dict:
        list_get.append(dict[key])
    Max = max(list_get)
    res_list = []
    for key in dict:
        if dict[key]==Max:
            res_list.append(key)
    return res_list

def stack(list):
    opened = 0
    closed = 0
    for el in list:
        if el == '[':
            opened+=1
        else:
            closed+=1
    return opened==closed

def checkForBadWord(string, word):
    return word in string