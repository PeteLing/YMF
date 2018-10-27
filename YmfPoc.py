

class YmfPoc:

    def __init__(self):
        self.info = {
            "name": "",         # poc命名
            "product": "",      # poc针对的应用和版本
            "author": "",       # poc作者
            "date": "",         # poc编写日期   如2018/10/26
            "description": "abcd",  # poc友好说明
        }
        self.options = {        # poc需要的参数

        }
        self.result = {
            "status": "N",      # poc执行后的状态 1-漏洞存在，0-漏洞不存在
            "data": "",         # poc执行返回数据
            "error": "",        # poc返回
        }

    # poc验证
    def verify(self):
        pass
