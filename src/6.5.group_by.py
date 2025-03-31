def group_by(func, array):
    ans = dict()
    for item in array:
        val = func(item)
        if val not in ans:
            ans[val] = [item]
        else:
            ans[val].append(item)
    return ans
