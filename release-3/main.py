def fullName(obj):
    return obj["surname"] + ' ' + obj["name"]


def checkForProperyAndValue(obj, key_name):
    for key in obj:
        return key==key_name and obj[key]>0