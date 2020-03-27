# https://www.acmicpc.net/problem/9498

score = int(input())
grade = ('A', 'B', 'C', 'D', 'F')

if score >= 90:
	print(grade[0])
elif score >= 80:
	print(grade[1])
elif score >= 70:
	print(grade[2])
elif score >= 60:
	print(grade[3])
else:
	print(grade[4])
