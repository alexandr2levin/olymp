import sys
import time


def second_max_int_in_list(ints_list):
    max_value = -sys.maxsize
    second_max_value = -sys.maxsize
    for value in ints_list:
        if(value >= max_value):
            second_max_value = max_value
            max_value = value
    return second_max_value


def find_most_suitable_present(presents_coast, score):
    tmp_list = presents_coast[:score]
    # print('score: {}; presents to choose left: {}'
    #      .format(score, tmp_list))
    return second_max_int_in_list(tmp_list)


input_file = open("./input.txt")


presents_count = int(input_file.readline())
max_score = presents_count
presents_coast = list(map(lambda s: int(s), input_file.readline().split(" ")))

# print('presents_count: ' + str(presents_count))
# print('presents_coast: ' + str(presents_coast))

startTime = time.time()

results = []

for k in range(2, presents_count + 1):
    # print('processing k for: ' + str(k))
    result = find_most_suitable_present(presents_coast, k)
    results.append(result)

print(str(results).strip('[]').replace(',', ''))

# print('exec time: {} millis'.format(time.time() - startTime))
