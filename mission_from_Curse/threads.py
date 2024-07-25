import threading

counter = 0

def add():
    global counter
    for i in range(100000):
        counter += 1


def less():
    global counter
    for i in range(100000):
        counter -= 1




thread1 = threading.Thread(target=add)
thread2 = threading.Thread(target=less)

thread1.start()
thread2.start()




print("Final counter value: "  + str(counter))
