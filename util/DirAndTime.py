#encoding = utf-8
import time,os
from  datetime import datetime
from config.VarConfig import screenPicturesDir
import config.Globalvar as gl
#获取当前日期
def getCurrentDate():
    timeTup = time.localtime()
    currentDate = str(timeTup.tm_year) +"-"+ \
        str(timeTup.tm_mon) + "-" + str(timeTup.tm_mday)
    return currentDate
#获取当前的时间
def getCurrentTime():
    timeStr = datetime.now()
    # 获取时间
    nowTime = timeStr.strftime('%Y-%m-%d-%H-%M-%S')
    return  nowTime
#创建截图存放的目录
def createCurrentDateDir():
    # 获取测试用例的名称
    Casenamern= gl.get_value('testcasename_ex')
    # 命名文件夹名称为用例名称
    dirName = os.path.join(screenPicturesDir,getCurrentDate(),Casenamern)
    # casedirName = os.path.join(dirName,Casenamern)
    if not os.path.exists(dirName):
        os.makedirs(dirName)
        # if not os.path.exists(casedirName):
        #     os.makedirs(casedirName)
            # return casedirName
    return dirName
if __name__ == '__main__':
    print(getCurrentDate())
    print(createCurrentDateDir())
    print(getCurrentTime())
    # print(testcasenamein_ex)