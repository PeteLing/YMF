from urllib.parse import urlparse
from YmfPoc import YmfPoc
import redis


class redis_unauth_BaseVerify(YmfPoc):

    def __init__(self, url):
        super(self.__class__, self).__init__()
        self.info = {
            "name": "redis unauth",         # poc命名
            "product": "redis",      # poc针对的应用和版本
            "author": "unknow",       # poc作者
            "date": "2018/10/27",         # poc编写日期   如2018/10/26
            "description": "redis无用户密码可远程登陆",  # poc友好说明
        }
        self.options = {        # poc需要的参数
            "url": url,
        }
        self.result = {
            "status": "N",      # poc执行后的状态 1-漏洞存在，0-漏洞不存在
            "data": "",         # poc执行返回数据
            "error": "",        # poc返回
        }

    # poc验证
    def verify(self):
        port = 6379
        if r"http" in self.options['url']:
            # 提取host
            host = urlparse(self.options['url'])[1]
            try:
                port = int(host.split(':')[1])
            except:
                pass
            flag = host.find(":")
            if flag != -1:
                host = host[:flag]
        else:
            if self.options['url'].find(":") >= 0:
                host = self.options['url'].split(":")[0]
                port = int(self.options['url'].split(":")[1])
            else:
                host = self.options['url']

        try:
            r = redis.Redis(host, port=port, db=0, socket_timeout=6.0)
            if r.ping() is True:
                self.result['status'] = True
            else:
                self.result['status'] = False
        except:
            self.result['status'] = False
            self.result['error'] = "连接超时"