#!/usr/bin/python
# -*- coding: utf-8 -*-
import telebot
from telebot import types
import time
import urllib
import json
import redis


token = "402460847:AAEqegt0-wvZAzlt0pXPinvhuzZd0gAbwS4"
bot = telebot.TeleBot(token)
sudo = 382393211
logchannel = -1001111733677
f = "\n \033[01;30m Bot Firstname: {} \033[0m".format(bot.get_me().first_name)
u = "\n \033[01;34m Bot Username: {} \033[0m".format(bot.get_me().username)
i = "\n \033[01;32m Bot ID: {} \033[0m".format(bot.get_me().id)
c = "\n \033[01;31m Bot Is Online Now! \033[0m"
print(f + u + i + c)
print("\n\nBot Started In :")
localtime = time.asctime( time.localtime(time.time()) )
print ("Local current time :", localtime)
bot.send_message(logchannel,"Bot Is Started in => {}".format(localtime))
#redis
db = "https://api.telegram.org/bot{}/getMe?".format(token)
res = urllib.request.urlopen(db)
res_body = res.read()
parsed_json = json.loads(res_body.decode("utf-8"))
botid = parsed_json['result']['id']
botuser = parsed_json['result']['username']
#redis connector
R = redis.StrictRedis(host='localhost', port=6379, db=0)
bhash = "bannedsalvan"
mhash = "membersalvan"

#start
@bot.message_handler(commands=['start','Start'])
def start(m):
    banlist = R.sismember(bhash, '{}'.format(m.from_user.id))
    if str(banlist) == 'False':
        markup = types.InlineKeyboardMarkup()
        if m.chat.id == sudo:
            members = types.InlineKeyboardButton("Members",callback_data = 'members')
            markup.add(members)
        userid = m.from_user.id
        urls = types.InlineKeyboardButton('👨‍💼 ایدی ادمین 🕺',url='https://t.me/Th3_uniqu3')
        fun = types.InlineKeyboardButton('🤽‍♀ محصولات ⛹️',callback_data = 'mahsolat')
        idadadi = types.InlineKeyboardButton('🕵️ اطلاعات کاربری شما 👀',callback_data = 'idadadi')
        alvaninfo = types.InlineKeyboardButton('🕵️ درباره ما 👀',callback_data = 'alvaninfo')
        markup.add(fun,idadadi)
        markup.add(urls)
        markup.add(alvaninfo)
        #cmember =
        if R.sismember(mhash,m.from_user.id):
            bot.reply_to(m, "🗣 سلام "+str(m.from_user.first_name)+" ✋️",reply_markup = markup)
        else:
            bot.reply_to(m, "🗣 سلام خوش امدی "+str(m.from_user.first_name)+" ✋️",reply_markup = markup)
            R.sadd(mhash,m.from_user.id)
    else:
        bot.reply_to(m, "🗣"+str(m.from_user.first_name)+" You Is Banned In This Robot")
@bot.callback_query_handler(func=lambda call: True)
def callbacks(call):
    if call.message:
        try:
            banlist = R.sismember(bhash, '{}'.format(call.from_user.id))
            if str(banlist) == 'False':
                if call.data == "menu":
                    markup = types.InlineKeyboardMarkup()
                    if call.message.chat.id == sudo:
                        members = types.InlineKeyboardButton("Members",callback_data = 'members')
                        markup.add(members)
                    urls = types.InlineKeyboardButton('👨‍💼 ایدی ادمین 🕺',url='https://t.me/Th3_uniqu3')
                    fun = types.InlineKeyboardButton('🤽‍♀ محصولات ⛹️',callback_data = 'mahsolat')
                    idadadi = types.InlineKeyboardButton('🕵️ اطلاعات کاربری شما 👀',callback_data = 'idadadi')
                    alvaninfo = types.InlineKeyboardButton('🕵️ درباره ما 👀',callback_data = 'alvaninfo')
                    markup.add(fun,idadadi)
                    markup.add(urls)
                    markup.add(alvaninfo)
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text ="🗣 سلامی دوباره "+str(call.from_user.first_name)+" ✋️",reply_markup=markup)
                markup = types.InlineKeyboardMarkup()
                back = types.InlineKeyboardButton('🔙 Back 🔙', callback_data = 'menu')
                markup.add(back)
                if call.data == "members":
                    membersids = "Users : " + str(R.scard(mhash)) + "\nNew Members :"+ str(R.smembers(mhash))
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = membersids,reply_markup=markup)
                elif call.data == "mahsolat":
                    textt = "یکی از گروه های محصولات را انتخاب کنید."
                    narmafzar = types.InlineKeyboardButton("نرم افزار",callback_data="software")
                    hardware = types.InlineKeyboardButton("سخت افزار",callback_data="hardware")
                    janebipc = types.InlineKeyboardButton("لوازم جانبی کامپیوتر",callback_data="janebipc")
                    janebimobile = types.InlineKeyboardButton("لوازم جانبی موبایل",callback_data="janebimobile")
                    console = types.InlineKeyboardButton("کنسول بازی",callback_data="console")
                    markup.add(narmafzar)
                    markup.add(hardware,janebipc)
                    markup.add(janebimobile)
                    markup.add(console)
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = textt,reply_markup=markup)

                elif call.data == "software":
                    textt = "یک گروه را انتخاب کنید."
                    janebisoft = types.InlineKeyboardButton("نرم افزار کاربردی",callback_data="janebisoft")
                    systemamel = types.InlineKeyboardButton("سیستم عامل",callback_data="systemamel")
                    markup.add(janebisoft,systemamel)
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = textt,reply_markup=markup)
                elif call.data == "janebisoft":
                    bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="تمام برنامه های کاربردی موجود است.")
                elif call.data == "systemamel":
                    textt = "در فروشگاه الوان سیستم عامل های زیر موجود است برای دیدن قیمت ها بر روی دکمه ها کلیک کنید."
                    debian = types.InlineKeyboardButton("Debian - دبیان",callback_data="debian")
                    fedora = types.InlineKeyboardButton("Fedora - فدورا",callback_data="fedora")
                    ubuntu = types.InlineKeyboardButton("Ubuntu - اوبونتو",callback_data="ubuntu")
                    windows = types.InlineKeyboardButton("Windows - ویندوز",callback_data="windows")
                    markup.add(debian)
                    markup.add(ubuntu)
                    markup.add(fedora)
                    markup.add(windows)
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = textt,reply_markup=markup)
                elif call.data == "debian":
                    bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="دبیان یک سیستم عامل بر پایه gnu/linux است\n قیمت : 13000 تومان")
                elif call.data == "fedora":
                    bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="فدورا یک سیستم عامل بر پایه gnu/linux است\n قیمت : 13000 تومان")
                elif call.data == "ubuntu":
                    bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="اوبونتو یک سیستم عامل بر پایه Debian است\n قیمت : 13000 تومان")
                elif call.data == "windows":
                    bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="ویندوز 7 و 8 و 10 و xp \n قیمت : 13000 تومان")
                elif call.data == "idadadi":
                    usernamelink = types.InlineKeyboardButton("🔰 UserLink 🔰",url="https://t.me/"+str(call.from_user.username))
                    markup.add(usernamelink)
                    lastname = str(call.from_user.last_name)
                    if lastname.endswith('None'):
                        lastname= lastname.replace('None','')
                    useridd = str(call.from_user.id)
                    usernamet =  str(call.from_user.username)
                    firstnamee = str(call.from_user.first_name)
                    textt = "🆔 ID Number : <code>{}</code> 🆔\n⚜️ Username : @{} ⚜️\n〽️ Name : {} {} 〽️".format(useridd,usernamet,firstnamee,lastname)
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = textt, reply_markup=markup, parse_mode="HTML")
                elif call.data == "alvaninfo":
                    shomare = types.InlineKeyboardButton("تماس",callback_data="shomare")
                    addres = types.InlineKeyboardButton("ادرس",url="https://goo.gl/maps/RwoZG8iesM62")
                    markup.add(addres,shomare)
                    textt="🖥 گروه فنی مهندسی الوان رایانه 🖥\n📞 شماره تماس : 09354016773 - 09123151082 - 66681191 - 66695893 📞\n📤 ادرس : سی متری جی - خیابان سادات - خیابان برادران فلاح - پلاک 175 📥"
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = textt, reply_markup=markup, parse_mode="HTML")
                elif call.data == "shomare":
                    textt = "شماره برای شما ارسال شد.\nبرای بازگشت به منوی اصلی دکمه بازگشت را بزنید."
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = textt, reply_markup=markup, parse_mode="HTML")
                    bot.send_contact(call.message.chat.id,phone_number="+989354016773",first_name="Alvan Rayane", last_name=None, disable_notification=None)
            else:
                bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="You Are Banned!")
        except Exception as e:
            print(e)
#sudo commands
@bot.message_handler(commands=['ban'])
def gb(m):
    if m.from_user.id == sudo:
        ids = m.text.split()[1]
        R.sadd(bhash,int(ids))
        bot.send_message(int(ids), '<b>You Are Banned!</b>',parse_mode='HTML')
        bot.send_message(m.chat.id, 'Banned!')

@bot.message_handler(commands=['unban'])
def unban(m):
    if m.from_user.id == sudo:
        unban_id = m.text.split()[1]
        R.srem(bhash,unban_id)
        bot.send_message(int(unban_id), '<b>You Are UnBanned!</b>',parse_mode='HTML')
        bot.send_message(m.chat.id, '*Unbanned*', parse_mode='Markdown')

'''@bot.message_handler(commands=['sendall'])
def sendall(m):
    if m.chat.id == sudo :
        text = m.text.replace('/sendall ','')
        ids = R.smembers(mhash)
        for id in ids:
            try:
                bot.send_message(id,text)
                print("Delevered to "+str(id))
            except:
                R.srem(mhash,id)'''
@bot.message_handler(commands=['fwdtoall'])
def fwdall(m):
    if m.chat.id == sudo :
        if m.reply_to_message:
            mid = m.reply_to_message.message_id
            ids = R.smembers(mhash)
            for id in ids:
                try:
                    bot.forward_message(id,m.chat.id,mid)
                    print("Delevered to "+str(id))
                except:
                    R.srem(mhash,id)

bot.polling(True)
