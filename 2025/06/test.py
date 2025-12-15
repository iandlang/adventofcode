import part2 as p2

data = p2.load_data("data.txt")
# print(list(data))
# for line in data:
#     pass
#     print(line)
# data = p2.load_data("test.txt")

nums=[]
result = 0
for line in data:
    nums = ("".join(line[:-1]).strip())

    if nums != "" and line[-1] in ("+", "*"):
        print("setting op")
        op = line[-1]
        calc = 0 if op == "+" else 1

    print(f"line {line} nums {nums} op {op} calc {calc}")


    if nums != "":
        if op == "*":
            calc *= int(nums)
            print(f"op {op} {calc} {nums}")
        if op == "+":
            calc += int(nums)
            print(f"op {op} {calc} {nums}")
    else:
        print(f"calc: {calc}")
        result += calc
        print(f"result: {result}")
        calc == 0
result += calc

print(f"result: {result}")