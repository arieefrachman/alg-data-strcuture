
def is_isogram(string):
    if string == "":
        return True
    x = sorted(string.lower())
    for i in range(len(x)-1):
        if x[i] == x[i+1]:
            return False
    return True


def test_answer():
    assert is_isogram("subdermatoglyphic") == True
    assert is_isogram("good morning") == False
    assert is_isogram("aba") == False
    assert is_isogram("") == True
