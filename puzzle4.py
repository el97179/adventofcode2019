min_val = 156218
max_val = 652527


def criterion_a(d6, d5, d4, d3, d2, d1):
    return not (d6 != d5 != d4 != d3 != d2 != d1)


def criterion_b(d6, d5, d4, d3, d2, d1):
    if (d6 == d5 != d4):
        return True
    if (d6 != d5 == d4 != d3):
        return True
    if (d5 != d4 == d3 != d2):
        return True
    if (d4 != d3 == d2 != d1):
        return True
    if (d3 != d2 == d1):
        return True
    return False


counter_a = 0
counter_b = 0
for d6 in range(1, 7):
    for d5 in range(d6, 10):
        for d4 in range(d5, 10):
            for d3 in range(d4, 10):
                for d2 in range(d3, 10):
                    for d1 in range(d2, 10):
                        val = d6*100000 + d5*10000 + d4*1000 + d3*100 + d2*10 + d1*1
                        if ((val >= min_val) and (val <= max_val)):
                            if criterion_a(d6, d5, d4, d3, d2, d1):
                                # print(val)
                                counter_a += 1
                            if criterion_b(d6, d5, d4, d3, d2, d1):
                                # print(val)
                                counter_b += 1
print(counter_a)
print(counter_b)
