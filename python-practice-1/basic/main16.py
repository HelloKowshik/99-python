from multiprocessing import Process, cpu_count
import time


def counter(num):
    c = 0
    while c <= num:
        c += 1

def main():
    print(cpu_count())
    # a = Process(target=counter, args=(1000000000,))
    a = Process(target=counter, args=(125000000,))
    b = Process(target=counter, args=(125000000,))
    c = Process(target=counter, args=(125000000,))
    d = Process(target=counter, args=(125000000,))
    e = Process(target=counter, args=(125000000,))
    f = Process(target=counter, args=(125000000,))
    g = Process(target=counter, args=(125000000,))
    h = Process(target=counter, args=(125000000,))

    # a.start()
    # b.start()
    # c.start()
    # d.start()
    # e.start()
    # f.start()
    # g.start()
    # h.start()

    a.join()
    b.join()
    c.join()
    d.join()
    e.join()
    f.join()
    g.join()
    h.join()

    print(f'Finished is {time.perf_counter()} seconds!')        

if __name__ == '__main__':
    main()
