from time import sleep
import time
import requests

#telegram bot_id and chat_id
bot_token=''
chat_id=''

#課堂內容(你看看延平多痛苦（誤)
cls=[[['學校活動'],['英文'],['化學'],['國文'],['地理'],['生物'],['公民'],['歷史'],['數學']],
     [['彈性課程'],['地科'],['數學'],['數學'],['資訊'],['西洋影視'],['國文'],['國文'],['英文']],
     [['數學'],['物理'],['生活科技'],['體育'],['國文'],['化學'],['音樂'],['英文'],['英文']],
     [['數學'],['論孟選讀'],['生物'],['多元選修'],['歷史'],['化學'],['英文'],['國防'],['物理']],
     [['彈性課程'],['英文'],['數學'],['地理'],['公民'],['國文'],['體育'],['物理'],['社團']]]

#呼叫時間
calltime=[[[7],[51]],[[8],[51]],[[9],[51]],[[10],[51]],[[13],[2]],[[13],[51]],[[14],[51]],[[15],[51]],[[16],[44]]]

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
