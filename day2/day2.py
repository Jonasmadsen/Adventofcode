def day2_1():
    lines = open('day2_input.txt', 'r').read().split("\n")
    depth = 0
    forwardness = 0
    for i in range(len(lines)):
        op = lines[i].split(" ")[0]
        val = lines[i].split(" ")[1]
        if op == "forward":
            forwardness += int(val)
        elif op == "up":
            depth -= int(val)
        elif op == "down":
            depth += int(val)
    print(f"Final location: forward: {forwardness}, depth: {depth}, vector: {forwardness*depth}")


def day2_2():
    lines = open('day2_input.txt', 'r').read().split("\n")
    depth = 0
    forwardness = 0
    aim = 0
    for i in range(len(lines)):
        op = lines[i].split(" ")[0]
        val = lines[i].split(" ")[1]
        if op == "forward":
            forwardness += int(val)
            depth += int(val) * aim
        elif op == "up":
            aim -= int(val)
        elif op == "down":
            aim += int(val)
    print(f"Final location: forward: {forwardness}, depth: {depth}, vector: {forwardness*depth}")


if __name__ == '__main__':
    day2_2()
