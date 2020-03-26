def capitalize(s):
    odd = []
    even = []
    strE = ""
    strO = ""
    for i in range(len(s)):
        if i % 2 != 0:
            odd.append(s[i].upper())
            even.append(s[i].lower())
        else:
            odd.append(s[i].lower())
            even.append(s[i].upper())
        strE += even[i]
        strO += odd[i]

    return [strE, strO]


def test_answer():
    assert capitalize("abcdef") == ['AbCdEf', 'aBcDeF']
    assert capitalize("codewars") == ['CoDeWaRs', 'cOdEwArS']
    assert capitalize("abracadabra") == ['AbRaCaDaBrA', 'aBrAcAdAbRa']
