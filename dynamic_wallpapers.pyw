import os
import datetime
import ctypes
import schedule
import time

path  = 'D:\\Python scripts\\Dynamic_Wallpaper\\Wallpapers\\MacOS Big Sur '

def changeBG(wall):
    ctypes.windll.user32.SystemParametersInfoW(20,0,path+ wall +'.png',3)

if __name__ == '__main__':
    now = datetime.datetime.now()
    hour =  now.hour
    if ((hour >=19) & (hour <= 23)) or ((hour >=0) & (hour <=4)):
        changeBG('8')
    elif hour == 5:
        changeBG('1')
    elif (hour>=6) & (hour <=8):
        changeBG('2')
    elif (hour>=9) & (hour <=11):
        changeBG('3')
    elif (hour >= 12) & (hour <=15):
        changeBG('4')
    elif hour == 16:
        changeBG('5')
    elif hour == 17:
        changeBG('6')
    elif hour == 18:
        changeBG('7')
    

    schedule.every().day.at("19:40").do(changeBG,'8')
    schedule.every().day.at("05:00").do(changeBG,'1')
    schedule.every().day.at("06:00").do(changeBG,'2')
    schedule.every().day.at("09:00").do(changeBG,'3')
    schedule.every().day.at("12:00").do(changeBG,'4')
    schedule.every().day.at("16:00").do(changeBG,'5')
    schedule.every().day.at("17:00").do(changeBG,'6')
    schedule.every().day.at("18:00").do(changeBG,'7')

    while True:
        schedule.run_pending()
        time.sleep(1)