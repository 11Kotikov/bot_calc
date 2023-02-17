from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def keyboard():
    calc_keyboard = InlineKeyboardMarkup(row_width=4)
    calc_keyboard.add(InlineKeyboardButton('(', callback_data='('),
                      InlineKeyboardButton(')', callback_data=')'),
                      InlineKeyboardButton('/', callback_data='/'),
                      InlineKeyboardButton('<=', callback_data='<='),
                      InlineKeyboardButton('7', callback_data='7'),
                      InlineKeyboardButton('8', callback_data='8'),
                      InlineKeyboardButton('9', callback_data='9'),
                      InlineKeyboardButton('*', callback_data='*'),
                      InlineKeyboardButton('4', callback_data='4'),
                      InlineKeyboardButton('5', callback_data='5'),
                      InlineKeyboardButton('6', callback_data='6'),
                      InlineKeyboardButton('+', callback_data='+'),
                      InlineKeyboardButton('1', callback_data='1'),
                      InlineKeyboardButton('2', callback_data='2'),
                      InlineKeyboardButton('3', callback_data='3'),
                      InlineKeyboardButton('-', callback_data='-'),
                      InlineKeyboardButton('0', callback_data='0'),
                      InlineKeyboardButton('=', callback_data='='),
                      InlineKeyboardButton('выход', callback_data='выход'),
                      InlineKeyboardButton('i', callback_data='i'))
    return calc_keyboard
