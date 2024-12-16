import datetime as dt  # datetime 모듈
import tkinter as tk  # tkinter 모듈
import winsound  # winsound 모듈

# 스누즈 관련 설정
SNOOZE_INTERVAL = 60  # 스누즈 간격 (초)

# 알람 상태 관리
alarm_active = False  # 알람이 현재 울리는 상태인지 여부

# GUI 설정
time_program = tk.Tk()
time_program.title("Digital Clock")  # GUI창 이름
time_program.geometry("460x200")  # GUI창 크기


def clock():  # 시간을 나타내는 함수
    now = dt.datetime.now()  # 현재 시간을 가져옴
    time1 = "{}년 {}월 {}일".format(now.year, now.month, now.day)  # 날짜
    time2 = "{} {}시 {}분 {}초".format(
        now.strftime('%p'), now.strftime('%I'), now.minute, now.second
    )  # 시간
    interface_time1.config(text=time1)  # 날짜 출력
    interface_time2.config(text=time2)  # 시간 출력
    time_program.after(1000, clock)  # 1초마다 clock 함수 실행


def ring():  # 알람 울리기
    global alarm_active
    alarm_active = True  # 알람 활성화
    sol = {'do': 261, 're': 293, 'mi': 329, 'pa': 349, 'sol': 391}
    mel = ['do', 're', 'mi', 'pa', 'sol', 'sol', 'sol']
    for melody in mel:
        winsound.Beep(sol[melody], 500)  # 알람 소리
    interface_alarmset1.config(bg='yellow')  # 배경색 변경
    time_program.after(SNOOZE_INTERVAL * 1000, snooze_check)  # 스누즈 체크


def snooze_check():  # 알람 스누즈 상태 확인
    if alarm_active:  # 알람이 꺼지지 않았다면
        ring()  # 다시 알람 울리기


def Alarm_set():  # 알람 시간 설정
    global alarm_hour, alarm_min, alarm_sec
    try:
        alarm_hour = int(hour_entry.get())
        alarm_min = int(min_entry.get())
        alarm_sec = int(sec_entry.get())

        # 입력값 검증
        if not (0 <= alarm_hour < 24 and 0 <= alarm_min < 60 and 0 <= alarm_sec < 60):
            raise ValueError("Invalid time input")

        alarm_time = dt.time(alarm_hour, alarm_min, alarm_sec)
        interface_alarmset1.config(
            text=f"{alarm_time.strftime('%I')}시 {alarm_min}분 {alarm_sec}초", bg="white"
        )
        Alarm_ex()  # 알람 실행
    except ValueError:
        interface_alarmset1.config(text="유효하지 않은 시간입니다.", bg="red")


def Alarm_ex():  # 알람 기능 실행
    global alarm_active
    if time_check() and not alarm_active:  # 알람 시간이 되었고, 알람이 울리지 않은 상태라면
        ring()  # 알람 울리기
    time_program.after(1000, Alarm_ex)  # 1초마다 다시 실행


def time_check():  # 현재 시간과 알람 시간 비교
    now = dt.datetime.now()
    return now.hour == int(alarm_hour) and now.minute == int(alarm_min) and now.second == int(alarm_sec)


def Alarm_del():  # 알람 취소
    global alarm_active
    alarm_active = False  # 알람 비활성화
    interface_alarmset1.config(text=" ", bg=time_program.cget('bg'))  # 화면 초기화


# GUI 구성
interface_time1 = tk.Label(font=(100), width=50)  # 날짜 출력
interface_time1.place(x=0, y=0)

interface_time2 = tk.Label(font=(100), width=50)  # 시간 출력
interface_time2.place(x=0, y=20)

interface_alarm = tk.Label(font=(100), text='시    분    초  ', width=50)  # 알람 입력 안내
interface_alarm.place(x=0, y=40)

hour_entry = tk.Entry(width=2)  # 알람 시 입력
hour_entry.place(x=180, y=66)

min_entry = tk.Entry(width=2)  # 알람 분 입력
min_entry.place(x=215, y=66)

sec_entry = tk.Entry(width=2)  # 알람 초 입력
sec_entry.place(x=250, y=66)

alarm_but = tk.Button(text='알람 설정', bg='skyblue', command=Alarm_set)  # 알람 설정 버튼
alarm_but.place(x=160, y=100)

alarm_but2 = tk.Button(text='알람 취소', bg='red', command=Alarm_del)  # 알람 취소 버튼
alarm_but2.place(x=230, y=100)

interface_alarmset1 = tk.Label(font=(100), text=' ', width=50)  # 알람 설정 상태 출력
interface_alarmset1.place(x=0, y=130)

# 실행
clock()
time_program.mainloop()



