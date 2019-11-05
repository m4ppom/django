# python: blocking
from time import sleep

# print('hi')
# sleep(3)
# print('bye')


def sleep_3s():
    sleep(3)
    print('wake up')


print('start sleeping')
sleep_3s()
print('end of program')
