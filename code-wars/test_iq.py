
def iq_test(numbers):
    odd = []
    even = []
    for i in range(len(numbers)):
        if int(numbers[i]) % 2 != 0:
            odd.append(i)
        else:
            even.append(i)
    if len(odd) == 1:
        return odd[0]+1
    else:
        return even[0] + 1


def test_answer():
    assert iq_test("2 4 7 8 10".split(" ")) == 3

