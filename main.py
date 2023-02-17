import telebot
from telebot import *
import telebot.types
import user_interface as ui
import set_sample as ss
import calculations as calc
from my_token import my_token


bot = telebot.TeleBot(my_token)

sample = ''


@bot.message_handler(commands=['calc'])
def calc_command(message: types.Message):
    bot.send_message(message.chat.id, '0', reply_markup=ui.keyboard())


@bot.callback_query_handler(lambda callback: callback.data)
def get_value(callback: types.CallbackQuery):
    global sample
    if callback.data == '=':
        list_example = ss.get_data(sample)
        result = calc.get_result(list_example)
        bot.edit_message_text(f'{sample} = {result}', callback.message.chat.id, callback.message.id,
                              reply_markup=ui.keyboard())
        sample = ''
    elif callback.data == 'выход':
        bot.delete_message(callback.message.chat.id, callback.message.id)
        sample = ''
    elif callback.data == '<=':
        if len(sample) == 1:
            sample = ''
            bot.edit_message_text(
                '0', callback.message.chat.id, callback.message.id, reply_markup=ui.keyboard())
        else:
            sample = sample[:-1]
            bot.edit_message_text(sample, callback.message.chat.id,
                                  callback.message.id, reply_markup=ui.keyboard())
    else:
        sample += callback.data
        bot.edit_message_text(sample, callback.message.chat.id,
                              callback.message.id, reply_markup=ui.keyboard())


bot.polling(none_stop=True)
