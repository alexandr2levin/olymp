import sys
import datetime
import math

def can_place_modules(modules_count, module_width, module_height, area_width, area_height):
    modules_can_be_placed_in_row = math.floor(area_width / module_width)
    rows_can_be_count = math.floor(area_height / module_height)
    modules_can_be_placed = modules_can_be_placed_in_row * rows_can_be_count
    return modules_count <= modules_can_be_placed

def max_d(raw_max_d, modules_count, module_width, module_height, area_width, area_height):
    start_d = 0
    end_d = raw_max_d
    while not start_d == end_d:
        middle_d = (start_d + end_d) // 2 + 1

        new_module_width = module_width + (middle_d * 2)
        new_module_height = module_height + (middle_d * 2)
        # print("middle d: {}".format(middle_d))
        # print("before: {}..{}".format(start_d, end_d))
        # tmp_start_d = start_d
        # tmp_end_d = end_d
        if(can_place_modules(modules_count, new_module_width, new_module_height, area_width, area_height)):
            # print("can place, ")
            start_d = middle_d
        else:
            # print("can't place")
            end_d = middle_d - 1
        # if(tmp_start_d == start_d and tmp_end_d == end_d):
        #     raise Exception("ran into cycle")
        #     return -1
        # print("after: {}..{}".format(start_d, end_d))
    return start_d

input_file = open("./input.txt")

input_values = input_file.readline().split(" ")

modules_count = int(input_values[0])
module_width = int(input_values[1])
module_height = int(input_values[2])
area_width = int(input_values[3])
area_height = int(input_values[4])

start_time = datetime.datetime.now()

area_s = area_width * area_height
module_s_raw = area_s / modules_count

a = module_width
b = module_height
s = module_s_raw
D = math.pow(a, 2)+2*a*b+math.pow(b, 2)-4*(-s+a*b)
d_first = (-a-b+math.sqrt(D))/4
d_second = (-a-b-math.sqrt(D))/4
raw_max_d = int(max(d_first, d_second)) 

max_d_ver = max_d(raw_max_d, modules_count, module_width, module_height, area_width, area_height)
max_d_hor = max_d(raw_max_d, modules_count, module_height, module_width, area_width, area_height)
max_d = max(max_d_ver, max_d_hor)

# print("exec time: {}".format(datetime.datetime.now() - start_time))
print(max_d)