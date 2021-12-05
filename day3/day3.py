def day3_1(lines):
    sum_list = dict()
    for i in range(len(lines[0])):
        sum_list[str(i)] = 0
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            sum_list[str(j)] += int(lines[i][j])
    gamma = ""
    epsilon = ""
    for i in range(len(lines[0])):
        if sum_list[str(i)] > 499:
            gamma = gamma + "1"
            epsilon = epsilon + "0"
        else:
            gamma = gamma + "0"
            epsilon = epsilon + "1"
    print("power: " + str(int(epsilon, 2)*int(gamma, 2)))


def day3_2(lines):
    row_length = len(lines[0])
    row_remain = lines
    oxy = 0
    co2 = 0
    for i in range(row_length):
        count = 0
        found_rows = list()
        for row in row_remain:
            if row[i] == "1":
                count += 1
        if count > len(row_remain)/2:
            for row in row_remain:
                if row[i] == "1":
                    found_rows.append(row)
        elif count < len(row_remain)/2:
            for row in row_remain:
                if row[i] == "0":
                    found_rows.append(row)
        elif count == len(row_remain)/2:
            for row in row_remain:
                if row[i] == "1":
                    found_rows.append(row)
        row_remain = found_rows
        if len(row_remain) == 1:
            oxy = int(row_remain[0], 2)
    row_remain = lines
    for i in range(row_length):
        count = 0
        found_rows = list()
        for row in row_remain:
            if row[i] == "1":
                count += 1
        if count > len(row_remain)/2:
            for row in row_remain:
                if row[i] == "0":
                    found_rows.append(row)
        elif count < len(row_remain)/2:
            for row in row_remain:
                if row[i] == "1":
                    found_rows.append(row)
        elif count == len(row_remain)/2:
            for row in row_remain:
                if row[i] == "0":
                    found_rows.append(row)
        row_remain = found_rows
        if len(row_remain) == 1:
            co2 = int(row_remain[0], 2)
    print("life scrub: " + str(oxy*co2))


if __name__ == '__main__':
    line_input = open('./day3/day3_input.txt', 'r').read().split("\n")
    day3_1(line_input)
    day3_2(line_input)
