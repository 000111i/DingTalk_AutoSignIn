import pyautogui
import random
import msvcrt
import time
import os


#定义全局变量
# superPath = 'D:\\A_Plug_Program\\pyautoGUItest\\picture\\' #在vscode下测似使用（因为vscode默认是使用c盘下启动运行）
superPath = os.path.abspath('..') + '\\picture\\' #根路径  （可以正常使用）（用于生成exe并且跨平台时用）
cycVar = 1 #循环变量。也是全局变量


def Front_Part():
    global cycVar #声明全局变量
    flag = 1
    while flag == 1:
        try:
            pyautogui.doubleClick(pyautogui.center(pyautogui.locateOnScreen(superPath+'dingding.png',confidence = 0.8))) #打开钉钉
            flag += 1
        except TypeError:
            print('[error]:未找到“钉钉”,正在继续等待')

    while flag == 2:
        try:
            pyautogui.click(pyautogui.center(pyautogui.locateOnScreen(superPath+'work.png',confidence = 0.9))) #打开“工作”
            flag += 1
        except TypeError:
            print('[error]:未找到“工作”,正在继续等待')
        
    while (flag == 3) & (cycVar <= 20):
        try:
            pyautogui.click(pyautogui.center(pyautogui.locateOnScreen(superPath+'smart.png',confidence = 0.8))) #打开“工作”
            flag += 1
        except TypeError:
            print("[error]:未找到“智能填表”,正在尝试第",cycVar,"次")
            cycVar += 1

    if cycVar == 21:
        print('[update]:没有找到“智能填表”,所以尝试找到[填写]');
        cycVar = 1
        flag += 1


    while flag == 4:
        try:
            pyautogui.click(pyautogui.center(pyautogui.locateOnScreen(superPath+'tianxie.png',confidence = 0.8)))#打开“填写”
            flag += 1
        except TypeError:
            print('[error],未找到[填写],正在尝试第',cycVar,'次')
            cycVar += 1
        
    while flag == 5:
        try:
            pyautogui.click(pyautogui.center(pyautogui.locateOnScreen(superPath+'jiankangshujvshangchuan.png',confidence = 0.8))) #黑龙江健康上报
            flag += 1
        except TypeError:
            print('[error],未找到[黑龙江健康上报],正在继续尝试')

    time.sleep(0.5)

def Find_flag(titlex, titley):
    # while True:
    #     try:
    #         titlex, titley = pyautogui.center(pyautogui.locateOnScreen(superPath+'fuzhuduiqi.png', coufidence = 0.6)) #这是新版对齐
    #         break;
    #     except TypeError:
    #         print('[error],未找到定位图片,正在继续寻找')

    while True:
        try:
            x, y = pyautogui.center(pyautogui.locateOnScreen(superPath+'daitianxie.png')) #这是新版对齐
            break;
        except TypeError:
            print('[error],未找到“待填写”图片,正在继续寻找')

    return x - titlex, y - titley

def ClickX():
    while True:
        try:
            tx, ty = (pyautogui.center(pyautogui.locateOnScreen(superPath+'osgongzuotai.png',confidence=0.8)))
                    # pyautogui.doubleClick(pyautogui.center(pyautogui.locateOnScreen(s+'tijiao.png',confidence=0.5))) #点击提交
            break;
        except TypeError:
            print('[error],未找到“OA标识”,正在继续寻找')
    return (tx + 365),(ty) #偏移量 （日期：1.26）

def autoFinally(x, y):
    time.sleep(0.5)
    row, col = x, y #分别是行和列
   
    count = 0
    i = 0
    errorCyc = 0
    while col <= (y+2*80):
       
        row = x
        while row <= (x+3*150):
            pyautogui.doubleClick(row, col) #先点击最左侧第一个
            count += 1
            
            errorFlag = 0
           

            time.sleep(0.5)

            
            while i < 25:
                try:
                    # pyautogui.moveTo(pyautogui.center(pyautogui.locateOnScreen(superPath+'tijiao.png',confidence=0.8))) #测试用
                    pyautogui.doubleClick(pyautogui.center(pyautogui.locateOnScreen(superPath+'tijiao.png',confidence=0.8))) #点击提交
                    try:
                        time.sleep(0.5)
                        pyautogui.doubleClick(pyautogui.center(pyautogui.locateOnScreen(superPath+'wozhidaole.png',confidence=0.8))) #点击我知道了
                        errorCyc += 1
                        errorFlag = 1
                    except:
                        i = 1
                        break;
                    i=1; #重置
                    break;
                except TypeError:
                    print('[error],未找到“提交”按钮,正在等待',i)
                    # 一边滚动一边判断
                    time.sleep(0.1)
                    pyautogui.scroll(-200) #滚动
                    i+=1

            if(i==25):
                i=1; #重置
                print('没有找到“提交”，所以点击“x”，继续下一步')

            time.sleep(0.5)

            pyautogui.doubleClick(ClickX())

            time.sleep(0.5)
            if(errorCyc == 2):
                errorCyc = 0 #重置
                print("随机生成一个2到5秒的延迟")
                time.sleep(random.randint(2,5))

            if errorFlag == 1:
                continue;

            row += 150
                
        if errorFlag == 1:
            continue;

        col += 80









def Latter_Part():
    pyautogui.scroll(-100) #向下滚动
    while True:
        try:
            titlex, titley = pyautogui.center(pyautogui.locateOnScreen(superPath+'fuzhuduiqi.png', confidence = 0.8)) #这是新版对齐
            break;
        except TypeError:
            print('[error],未找到定位图片1,正在继续寻找')

    dx,dy = Find_flag(titlex, titley)
    x, y = titlex + dx, titley + dy
    autoFinally(x, y)

    
    
    



if __name__ == "__main__":
    pyautogui.alert('Hey,伙计:\n这是一个自动签到的程序,你懂的吧.'+
    '\n当你点击这个exe的时候,他会自动运行,如果有什么情况导致它运行错误'+
    '请手动点击下一项操作试试.\n我在这里感谢您!!!') # 返回OK 
    pyautogui.hotkey('winleft', 'd') #快捷键清屏
    Front_Part() #前半段项目
    Latter_Part()
    