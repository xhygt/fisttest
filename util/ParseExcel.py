# encoding =utf-8
import openpyxl
from openpyxl.styles import  Border,Side,Font
import time

class ParseExcel(object):

    def __init__(self):
        self.workbook = None
        self.excelFile = None
        self.font = Font(color = None) # 设置字体的颜色
        # 颜色对应的 RGB 值
        self.RGBDict = {'red': 'FFFF3030', 'green':'FF008B00'}

    def loadWorkBook(self,excelPathAndName):
        # 将 Excel 文件加载到内存，并获取其 workbook 对象
        try:
            self.workbook = openpyxl.load_workbook(excelPathAndName)
        except Exception as e:
            raise e
        self.excelFile = excelPathAndName
        return  self.workbook

    def getSheetByname(self,sheetName):
        # 根据 sheet 名获取该 sheet 对象
        try:
            sheet = self.workbook.get_sheet_by_name(sheetName)
            return  sheet
        except Exception as e:
            raise e

    def getSheetByIndex(self,sheetIndex):
        #根据 sheet 的索引号获取该 sheet 对象
        try:
            sheetname = self.workbook.get_sheet_names()[sheetIndex]
        except Exception as e:
            raise e
        sheet = self.workbook.get_sheet_by_name(sheetname)
        return sheet

    def getRowsNumber(self,sheet):
        # 获取 sheet 中有数据区域的结束行号
        return  sheet.max_row

    def getColsNumber(self,sheet):
        # 获取 sheet 中有数据区域的结束列号
        return  sheet.max_column

    def getStartRowNumber(self,sheet):
        # 获取 sheet 中有数据区域的开始行号
        return  sheet.min_row

    def getStartColNumber(self,sheet):
        # 获取 sheet 中有数据区域的开始列好：
        return  sheet.min_column

    def getRow(self,sheet,rowNo):
        # 获取 sheet 中某一行，返回的是这一行所有的数据内容组成的 tuple,
        # 下表从 1 开始，sheet.rows[1]表示第一行
        try:
            return  sheet.rows[rowNo -1]
        except Exception as e:
            raise  e

if __name__ == '__main__':
    # 测试代码
    pe = ParseExcel()
    # 测试所需 Excel 文件"XXX.xlsx"请自行创建
    pe.loadWorkBook(u'/Users/dingyq/Desktop/test.xlsx')
    print("通过名称获取 sheet 对象的名字:", \
          pe.getSheetByname(u'联系人'))

    print("通过 index 序号获取 sheet 对象的名字：", \
          pe.getSheetByIndex(0).title)
    sheet = pe.getSheetByIndex(0)
    print (type(sheet))
    print(pe.getRowsNumber(sheet)) # 获取最大行
    print(pe.getColsNumber(sheet)) # 获取最大列
    rows = pe.getRow(sheet,1) # 获取第一行
    for i in rows:
        print(i.value)
    #print(pe.getCellofValue(sheet,rowNo = 1, colsNo = 1))
    #pe.writeCell(sheet,u'我爱祖国', rowNo = 10, colsNo = 10)
    #pe.writeCellCurrentTime(sheet,rowNo = 10 ,colsNo =10)



