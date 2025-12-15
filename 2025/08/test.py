import part2 as p2

data = p2.load_data("test.txt")
# print(list(data))
for line in data:
    print(line)
# data = p2.load_data("test.txt")

# print("====")

# for line in data:
#     print(''.join(line[:-1]), line[-1])