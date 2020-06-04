from time import sleep
import time
import requests

#telegram bot_id and chat_id
bot_token=''
chat_id=''

#課堂內容(你看看延平多痛苦（誤)
cls=[[['物理'],['物理'],['英文'],['英文'],['歷史'],['公民'],['數學'],['數學'],['放學']],
     [['數學'],['公民'],['體育'],['英文'],['美術'],['美術'],['國文'],['放學'],['放學']],
     [['國文'],['數學'],['物理'],['英文'],['地理'],['化學'],['化學'],['放學'],['放學']],
     [['地理'],['化學'],['健護'],['健護'],['文化'],['國文'],['歷史'],['英文'],['放學']],
     [['生物'],['生物'],['國文'],['體育'],['數學'],['班級'],['班級'],['放學'],['放學']]]

#呼叫時間
calltime=[[[8],[0]],[[9],[0]],[[10],[0]],[[11],[0]],[[13],[0]],[[14],[0]],[[15],[0]],[[16],[0]],[[17],[0]]]

###don't edit after this line###

def callf(day):
    if day>4:
        return
    while(True):
        localtime = time.localtime(time.time())
        print(localtime)
        for i in range(0,len(calltime),1):
            if localtime.tm_hour==calltime[i][0][0] and localtime.tm_min==calltime[i][1][0] :
                r = requests.get('https://api.telegram.org/bot'+bot_token+'/sendMessage?chat_id='+chat_id+'&text='+str(cls[day][i][0]))
                sleep(70)
        sleep(50)
        if(localtime.tm_hour>16):
            break

def main():
    localtime = time.localtime(time.time())
    #if localtime.tm_wday !=5 and localtime.tm_wday !=6:
    print(localtime)
    callf(localtime.tm_wday)

main()
