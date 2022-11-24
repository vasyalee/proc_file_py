part = [2, 3, 8, 7, 7, 8, 4, 2]

def check(_first, _last, _nums):
    if _nums[_first] == _nums[_last] and _first <= _last and _first + 1 > _last - 1:
        return True
    elif _first <= _last and _nums[_first] == _nums[_last] and _first + 1 <= _last - 1:
        return check(_first + 1, _last - 1, _nums)
    elif _nums[_first] != _nums[_last]:
        return False;

flag = False
first = 0
last = len(part) - 1;
mxlen = 0

for first in range(len(part) - 1):
    for last in range(len(part) - 1, first, -1):
        if part[first] == part[last]:
            checker = check(first, last, part)
            if checker:
                flag = True

                if len(part[first:last+1]) > mxlen:
                    print(part[first:last+1])
                    mxlen = len(part[first:last + 1])




if flag == False:
    print("Found nothing")