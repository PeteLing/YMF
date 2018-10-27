import threading
import multiprocessing
import sys
from pocManager import pocdb_manager


class VerifyThread(threading.Thread):
    def __init__(self, pocManager):
        threading.Thread.__init__(self)
        self.poc_manager = pocManager

    def run(self):
        while self.poc_manager.has_new_poc():
            try:
                poc = self.poc_manager.get_new_poc()
                print("[+]start verify the poc: " + poc.info['name'])
                poc.verify()
            except Exception as e:
                print(e)


def start_verify_poc(threading_num, manager):
    threads = []
    for i in range(threading_num):
        thread = VerifyThread(manager)
        thread.setDaemon(True)
        thread.start()
        threads.append(thread)
    for t in threads:
        t.join()


def print_help():
    print('Usage: python3 Ymf.py -u http://www.example.com            对url执行所有poc检测')
    print('Usage: python3 Ymf.py -u http://www.example.com -o pocname 对指定url用指定poc检测')
    print('Usage: python3 Ymf.py -r filepath -o pocname               用指定的poc检测文件中所有url')
    print('Usage: python3 Ymf.py -l                                   列出所有poc')
    print('Usage: python3 -h                                          输出帮助信息')


def get_poc_name():
    man = pocdb_manager('')
    for poc in man.new_poc_set:
        print('Poc: ' + poc)


def verify_one_with_all_poc(url):
    print('[-]' + url)
    pv = pocdb_manager(url)
    start_verify_poc(multiprocessing.cpu_count(), pv)
    poc_dict = pv.poc_dict
    print('[!]result for url: ' + url)
    for name, poc in poc_dict.items():
        print(poc.info['name'] + ': ' + ' '*(50 - len(poc.info['name'])) + str(poc.result['status']))


def verify_one_with_poc(url, pocname):
    man = pocdb_manager(url)
    poc = man.poc_dict[pocname]
    poc.verify()
    print('[!]result for url: ' + url)
    print(poc.info['name'] + ': ' + ' ' * (50 - len(poc.info['name'])) + str(poc.result['status']))


def verify_urls_with_poc(filename, pocname):
    with open(filename, 'r', encoding='utf-8') as f:
        urls = f.readlines()
        for url in urls:
            verify_one_with_poc(url, pocname)


def verify_urls_with_all_poc(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        urls = f.readlines()
        for url in urls:
            verify_one_with_all_poc(url)


def main():
    if sys.argv[1] == '-h':
        print_help()
    elif sys.argv[1] == '-l':
        get_poc_name()
    elif sys.argv[1] == '-u' and len(sys.argv) == 3:
        verify_one_with_all_poc(sys.argv[2])
    elif sys.argv[1] == '-u' and sys.argv[3] == '-o':
        verify_one_with_poc(sys.argv[2], sys.argv[4])
    elif sys.argv[1] == '-r' and sys.argv[3] == '-o':
        verify_urls_with_poc(sys.argv[2], sys.argv[4])
    elif sys.argv[1] == '-r' and sys.argv[3] == '-a':
        verify_urls_with_all_poc(sys.argv[2])
    else:
        print_help()


if __name__ == '__main__':
    main()
