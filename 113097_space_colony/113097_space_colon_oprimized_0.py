import sys
import datetime
import math


def can_place_modules(modules_count, module_width, module_height, area_width, area_height):
    modules_can_be_placed_in_row = math.floor(area_width / module_width)
    rows_can_be_count = math.floor(area_height / module_height)
    modules_can_be_placed = modules_can_be_placed_in_row * rows_can_be_count
    return modules_count <= modules_can_be_placed


input_file = open("./input.txt")

input_values = input_file.readline().split(" ")

modules_count = int(input_values[0])
module_width = int(input_values[1])
module_height = int(input_values[2])
area_width = int(input_values[3])
area_height = int(input_values[4])

start_time = datetime.datetime.now()

result_protection_fatness = -1
for prot_fatness in range(sys.maxsize):
    new_module_width = module_width + (prot_fatness * 2)
    new_module_height = module_height + (prot_fatness * 2)
    print("try with prot_fatness: {}".format(prot_fatness))
    if (can_place_modules(modules_count, new_module_width, new_module_height, area_width, area_height) and 
        can_place_modules(modules_count, new_module_height, new_module_width, area_width, area_height)):
        result_protection_fatness = prot_fatness

print("exec time: {}".format(datetime.datetime.now() - start_time))
print(result_protection_fatness)