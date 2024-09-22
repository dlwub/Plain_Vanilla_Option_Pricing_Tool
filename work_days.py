import datetime, time
import math
#Calculates number of work days between two dates (the first date inclusive and the second date exclusive) based on U.S public holidays
def work_days(date_1,date_2):
    date_1 = str(date_1)
    date_2 = str(date_2)    
    start = date_1    
    end = date_2
    date_1 = datetime.datetime(int(date_1[0:4]),int(date_1[4:6]),int(date_1[6:8]))
    date_1 = time.mktime(date_1.timetuple()) #Converting it to seconds
    date_2 = datetime.datetime(int(date_2[0:4]),int(date_2[4:6]),int(date_2[6:8]))
    date_2 = time.mktime(date_2.timetuple())
    days_bn = round((date_2-date_1)/(24*3600),0)
    k,r = divmod(days_bn, 7)    
    #Checks if there is Sunday or Saturday in the last r days (by symmetry it is the same as checking for a weekend day in the first r days starting from the starting date
    z = int(datetime.datetime(int(start[0:4]),int(start[4:6]),int(start[6:8])).strftime('%w')) # The weekday of the start date
    week_ends = 0
    if r == 0:
        week_ends = 0        
    elif z == 0:
        week_ends = 1        
    elif z+r <7:
        week_ends = 0        
    elif z+r==7:
        week_ends = 1        
    elif z+r > 7:
        week_ends = 2
        
    holiday=0
    holiday_0 = []
    holiday_1 = []
    if start[0:4]!= end[0:4]:
        #New year,July 4,Christmas
        holiday_2 = [start[0:4]+'0101',start[0:4]+'0704',start[0:4]+'1225',end[0:4]+'0101',end[0:4]+'0704',end[0:4]+'1225']
        i=0
        while i < len(holiday_2):            
            if int(start)<= int(holiday_2[i])< int(end):  #Checks if the date is between the start date and the end date and adds it to the list if it is so
                x = int(datetime.datetime(int(holiday_2[i][0:4]),int(holiday_2[i][4:6]),int(holiday_2[i][6:8])).strftime('%w')) #Gets the weekday
                if x!=0 and x!=6: #Checks if the date is not on Saturday or Sunday and adds it to the holiday
                    holiday = holiday+1
            i=i+1        
        #Thanks giving,Third Monday of Jan, Third Monday of Feb, Last Monday of May,First Monday of September 
        holiday_3 = [start[0:4]+'1122',end[0:4]+'1122', start[0:4]+'0115',end[0:4]+'0115',start[0:4]+'0215',end[0:4]+'0215',start[0:4]+'0525',end[0:4]+'0525',start[0:4]+'0901',end[0:4]+'0901']
        y = int(datetime.datetime(int(holiday_3[0][0:4]),int(holiday_3[0][4:6]),int(holiday_3[0][6:8])).strftime('%w'))
        if y <=4:
                     z=26-y
                     holiday_0.append(start[0:4]+'11'+str(z))
        else:
                     z=33-y
                     holiday_0.append(start[0:4]+'11'+str(z))
                     
        y = int(datetime.datetime(int(holiday_3[1][0:4]),int(holiday_3[1][4:6]),int(holiday_3[1][6:8])).strftime('%w'))
        if y <=4:
                     z=26-y
                     holiday_0.append(end[0:4]+'11'+str(z))
        else:
                     z=33-y
                     holiday_0.append(end[0:4]+'11'+str(z))

        y = int(datetime.datetime(int(holiday_3[2][0:4]),int(holiday_3[2][4:6]),int(holiday_3[2][6:8])).strftime('%w'))
        if y <=1:
                     z=16-y
                     holiday_0.append(start[0:4]+'01'+str(z))
        else:
                     z=23-y
                     holiday_0.append(start[0:4]+'01'+str(z))

        y = int(datetime.datetime(int(holiday_3[3][0:4]),int(holiday_3[3][4:6]),int(holiday_3[3][6:8])).strftime('%w'))
        if y <=1:
                     z=16-y
                     holiday_0.append(end[0:4]+'01'+str(z))
        else:
                     z=23-y
                     holiday_0.append(end[0:4]+'01'+str(z))     
    
        y = int(datetime.datetime(int(holiday_3[4][0:4]),int(holiday_3[4][4:6]),int(holiday_3[4][6:8])).strftime('%w'))
        if y <=1:
                     z=16-y
                     holiday_0.append(start[0:4]+'02'+str(z))
        else:
                     z=23-y
                     holiday_0.append(start[0:4]+'02'+str(z))
                     
        y = int(datetime.datetime(int(holiday_3[5][0:4]),int(holiday_3[5][4:6]),int(holiday_3[5][6:8])).strftime('%w'))
        if y <=1:
                     z=16-y
                     holiday_0.append(end[0:4]+'02'+str(z))
        else:
                     z=23-y
                     holiday_0.append(end[0:4]+'02'+str(z))

        y = int(datetime.datetime(int(holiday_3[6][0:4]),int(holiday_3[6][4:6]),int(holiday_3[6][6:8])).strftime('%w'))
        if y <=1:
                     z=26-y
                     holiday_0.append(start[0:4]+'05'+str(z))
        else:
                     z=33-y
                     holiday_0.append(start[0:4]+'05'+str(z))

        y = int(datetime.datetime(int(holiday_3[7][0:4]),int(holiday_3[7][4:6]),int(holiday_3[7][6:8])).strftime('%w'))
        if y <=1:
                     z=26-y
                     holiday_0.append(end[0:4]+'05'+str(z))
        else:
                     z=33-y
                     holiday_0.append(end[0:4]+'05'+str(z))
        
        y = int(datetime.datetime(int(holiday_3[8][0:4]),int(holiday_3[8][4:6]),int(holiday_3[8][6:8])).strftime('%w'))
        if y <=1:
                z=2-y
                z=str(z)
                holiday_0.append(start[0:4]+'09'+str(z.zfill(2)))
        else:
                z=9-y
                z=str(z)
                holiday_0.append(start[0:4]+'09'+str(z.zfill(2)))
            
        y = int(datetime.datetime(int(holiday_3[9][0:4]),int(holiday_3[9][4:6]),int(holiday_3[9][6:8])).strftime('%w'))
        if y <=1:
                     z=2-y
                     z=str(z)
                     holiday_0.append(end[0:4]+'09'+str(z.zfill(2)))
        else:
                     z=9-y
                     z=str(z)
                     holiday_0.append(end[0:4]+'09'+str(z.zfill(2)))           
        
        #Checking if elements of holiday_0 are in between the start and the end date
        i=0
        while i <len(holiday_0):
            if int(start)<=int(holiday_0[i])< int(end):
                holiday=holiday+1
            i=i+1

        # Good Friday calculation
        q_0, a_0 = divmod(int(start[0:4]),19)
        q_0, a_1 = divmod(int(end[0:4]),19)
        b_0, c_0 = divmod(int(start[0:4]),100)
        b_1, c_1 = divmod(int(end[0:4]),100)        
        d_0, e_0 = divmod(b_0,4)
        d_1, e_1 = divmod(b_1,4)
        f_0, r_0 = divmod((b_0 + 8),25)
        f_1, r_0 = divmod((b_1 + 8),25)
        g_0, r_0 = divmod((b_0 - f_0 + 1),3)
        g_1, r_0 = divmod((b_1 - f_1 + 1),3)
        q_0, h_0 = divmod((19*a_0 + b_0 - d_0 -g_0 + 15),30)
        q_0, h_1 = divmod((19*a_1 + b_1 - d_1 -g_1 + 15),30)
        i_0, k_0 = divmod(c_0,4)
        i_1, k_1 = divmod(c_1,4)
        q_0, l_0 = divmod((32 + 2*e_0 + 2*i_0 - h_0 - k_0),7)
        q_0, l_1 = divmod((32 + 2*e_1 + 2*i_1 - h_1 - k_1),7)
        m_0, r_0 = divmod((a_0 + 11*h_0 + 22*l_0),451)
        m_1, r_0 = divmod((a_1 + 11*h_1 + 22*l_1),451)
        mo_0, r_0 = divmod((h_0 + l_0 - 7*m_0 + 114),31)
        mo_1, r_0 = divmod((h_1 + l_1 - 7*m_1 + 114),31)
        q_0, p_0 = divmod((h_0 + l_0 -7*m_0 +114),31)
        q_0, p_1 = divmod((h_1 + l_1 -7*m_1 +114),31)
        x_0 = str(mo_0)
        x_1 = str(mo_1)
        y_0 = str(p_0 -1)
        y_1 = str(p_1 -1)
        holiday_1.append(start[0:4]+str(x_0.zfill(2))+str(y_0.zfill(2)))
        holiday_1.append(end[0:4]+str(x_1.zfill(2))+str(y_1.zfill(2)))
        i=0
        while i <len(holiday_1):
            if int(start)<=int(holiday_1[i])< int(end):
                holiday=holiday+1
            i=i+1       
                
    else:
        holiday_2 = [start[0:4]+'0101',start[0:4]+'0704',start[0:4]+'1225']
        i=0
        while i < len(holiday_2):
            if int(start)<= int(holiday_2[i])< int(end):
                x = int(datetime.datetime(int(holiday_2[i][0:4]),int(holiday_2[i][4:6]),int(holiday_2[i][6:8])).strftime('%w'))
                if x!=0 and x!=6:
                    holiday = holiday+1               
            i=i+1       
    
        holiday_3 =  [start[0:4]+'1122',start[0:4]+'0115',start[0:4]+'0215',start[0:4]+'0525',start[0:4]+'0901']
        y = int(datetime.datetime(int(holiday_3[0][0:4]),int(holiday_3[0][4:6]),int(holiday_3[0][6:8])).strftime('%w'))
        if y <=4:
            z=26-y
            holiday_0.append(start[0:4]+'11'+str(z))
        else:
            z=33-y
            holiday_0.append(start[0:4]+'11'+str(z))
        y = int(datetime.datetime(int(holiday_3[1][0:4]),int(holiday_3[1][4:6]),int(holiday_3[1][6:8])).strftime('%w'))
        if y <=1:
            z=16-y
            holiday_0.append(start[0:4]+'01'+str(z))
        else:
            z=23-y
            holiday_0.append(start[0:4]+'01'+str(z))
        y = int(datetime.datetime(int(holiday_3[2][0:4]),int(holiday_3[2][4:6]),int(holiday_3[2][6:8])).strftime('%w'))
        if y <=1:
            z=16-y
            holiday_0.append(start[0:4]+'02'+str(z))
        else:
            z=23-y
            holiday_0.append(start[0:4]+'02'+str(z))
        y = int(datetime.datetime(int(holiday_3[3][0:4]),int(holiday_3[3][4:6]),int(holiday_3[3][6:8])).strftime('%w'))
        if y <=1:
            z=26-y
            holiday_0.append(start[0:4]+'05'+str(z))
        else:
            z=33-y
            holiday_0.append(start[0:4]+'05'+str(z))
        y = int(datetime.datetime(int(holiday_3[4][0:4]),int(holiday_3[4][4:6]),int(holiday_3[4][6:8])).strftime('%w'))
        if y <=1:
            z=2-y
            z=str(z)
            holiday_0.append(start[0:4]+'09'+str(z.zfill(2)))
        else:
            z=9-y
            z=str(z)
            holiday_0.append(start[0:4]+'09'+str(z.zfill(2))) #zero-padding in the date       
                        
        
    #Checking if elements of holiday_0 are in between the start and the end date
        i=0
        while i <len(holiday_0):
            if int(start)<=int(holiday_0[i])< int(end):
                holiday=holiday+1
            i=i+1

    # Good Friday calculation
        q_0, a_0 = divmod(int(start[0:4]),19)        
        b_0, c_0 = divmod(int(start[0:4]),100)               
        d_0, e_0 = divmod(b_0,4)        
        f_0, r_0 = divmod((b_0 + 8),25)        
        g_0, r_0 = divmod((b_0 - f_0 + 1),3)        
        q_0, h_0 = divmod((19*a_0 + b_0 - d_0 -g_0 + 15),30)        
        i_0, k_0 = divmod(c_0,4)        
        q_0, l_0 = divmod((32 + 2*e_0 + 2*i_0 - h_0 - k_0),7)        
        m_0, r_0 = divmod((a_0 + 11*h_0 + 22*l_0),451)        
        mo_0, r_0 = divmod((h_0 + l_0 - 7*m_0 + 114),31)        
        q_0, p_0 = divmod((h_0 + l_0 -7*m_0 +114),31)        
        x_0 = str(mo_0)        
        y_0 = str(p_0 -1)        
        holiday_1.append(start[0:4]+str(x_0.zfill(2))+str(y_0.zfill(2)))
        if int(start)<=int(holiday_1[0])< int(end):
            holiday=holiday+1
            
    work_days = days_bn - 2*k - week_ends - holiday
    return work_days


    


