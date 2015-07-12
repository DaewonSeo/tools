#coding:utf-8

import random

def main():
	elevator_1 = random.randint(1,15)
	elevator_2 = random.randint(1,15)

	present_floor = int(raw_input("지금 몇층인가요?"))
	target_floor = int(raw_input("몇층으로 가실 건가요?"))

	moving_elevator = ""
	#두개의 엘리베이터중 움직일 엘리베이터를 결정하는 과정
	if ((elevator_1 - present_floor) ** 2) > ((elevator_2 - present_floor) ** 2):
		print "elevator_2이 움직입니다."
		moving_elevator = elevator_2

	elif ((elevator_1 - present_floor) ** 2) < ((elevator_2 - present_floor) ** 2):
		print "elevator_1이 움직입니다."
		moving_elevator = elevator_1

	else:
		print "둘다 작동가능합니다."
		moving_elevator = elevator_1

	print "{}층에서 엘리베이터가 출발합니다.".format(moving_elevator)

	#선택된 엘리베이터가 내가 버튼을 누른 층으로 이동하는 과정
	if moving_elevator > present_floor:
		while moving_elevator > present_floor:
			print "엘리베이터는 현재 {}층입니다.".format(moving_elevator)	
			moving_elevator -= 1
		print "탑승합니다."

	elif moving_elevator < present_floor:
		while moving_elevator < present_floor:
			print "엘리베이터는 현재 {}층입니다.".format(moving_elevator)	
			moving_elevator += 1
		print "탑승합니다."
				
	else:
		print "엘리베이터는 현재 {}층입니다.".format(moving_elevator)
		print "탑승합니다."

	#도착한 엘리베이터를 탑승하고 원하는 층으로 이동하는 과정	
	if moving_elevator > target_floor:
		while moving_elevator != target_floor:
			print "엘리베이터는 현재 {}층입니다.".format(moving_elevator)
			moving_elevator -= 1
		print "도착하였습니다."

	elif moving_elevator < target_floor:
		while moving_elevator != target_floor:
			print "엘리베이터는 현재 {}층입니다.".format(moving_elevator)
			moving_elevator += 1
		print "도착하였습니다."


main()
