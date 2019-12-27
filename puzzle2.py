input = [1, 0, 0, 3, 1, 1, 2, 3, 1, 3, 4, 3, 1, 5, 0, 3, 2, 1, 13, 19, 1, 9, 19, 23, 1, 6, 23, 27, 2, 27, 9, 31, 2, 6, 31, 35, 1, 5, 35, 39, 1, 10, 39, 43, 1, 43, 13, 47, 1, 47, 9, 51, 1, 51, 9, 55, 1, 55, 9, 59, 2, 9, 59, 63, 2, 9, 63, 67, 1, 5, 67, 71, 2, 13, 71, 75, 1, 6, 75, 79, 1, 10,
         79, 83, 2, 6, 83, 87, 1, 87, 5, 91, 1, 91, 9, 95, 1, 95, 10, 99, 2, 9, 99, 103, 1, 5, 103, 107, 1, 5, 107, 111, 2, 111, 10, 115, 1, 6, 115, 119, 2, 10, 119, 123, 1, 6, 123, 127, 1, 127, 5, 131, 2, 9, 131, 135, 1, 5, 135, 139, 1, 139, 10, 143, 1, 143, 2, 147, 1, 147, 5, 0, 99, 2, 0, 14, 0]


def int_code(input, noun, verb):
    output = input[:]
    output[1] = noun
    output[2] = verb
    ind = 0
    out_of_index = False
    while input[ind] != 99:
        try:
            if ind < 0 or ind > len(input):
                out_of_index = True
                break
            op = output[ind]
            if op == 1:
                output[output[ind+3]] = output[output[ind+1]] + output[output[ind+2]]
            elif op == 2:
                output[output[ind+3]] = output[output[ind+1]] * output[output[ind+2]]
            elif op == 99:
                break
            ind += 4
        except Exception as e:
            print(e)
            out_of_index = True
            break
    return output, out_of_index


output, out_of_index_flag = int_code(input, 12, 2)
print(output[0])

for noun in range(100):
    for verb in range(100):
        output, out_of_index = int_code(input, noun, verb)
        if not out_of_index and output[0] == 19690720:
            print(f"noun = {noun} and verb = {verb}")
            print(100*noun+verb)
            break
