def day2_1(lines):
    depth = 0
    forward = 0
    for i in range(len(lines)):
        op, val = lines[i].split(" ")
        if op == "forward":
            forward += int(val)
        elif op == "up":
            depth -= int(val)
        elif op == "down":
            depth += int(val)
    print(f"Final location: forward: {forward}, depth: {depth}, vector: {forward*depth}")


def day2_2(lines):
    depth = 0
    forward = 0
    aim = 0
    for i in range(len(lines)):
        op, val = lines[i].split(" ")
        if op == "forward":
            forward += int(val)
            depth += int(val) * aim
        elif op == "up":
            aim -= int(val)
        elif op == "down":
            aim += int(val)
    print(f"Final location: forward: {forward}, depth: {depth}, vector: {forward*depth}")


if __name__ == '__main__':
    line_input = open('./day2/day2_input.txt', 'r').read().split("\n")
    day2_1(line_input)
    day2_2(line_input)
