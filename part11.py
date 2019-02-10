#!
# 11
# 11.1 concurrency
# i/o 바운드: 프로세스가 진행되는 속도가 i/o 하위 시스템의 속도에 의해 제한됨을 의미
# 	디스크의 데이터를 처리하는 작업은 i/o바운드일 가능성이 큼.
# cpu 바운드: 프로세스가 진행되는 속도가 cpu속도에 의해 제한되는 것을 의미
#	작은 행렬을 곱하는 것과 같이 작은 숫자 집합에 대해 계산을 수행하는 작업은 cpu 바운드일 가능성이 큼
# 동기 synchronous
# 비동기 asynchronous
# 11.1.1 queue
# FIFO
# 11.1.2 PROCESS
# 한대의 식기세척기와 여러 대의 건조기 프로세스
# import multiprocessing as mp 

# def washer(dishes, output):
# 	for dish in dishes:
# 		print('Washing', dish, 'dish')
# 		output.put(dish)

# def dryer(input):
# 	while True:
# 		dish = input.get()
# 		print('Drying', dish, 'dish')
# 		input.task_done()

# dish_queue = mp.JoinableQueue()
# dryer_proc = mp.Process(target=dryer, args=(dish_queue,))
# dryer_proc.daemon = True
# dryer_proc.start()
# dishes = ['salad', 'bread', 'entree', 'desert']
# washer(dishes, dish_queue)
# dish_queue.join()

#11.1.3 thread
# 예제1
# import threading

# def do_this(what):
# 	whoami(what)

# def whoami(what):
# 	print("Thread %s says: %s" % (threading.current_thread(), what))

# if __name__ == "__main__":
# 	whoami("I'm the main program")
# 	for n in range(4):
# 		p = threading.Thread(target=do_this, args=("I'm function %s" % n,))
# 		p.start()
# 예제2
# import threading, queue 
# import time

# def washer(dishes, dish_queue):
# 	for dish in dishes:
# 		print("Washing ", dish, '-dish')
# 		time.sleep(5)
# 		dish_queue.put(dish)

# def dryer(dish_queue):
# 	while True:
# 		dish = dish_queue.get()
# 		print("Drying ", dish, 'dish')
# 		time.sleep(10)
# 		dish_queue.task_done()

# dish_queue = queue.Queue()

# for n in range(2):
# 	dryer_thread = threading.Thread(target=dryer, args=(dish_queue,))
# 	dryer_thread.start()

# dishes = ['salad', 'bread', 'entree', 'desert']
# washer(dishes, dish_queue)
# dish_queue.join()

# I/O 바운드 문제 - 스레스 사용
# CPU 바운드 문제 - 프로세스, 네트워킹, 이벤트 사용

# 11.1.4 그린 스레드와 gevent
# 엔진엑스 서버는 이벤트 기반 프로그래밍

# 11.2
# 11.2.3 tcp/ip

# 11.2.4 socket

# 11.2.5 ZeroMQ
# 11.2.6 scapy

