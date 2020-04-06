from telebot import TeleBot, types
from config import TOKEN, COLLECTOR, comments_kb
import validators
from models import Person

bot = TeleBot(TOKEN)
current_state = -1
new_person = {}


def add_new_person_into_db(person):
    global current_state
    current_state = -1
    print(Person.objects.create(**person).save())


class Send:

    @staticmethod
    def request_new_data(chat_id):
        bot.send_message(
            chat_id=chat_id,
            text=f'Thanks! {COLLECTOR[current_state]["text"]}',
            reply_markup=comments_kb() if COLLECTOR[current_state]["column"] == "comments" else None
        )

    @staticmethod
    def tell_success(chat_id):
        bot.send_message(
            chat_id=chat_id,
            text="New person was successfully added into database\n"
                 "Please type /start to add one more person"
        )

    @staticmethod
    def intro(chat_id):
        bot.send_message(
            chat_id=chat_id,
            text="Hi! I am HelperBot! I will collect some data about you"
        )

    @staticmethod
    def without_intro(chat_id):
        bot.send_message(
            chat_id=chat_id,
            text="Please type /start to find out what this bot can do"
        )

    @staticmethod
    def invalid_phone_message(chat_id):
        bot.send_message(
            chat_id=chat_id,
            text=f'Invalid phone format. {COLLECTOR[2]["text"]}'
        )

    @staticmethod
    def invalid_email_message(chat_id):
        bot.send_message(
            chat_id=chat_id,
            text=f'Invalid email format. {COLLECTOR[3]["text"]}'
        )


@bot.message_handler(commands=['start'])
def start_handler(message: types.Message):
    global current_state
    current_state = 0

    Send.intro(message.chat.id)
    Send.request_new_data(message.chat.id)


@bot.message_handler(content_types=['text'])
def data_handler(message: types.Message):
    global current_state
    if current_state == -1:
        Send.without_intro(message.chat.id)
    elif current_state < len(COLLECTOR):
        if COLLECTOR[current_state]['column'] == 'phone_number':
            if not validators.is_phone_valid(message.text):
                Send.invalid_phone_message(message.chat.id)
                return None
        elif COLLECTOR[current_state]['column'] == 'email':
            if not validators.is_email_valid(message.text):
                Send.invalid_email_message(message.chat.id)
                return None
        new_person[COLLECTOR[current_state]['column']] = message.text
        current_state += 1
        if current_state < len(COLLECTOR):
            Send.request_new_data(message.chat.id)
        else:
            add_new_person_into_db(new_person)
            Send.tell_success(message.chat.id)


@bot.callback_query_handler(func=lambda c: c.data == 'no_comments')
def no_comments_callback_handler(call):
    new_person['comments'] = "No comments left"
    add_new_person_into_db(new_person)
    Send.tell_success(call.message.chat.id)


bot.polling()
