from telebot import TeleBot
 
Foolproof_bot_for_stories_bot= TeleBot('7716157447:AAGchXadXlgeNFQGYC_JDuc-6VIqlu-9QkU')
 
@Foolproof_bot_for_stories_bot.message_handler(commands=['start'])
def start(message):
    Foolproof_bot_for_stories_bot.send_massage(message.chat.id, '*Приветсвую мечтатель*',parse_mode='Markdown')
    
@Foolproof_bot_for_stories_bot.message_handler(commands=['quote'])
def tale(message):
    Foolproof_bot_for_stories_bot.send_massage(message.chat.id, '[*Здесь рассказывается сказка*](https://ru.wikipedia.org/wiki/Щелкунчик_и_Мышиный_король)', parse_mode='Markdown')

@Foolproof_bot_for_stories_bot.message_handler(commands=['advice'])
def advice(message):
    Foolproof_bot_for_stories_bot.send_massage(message.chat.id,'Eсли только у тебя есть глаза, ты всюду увидишь сверкающие цукатные рощи, прозрачные марципановые замки — словом, всякие чудеса и диковинки.')


    
Foolproof_bot_for_stories_bot.infinity_polling()
 