# import threading
# def task(arg):
#      print(arg)
# #
# # # 创建了一个线程
# t = threading.Thread(target=task, args=(1,))
# # # target => 执行的目标：一般函数
# # # args => 元组
# # # 启动线程
# t.start()

#
#
#
# import threading
# import time
# #
# def task(arg):
#      print(arg)
#      time.sleep(1)
# #
#
# for i in range(10):
#      task(1)
# #     task*10
#
#
# for i in range(10):
# #     # 创建了一个线程
#      t = threading.Thread(target=task, args=(1,))
# #     # 启动线程
#      t.start()
# #
# # time.sleep()的时间+print*10次


# import threading
# import time
# NUM = 0
#
# def task():
#     print('running...')
#     global NUM
#     # 加锁
#     lock.acquire()
#     NUM += 1
#     time.sleep(1)
#     print(NUM)
#     # 释放锁
#     lock.release()
# #     # acquire与release要成对出现
# #     # RLock可嵌套， Lock不可嵌套
# #
# print('app start')
# # # 实例化一个锁
# lock = threading.Lock()
# #
# for i in range(10):
#     # 创建了一个线程
#     t = threading.Thread(target=task, args=())
#     # 启动线程
#     t.start()
# print('app end')


# 信号锁-BoundedSemaphore
# 同时允许N个线程执行内容
# 注意：不是N个线程为一组

# import threading
# import time
# import random
#
# NUM = 0
#
# def task(n):
#     lock.acquire()
#     global NUM
#     NUM += 1
#     sleeptime = random.randint(0,5)
#     print('sleeptime:',sleeptime)
#     time.sleep(sleeptime)
#     print(NUM)
#     lock.release()
# #
# #
# lock = threading.BoundedSemaphore(1)
# for i in range(10):
#     t = threading.Thread(target=task, args=(i,))
#     # args: 可迭代对象
#     t.start()


# import threading
# import time
# #
# #
# def task(i):
#     print(i, 'start')
#     event_lock.wait()
#     print(i, 'end')
#
# event_lock = threading.Event()
# for i in range(10):
#     t = threading.Thread(target=task, args=(i,))
#     t.start()
#
# while True:
#     flag = input('>>>')
#     if flag == '1':
#         event_lock.set()
#         break

# import threading
# import time
#
# def task(i):
#     print(i, 'start')
#     event_lock.wait()
#     print(i, 'end')
#
#
# event_lock = threading.Event()
# for i in range(10):
#     t = threading.Thread(target=task, args=(i,))
#     t.start()
#
# while True:
#     flag = input('>>>')
#     if flag == "1":
#         event_lock.set()
#         break

#
# import threading
# import time
#
#
# def condition():
#     ret = False
#     a = input(">>>")
#     if a == "yes":
#         ret = True
#     return ret
#
# def task(con_lock, i):
#     print(i, 'start')
#     con_lock.acquire()
#     con_lock.wait_for(condition)
#     # wait_for接收一个函数的返回值
#     print(i, 'doing')
#     con_lock.release()
#     print(i, 'end')
#
#
# con_lock = threading.Condition()
# for i in range(10):
#     t = threading.Thread(target=task, args=(con_lock,i))
#     t.start()


# import threading
# def task(con_lock, i):
#     print(i, 'start')
#     con_lock.acquire()
#     con_lock.wait()
#     print(i, 'doing')
#     con_lock.release()
#     print(i, 'end')
# #
# con_lock = threading.Condition()
# for i in range(10):
#     t = threading.Thread(target=task, args=(con_lock,i))
#     t.start()
# #
# #
# while True:
#     flag = input('>>>')
#     if flag == "exit":
#         break
#     con_lock.acquire()
#     con_lock.notify(3)  # 默认1个
#     # con_lock.notify_all()
#     con_lock.release()


# import queue
# q = queue.Queue(5)
# q.put(1)
# q.put(2)
# q.put(3)
# q.put(4)
# q.put(5)
# a = q.get()
# print(a)


# import time
# import queue
# import threading
#
# q = queue.Queue(10)
#
# def productor():
#     while True:
#         print('我做了一个包子')
#         q.put('我做了一个包子')
#         time.sleep(5)
# def consumer():
#     while True:
#         if not q.empty():
#             print('我吃了一个包子')
#             time.sleep(1)
#         else:
#             print('没有包子了')
#
# for i in range(2):
#     t1 = threading.Thread(target=productor)
#     t1.start()
#
# t2 = threading.Thread(target=consumer)
# t2.start()