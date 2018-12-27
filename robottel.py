 #!/usr/bin/python3.6
import telepot
import time
import urllib3

# You can leave this bit out if you're using a paid PythonAnywhere account
proxy_url = "http://proxy.server:3128"
telepot.api._pools = {
    'default': urllib3.ProxyManager(proxy_url=proxy_url, num_pools=3, maxsize=10, retries=False, timeout=30),
}
telepot.api._onetime_pool_spec = (urllib3.ProxyManager, dict(proxy_url=proxy_url, num_pools=1, maxsize=1, retries=False, timeout=30))
# end of the stuff that's only needed for free accounts

bot = telepot.Bot('679358366:AAFVKfDsczRpcF1Jr0dUbnkk6YcuN96jQMY')

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)
    if content_type=='text':
        if msg['text']=='/start':
            bot.sendMessage(chat_id,'.سلام.به ربات آثار شعرا خوش آمدید ')
            bot.sendMessage(chat_id,'1-قیصر امین پور')
            bot.sendMessage(chat_id,'2-ملک الشعرای بهار')
            bot.sendMessage(chat_id,'3-هوشنگ ابتهاج')
            bot.sendMessage(chat-id,'4-شهریار')
            bot.sendMessage(chat_id,'5-سهراب سپهری')
        elif msg['text']=='1':
            bot.sendMessage(chat_id,'آینه های ناگهان ، به قول پرستو ، ظهر روز دهم ، مثل چشمه مثل رود، دستور زبان عشق ،گل ها همه آفتاب گردانند ، بی بال پریدن ')
        elif msg['text']=='2':
            bot.sendMessage(chat_id,'سبک شناسی،تاریخ احزاب سیاسی')
        elif msg['text']=='3':
            bot.sendMessage(chat_id,'نخستین نغمه ها،شبگیر،چند برگ از یلدا،تا صبح شب یلدا،یادگار خون سرو')
        elif msg['text']=='4':
            bot.sendMessage(chat_id,'حیدربابا یه سلام،مجموعه پنج جلدی،دیوان ترکی')
        elif msg['text']=='5':
            bot.sendMessage(chat_id,'هشت کتاب')
        else:
            bot.sendMessage(chat_id, 'این شاعر ثبت نشده است')


bot.message_loop(handle)

print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)
