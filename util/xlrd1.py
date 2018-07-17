"""
# #需要修改
import xlrd
import xlwt
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
            self.workbook = xlrd.open_workbook(excelPathAndName)
        except Exception as e:
            raise e
        self.excelfile = excelPathAndName
        return  self.workbook

    def getSheetByname(self,sheetName):
        # 根据 sheet 名获取该 sheet 对象
        try:
            sheet = self.workbook.sheet_by_name(sheetName)
            #sheet = self.workbook.sheet_names()
            return  sheet
        except Exception as e:
            raise e
    def getSheetByIndex(self,sheetIndex):
        #根据 sheet 的索引号获取该 sheet 对象
        try:
            sheetname = self.workbook.sheet_loaded(sheetIndex)
        except Exception as e:
            raise e
        sheet = self.workbook.sheet_by_name(sheetname)
        return sheet
    def getRowsNumber(self,sheet):
        # 获取 sheet 中有数据区域的结束行号
        return  sheet.max_row

    def getColsNumber(self,sheet):
        # 获取 sheet 中有数据区域的结束列号
        return  sheet.max_column
if __name__ == '__main__':
    # 测试代码
    pe = ParseExcel()
    # 测试所需 Excel 文件"XXX.xlsx"请自行创建
    pe.loadWorkBook(u'/Users/dingyq/pyauto/datas/test.xlsx')
    print("通过名称获取 sheet 对象的名字:", \
          pe.getSheetByname(u'联系人'))
    sheet = pe.getSheetByIndex(0)
    print(pe.getColsNumber(sheet))
    print(pe.getRowsNumber(sheet))

    #print("通过 index 序号获取 sheet 对象的名字：", \
         # pe.getSheetByIndex(0).title)
   # sheet = pe.getSheetByIndex(0)
    #print (type(sheet))
    #print(pe.getRowsNumber(sheet)) # 获取最大行
    #print(pe.getColsNumber(sheet)) # 获取最大列
    #错误开始
    #rows = pe.getRow(sheet,1) # 获取第一行
    ##   print(i.value)
    #print(pe.getCellofValue(sheet,rowNo = 1, colsNo = 1))
    #pe.writeCell(sheet,u'我爱祖国', rowNo = 10, colsNo = 10)
    #pe.writeCellCurrentTime(sheet,rowNo = 10 ,colsNo =10)
"""
