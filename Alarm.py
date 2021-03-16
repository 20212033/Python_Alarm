import datetime as dt # datetime 모듈
import time           # time 모듈
import tkinter as tk  # tkinter 모듈
import winsound       # winsound 모듈



time_program = tk.Tk()
time_program.title("Digital Clock") # GUI창 이름
time_program.geometry("460x200")    # GUI창 크기


def clock():  # 시간을 나타내는 함수
    now = dt.datetime.now() # 지금 시간을 now에 받는다
    time1 = ("{}년 {}월 {}일".format(now.year, now.month, now.day)) # 년, 월, 일을 출력한다
    time2 = ("{} {}시 {}분 {}초".format(now.strftime('%p'), now.strftime('%I'), now.minute, now.second)) # AMorPM 시, 분 초를 출력한다
    interface_time1.config(text = time1, ) # 미리 만들어둔 라벨에 값을 바꿔주어 화면에 출력시킨다
    interface_time2.config(text = time2, ) # 미리 만들어둔 라벨에 값을 바꿔주어 화면에 출력시킨다
    time_program.after(1000,clock) # 1초마다 clock 함수를 실행시킨다

def ring(): # 알람 시간이 적중했을 때 소리와 배경색을 바꿔주는 함수
    sol = {'do':261, 're':293, 'mi':329, 'pa':349, 'sol':391}

    mel = ['do','re','mi','pa','sol','sol','sol']
    dur = [1,1,1,1,1,1,1]

    music = zip(mel,dur)
    for melody, duration in music:
        winsound.Beep(sol[melody],1000)  # 도,레,미,파,솔,솔,솔 소리를 1초씩 낸다
    interface_alarmset1.config(bg = 'yellow') # 미리 만들어둔 라벨의 배경색을 노란색으로 바꿔준다
        
    

def Alarm_set(): # 엔트리에 입력받은 시간을 저장하는 함수
    
     global alarm_hour # 알람 시
     alarm_hour = hour_entry.get()
     global alarm_min  # 알람 분 
     alarm_min = min_entry.get()
     global alarm_sec  # 알람 초
     alarm_sec = sec_entry.get()

     alarm_time = dt.time(int(alarm_hour), int(alarm_min), int(alarm_sec))  # 시간으로 설정
     
     interface_alarmset1.config(text = '{}시 {}분 {}초'.format(alarm_time.strftime('%I'),alarm_min,alarm_sec)) # 미리 만들어둔 라벨에 값을 바꾸어 알람시간을 출력시킨다
     Alarm_ex()



def Alarm_ex(): # 알람 기능을 실행하는 함수
    

    check = time_check()
    if(check == 1): 
        ring()  # 소리를 울린다
    time_program.after(1000,Alarm_ex) # 1초마다 Alarm_ex 함수를 실행시킨다

    
def time_check(): # 알람 시간과 현재 시간이 같으면 1을 반환하는 함수
    now = dt.datetime.now() #현재 시간을 받는다
    now_time = dt.time(now.hour, now.minute, now.second) # 현재 시간을 now_time에 시,분,초로 저장한다
    
    alarm_time = dt.time(int(alarm_hour), int(alarm_min), int(alarm_sec)) # 알람 시간을 alarm_time에 저장한다
    
    if(alarm_time == now_time): # 현재 시간과 알람시간이 같으면
        flag = 1  # flag를 1로 설정한다
    else:
        flag = 0  
    return flag   # flag를 0으로 설정한다

  
def Alarm_del(): # 알람 삭제 기능
    interface_alarmset1.config(text = ' ', bg = time_program.cget('bg'))
    
    
interface_time1 = tk.Label(font = (100), width = 50) # 년, 월, 일을 출력하는 라벨
interface_time1.place(x = 0, y= 0)

interface_time2 = tk.Label(font = (100), width = 50) # 시간, 분, 초를 출력하는 라벨 
interface_time2.place(x = 0, y = 20)

interface_alarm = tk.Label(font = (100), text = '시    분    초  ', width = 50) # 시, 분 ,초 텍스트를 출력하는 라
interface_alarm.place(x = 0, y = 40)
  
hour_entry = tk.Entry(width = 2)  # 알람기능에서 시간을 입력받는 엔트리
hour_entry.place(x = 180, y = 66)

min_entry = tk.Entry(width = 2) # 알람기능에서 분을 입력받는 엔트리
min_entry.place(x = 215, y = 66)

sec_entry = tk.Entry(width = 2) # 알람기능에서 초를 입력받는 엔트리
sec_entry.place(x = 250, y = 66)

alarm_but = tk.Button(text='알람 설정', bg ='skyblue', command = Alarm_set) # 알람 설정 버튼
alarm_but.place(x = 160, y =100 )
alarm_but2 = tk.Button(text='알람 취소', bg ='red', command = Alarm_del) # 알람 취소 버튼
alarm_but2.place(x = 230, y =100)

interface_alarmset1 = tk.Label(font = (100), text = ' ', width = 50) # 알람 시간을 출력하는 라벨
interface_alarmset1.place(x = 0, y = 130)



clock()

time_program.mainloop()


