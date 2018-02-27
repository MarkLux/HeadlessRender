# -*- coding:utf-8
from headless_render import HeadlessRenderService
from headless_render.ttypes import Request
import time
from thrift.transport import TSocket, TTransport
from thrift.protocol import TBinaryProtocol
from config.constant import RPC_PORT


def request_render(ad_id, url):
    transport = TSocket.TSocket('localhost', RPC_PORT)
    transport = TTransport.TBufferedTransport(transport)
    protocol = TBinaryProtocol.TBinaryProtocol(transport)
    client = HeadlessRenderService.Client(protocol)
    transport.open()
    req = Request(url, ad_id)
    html = client.getRenderHtml(req)

    return html


if __name__ == '__main__':
    ad_id = int(raw_input('ad_id:'))
    url = str(raw_input('url:'))
    start_time = time.time()
    html = request_render(ad_id, url)
    end_time = time.time()
    print html
    print 'time used: %s s' % (str(end_time - start_time))
