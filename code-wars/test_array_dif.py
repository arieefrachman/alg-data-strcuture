def array_diff(a, b):
    return [x for x in a if x not in b]


def test_answer():
    assert array_diff([1,2], [1]) == [2]
    assert array_diff([7, 13, -18, -2, -2, 19, -6, 18, 2, -15, -11, 19],[18, 7, 0, 7, -16]) == [13, -18, -2, -2, 19, -6, 2, -15, -11, 19]
    assert array_diff([1,2,2], [1]) == [2, 2]