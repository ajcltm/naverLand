
def formatting(value):
    if value == None or value == 0 :
        value = '-'
    else :
        if not isinstance(value, str):
            value = "{:,}".format(value)
        else:
            value = str(value)
    return value
