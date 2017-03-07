import threading


class ThreadHelper:

    def work(self, name, n):
        for num in range(0, n):
            print(name + " Number " +  repr(num) )



if __name__ == '__main__':
    thread_helper = ThreadHelper()
    thread1 = threading.Thread(target=thread_helper.work, args=("Touhid", 100))
    thread1.start()

    thread2 = threading.Thread(target=thread_helper.work, args=("Mia", 100))
    thread2.start()