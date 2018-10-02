#encoding = utf-8
import win32clipboard as w
# import win32clipboard
import win32con

class Clipboard(object):
    '''模拟Windows设置剪切板'''
    #读取剪切版
    @staticmethod
    def getText():
        #打开剪切板
        w.OpenClipboard()
        #获取剪切版中的数据
        d = w.GetClipboardData(win32con.CF_TEXT)
        #关闭剪切板
        w.CloseClipboard()
        #返回剪切板数据给调用
        return  d
    #设置剪切板内容
    @staticmethod
    def setText(aString):
        #打开剪切板
        w.OpenClipboard()
        #清空剪切板
        w.EmptyClipboard()
        #将数据astring 写入剪切板
        w.SetClipboardData(win32con.CF_TEXT,aString)
        #关闭剪切板
        w.CloseClipboard()