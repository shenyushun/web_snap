# coding=utf-8
'''
@Author：XingSongYan
@CreateDate： Wed Apr 29 09:12:56 HKT 2015
@FileName：
@Description：负责把传入的url进行快照并生成pdf。接口以post的方法接受3个参数：
              url---页面url
              name----保pdf文件名
'''
import web
import pdfkit
from urllib import unquote

urls = (
    '/', 'index'
)


class index:

    def GET(self):
        return "Hello, Get!"

    def POST(self):
        data = web.data()
        temp = [x for x in data.split("&")]
        temp.sort()
        try:
            url = temp[1].split("=")[1]
            name = temp[0].split("=")[1]
            urld = unquote(url).decode('utf8')
            filename = "%s.pdf" % name
            pdfkit.from_url(str(urld), filename)
        except Exception as e:
            pdfkit.from_string(str(e), 'error_%s.pdf' % name)
        return "sucess"

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
