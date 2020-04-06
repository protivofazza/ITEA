from telebot import types

TOKEN = "1215349361:AAHtLg1dRZwIY07jl9vnv3BwrPn_vPdEgms"

COLLECTOR = (
    {
        'text': 'Please enter your name',
        'column': 'name'
    },
    {
        'text': 'Please enter your surname',
        'column': 'surname'
    },
    {
        'text': 'Please enter your phone number in format +380XXXXXXXXX',
        'column': 'phone_number'
    },
    {
        'text': 'Please enter your e-mail address in format example@gmail.com',
        'column': 'email'
    },
    {
        'text': 'Please enter your home address',
        'column': 'address'
    },
    {
        'text': 'Please write any additional comments if you have ones',
        'column': 'comments'
    }
)


def comments_kb():
    kb = types.InlineKeyboardMarkup(row_width=1)
    buttons = [
        types.InlineKeyboardButton("No comments", callback_data="no_comments")
    ]
    kb.add(*buttons)
    return kb
