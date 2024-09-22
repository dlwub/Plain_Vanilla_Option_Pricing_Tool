from PyQt4 import QtCore, QtGui
import sys
import PVOPT
import blackscholes
import modified_BS
import european_dividend_yield
import Bos_Vandermark
import volatility_calc


class MainWindow(QtGui.QMainWindow, PVOPT.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow,self).__init__(parent)
        
   
def showMessage():
    global ui
    ui.textEdit.setText("<font color=red>Please insert all required fields!</font>")

def update():
    global z
    x = ui.lineEdit_7.text()
    if x==" ":
        ui.textEdit.setText("<font color=red>Please insert a value!</font>")
    else:
        z.append(x)
        ui.lineEdit_7.clear()
    return    

def modify():
    global i
    del(z[-1])
    i = i-1
    return 

def take_div():
    global n, i
    n = ui.spinBox.value()
    z=[]
    i = 1    
    while i <=2*n:
        ui.pushButton_4.clicked.connect(update)        
        ui.pushButton_5.clicked.connect(modify)
        i = i+1
    return

def check_input():
    global num, S_0, K, r, q, k, T, sigma, num2, m, div, symbol, n_1, source, n
    
    if num == 0:
        ui.textEdit.setText("<font color=red>Please first select the option category you want to valuate!</font>")
        
    if num == 1:
        K = ui.lineEdit_2.text()
        r = ui.lineEdit_3.text()
        m = ui.lineEdit_12.text()
        symbol = ui.lineEdit_9.text()
        n_1 = ui.lineEdit_8.text()
        source = ui.comboBox.currentIndex()
        num2 = ui.comboBox_2.currentIndex()
        if K == " " or r == " " or m==" " or symbol==" " or n_1 == " " or source ==0 or num2 ==0:
            showMessage()
        else:
            K = float(K)
            r = float(r)
            r = r/float(100)
            m = str(m)              
            n_1 = int(n_1)
            try:
                S_0, T, sigma = volatility_calc.volatility(source, symbol, m, n_1)
            except ValueError:
                ui.textEdit.setText("<font color=red>Failed to download. Please try the other data source.</font>")
            if num2==1:
                try:
                    c = blackscholes.price_calc_call(S_0, K, T, r, sigma)
                    ui.textEdit.setText("The price of European call option is %.2f"%c)
                except ValueError:
                    ui.textEdit.setText("<font color=red>Error!</font>")
            elif num2==2:
                try:
                    p = blackscholes.price_calc_put(S_0, K, T, r, sigma)
                    ui.textEdit.setText("The price of European put option is %.2f"%p)
                except ValueError:
                    ui.textEdit.setText("<font color=red>Error!</font>")    
        
    if num == 2:
        S_0 = ui.lineEdit.text()             
        K = ui.lineEdit_2.text()
        r = ui.lineEdit_3.text()        
        T = ui.lineEdit_4.text()        
        sigma = ui.lineEdit_5.text()        
        num2 = ui.comboBox_2.currentIndex()
        if S_0 == " " or K == " " or r == " " or T == " " or sigma == " " or num2 ==0:
            showMessage()
        else:            
            S_0 = float(S_0)
            K = float(K)
            r = float(r)
            r = r/float(100)
            T = float(T)
            sigma = float(sigma)
            if num2==1:
                try:
                    c = blackscholes.price_calc_call(S_0, K, T, r, sigma)
                    ui.textEdit.setText("The price of the European call option is %.2f"%c)                           
                except ValueError:
                    ui.textEdit.setText("<font color=red>Error!</font>")
                    
            elif num2==2:
                try:
                    p = blackscholes.price_calc_put(S_0, K, T, r, sigma)
                    ui.textEdit.setText("The price of the European put option is %.2f"%p)                           
                except ValueError:
                    ui.textEdit.setText("<font color=red>Error!</font>")
                    
    if num == 3:
        K = ui.lineEdit_2.text()
        r = ui.lineEdit_3.text()
        m = ui.lineEdit_12.text()
        div = ui.lineEdit_6.text()
        symbol = ui.lineEdit_9.text()
        n_1 = ui.lineEdit_8.text()
        source = ui.comboBox.currentIndex()
        n = ui.lineEdit_10.text()
        q = ui.lineEdit_6.text()        
        num2 = ui.comboBox_2.currentIndex()
        if K == " " or r == " " or m == " " or q == " " or symbol==" " or n_1 == " " or source ==0 or n==" " or num2 ==0:
            showMessage()
        else:
            K = float(K)
            r = float(r)
            r = r/float(100)
            m = int(m)
            q = float(q)
            q = q/float(100)
            n_1 = int(n_1)
            n = int(n)
            try:
                S_0, T, sigma = volatility_calc.volatility(source, symbol, m, n_1)
            except ValueError:
                ui.textEdit.setText("<font color=red>Failed to download. Please try the other data source.</font>")
            if num2==1:
                try:
                    c = modified_BS.call(S_0, K, T, r, q, n, sigma)
                    ui.textEdit.setText("The price of the European call option is %.2f"%c)                           
                except ValueError:
                    ui.textEdit.setText("<font color=red>Error!</font>")
                    
            elif num2==2:
                try:
                    p = modified_BS.put(S_0, K, T, r, q, n, sigma)
                    ui.textEdit.setText("The price of the European put option is %.2f"%p)                           
                except ValueError:
                    ui.textEdit.setText("<font color=red>Error!</font>")
    
    if num == 4:
        S_0 = ui.lineEdit.text()             
        K = ui.lineEdit_2.text()        
        r = ui.lineEdit_3.text()        
        T = ui.lineEdit_4.text()        
        sigma = ui.lineEdit_5.text()
        q = ui.lineEdit_6.text()
        n = ui.spinBox.text()
        num2 = ui.comboBox_2.currentIndex()
        if S_0 == " " or K == " " or r == " " or T == " " or sigma == " " or q == " " or n ==" " or num2 ==0:
            showMessage()
        else:            
            S_0 = float(S_0)
            K = float(K)
            r = float(r)
            r = r/float(100)
            T = float(T)
            sigma = float(sigma)
            q = float(q)
            q = q/float(100)
            n =int(n)
            
            if num2==1:
                try:
                    c = modified_BS.call(S_0, K, T, r, q, n, sigma)
                    ui.textEdit.setText("The price of the European call option is %.2f"%c)                           
                except ValueError:
                    ui.textEdit.setText("<font color=red>Error!</font>")
                    
            elif num2==2:
                try:
                    p = modified_BS.put(S_0, K, T, r, q, n, sigma)
                    ui.textEdit.setText("The price of the European put option is %.2f"%p)                           
                except ValueError:
                    ui.textEdit.setText("<font color=red>Error!</font>")
                    
    if num == 5:
        K = ui.lineEdit_2.text()
        r = ui.lineEdit_3.text()
        m = ui.lineEdit_12.text()
        div = ui.lineEdit_6.text()
        symbol = ui.lineEdit_9.text()
        n_1 = ui.lineEdit_8.text()
        source = ui.comboBox.currentIndex()
        q = ui.lineEdit_6.text()
        n = ui.spinBox.text()
        k = ui.lineEdit_11.text()
        num2 = ui.comboBox_2.currentIndex()
        if K == " " or r == " " or m == " " or q == " " or symbol==" " or n_1 == " " or source ==0 or n==" " or k==" " or num2 ==0:
            showMessage()
        else:
            K = float(K)
            r = float(r)
            r = r/float(100)
            m = int(m)
            q = float(q)
            q = q/float(100)
            n_1 = int(n_1)
            n = int(n)
            k = int(k)
            try:
                S_0, T, sigma = volatility_calc.volatility(source, symbol, m, n_1)
            except ValueError:
                ui.textEdit.setText("<font color=red>Failed to download. Please try the other data source.</font>")
            if num2==1:
                try:
                    c = european_dividend_yield.call(S_0, K, r, q, T, sigma, n, k)
                    ui.textEdit.setText("The price of the European call option is %.2f"%c)                           
                except ValueError:
                    ui.textEdit.setText("<font color=red>Error!</font>")
                    
            elif num2==2:
                try:
                    p = european_dividend_yield.put(S_0, K, r, q, T, sigma, n, k)
                    ui.textEdit.setText("The price of the European put option is %.2f"%p)                           
                except ValueError:
                    ui.textEdit.setText("<font color=red>Error!</font>")
    
    if num == 6:
        S_0 = ui.lineEdit.text()             
        K = ui.lineEdit_2.text()        
        r = ui.lineEdit_3.text()        
        T = ui.lineEdit_4.text()        
        sigma = ui.lineEdit_5.text()
        q = ui.lineEdit_6.text()
        n = ui.spinBox.text()
        k = ui.lineEdit_11.text()
        num2 = ui.comboBox_2.currentIndex()
        if S_0 == " " or K == " " or r == " " or T == " " or sigma == " " or q == " " or n ==" " or num2 ==0:
            showMessage()
        else:            
            S_0 = float(S_0)
            K = float(K)
            r = float(r)
            r = r/float(100)
            T = float(T)
            sigma = float(sigma)
            q = float(q)
            q = q/float(100)
            n =int(n)
            k = int(k)
            
            if num2==1:
                try:
                    c = european_dividend_yield.call(S_0, K, r, q, T, sigma, n, k)
                    ui.textEdit.setText("The price of the European call option is %.2f"%c)                           
                except ValueError:
                    ui.textEdit.setText("<font color=red>Error!</font>")
                    
            elif num2==2:
                try:
                    p = european_dividend_yield.put(S_0, K, r, q, T, sigma, n, k)
                    ui.textEdit.setText("The price of the European put option is %.2f"%p)                           
                except ValueError:
                    ui.textEdit.setText("<font color=red>Error!</font>")
                    
    if num == 7:
        K = ui.lineEdit_2.text()
        r = ui.lineEdit_3.text()
        m = ui.lineEdit_12.text()
        symbol = ui.lineEdit_9.text()
        n_1 = ui.lineEdit_8.text()
        n = ui.spinBox.value()        
        source = ui.comboBox.currentIndex()
        num2 = ui.comboBox_2.currentIndex()
        if K == " " or r == " " or m == " " or symbol==" " or n_1 == " " or n == " " or source ==0 or num2 ==0:
            showMessage()
        elif i < 2*n:
            ui.textEdit.setText("<font color=red>Please insert all dividend times and their corresponding dividends!</font>") 
        else:
            K = float(K)
            r = float(r)
            r = r/float(100)
            m = int(m)
            n_1 = int(n_1)
            n = int(n)
            
            try:
                S_0, T, sigma = volatility_calc.volatility(source, symbol, m, n_1)
            except ValueError:
                ui.textEdit.setText("<font color=red>Failed to download. Please try the other data source.</font>")
            if num2==1:
                try:
                    c = Bos_Vandermark.call(S_0, K, r, T, sigma, n)
                    ui.textEdit.setText("The price of the European call option is %.2f"%c)                           
                except ValueError:
                    ui.textEdit.setText("<font color=red>Error!</font>")
                    
            elif num2==2:
                try:
                    p = Bos_Vandermark.put(S_0, K, r, T, sigma, n)
                    ui.textEdit.setText("The price of the European put option is %.2f"%p)                           
                except ValueError:
                    ui.textEdit.setText("<font color=red>Error!</font>")
    
    if num == 8:
        S_0 = ui.lineEdit.text()             
        K = ui.lineEdit_2.text()        
        r = ui.lineEdit_3.text()        
        T = ui.lineEdit_4.text()        
        sigma = ui.lineEdit_5.text()
        n = ui.spinBox.value()
        num2 = ui.comboBox_2.currentIndex()
        if S_0 == " " or K == " " or r == " " or T == " " or sigma == " " or n == " " or num2 ==0:
            showMessage()
        elif i < 2*n:
            ui.textEdit.setText("<font color=red>Please insert all dividend times and their corresponding dividends!</font>")            
        else:            
            S_0 = float(S_0)
            K = float(K)
            r = float(r)
            r = r/float(100)
            T = float(T)
            sigma = float(sigma)
            n = int(n)
            if num2==1:
                try:
                    c = Bos_Vandermark.call(S_0, K, r, T, sigma,n)
                    ui.textEdit.setText("The price of the European call option is %.2f"%c)                           
                except ValueError:
                    ui.textEdit.setText("<font color=red>Error!</font>")
                    
            elif num2==2:
                try:
                    p = Bos_Vandermark.put(S_0, K, r, T, sigma,n)
                    ui.textEdit.setText("The price of the European put option is %.2f"%p)                           
                except ValueError:
                    ui.textEdit.setText("<font color=red>Error!</font>")
                    
def disable_button():
    global ui, num, S_0, K, r, T, sigma, num2
    num = ui.comboBox_5.currentIndex()
    if num == 0:        
        ui.lineEdit.show()    #current stock price
        ui.label.show()
        ui.label_4.show()     #duration
        ui.lineEdit_4.show()
        ui.label_5.show()     #volatility
        ui.lineEdit_5.show()
        ui.lineEdit_6.show()  #dividend yield
        ui.label_6.show()
        ui.lineEdit_7.show()  #time of dividend and dividends
        ui.label_7.show()
        ui.spinBox.show()     #number of dividends
        ui.label_10.show()
        ui.lineEdit_11.show() #number of binomial steps
        ui.label_11.show()        
        ui.label_12.show()    #maturity duty
        ui.lineEdit_12.show()
        ui.label_13.show()    #company symbol
        ui.lineEdit_9.show()
        ui.label_14.show()    #number of days of data
        ui.lineEdit_8.show()
        ui.comboBox.show()    #data source
        ui.label_15.show()
        ui.pushButton_4.show() # button for inserting dividend
        ui.pushButton.clicked.connect(check_input)
                
    elif num==1:
        ui.lineEdit.hide()    #current stock price
        ui.label.hide()
        ui.label_4.hide()     #duration
        ui.lineEdit_4.hide()
        ui.label_5.hide()     #volatility
        ui.lineEdit_5.hide()
        ui.lineEdit_6.hide()  #dividend yield
        ui.label_6.hide()
        ui.lineEdit_7.hide()  #time of dividend and dividends
        ui.label_7.hide()
        ui.spinBox.hide()    #number of dividends
        ui.label_10.hide()
        ui.lineEdit_11.hide() #number of binomial steps
        ui.label_11.hide()        
        ui.label_12.show()    #maturity duty
        ui.lineEdit_12.show()
        ui.label_13.show()    #company symbol
        ui.lineEdit_9.show()
        ui.label_14.show()    #number of days of data
        ui.lineEdit_8.show()
        ui.comboBox.show()    #data source
        ui.label_15.show()
        ui.pushButton.clicked.connect(check_input) 
        
    elif num==2:
        ui.lineEdit.show()    #current stock price
        ui.label.show()
        ui.label_4.show()     #duration
        ui.lineEdit_4.show()
        ui.label_5.show()     #volatility
        ui.lineEdit_5.show()
        ui.lineEdit_6.hide()  #dividend yield
        ui.label_6.hide()
        ui.lineEdit_7.hide()  #time of dividend and dividends
        ui.label_7.hide()
        ui.spinBox.hide() #number of dividends
        ui.label_10.hide()
        ui.lineEdit_11.hide() #number of binomial steps
        ui.label_11.hide()        
        ui.label_12.hide()    #maturity duty
        ui.lineEdit_12.hide()
        ui.label_13.hide()    #company symbol
        ui.lineEdit_9.hide()
        ui.label_14.hide()    #number of days of data
        ui.lineEdit_8.hide()
        ui.comboBox.hide()    #data source
        ui.label_15.hide()
        ui.pushButton.clicked.connect(check_input) 
               
    elif num==3:
        ui.lineEdit.hide()    #current stock price
        ui.label.hide()
        ui.label_4.hide()     #duration
        ui.lineEdit_4.hide()
        ui.label_5.hide()     #volatility
        ui.lineEdit_5.hide()
        ui.lineEdit_6.show()  #dividend yield
        ui.label_6.show()
        ui.lineEdit_7.hide()  #time of dividend and dividends
        ui.label_7.hide()
        ui.spinBox.show() #number of dividends
        ui.label_10.show()
        ui.lineEdit_11.hide() #number of binomial steps
        ui.label_11.hide()        
        ui.label_12.show()    #maturity duty
        ui.lineEdit_12.show()
        ui.label_13.show()    #company symbol
        ui.lineEdit_9.show()
        ui.label_14.show()    #number of days of data
        ui.lineEdit_8.show()
        ui.comboBox.show()    #data source
        ui.label_15.show()
        ui.pushButton.clicked.connect(check_input) 
        
    elif num==4:
        ui.lineEdit.show()    #current stock price
        ui.label.show()
        ui.label_4.show()     #duration
        ui.lineEdit_4.show()
        ui.label_5.show()     #volatility
        ui.lineEdit_5.show()
        ui.lineEdit_6.show()  #dividend yield
        ui.label_6.show()
        ui.lineEdit_7.hide()  #time of dividend and dividends
        ui.label_7.hide()
        ui.spinBox.show() #number of dividends
        ui.label_10.show()
        ui.lineEdit_11.hide() #number of binomial steps
        ui.label_11.hide()        
        ui.label_12.hide()    #maturity duty
        ui.lineEdit_12.hide()
        ui.label_13.hide()    #company symbol
        ui.lineEdit_9.hide()
        ui.label_14.hide()    #number of days of data
        ui.lineEdit_8.hide()
        ui.comboBox.hide()    #data source
        ui.label_15.hide()
        ui.pushButton.clicked.connect(check_input) 
        
    elif num==5:
        ui.lineEdit.hide()    #current stock price
        ui.label.hide()
        ui.label_4.hide()     #duration
        ui.lineEdit_4.hide()
        ui.label_5.hide()     #volatility
        ui.lineEdit_5.hide()
        ui.lineEdit_6.show()  #dividend yield
        ui.label_6.show()
        ui.lineEdit_7.hide()  #time of dividend and dividends
        ui.label_7.hide()
        ui.spinBox.show() #number of dividends
        ui.label_10.show()
        ui.lineEdit_11.show() #number of binomial steps
        ui.label_11.show()        
        ui.label_12.show()    #maturity duty
        ui.lineEdit_12.show()
        ui.label_13.show()    #company symbol
        ui.lineEdit_9.show()
        ui.label_14.show()    #number of days of data
        ui.lineEdit_8.show()
        ui.comboBox.show()    #data source
        ui.label_15.show()
        ui.pushButton.clicked.connect(check_input) 
        
    elif num==6:
        ui.lineEdit.show()    #current stock price
        ui.label.show()
        ui.label_4.show()     #duration
        ui.lineEdit_4.show()
        ui.label_5.show()     #volatility
        ui.lineEdit_5.show()
        ui.lineEdit_6.show()  #dividend yield
        ui.label_6.show()
        ui.lineEdit_7.hide()  #time of dividend and dividends
        ui.label_7.hide()
        ui.spinBox.show() #number of dividends
        ui.label_10.show()
        ui.lineEdit_11.show() #number of binomial steps
        ui.label_11.show()        
        ui.label_12.hide()    #maturity duty
        ui.lineEdit_12.hide()
        ui.label_13.hide()    #company symbol
        ui.lineEdit_9.hide()
        ui.label_14.hide()    #number of days of data
        ui.lineEdit_8.hide()
        ui.comboBox.hide()    #data source
        ui.label_15.hide()
        ui.pushButton.clicked.connect(check_input)
        
    elif num==7:
        ui.lineEdit.hide()    #current stock price
        ui.label.hide()
        ui.label_4.hide()     #duration
        ui.lineEdit_4.hide()
        ui.label_5.hide()     #volatility
        ui.lineEdit_5.hide()
        ui.lineEdit_6.hide()  #dividend yield
        ui.label_6.hide()
        ui.lineEdit_7.show()  #time of dividend and dividends
        ui.label_7.show()
        ui.spinBox.show()    #number of dividends
        ui.label_10.show()
        ui.lineEdit_11.hide() #number of binomial steps
        ui.label_11.hide()        
        ui.label_12.show()    #maturity duty
        ui.lineEdit_12.show()
        ui.label_13.show()    #company symbol
        ui.lineEdit_9.show()
        ui.label_14.show()    #number of days of data
        ui.lineEdit_8.show()
        ui.comboBox.show()    #data source
        ui.label_15.show()
        ui.spinBox.valueChanged.connect(take_div)
        ui.pushButton.clicked.connect(check_input) 
        
    elif num==8:
        ui.lineEdit.show()    #current stock price
        ui.label.show()
        ui.label_4.show()     #duration
        ui.lineEdit_4.show()
        ui.label_5.show()     #volatility
        ui.lineEdit_5.show()
        ui.lineEdit_6.hide()  #dividend yield
        ui.label_6.hide()
        ui.lineEdit_7.show()  #time of dividend and dividends
        ui.label_7.show()
        ui.spinBox.show() #number of dividends
        ui.label_10.show()
        ui.lineEdit_11.hide() #number of binomial steps
        ui.label_11.hide()        
        ui.label_12.hide()    #maturity duty
        ui.lineEdit_12.hide()
        ui.label_13.hide()    #company symbol
        ui.lineEdit_9.hide()
        ui.label_14.hide()    #number of days of data
        ui.lineEdit_8.hide()
        ui.comboBox.hide()    #data source
        ui.label_15.hide()
        ui.spinBox.valueChanged.connect(take_div)
        ui.pushButton.clicked.connect(check_input) 
        
    elif num==9:
        ui.lineEdit.hide()    #current stock price
        ui.label.hide()
        ui.label_4.hide()     #duration
        ui.lineEdit_4.hide()
        ui.label_5.hide()     #volatility
        ui.lineEdit_5.hide()
        ui.lineEdit_6.hide()  #dividend yield
        ui.label_6.hide()
        ui.lineEdit_7.show()  #time of dividend and dividends
        ui.label_7.show()
        ui.spinBox.show() #number of dividends
        ui.label_10.show()
        ui.lineEdit_11.show() #number of binomial steps
        ui.label_11.show()        
        ui.label_12.show()    #maturity duty
        ui.lineEdit_12.show()
        ui.label_13.show()    #company symbol
        ui.lineEdit_9.show()
        ui.label_14.show()    #number of days of data
        ui.lineEdit_8.show()
        ui.comboBox.show()    #data source
        ui.label_15.show()
        ui.pushButton.clicked.connect(check_input) 
        
    elif num==10:
        ui.lineEdit.show()    #current stock price
        ui.label.show()
        ui.label_4.show()     #duration
        ui.lineEdit_4.show()
        ui.label_5.show()     #volatility
        ui.lineEdit_5.show()
        ui.lineEdit_6.hide()  #dividend yield
        ui.label_6.hide()
        ui.lineEdit_7.show()  #time of dividend and dividends
        ui.label_7.show()
        ui.spinBox.show() #number of dividends
        ui.label_10.show()
        ui.lineEdit_11.show() #number of binomial steps
        ui.label_11.show()        
        ui.label_12.hide()    #maturity duty
        ui.lineEdit_12.hide()
        ui.label_13.hide()    #company symbol
        ui.lineEdit_9.hide()
        ui.label_14.hide()    #number of days of data
        ui.lineEdit_8.hide()
        ui.comboBox.hide()    #data source
        ui.label_15.hide()
        ui.pushButton.clicked.connect(check_input) 
        
    elif num==11:
        ui.lineEdit.hide()    #current stock price
        ui.label.hide()
        ui.label_4.hide()     #duration
        ui.lineEdit_4.hide()
        ui.label_5.hide()     #volatility
        ui.lineEdit_5.hide()
        ui.lineEdit_6.hide()  #dividend yield
        ui.label_6.hide()
        ui.lineEdit_7.hide()  #time of dividend and dividends
        ui.label_7.hide()
        ui.spinBox.hide() #number of dividends
        ui.label_10.hide()
        ui.lineEdit_11.show() #number of binomial steps
        ui.label_11.show()        
        ui.label_12.show()    #maturity duty
        ui.lineEdit_12.show()
        ui.label_13.show()    #company symbol
        ui.lineEdit_9.show()
        ui.label_14.show()    #number of days of data
        ui.lineEdit_8.show()
        ui.comboBox.show()    #data source
        ui.label_15.show()
        ui.pushButton.clicked.connect(check_input) 
        
    elif num==12:
        ui.lineEdit.show()    #current stock price
        ui.label.show()
        ui.label_4.show()     #duration
        ui.lineEdit_4.show()
        ui.label_5.show()     #volatility
        ui.lineEdit_5.show()
        ui.lineEdit_6.hide()  #dividend yield
        ui.label_6.hide()
        ui.lineEdit_7.hide()  #time of dividend and dividends
        ui.label_7.hide()
        ui.spinBox.hide() #number of dividends
        ui.label_10.hide()
        ui.lineEdit_11.show() #number of binomial steps
        ui.label_11.show()        
        ui.label_12.hide()    #maturity duty
        ui.lineEdit_12.hide()
        ui.label_13.hide()    #company symbol
        ui.lineEdit_9.hide()
        ui.label_14.hide()    #number of days of data
        ui.lineEdit_8.hide()
        ui.comboBox.hide()    #data source
        ui.label_15.hide()
        ui.pushButton.clicked.connect(check_input) 
        
    elif num==13:
        ui.lineEdit.hide()    #current stock price
        ui.label.hide()
        ui.label_4.hide()     #duration
        ui.lineEdit_4.hide()
        ui.label_5.hide()     #volatility
        ui.lineEdit_5.hide()
        ui.lineEdit_6.show()  #dividend yield
        ui.label_6.show()
        ui.lineEdit_7.hide()  #time of dividend and dividends
        ui.label_7.hide()
        ui.spinBox.hide() #number of dividends
        ui.label_10.hide()
        ui.lineEdit_11.hide() #number of binomial steps
        ui.label_11.hide()        
        ui.label_12.show()    #maturity duty
        ui.lineEdit_12.show()
        ui.label_13.show()    #company symbol
        ui.lineEdit_9.show()
        ui.label_14.show()    #number of days of data
        ui.lineEdit_8.show()
        ui.comboBox.show()    #data source
        ui.label_15.show()
        ui.pushButton.clicked.connect(check_input) 
        
    elif num==14:
        ui.lineEdit.show()    #current stock price
        ui.label.show()
        ui.label_4.show()     #duration
        ui.lineEdit_4.show()
        ui.label_5.show()     #volatility
        ui.lineEdit_5.show()
        ui.lineEdit_6.show()  #dividend yield
        ui.label_6.show()
        ui.lineEdit_7.hide()  #time of dividend and dividends
        ui.label_7.hide()
        ui.spinBox.hide() #number of dividends
        ui.label_10.hide()
        ui.lineEdit_11.hide() #number of binomial steps
        ui.label_11.hide()        
        ui.label_12.hide()    #maturity duty
        ui.lineEdit_12.hide()
        ui.label_13.hide()    #company symbol
        ui.lineEdit_9.hide()
        ui.label_14.hide()    #number of days of data
        ui.lineEdit_8.hide()
        ui.comboBox.hide()    #data source
        ui.label_15.hide()
        ui.pushButton.clicked.connect(check_input) 
        
    elif num==15:
        ui.lineEdit.hide()    #current stock price
        ui.label.hide()
        ui.label_4.hide()     #duration
        ui.lineEdit_4.hide()
        ui.label_5.hide()     #volatility
        ui.lineEdit_5.hide()
        ui.lineEdit_6.hide()  #dividend yield
        ui.label_6.hide()
        ui.lineEdit_7.show()  #time of dividend and dividends
        ui.label_7.show()
        ui.spinBox.show() #number of dividends
        ui.label_10.show()
        ui.lineEdit_11.show() #number of binomial steps
        ui.label_11.show()        
        ui.label_12.show()    #maturity duty
        ui.lineEdit_12.show()
        ui.label_13.show()    #company symbol
        ui.lineEdit_9.show()
        ui.label_14.show()    #number of days of data
        ui.lineEdit_8.show()
        ui.comboBox.show()    #data source
        ui.label_15.show()
        ui.pushButton.clicked.connect(check_input) 
        
    else:
        ui.lineEdit.show()    #current stock price
        ui.label.show()
        ui.label_4.show()     #duration
        ui.lineEdit_4.show()
        ui.label_5.show()     #volatility
        ui.lineEdit_5.show()
        ui.lineEdit_6.hide()  #dividend yield
        ui.label_6.hide()
        ui.lineEdit_7.show()  #time of dividend and dividends
        ui.label_7.show()
        ui.spinBox.show() #number of dividends
        ui.label_10.show()
        ui.lineEdit_11.show() #number of binomial steps
        ui.label_11.show()        
        ui.label_12.hide()    #maturity duty
        ui.lineEdit_12.hide()
        ui.label_13.hide()    #company symbol
        ui.lineEdit_9.hide()
        ui.label_14.hide()    #number of days of data
        ui.lineEdit_8.hide()
        ui.comboBox.hide()    #data source
        ui.label_15.hide()
        ui.pushButton.clicked.connect(check_input) 
        
def main():
    global ui
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = PVOPT.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()    
    ui.actionExit.triggered.connect(sys.exit)
    ui.comboBox_5.activated.connect(disable_button)    
    sys.exit(app.exec_())
           
               
if __name__ == "__main__":
    main()
 


