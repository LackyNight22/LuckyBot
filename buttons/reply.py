from telebot.types import ReplyKeyboardMarkup, KeyboardButton

COURSES = [
    "BackEnd",
    "FrondEnd",
    "Full Stack",
    "Mobile Programming",
    "Desktop Programming"
]

STUDY_TIME = [
    "Abetgacham",
    "Abetdan keyin",
    "Kechki"
]


def courses():
    markup = ReplyKeyboardMarkup(
        resize_keyboard=True)
    for i in COURSES:
        markup.add(
            KeyboardButton(i)
        )
    return markup


def share_contact():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(
        KeyboardButton(text="☎️ Telefon raqam", request_contact=True)
    )
    return markup


def share_location():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(
        KeyboardButton("📍Location", request_location=True)
    )
    return markup


def study_time():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    for i in STUDY_TIME:
        markup.add(KeyboardButton(text=i))
    return markup


def confirm():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(
        KeyboardButton("✅Ha"),
        KeyboardButton("❌Yoq")
    )
    return markup
