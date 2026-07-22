# Day 18 (Task 1)

def read_log_lines(filename):
    with open(filename) as f:
        for file in f:
            yield file


# x = read_log_lines(r"D:\vs code\cybersecurity-roadmap\Phase-0\Month-1\Week04\Learning\Python\hello.txt")
# for i in range(4):
#     print(next(x))

# print([line for line in open(r'D:\vs code\cybersecurity-roadmap\hello.txt', "r", encoding="UTF-8") if 'FAILED' in line])