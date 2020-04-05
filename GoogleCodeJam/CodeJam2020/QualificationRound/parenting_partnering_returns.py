# https://codingcompetitions.withgoogle.com/codejam/round/000000000019fd27/000000000020bdf9
# Solved Date:

MAX = 24 * 60 *2


def check_assigned(timetable, times):
    return all(timetable[times[0]:times[1]])


def assign_time(timetable, times):
    for time in range(times[0], times[1]):
        timetable[time] = False
    return timetable


def assign_timetable():
    cameron_timetable = [True for _ in range(MAX + 1)]
    jamie_timetable = [True for _ in range(MAX + 1)]
    schedule = []
    schedule_count = int(input())
    for _ in range(schedule_count):
        times = [int(x) for x in input().split()]
        if check_assigned(cameron_timetable, times):
            schedule.append('C')
            cameron_timetable = assign_time(cameron_timetable, times)
        elif check_assigned(jamie_timetable, times):
            schedule.append('J')
            jamie_timetable = assign_time(jamie_timetable, times)
        else:
            return "IMPOSSIBLE"
    return ''.join(schedule)


def main():
    test_case_num = int(input())
    for test_case in range(1, test_case_num+1):
        schedule = assign_timetable()
        print("Case #{}: {}".format(test_case, schedule))


if __name__ == '__main__':
    main()

