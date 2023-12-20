# import language as lg
from language import translate
import time

f = open("Night.Of.The.Living.Dead.1968.txt", "r")

# print(f.readlines())

# for line in f.readlines():
#     print(line)

# while True:
#     line = f.readline()
#     if line == "":
#         break
#     print(line.replace("\n", ""))

while True:
    line = f.readline()
    if line == "":
        break
    line = line.replace("\n", "")

    result = translate(line)
    print(line)
    # print(">", result)
    print(f"> {result}")

    time.sleep(1)  # 1초에 하나씩 출력.

f.close()