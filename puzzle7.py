import itertools

input_array = [3, 8, 1001, 8, 10, 8, 105, 1, 0, 0, 21, 46, 67, 76, 101, 118, 199, 280, 361, 442, 99999, 3, 9, 1002, 9, 4, 9, 1001, 9, 2, 9, 102, 3, 9, 9, 101, 3, 9, 9, 102, 2, 9, 9, 4, 9, 99, 3, 9, 1001, 9, 3, 9, 102, 2, 9, 9, 1001, 9, 2, 9, 1002, 9, 3, 9, 4, 9, 99, 3, 9, 101, 3, 9, 9, 4, 9, 99, 3, 9, 1001, 9, 2, 9, 1002, 9, 5, 9, 101, 5, 9, 9, 1002, 9, 4, 9, 101, 5, 9, 9, 4, 9, 99, 3, 9, 102, 2, 9, 9, 1001, 9, 5, 9, 102, 2, 9, 9, 4, 9, 99, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 101, 2, 9, 9, 4, 9, 3, 9, 101, 1, 9, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 101, 1, 9, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 101, 2, 9, 9, 4, 9, 99, 3, 9, 101, 1, 9, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 101, 1, 9, 9, 4, 9, 3, 9, 101, 2, 9, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 101, 2, 9, 9, 4,
               9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 101, 2, 9, 9, 4, 9, 99, 3, 9, 1001, 9, 1, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 101, 1, 9, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 1001, 9, 1, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 1001, 9, 1, 9, 4, 9, 3, 9, 101, 1, 9, 9, 4, 9, 3, 9, 101, 2, 9, 9, 4, 9, 99, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 1001, 9, 1, 9, 4, 9, 3, 9, 101, 2, 9, 9, 4, 9, 3, 9, 101, 2, 9, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 101, 1, 9, 9, 4, 9, 3, 9, 1001, 9, 2, 9, 4, 9, 99, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 101, 2, 9, 9, 4, 9, 3, 9, 101, 1, 9, 9, 4, 9, 3, 9, 101, 2, 9, 9, 4, 9, 3, 9, 1001, 9, 2, 9, 4, 9, 3, 9, 1001, 9, 2, 9, 4, 9, 3, 9, 101, 2, 9, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 101, 2, 9, 9, 4, 9, 99]

# input_array = [3, 225, 1, 225, 6, 6, 1100, 1, 238, 225, 104, 0, 1102, 45, 16, 225, 2, 65, 191, 224, 1001, 224, -3172, 224, 4, 224, 102, 8, 223, 223, 1001, 224, 5, 224, 1, 223, 224, 223, 1102, 90, 55, 225, 101, 77, 143, 224, 101, -127, 224, 224, 4, 224, 102, 8, 223, 223, 1001, 224, 7, 224, 1, 223, 224, 223, 1102, 52, 6, 225, 1101, 65, 90, 225, 1102, 75, 58, 225, 1102, 53, 17, 224, 1001, 224, -901, 224, 4, 224, 1002, 223, 8, 223, 1001, 224, 3, 224, 1, 224, 223, 223, 1002, 69, 79, 224, 1001, 224, -5135, 224, 4, 224, 1002, 223, 8, 223, 1001, 224, 5, 224, 1, 224, 223, 223, 102, 48, 40, 224, 1001, 224, -2640, 224, 4, 224, 102, 8, 223, 223, 1001, 224, 1, 224, 1, 224, 223, 223, 1101, 50, 22, 225, 1001, 218, 29, 224, 101, -119, 224, 224, 4, 224, 102, 8, 223, 223, 1001, 224, 2, 224, 1, 223, 224, 223, 1101, 48, 19, 224, 1001, 224, -67, 224, 4, 224, 102, 8, 223, 223, 1001, 224, 6, 224, 1, 223, 224, 223, 1101, 61, 77, 225, 1, 13, 74, 224, 1001, 224, -103, 224, 4, 224, 1002, 223, 8, 223, 101, 3, 224, 224, 1, 224, 223, 223, 1102, 28, 90, 225, 4, 223, 99, 0, 0, 0, 677, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1105, 0, 99999, 1105, 227, 247, 1105, 1, 99999, 1005, 227, 99999, 1005, 0, 256, 1105, 1, 99999, 1106, 227, 99999, 1106, 0, 265, 1105, 1, 99999, 1006, 0, 99999, 1006, 227, 274, 1105, 1, 99999, 1105, 1, 280, 1105, 1, 99999, 1, 225, 225, 225, 1101, 294, 0, 0, 105, 1, 0, 1105, 1, 99999, 1106, 0, 300, 1105, 1, 99999, 1, 225, 225, 225, 1101, 314, 0, 0, 106, 0, 0, 1105, 1, 99999, 7, 226, 677, 224, 102, 2, 223, 223, 1005, 224, 329, 1001, 223, 1, 223, 8, 226, 677, 224, 1002, 223, 2, 223, 1005, 224, 344, 101, 1, 223, 223, 8,
#                226, 226, 224, 1002, 223, 2, 223, 1006, 224, 359, 101, 1, 223, 223, 1008, 677, 226, 224, 1002, 223, 2, 223, 1005, 224, 374, 1001, 223, 1, 223, 108, 677, 677, 224, 1002, 223, 2, 223, 1005, 224, 389, 1001, 223, 1, 223, 1107, 226, 677, 224, 1002, 223, 2, 223, 1006, 224, 404, 101, 1, 223, 223, 1008, 226, 226, 224, 102, 2, 223, 223, 1006, 224, 419, 1001, 223, 1, 223, 7, 677, 226, 224, 1002, 223, 2, 223, 1005, 224, 434, 101, 1, 223, 223, 1108, 226, 226, 224, 1002, 223, 2, 223, 1005, 224, 449, 101, 1, 223, 223, 7, 226, 226, 224, 102, 2, 223, 223, 1005, 224, 464, 101, 1, 223, 223, 108, 677, 226, 224, 102, 2, 223, 223, 1005, 224, 479, 1001, 223, 1, 223, 1007, 677, 226, 224, 1002, 223, 2, 223, 1006, 224, 494, 1001, 223, 1, 223, 1007, 677, 677, 224, 1002, 223, 2, 223, 1006, 224, 509, 1001, 223, 1, 223, 107, 677, 677, 224, 1002, 223, 2, 223, 1005, 224, 524, 101, 1, 223, 223, 1108, 226, 677, 224, 102, 2, 223, 223, 1006, 224, 539, 1001, 223, 1, 223, 8, 677, 226, 224, 102, 2, 223, 223, 1005, 224, 554, 101, 1, 223, 223, 1007, 226, 226, 224, 102, 2, 223, 223, 1006, 224, 569, 1001, 223, 1, 223, 107, 677, 226, 224, 102, 2, 223, 223, 1005, 224, 584, 1001, 223, 1, 223, 108, 226, 226, 224, 102, 2, 223, 223, 1006, 224, 599, 1001, 223, 1, 223, 107, 226, 226, 224, 1002, 223, 2, 223, 1006, 224, 614, 1001, 223, 1, 223, 1108, 677, 226, 224, 1002, 223, 2, 223, 1005, 224, 629, 1001, 223, 1, 223, 1107, 677, 677, 224, 102, 2, 223, 223, 1005, 224, 644, 1001, 223, 1, 223, 1008, 677, 677, 224, 102, 2, 223, 223, 1005, 224, 659, 101, 1, 223, 223, 1107, 677, 226, 224, 1002, 223, 2, 223, 1006, 224, 674, 101, 1, 223, 223, 4, 223, 99, 226]
# input_array = [3,  15,  3,  16,  1002,  16,  10,  16,  1,  16,  15,  15,  4,  15,  99,  0,  0]
# input_array = [3,  23,  3,  24,  1002,  24,  10,  24,  1002,  23,  -1,
#                23,  101,  5,  23,  23,  1,  24,  23,  23,  4,  23,  99,  0,  0]
# input_array = [3,  31,  3,  32,  1002,  32,  10,  32,  1001,  31,  -2,  31,  1007,  31,  0,
#                33,  1002,  33,  7,  33,  1,  33,  31,  31,  1,  32,  31,  31,  4,  31,  99,  0,  0,  0]

# input_array = [3, 26, 1001, 26, -4, 26, 3, 27, 1002, 27, 2, 27, 1, 27, 26,
#                27, 4, 27, 1001, 28, -1, 28, 1005, 28, 6, 99, 0, 0, 5]
# input_array = [3, 52, 1001, 52, -5, 52, 3, 53, 1, 52, 56, 54, 1007, 54, 5, 55, 1005, 55, 26, 1001, 54,
#                -5, 54, 1105, 1, 12, 1, 53, 54, 53, 1008, 54, 0, 55, 1001, 55, 1, 55, 2, 53, 55, 53, 4,
#                53, 1001, 56, -1, 56, 1005, 56, 6, 99, 0, 0, 0, 0, 10]

read_count = 0
setting = 0
prev_output = 0


def get_digits(opcode):
    d1 = opcode % 10
    d2 = int((opcode % 100 - d1) / 10)
    d3 = int((opcode % 1000 - d1 - 10*d2) / 100)
    d4 = int((opcode % 10000 - d1 - 10*d2 - 100*d3) / 1000)
    d5 = int((opcode % 100000 - d1 - 10*d2 - 100*d3 - 1000*d4) / 10000)
    d12 = d1 + 10*d2
    return d12, d3, d4, d5


def int_code(array, ind=0):
    out_of_index = False
    code99 = False
    global read_count
    while True:
        try:
            if ind < 0 or ind > len(input_array):
                out_of_index = True
                break
            opcode, param_mode1, param_mode2, param_mode3 = get_digits(array[ind])

            if opcode == 1:
                param1 = (array[ind+1] if param_mode1 else array[array[ind+1]])
                param2 = (array[ind+2] if param_mode2 else array[array[ind+2]])
                address = ind+3 if param_mode3 else array[ind+3]
                array[address] = param1 + param2
                ind += 4
            elif opcode == 2:
                param1 = (array[ind+1] if param_mode1 else array[array[ind+1]])
                param2 = (array[ind+2] if param_mode2 else array[array[ind+2]])
                address = ind+3 if param_mode3 else array[ind+3]
                array[address] = param1 * param2
                ind += 4
            elif opcode == 3:
                if read_count == 0:
                    value = setting
                    read_count += 1
                    print(f"automatically inserted setting: {value}")
                elif read_count == 1:
                    value = prev_output
                    print(f"automatically inserted previous output: {value}")
                else:
                    print("error in read_count")
                # value = int(input("Insert value... "))
                array[array[ind+1]] = value
                ind += 2
            elif opcode == 4:
                param1 = (array[ind+1] if param_mode1 else array[array[ind+1]])
                value = param1
                print(f"output: {value}")
                output = value
                ind += 2
                break  # comment this line out for part_a
            elif opcode == 5:
                param1 = (array[ind+1] if param_mode1 else array[array[ind+1]])
                param2 = (array[ind+2] if param_mode2 else array[array[ind+2]])
                if param1 != 0:
                    ind = param2
                else:
                    ind += 3
            elif opcode == 6:
                param1 = (array[ind+1] if param_mode1 else array[array[ind+1]])
                param2 = (array[ind+2] if param_mode2 else array[array[ind+2]])
                if param1 == 0:
                    ind = param2
                else:
                    ind += 3
            elif opcode == 7:
                param1 = (array[ind+1] if param_mode1 else array[array[ind+1]])
                param2 = (array[ind+2] if param_mode2 else array[array[ind+2]])
                address = ind+3 if param_mode3 else array[ind+3]
                if param1 < param2:
                    array[address] = 1
                else:
                    array[address] = 0
                ind += 4
            elif opcode == 8:
                param1 = (array[ind+1] if param_mode1 else array[array[ind+1]])
                param2 = (array[ind+2] if param_mode2 else array[array[ind+2]])
                address = ind+3 if param_mode3 else array[ind+3]
                if param1 == param2:
                    array[address] = 1
                else:
                    array[address] = 0
                ind += 4
            elif opcode == 99:
                code99 = True
                output = None
                break
        except Exception as e:
            print(e)
            out_of_index = True
            break
    return array, out_of_index, output, ind, code99


def part_a():
    global read_count, setting, prev_output
    array = input_array[:]
    settings = [0, 1, 2, 3, 4]
    amplifiers = ["A", "B", "C", "D", "E"]
    max_output = 0
    read_count = 0
    for setting_perm in itertools.permutations(settings):
        prev_output = 0
        for idx, setting in enumerate(setting_perm):
            print(f"amplifier {amplifiers[idx]}:")
            # print(f"setting: {setting}")
            # print(f"prev_output: {prev_output}")
            read_count = 0
            _, _, prev_output, _, _ = int_code(array)
        print()
        if prev_output > max_output:
            max_output = prev_output

    print(f"max final output: {max_output}")


def part_b():
    global read_count, setting, prev_output
    settings = [5, 6, 7, 8, 9]
    amplifiers = ["A", "B", "C", "D", "E"]
    max_output = 0
    read_count = 0
    for setting_perm in itertools.permutations(settings):
        arrays = [input_array[:], input_array[:], input_array[:], input_array[:], input_array[:]]
        indices = [0, 0, 0, 0, 0]
        loop_counter = 0
        prev_output = 0
        exit_code = False
        while not exit_code:
            if loop_counter < len(setting_perm):
                read_count = 0
            idx = loop_counter % len(setting_perm)
            setting = setting_perm[idx]
            array = arrays[idx]
            ind = indices[idx]
            print(f"amplifier {amplifiers[idx]}:")
            print(f"setting: {setting}")
            print(f"prev_output: {prev_output}")
            array, _, prev_output, ind, exit_code = int_code(array, ind)
            if not exit_code:
                output = prev_output
            arrays[idx] = array[:]
            indices[idx] = ind
            loop_counter += 1
        print(f"combined_amp_output: {output}")
        if output > max_output:
            max_output = output
            max_settings = setting_perm

    print(f"max settings: {max_settings}")
    print(f"max final output: {max_output}")


part_b()
