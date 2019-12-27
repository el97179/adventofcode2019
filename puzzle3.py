import sys

input = ["R997,U849,R349,U641,R581,D39,R285,U139,R455,D346,L965,D707,R393,D302,L263,U58,R950,U731,R858,D748,R302,U211,R588,D441,L153,D417,R861,U775,R777,U204,R929,U868,L62,U163,R841,D214,L648,U626,R501,D751,L641,D961,L23,D430,L73,D692,R49,U334,L601,U996,R444,D658,R633,D30,L861,D811,R10,D394,R9,U227,L848,U420,L378,D622,L501,U397,R855,U369,R615,U591,L674,D166,L181,U61,L224,U463,L203,U594,R93,U614,L959,U198,L689,D229,L674,U255,R843,D382,R538,U923,L960,D775,L879,U97,R137,U665,L340,D941,L775,D57,R852,D167,R980,U704,L843,U989,L611,D32,L724,D790,L32,U984,L39,U671,L994,U399,R475,D85,L322,D936,R117,D261,R705,D696,L523,D433,L239,U477,L247,D465,R560,D902,L589,U682,R645,U376,L989,D121,L215,U514,R519,U407,L218,D444,R704,D436,L680,U759,R937,U400,R533,D860,R782,D233,R840,D549,L508,U380,L992,U406,L213,D403,L413,D532,L429,U186,R262,U313,L913,U873,L838,D882,R851,U70,R185,D131,R945,D595,L330,U446,R88,D243,L561,D952,R982,D395,L708,U459,L82,D885,L996,U955,L406,U697,L183,U266,L878,D839,R843,D891,R118,U772,R590,D376,L500,U370,R607,D12,L310,D436,L602,D365,R886,U239,L471,D418,L122,U18,R879,D693,R856,U848,L657,D911,L63,U431,R41,U752,R919,U323,L61,D263,L370,D85,R929,D213,R350,U818,R458,D912,R509,U394,L734,U49,R810,D87,L870,U658,R499,U550,L402,U244,L112,U859,R836,U951,R222,D944,L691,D731,R742,D52,R984,D453,L514,U692,R812,U35,L844,D177,L110,D22,R61,U253,R618,D51,R163,U835,R704,U148,R766,U297,R457,D170,L104,D441,R330,D330,R989,D538,R668,D811,R62,D67,L470,D526,R788,U376,R708,U3,R961",
         "L1009,D381,R970,U429,L230,D909,R516,D957,R981,U609,L480,D139,L861,U168,L48,U620,R531,D466,L726,D380,R977,D454,L318,D397,R994,U402,L77,U93,L359,D72,R968,D956,L174,D22,R218,U619,R593,U32,L154,U55,L169,U415,L171,U666,R617,U109,L265,U773,R541,D808,L797,U478,R731,U379,R311,D137,L806,U298,R362,D458,L254,D539,R700,U853,R246,D588,L28,U203,L432,U946,R663,D408,R974,U59,L683,D36,L139,U738,L780,U414,L401,D93,R212,D973,L710,U892,L357,D177,R823,D4,R46,D924,L235,D898,R67,U220,L592,U87,R94,U584,R979,D843,L299,D648,L491,U360,R824,D245,L944,D24,R616,U975,L4,U42,L984,U181,R902,D835,L687,D413,L767,U632,L754,U270,R413,U51,L825,D377,L596,U960,L378,U706,L859,D708,L156,D991,L814,U351,R923,D749,L16,D651,R20,D86,R801,U811,L228,U161,L871,U129,R215,U235,L784,U896,R94,U145,R822,U494,R248,D98,R494,U156,L495,U311,R66,D873,L294,D620,L885,U395,R778,D227,R966,U756,L694,D707,R983,D950,R706,D730,R415,U886,L465,D622,L13,D938,R324,D464,R723,U804,R942,D635,L729,D317,L522,U469,R550,D141,R302,U999,L642,U509,R431,D380,R18,D676,R449,D759,L495,U901,R1,D745,L655,U449,L439,D818,R55,D541,R420,U764,L426,D176,L520,U3,L663,D221,L80,D449,L987,U349,L71,U632,L887,D231,R655,D208,R698,D639,R804,U616,R532,U846,R363,D141,R659,U470,L798,U144,L675,U483,L944,U380,L329,U72,L894,D130,R53,U109,R610,U770,R778,U493,R972,D340,L866,U980,L305,D812,R130,D954,R253,D33,L912,U950,L438,D680,R891,U725,R171,D587,R549,D367,L4,U313,R522,D128,L711,D405,L769,D496,L527,U373,R725,D261,L268,D939,L902,D58,L858,D190,L442"]

# input = ["R75,D30,R83,U83,L12,D49,R71,U7,L72",
#          "U62,R66,U55,R34,D71,R55,D58,R83"]

# input = ["R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51",
#          "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"]


def read_input(input_path):
    return input_path.split(",")


def parse_direction(operation):
    direction = operation[0]
    length = int(operation[1:])
    return direction, length


def create_line_segment(init_point, direction, length):
    if direction == "R":
        x2 = init_point[0] + length
        y2 = init_point[1]
    if direction == "L":
        x2 = init_point[0] - length
        y2 = init_point[1]
    if direction == "U":
        x2 = init_point[0]
        y2 = init_point[1] + length
    if direction == "D":
        x2 = init_point[0]
        y2 = init_point[1] - length
    return [init_point[0], init_point[1], x2, y2]


def crossed_lines(old_line, new_line):
    minx1 = min(old_line[0], old_line[2])
    maxx1 = max(old_line[0], old_line[2])
    miny1 = min(old_line[1], old_line[3])
    maxy1 = max(old_line[1], old_line[3])
    minx2 = min(new_line[0], new_line[2])
    maxx2 = max(new_line[0], new_line[2])
    miny2 = min(new_line[1], new_line[3])
    maxy2 = max(new_line[1], new_line[3])

    if (minx1 != maxx1):
        # print("old: horizontal line")
        if (minx2 != maxx2):
            # print("new: horizontal line")
            if (miny1 != miny2):
                return None  # parallel, horizontal but not intersecting/overlaping lines
            else:
                print("horizontal overlap")
                endpoints = []
                if (maxx2 >= maxx1 >= minx2):
                    endpoints.append(maxx1)
                if (maxx2 >= minx1 >= minx2):
                    endpoints.append(minx1)
                if (maxx1 >= maxx2 >= minx1):
                    endpoints.append(maxx2)
                if (maxx1 >= minx2 >= minx1):
                    endpoints.append(minx2)
                if len(endpoints) == 0:
                    return None
                else:
                    intersection_point = (min(abs(endpoints[0]), abs(endpoints[1])), miny1)
                return intersection_point
        else:
            # print("new: vertical line")
            if ((maxx1 >= minx2 >= minx1) and (maxy2 >= miny1 >= miny2)):
                intersection_point = (minx2, miny1)
                print(f"hor/ver cross: {intersection_point}")
                return intersection_point
            else:
                return None
    else:
        # print("old: vertical line")
        if (minx2 != maxx2):
            # print("new: horizontal line")
            if ((maxx2 >= minx1 >= minx2) and (maxy1 >= miny2 >= miny1)):
                intersection_point = (minx1, miny2)
                print(f"hor/ver cross: {intersection_point}")
                return intersection_point
            else:
                return None
        else:
            # print("new: vertical line")
            if (minx1 != minx2):
                return None  # parallel, vertical but not intersecting/overlaping lines
            else:
                print("vertical overlap")
                endpoints = []
                if (maxy2 >= maxy1 >= miny2):
                    endpoints.append(maxy1)
                if (maxy2 >= miny1 >= miny2):
                    endpoints.append(miny1)
                if (maxy1 >= maxy2 >= miny1):
                    endpoints.append(maxy2)
                if (maxy1 >= miny2 >= miny1):
                    endpoints.append(miny2)
                if len(endpoints) == 0:
                    return None
                else:
                    intersection_point = (minx1, min(abs(endpoints[0]), abs(endpoints[1])))
                return intersection_point


def dist_to_point(line, point):
    dist = abs(line[2] - point[0]) + abs(line[3] - point[1])
    return dist


def min_manhattan(coords):
    closest_pt = [sys.maxsize, sys.maxsize]
    for point in coords:
        if abs(point[0][0]) + abs(point[0][1]) < abs(closest_pt[0]) + abs(closest_pt[1]):
            closest_pt[0] = point[0][0]
            closest_pt[1] = point[0][1]

    return closest_pt


wire1 = read_input(input[0])
line1 = []
length1 = 0
init_point = [0, 0]
for operation in wire1:
    direction, length = parse_direction(operation)
    # print(f"direction: {direction}, length: {length}")
    length1 += length
    line_segment = create_line_segment(init_point, direction, length)
    line1.append((line_segment, length1))
    init_point = line_segment[2:]

wire2 = read_input(input[1])
length2 = 0
init_point = [0, 0]
intersection_points = []
for operation in wire2:
    direction, length = parse_direction(operation)
    # print(f"direction: {direction}, length: {length}")
    length2 += length
    line_segment = create_line_segment(init_point, direction, length)
    for line1_seg in line1:
        inter_pt = crossed_lines(line1_seg[0], line_segment)
        length1 = line1_seg[1]
        if inter_pt is not None:
            trail1 = dist_to_point(line1_seg[0], inter_pt)
            trail2 = dist_to_point(line_segment, inter_pt)
            inter_length = length1 + length2 - trail1 - trail2
            intersection_points.append((inter_pt, inter_length))

    init_point = line_segment[2:]

closest_point = min_manhattan(intersection_points[1:])
# print(intersection_points)
print(f"closest_point: {closest_point}")
print(f"min distance: {abs(closest_point[0])+abs(closest_point[1])}")

min_intersection_dist = sys.maxsize
for inter_length in intersection_points[1:]:
    if inter_length[1] < min_intersection_dist:
        min_intersection_dist = inter_length[1]
print(f"min intersection distance: {min_intersection_dist}")
