import telebot
from telebot import types
import requests
import json
from datetime import datetime
import ast
import requests
from bs4 import BeautifulSoup as bs
import fake_useragent

bot = telebot.TeleBot('6126109448:AAHoIcLe8it1cA20SwZH6ZKkdMabIme2OFU')
count=0
count2=0
count1=0
res=''
result=''
finally_result=''
posts={}
a=''
keyboard=''
pars=''
photo_list=[]
v=0
token='d06b7235d06b7235d06b723524d37851d6dd06bd06b7235b47c4e741f6dc2323508c054'
count3=0
ept=''
n=''
src=''
res1=0
owner_id=''
url_for_pop=''
start_or_stop=0
domain_or_owner=0
criteries=0
class Pars():

    def start():
        try:
            global result
            global res
            global posts
            global ept
            global owner_id
            global src
            global domain_or_owner

            owner_id=''

            if res.replace('https://vk.com/id','')!=res:
                
                res=res.replace('https://vk.com/id','')
                owner_id=res

                token='d06b7235d06b7235d06b723524d37851d6dd06bd06b7235b47c4e741f6dc2323508c054'
                url1=f'https://api.vk.com/method/wall.get?owner_id={res}&access_token={token}&v=5.81'

                req=requests.get(url1)
                src=req.json()
                posts=src['response']
                
            elif res.replace('https://vk.com/club','')!=res:
                
                res=res.replace('https://vk.com/club','')
                owner_id=res

                token='d06b7235d06b7235d06b723524d37851d6dd06bd06b7235b47c4e741f6dc2323508c054'
                url1=f'https://api.vk.com/method/wall.get?owner_id={res}&access_token={token}&v=5.81'

                req=requests.get(url1)
                src=req.json()
                posts=src['response']
                               
        
            elif res.replace('vk.com/public','')!=res:
                res=res.replace('https://vk.com/public','')
                owner_id='-'+res

                token='d06b7235d06b7235d06b723524d37851d6dd06bd06b7235b47c4e741f6dc2323508c054'
                url=f'https://api.vk.com/method/wall.get?owner_id={res}&access_token={token}&v=5.81&extended=1&count=100'
                req=requests.get(url)
                src=req.json()
                with open('post_and_owner_information.json','w',encoding='utf-8') as file:
                    json.dump(src,file,indent=4,ensure_ascii=False)
                posts=src['response']
            elif res.replace('https://vk.com/wall','')!=res:
                res=res.replace('https://vk.com/wall','')

                token='d06b7235d06b7235d06b723524d37851d6dd06bd06b7235b47c4e741f6dc2323508c054'
                url=f'https://api.vk.com/method/wall.getById?posts={res}&access_token={token}&v=5.81'

                req=requests.get(url)
                src=req.json()
                result=src['response'][0]

                with open('post_and_owner_information.json','w',encoding='utf-8') as file:
                    json.dump(src,file,indent=4,ensure_ascii=False)


            else:
                res=res.replace('https://vk.com/','')
                owner_id=res

                token='d06b7235d06b7235d06b723524d37851d6dd06bd06b7235b47c4e741f6dc2323508c054'
                url1=f'https://api.vk.com/method/wall.get?domain={res}&access_token={token}&v=5.81'

                req=requests.get(url1)
                src=req.json()
                posts=src['response']
                
                owner_id=posts['items'][0]['owner_id']

            return 'b'
        except:
            return 'Неправильный url'


    def information():
        global result
        global finally_result
        global photo_list
        global token
        global v
        global start_or_stop
        photo_list=[]
        if 'copy_history' in result:
            dop_text=ast.literal_eval(str((dict(result)['copy_history']))[1:-1])
            result1=f"Текст автора:\n {dict(result)['text']}\n Текст от другой группы в этом посте: \n{dop_text['text']}".replace('\n\n','\n')
            g=dict(dop_text)['attachments']
                                                
            if len(g)==2:

                if g[0]['type']=='photo':
                    photo_list.append(g['photo']['sizes'][-1]['url'])
                    v=1
                if g[0]['type']=='video':
                    result1= 'Видео времено недоступно\n'+result1

            else:
                error=''
                for gf in range(len(g)):

                    d=g[gf]
                    if d['type']=='photo':
                        photo_list.append(d['photo']['sizes'][-1]['url'])
                        v=1

                    if d['type']=='video':
                        error='Видео времено недоступно\n'
                result1=error+result1
        else:
            result1=f"Текст автора:\n {dict(result)['text']}\n".replace('\n\n','\n')
            g=dict(result)['attachments']

            if len(g)==2:

                if g[0]['type']=='photo':
                    photo_list.append(g['photo']['sizes'][-1]['url'])
                    v=1
                if g[0]['type']=='video':
                    result1= 'Видео времено недоступно\n'+result1

            else:
                error=''
                for gf in range(len(g)):

                    d=g[gf]
                    if d['type']=='photo':
                        photo_list.append(d['photo']['sizes'][-1]['url'])
                        v=1

                    if d['type']=='video':
                        error='Видео времено недоступно\n'
                result1=error+result1

        if 'views' in result:
            result2=f"Просмотры: {dict(result)['views']['count']}"
        result3=f"Лайки: {dict(result)['likes']['count']}"
        result4=f"Репосты: {dict(result)['reposts']['count']}"
        result5=f"Комментарии: {dict(result)['comments']['count']}"
        result6=f"Дата публикации: {datetime.utcfromtimestamp(result['date']).strftime('%Y %m %d ') }"

        finally_result='\n'+result1+'\n'+result2+'\n'+result3+'\n'+result4+'\n'+result5+'\n'+result6
        return finally_result

    def how_many_posts():
        global posts
        global finally_result

        finally_result=f"Кол-во постов: {posts['count']}"
        return finally_result


    def pop():
        global token
        global owner_id
        global src
        global url_for_pop
        global res
        global start_or_stop
        global criteries
        if start_or_stop==1:
            if criteries==1:
                criteries1='likes'
                name='\n Кол-во лайков: '
            elif criteries==2:
                criteries1='reposts'
                name='\n Кол-во репостов: '
            elif criteries==3:
                criteries1='views'
                name='\n Кол-во просмотров: '
            elif criteries==4:
                criteries1='comments'
                name='\n Кол-во комментариев: '
            start_or_stop=0
            offset=0
            url=f'https://api.vk.com/method/wall.get?owner_id={owner_id}&count=40&access_token={token}&v=5.81&extended=1'
            req=requests.get(url)
            src=req.json()
            all_posts=[]
            posts_for1=src['response']['count']
            pop_id={}
            while offset<posts_for1:
                url=f'https://api.vk.com/method/wall.get?owner_id={owner_id}&count=100&access_token={token}&v=5.81&extended=1&count=100&offset={offset}'
                offset+=100
                req=requests.get(url)
                src=req.json()
                for pop_likes in src['response']['items']:
                    if 'views' in pop_likes:
                        pop_id[f"{pop_likes['id']}"]=int(f"{pop_likes[criteries1]['count']}")
                        a=str(f"{pop_likes['owner_id']}")
                    
            n=0
            while n!=int(res1):
                all_posts.append(dict([max(pop_id.items(), key=lambda k_v: k_v[1])]))
                delete=dict([max(pop_id.items(), key=lambda k_v: k_v[1])]).keys()
                for d in delete:
                    del pop_id[f"{d}"]
                n+=1
            url_for_pop=''
            for i in range(len(all_posts)):
                for h in dict(all_posts[int(i)]).keys():

                    url_for_pop+=str(i+1)+'. https://vk.com/wall'+a+'_'+h+name+str(all_posts[int(i)][f'{h}'])+'\n'

closed=0
st=0
keyboard1=''
@bot.message_handler(commands=['start'])
def inline_buttons(message):
    global count
    global photo_list
    global closed
    global keyboard1
    global st

    if count==0:
        keyboard1 = types.InlineKeyboardMarkup()
        pars_group = types.InlineKeyboardButton(text='По группе/сообществу/аккаунту 👤', callback_data='pars_group')
        pars_post = types.InlineKeyboardButton(text='По посту 📝 ', callback_data='pars_post')
        posts_on_time=types.InlineKeyboardButton(text='Отправлять посты по времени 🕐 ', callback_data='post_on_time')
        keyboard1.add(pars_post)
        keyboard1.add(pars_group)
        keyboard1.add(posts_on_time)
        if closed==0:
            st=bot.send_message(message.from_user.id, text='Найти информацию в ВК', reply_markup=keyboard1,disable_web_page_preview=True)
        else:
            bot.send_message(message.chat.id, text='Извинити, функция находиться в процессе разработки \nНайти информацию в ВК', reply_markup=keyboard1,disable_web_page_preview=True)
            closed=0
        #markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        #btn1 = types.KeyboardButton("👋 Поздороваться")
        #btn2 = types.KeyboardButton("❓ Задать вопрос")
        #markup.add(btn1, btn2)
        #bot.send_message(message.chat.id, text="Привет, {0.first_name}! Я тестовый бот для твоей статьи для habr.com".format(message.from_user), reply_markup=markup)


@bot.message_handler(commands=['return'])
def inline_buttons4(message):
    global count
    global n
    global st
    global keyboard1

    keyboard1 = types.InlineKeyboardMarkup()
    pars_group = types.InlineKeyboardButton(text='По группе/сообществу/аккаунту 👤', callback_data='pars_group')
    pars_post = types.InlineKeyboardButton(text='По посту 📝', callback_data='pars_post')
    posts_on_time=types.InlineKeyboardButton(text='Отправлять посты по времени 🕐', callback_data='post_on_time')
    keyboard1.add(pars_post)
    keyboard1.add(pars_group)
    keyboard1.add(posts_on_time)

    st=bot.send_message(message.from_user.id, text='Найти информацию в ВК',reply_markup=keyboard1,disable_web_page_preview=True)
    count=0
    
    
@bot.message_handler(commands=['return1'])

def inline_buttons2(message):
    global count
    global count2

    bot.send_message(message.chat.id,text='Вставьте ссылку на пост')
    count2=2
    count=0

@bot.message_handler(commands=['return2'])
def inline_buttons6(message):
    global count
    global count2
    bot.send_message(message.chat.id,text='Вставьте ссылку на группу/сообщество/аккаунт')
    count2=1
    count=0


@bot.callback_query_handler(func=lambda call: True)

def questions(call):
    global count
    global count2
    global res
    global keyboard1
    global st

    if call.data=='pars_group' :

        bot.send_message(call.message.chat.id, text="Вставьте ссылку на группу/сообщество/аккаунт")
        count2=1

    elif call.data=='pars_post':
        count2=2
        bot.send_message(call.message.chat.id,text='Вставьте ссылку на пост')


    elif call.data=='information':
        count2=3
        answer(call.message)

    elif call.data=='how_many_posts':
        count2=5
        answer(call.message)

    elif call.data=='popular_posts':
        count2=7
        answer(call.message)

    elif call.data=='post_on_time':
        count2=4
        bot.edit_message_text(chat_id = call.message.chat.id,message_id = st.message_id,text='Извините, функция находиться в процессе разработки \nНайти информацию в ВК',reply_markup=keyboard1)
        #bot.send_message(call.message.chat.id,text='Вставьте ссылку(-и) на группу(-ы) с которой(-ых)\n будут отправляться посты (каждая ссылка с новой строки)')
        
    elif call.data=='pop_likes':
        bot.send_message(call.message.chat.id,text='Сколько поп. постов нужно выслать')
        count2=12
    elif call.data=='pop_reposts':
        count2=9
        bot.send_message(call.message.chat.id,text='Сколько поп. постов нужно выслать')
    elif call.data=='pop_views':
        count2=10
        bot.send_message(call.message.chat.id,text='Сколько поп. постов нужно выслать')
    elif call.data=='pop_comments':
        count2=11
        bot.send_message(call.message.chat.id,text='Сколько поп. постов нужно выслать')


@bot.message_handler(content_types=['text'])


def answer(message):
    global count
    global res
    global count2
    global a
    global keyboard
    global pars
    global photo_list
    global v
    global count3
    global res1

    if count2==1:
        if 'https://vk.com/' in message.text:
            res=message.text
            inline_buttons1(message)
        else:
            bot.send_message(message.chat.id,'Ошибка ❌\nВставьте правильную ссылку на группу/сообщество/аккаунт')


    elif count2==2:

        if 'https://vk.com/wall' in message.text:
            res=message.text
            inline_buttons1(message)
        else:
            bot.send_message(message.chat.id,'Ошибка ❌\nВставьте правильную ссылку на пост')



    elif count2==3:
        pars_start=Pars.start()
        if 'Неправильный url' in pars_start:
            count2=2
            answer(message)
        else:
            b=Pars.information()
            count3=2
            count=0
            albom_photos=[]
            if v==1:
                for i in photo_list:
                        albom_photos.append(telebot.types.InputMediaPhoto(i))

                bot.send_media_group(message.chat.id, albom_photos)
            bot.send_message(message.chat.id,'Информация о посте\n'+b+'\n\nЧтобы начать сначала /return  🔄\nЧтобы повторить поиск /return1   📝',disable_web_page_preview=True)
            count2=2


    elif count2==5:
        pars_start=Pars.start()
        if 'Неправильный url' in pars_start:
            count2=1
            answer(message)
        else:
            count3=3
            count2=2
            count=0
            bot.edit_message_text(chat_id = message.chat.id, message_id = a.message_id, text = f"{Pars.how_many_posts()}\nНачать сначала /return 🔄\nПовторить поиск по групппам /return2 👤\n\nВыберите дальнейшее действие ", reply_markup=keyboard)

    #elif count2==4:
        #c=0
        #res=''
        #while c!=5:
        #    if message.text!=res:
        #        print(message.text)
        #        c+=1
        #    res=message.text
        #    message.text=''
        #count2=6
        #inline_buttons1(message)

    elif count2==7:
        keyboard=types.InlineKeyboardMarkup()
        pop_likes = types.InlineKeyboardButton(text='Лайкам 👍🏻', callback_data='pop_likes')
        pop_reposts = types.InlineKeyboardButton(text='Репостам 📣', callback_data='pop_reposts')
        pop_views = types.InlineKeyboardButton(text='Просмотрам 👁️', callback_data='pop_views')
        pop_all = types.InlineKeyboardButton(text='Комментариям 💬', callback_data='pop_comments')
        

        keyboard.add(pop_likes,pop_reposts)
        keyboard.add(pop_views,pop_all)
        bot.edit_message_text(chat_id = message.chat.id, message_id = a.message_id, text = 'Начать сначала /return 🔄 \nПовторить поиск по группам /return2 👤 \n\nПосты будут отбираться по', reply_markup=keyboard)
        count=1
        inline_buttons(message)

    elif count2==12:
        if message.text.isdigit():
            res1=message.text
            bot.send_message(message.chat.id,text='Подождите, это может занять несколько минут, взависимости от кол-во постов 🕐')
            inline_buttons1(message)
        else:
            bot.send_message(message.chat.id,text='Ошибка ❌')
    elif count2==11:
        if message.text.isdigit():
            res1=message.text
            bot.send_message(message.chat.id,text='Подождите, это может занять несколько минут, взависимости от кол-во постов 🕐')
            inline_buttons1(message)
        else:
            bot.send_message(message.chat.id,text='Ошибка ❌')
    elif count2==10:
        if message.text.isdigit():
            res1=message.text
            bot.send_message(message.chat.id,text='Подождите, это может занять несколько минут, взависимости от кол-во постов 🕐')
            inline_buttons1(message)
        else:
            bot.send_message(message.chat.id,text='Ошибка ❌')

    elif count2==9:
        
        if message.text.isdigit():
            res1=message.text
            bot.send_message(message.chat.id,text='Подождите, это может занять несколько минут, взависимости от кол-во постов 🕐')
            inline_buttons1(message)
        else:
            bot.send_message(message.chat.id,text='Ошибка ❌')

def inline_buttons1(message):
    global count2
    global count
    global count1
    global res
    global a
    global keyboard
    global pars
    global url_for_pop
    global start_or_stop
    global closed
    global criteries

    if count2==1:
        keyboard = types.InlineKeyboardMarkup()
        pars_post1 = types.InlineKeyboardButton(text='Найти информацию по посту 📝 ', callback_data='pars_post')
        how_many_posts = types.InlineKeyboardButton(text='Сколько постов на странице  🗂', callback_data='how_many_posts')
        popular_posts = types.InlineKeyboardButton(text='Популярные посты 📈 ', callback_data='popular_posts')
        keyboard.add(pars_post1)
        keyboard.add(how_many_posts)
        keyboard.add(popular_posts)
        a=bot.send_message(message.from_user.id, text='Начать сначала /return 🔄\nПовторить поиск по группам /return2 👤 \n\nВыберите дальнейшее действие', reply_markup=keyboard)
        count=1
        inline_buttons(message)



    if count2==2:
        keyboard = types.InlineKeyboardMarkup()
        information = types.InlineKeyboardButton(text='Получить информацию 📥', callback_data='information')
        keyboard.add(information)
        bot.send_message(message.from_user.id, text='Выберите дальнейшее действие', reply_markup=keyboard)
        count=1
        inline_buttons(message)

    #elif count2==4:
    #    #keyboard = types.InlineKeyboardMarkup()
    #    #tn = types.InlineKeyboardButton(text='10 мин', callback_data='tn')
    #    #ty = types.InlineKeyboardButton(text='30 мин', callback_data='ty')
    #    #sy = types.InlineKeyboardButton(text='60 мин', callback_data='sy')
    #    #keyboard.add(tn,ty,sy)
    #    #bot.send_message(message.from_user.id, text='Через сколько минут отправлять посты', reply_markup=keyboard)
    #    #count=1
    #    closed=1
    #    inline_buttons(message)
        

    elif count2==12:
        criteries=1
        start_or_stop=1
        Pars.start()
        Pars.pop()
  
        bot.send_message(message.from_user.id,text=url_for_pop+'\nЧтобы повторить - просто введите кол-во нужных постов \nЧтобы начать сначала /return  🔄 \n Чтобы начать поиск по группам /return2 👤 ',disable_web_page_preview=True)

    elif count2==9:
        criteries=2
        start_or_stop=1
        Pars.start()
        Pars.pop()
        bot.send_message(message.from_user.id,text=url_for_pop+'\nЧтобы повторить - просто введите кол-во нужных постов \nЧтобы начать сначала /return  🔄 \n Чтобы начать поиск по группам /return2 👤 ',disable_web_page_preview=True)
    elif count2==10:
        criteries=3
        start_or_stop=1
        Pars.start()
        Pars.pop()
        bot.send_message(message.from_user.id,text=url_for_pop+'\nЧтобы повторить - просто введите кол-во нужных постов \nЧтобы начать сначала /return  🔄 \n Чтобы начать поиск по группам /return2 👤 ',disable_web_page_preview=True)
    elif count2==11:
        criteries=4
        start_or_stop=1
        Pars.start()
        Pars.pop()
        bot.send_message(message.chat.id,text=url_for_pop+'\n\nЧтобы повторить - просто введите кол-во нужных постов \nЧтобы начать сначала /return  🔄 \n Чтобы начать поиск по группам /return2 👤 ',disable_web_page_preview=True)


if __name__ == '__main__':
    bot.infinity_polling()
