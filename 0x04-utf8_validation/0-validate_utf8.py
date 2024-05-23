def validUTF8(data):
    """Check if valid UTF8."""
    flag = 0
    for i in data:
        if i >= 0x80 and flag == 0:
            return False
        if i & 0xC0 == 0x80:
            flag += 1
            if flag > 1 or (flag == 1 and i & 0xE0 == 0xA0):
                return False
        else:
            flag = 0
    return flag == 0
