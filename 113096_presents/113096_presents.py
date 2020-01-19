

def find_most_suitable_present(presents_coast, score):
    tmp_presents_coast = list(presents_coast)
    tmp_presents_coast = tmp_presents_coast[:score]
    tmp_presents_coast.remove(max(tmp_presents_coast))
    # print('score: {}; presents to choose left: {}'
    #       .format(score, tmp_presents_coast))
    return max(tmp_presents_coast)


input_file = open("./input.txt")


presents_count = int(input_file.readline())
max_score = presents_count
presents_coast = list(map(lambda s: int(s), input_file.readline().split(" ")))

# print('presents_count: ' + str(presents_count))
# print('presents_coast: ' + str(presents_coast))

results = []

for k in range(2, presents_count + 1):
    # print('processing k for: ' + str(k))
    result = find_most_suitable_present(presents_coast, k)
    results.append(result)

print(str(results).strip('[]').replace(',', ''))
