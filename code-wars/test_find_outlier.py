
def find_outlier(arr):
    odd = []
    even = []
    for i in range(len(arr)):
        if arr[i] % 2 != 0:
            odd.append(arr[i])
        else:
            even.append(arr[i])

    if len(odd) == 1:
        return odd[0]
    else:
        return even[0]


def find_outlierI(int):
    odds = [x for x in int if x%2!=0]
    evens= [x for x in int if x%2==0]
    return odds[0] if len(odds)<len(evens) else evens[0]


def test_answer():
    assert find_outlier([160, 3, 1719, 19, 11, 13, -21]) == 160
