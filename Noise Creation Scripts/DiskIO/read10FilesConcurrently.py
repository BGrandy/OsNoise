import threading

class FileReaderThread(threading.Thread):
    def __init__(self, file_path):
        threading.Thread.__init__(self)
        self.file_path = file_path
        self.file_content = None

    def run(self):
        with open(self.file_path, 'r') as f:
            self.file_content = f.read()

if __name__ == '__main__':
    file_paths = ['/home/ben/Desktop/Python/file1.txt', '/home/ben/Desktop/Python/file2.txt', '/home/ben/Desktop/Python/file3.txt', '/home/ben/Desktop/Python/file4.txt', '/home/ben/Desktop/Python/file5.txt', '/home/ben/Desktop/Python/file6.txt', '/home/ben/Desktop/Python/file7.txt', '/home/ben/Desktop/Python/file8.txt', '/home/ben/Desktop/Python/file9.txt', '/home/ben/Desktop/Python/file10.txt',]
    file_reader_threads = []

    # create threads for each file path
    for file_path in file_paths:
        thread = FileReaderThread(file_path)
        file_reader_threads.append(thread)

    # start all threads
    for thread in file_reader_threads:
        thread.start()

    # wait for all threads to complete
    for thread in file_reader_threads:
        thread.join()

    # print the content of each file
    for i, thread in enumerate(file_reader_threads):
        print(f'File {i+1} content: {thread.file_content}')

