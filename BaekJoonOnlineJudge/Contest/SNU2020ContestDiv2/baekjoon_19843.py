import sys

read = sys.stdin.readline
DAYS = ("Mon", "Tue", "Wed", "Thu")


def return_days(day):
    if day == DAYS[0]:
        num = 0
    elif day == DAYS[1]:
        num = 1
    elif day == DAYS[2]:
        num = 2
    elif day == DAYS[3]:
        num = 3
    else:
        num = 4
    return num


def conv_table(table):
    time_table = [False for _ in range(5 * 24)]
    for index in range(len(table)):
        start = return_days(table[index][0]) * 24 + int(table[index][1])
        end = return_days(table[index][2]) * 24 + int(table[index][3]) - 1
        for j in range(start, end + 1):
            time_table[j] = True
    return time_table


def main():
    plan_time, num = [int(x) for x in read().split()]
    table = list()
    for _ in range(num):
        table.append(read().split())
    sleeping_time = sum(conv_table(table))
    need_time = plan_time - sleeping_time
    if need_time <= 0:
        print(0)
    elif need_time <= 48:
        print(need_time)
    else:
        print(-1)


if __name__ == "__main__":
    main()
