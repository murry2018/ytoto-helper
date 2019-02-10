import os
from os import system

print("*** 연세토토 베팅 도우미 v.1 ***\r\n")

# 현재 디렉토리에서...
files = [f for f in os.listdir('.') if os.path.isfile(f)]
for filename in files:
    # 확장자가 dat인 파일만 탐색
    # dat 파일에 마일리지 기록이 들어있음
    split = os.path.splitext(filename)
    try: extension = split[1]
    except IndexError: continue
    if extension != '.dat': continue
    # 마일리지 자료 통계 출력
    print("===== {} =====".format(split[0]))
    system("python mileage.py < {}".format(filename))
