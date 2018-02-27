# -*- coding:utf-8

from headless_render import HeadlessRenderService
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer
from config.constant import RPC_HOST, RPC_PORT, DRIVER
from drivers.chrome_headless import ChromeHeadlessDriver
from drivers.firefox_headless import FirefoxHeadlessDriver
from drivers.phantom_js import PhantomJsDriver
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class HeadlessRenderHandler(object):
    def __init__(self):
        self.driver = None
        if DRIVER == 'chrome':
            self.driver = ChromeHeadlessDriver()
        elif DRIVER == 'phantomjs':
            self.driver = PhantomJsDriver()
        else:
            # 默认Firefox
            self.driver = FirefoxHeadlessDriver()
        print DRIVER + 'driver loaded'

    def getRenderHtml(self, request):
        url = str(request.url)
        # ad_id = int(request.ad_id)

        try:
            rsp = self.driver.get_html(url)
        except Exception as e:
            print e.message
            rsp = ''
        return rsp


def serve():
    handler = HeadlessRenderHandler()
    processor = HeadlessRenderService.Processor(handler)
    transport = TSocket.TServerSocket(RPC_HOST, RPC_PORT)
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)
    print 'starting server listening on %s:%s' % (str(RPC_HOST), str(RPC_PORT))
    server.serve()


if __name__ == '__main__':
    serve()
