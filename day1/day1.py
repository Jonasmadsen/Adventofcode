def day1_1(lines):
    increased_count = 0
    for i in range(len(lines) - 1):
        if int(lines[i + 1]) > int(lines[i]):
            increased_count += 1
    print(f"increased {increased_count} times with single steps")


def day1_2(lines):
    increased_count = 0
    for i in range(len(lines)):
        if i + 4 > len(lines):
            continue
        if int(lines[i+1]) + int(lines[i+2]) + int(lines[i+3]) > int(lines[i]) + int(lines[i+1]) + int(lines[i+2]):
            increased_count += 1
    print(f"Increased {increased_count} times with sliding windows")


if __name__ == '__main__':
    line_input = open('./day1/day1_input.txt', 'r').read().split("\n")
    day1_1(line_input)
    day1_2(line_input)
