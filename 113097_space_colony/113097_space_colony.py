import sys

def can_place_modules(modules_count, module_width, module_height, area_width, area_height):
    # print(("modules_count: {}, modules_width: {}, "
    #    "module_height: {}, area_width: {}, area_height: {}")
    #    .format(modules_count, module_width, module_height,
    #           area_width, area_height))
    placed_modules = 0
    cur_y = 0
    for ver_index in range(sys.maxsize):
        # print("ver_index: {}".format(ver_index))
        cur_x = 0
        # print("cur_y: {}, module_height: {}".format(cur_y, module_height))
        tmp_y = cur_y + module_height
        if tmp_y > area_height:
            # print("going out of area_height: {}".format(tmp_y))
            return False
        else:
            cur_y = tmp_y
        for hor_index in range(sys.maxsize):
            # print("hor_index: {}".format(hor_index))
            tmp_x = cur_x + module_width
            if tmp_x > area_width:
                # print(" - going out of area_width: {}".format(tmp_x))
                # print("next row: cur_y: {}".format(cur_y))
                break
            else:
                cur_x = tmp_x
                placed_modules += 1
                # print("- place placed_modules: {}".format(placed_modules))
            if placed_modules == modules_count:
                # print("all modules are placed")
                return True
    raise Exception("this point can't be reached")



input_file = open("./input.txt")

input_values = input_file.readline().split(" ")

modules_count = int(input_values[0])
module_width = int(input_values[1])
module_height = int(input_values[2])
area_width = int(input_values[3])
area_height = int(input_values[4])

# print(("inital: modules_count: {}, modules_width: {}, "
#        "module_height: {}, area_width: {}, area_height: {}")
#        .format(modules_count, module_width, module_height,
#                area_width, area_height))

max_protection_fatness = 0
for prot_fatness in range(sys.maxsize):
    new_module_width = module_width + (prot_fatness * 2)
    new_module_height = module_height + (prot_fatness * 2)
    # print("try with prot_fatness: {}".format(prot_fatness))
    if (not can_place_modules(modules_count, new_module_width, new_module_height, area_width, area_height) and 
        not can_place_modules(modules_count, new_module_height, new_module_width, area_width, area_height)):
        break
    max_protection_fatness = prot_fatness

print(max_protection_fatness)