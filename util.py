import os
import re


def get_name_and_description(file_dir="System"):
    file_dir = os.path.dirname(os.path.realpath(__file__))+'/' + file_dir
    class_and_description = []
    for _, _, files in os.walk(file_dir):
            for file in files:
                if '__init__' not in file and file != 'main.py' and file != '.DS_Store':
                    with open(file_dir + '/' + file, 'r', encoding='utf-8') as f:
                        code = f.read()
                        des_compile = re.compile(r'\"name\": \"(.*)\"')
                        class_compile = re.compile(r'class (.*)\(.*\):')
                        des = des_compile.findall(code)
                        classname = class_compile.findall(code)
                        class_and_description.append({des[0]: classname[0]})
            return class_and_description


if __name__ == '__main__':
    # print(get_sys_name_and_description())
    print(get_name_and_description('Information'))