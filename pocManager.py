from Information.main import *
from System.main import *
from util import get_name_and_description


class pocdb_manager:

    def __init__(self, url):
        self.url = url
        information_class = get_name_and_description('Information')
        system_class = get_name_and_description('System')
        self.informationpocdict = {}
        for item in information_class:
            for key, value in item.items():
                self.informationpocdict[key] = eval(value)(url)

        self.systempocdict = {}
        for item in system_class:
            for key, value in item.items():
                self.systempocdict[key] = eval(value)(url)

        self.poc_dict = dict(self.informationpocdict, **self.systempocdict)
        self.new_poc_set = set(self.poc_dict)
        self.old_poc_set = set()

    def has_new_poc(self):
        return self.new_poc_size() != 0

    def get_new_poc(self):
        poc_name = self.new_poc_set.pop()
        poc = self.poc_dict[poc_name]
        self.old_poc_set.add(poc_name)
        return poc

    def new_poc_size(self):
        return len(self.new_poc_set)

    def old_poc_size(self):
        return len(self.new_poc_set)


if __name__ == '__main__':
    pocdb = pocdb_manager('www.baidu.com')
    poc = pocdb.get_new_poc()
    print(type(poc))
    # a = eval("A")("abc")
    # print(type(a))
    # a.pr()
