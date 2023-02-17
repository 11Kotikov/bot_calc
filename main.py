import telebot
from telebot import *
import telebot.types
import user_interface as ui
import set_sample as ss
import calculations as calc
from my_token import my_token


bot = telebot.TeleBot(my_token)

example = ''


@bot.message_handler(commands=['calc'])
def calc_command(message: types.Message):
    bot.send_message(message.chat.id, '0', reply_markup=ui.keyboard())


@bot.callback_query_handler(lambda callback: callback.data)
def get_value(callback: types.CallbackQuery):
    global example
    if callback.data == '=':
        list_example = ss.get_data(example)
        result = calc.get_result(list_example)
        bot.edit_message_text(f'{example} = {result}', callback.message.chat.id, callback.message.id,
                              reply_markup=ui.keyboard())
        example = ''
    elif callback.data == 'выход':
        bot.delete_message(callback.message.chat.id, callback.message.id)
        example = ''
    elif callback.data == '<=':
        if len(example) == 1:
            example = ''
            bot.edit_message_text(
                '0', callback.message.chat.id, callback.message.id, reply_markup=ui.keyboard())
        else:
            example = example[:-1]
            bot.edit_message_text(example, callback.message.chat.id,
                                  callback.message.id, reply_markup=ui.keyboard())
    else:
        example += callback.data
        bot.edit_message_text(example, callback.message.chat.id,
                              callback.message.id, reply_markup=ui.keyboard())


bot.polling(none_stop=True)
