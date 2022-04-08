def solution():
    s = "asdfbb123"
    len_of_s = len(s)
    if len_of_s == 0:
        return 0
    max_len = 1
    for i in range(len_of_s):
        start = i
        end = 0
        showed = set()
        showed.add(s[i])
        for j in range(i + 1, len_of_s):
            if s[j] in showed:
                break
            showed.add(s[j])
            end = j
            # print(s[j])
        # max_len = (max_len if (end - start + 1) < max_len else (end - start + 1))
        max_len = (max_len if (j - i + 1) < max_len else (j - i + 1))
    return max_len


print(solution())
