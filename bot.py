import os

import dns.resolver
import telebot

import models
import settings

dns.resolver.default_resolver = dns.resolver.Resolver(configure=False)
dns.resolver.default_resolver.nameservers = ["8.8.8.8"]

bot = telebot.TeleBot(os.environ.get("TOKEN"))


@bot.message_handler(commands=["start"])
def send_start_message(message: telebot.types.Message) -> None:
    markup = telebot.types.InlineKeyboardMarkup()
    menu = models.WelcomeMenu()
    markup.add(*menu.buttons)
    bot.send_message(
        message.chat.id,
        settings.user_settings.welcome_message,
        reply_markup=markup,
    )


@bot.message_handler(commands=["menu"])
def get_main_menu(message: telebot.types.Message) -> None:
    _main_menu(message.chat.id)


def _main_menu(
    chat_id: str, items: dict | None = None, msg_id_to_delete: str | None = None
) -> None:
    if not items:
        items = {item: False for item in settings.user_settings.buttons_names.keys()}
    markup = telebot.types.InlineKeyboardMarkup()
    menu = models.MainMenu(**items)
    markup.add(*menu.buttons)

    if msg_id_to_delete:
        bot.delete_message(chat_id, msg_id_to_delete)
    bot.send_message(chat_id, menu.title, reply_markup=markup)


@bot.callback_query_handler(
    func=lambda call: models.CallBackData(from_str=call.data).action == "main_menu"
)
def main_menu(call: telebot.types.CallbackQuery) -> None:
    callback_data = models.CallBackData(from_str=call.data)
    if callback_data.items is None:
        items = None
    else:
        items_str: list[str] = callback_data.items.split()
        items = {
            item: items_str[i] == "1"
            for i, item in enumerate(settings.user_settings.buttons_names.keys())
        }
    _main_menu(call.message.chat.id, items, call.message.message_id)


@bot.callback_query_handler(
    func=lambda call: models.CallBackData(from_str=call.data).action == "buy"
)
def buy(call: telebot.types.CallbackQuery) -> None:
    form = {"username": call.message.chat.username}
    items = models.CallBackData(from_str=call.data).items.split()
    handlers = [
        get_beef_lung_big,
        get_beef_lung_small,
        get_beef_liver,
        get_beef_heart,
        get_beef_mix,
        get_liver_cookies,
    ]
    if not _register_next_step_handler(call.message.chat.id, 0, form, items, handlers):
        _send_main_menu_with_error(
            call.message.chat.id, settings.common_settings.no_item_selected
        )


def get_beef_lung_big(
    message: telebot.types.Message, form: dict, items: list[str], handlers: list
):
    form["beef_lung_big_gr"] = message.text
    if not _register_next_step_handler(message.chat.id, 1, form, items, handlers):
        msg = bot.reply_to(message, settings.user_settings.buy_form[-1])
        bot.register_next_step_handler(msg, get_city, form=form)


def get_beef_lung_small(
    message: telebot.types.Message, form: dict, items: list[str], handlers: list
):
    form["beef_lung_small_gr"] = message.text
    if not _register_next_step_handler(message.chat.id, 2, form, items, handlers):
        msg = bot.reply_to(message, settings.user_settings.buy_form[-1])
        bot.register_next_step_handler(msg, get_city, form=form)


def get_beef_liver(
    message: telebot.types.Message, form: dict, items: list[str], handlers: list
):
    form["beef_liver_gr"] = message.text
    if not _register_next_step_handler(message.chat.id, 3, form, items, handlers):
        msg = bot.reply_to(message, settings.user_settings.buy_form[-1])
        bot.register_next_step_handler(msg, get_city, form=form)


def get_beef_heart(
    message: telebot.types.Message, form: dict, items: list[str], handlers: list
):
    form["beef_heart_gr"] = message.text
    if not _register_next_step_handler(message.chat.id, 4, form, items, handlers):
        msg = bot.reply_to(message, settings.user_settings.buy_form[-1])
        bot.register_next_step_handler(msg, get_city, form=form)


def get_beef_mix(
    message: telebot.types.Message, form: dict, items: list[str], handlers: list
):
    form["beef_mix_gr"] = message.text
    if not _register_next_step_handler(message.chat.id, 5, form, items, handlers):
        msg = bot.reply_to(message, settings.user_settings.buy_form[-1])
        bot.register_next_step_handler(msg, get_city, form=form)


def get_liver_cookies(
    message: telebot.types.Message, form: dict, items: list[str], handlers: list
):
    form["liver_cookies_gr"] = message.text
    if not _register_next_step_handler(message.chat.id, 6, form, items, handlers):
        msg = bot.reply_to(message, settings.user_settings.buy_form[-1])
        bot.register_next_step_handler(msg, get_city, form=form)


def _register_next_step_handler(
    chat_id: str, current_step: int, form: dict, items: list[str], handlers: list
) -> bool:
    for i in range(current_step, len(items)):
        if items[i] == "1":
            msg = bot.send_message(chat_id, settings.user_settings.buy_form[i])
            bot.register_next_step_handler(
                msg, handlers[i], form=form, items=items, handlers=handlers
            )
            return True
    return False


def get_city(message: telebot.types.Message, form: dict):
    form["city"] = message.text
    _send_form(form)
    bot.send_message(
        message.chat.id,
        settings.user_settings.accept_form_report,
    )


def _send_main_menu_with_error(chat_id: str, error_message: str) -> None:
    markup = telebot.types.InlineKeyboardMarkup()
    menu = models.MainMenu()
    markup.add(*menu.buttons)
    bot.send_message(chat_id, error_message, reply_markup=markup)


def _send_form(form: dict) -> None:
    print(f"{form=}")
    bot.send_message(
        settings.common_settings.manager_chat_id,
        settings.user_settings.buy_message.format(
            username=form["username"],
            city=form["city"],
            beef_lung_big=form.get("beef_lung_big_gr", "0"),
            beef_lung_small=form.get("beef_lung_small_gr", "0"),
            beef_liver=form.get("beef_liver_gr", "0"),
            beef_heart=form.get("beef_heart_gr", "0"),
            beef_mix=form.get("beef_mix_gr", "0"),
            liver_cookies=form.get("liver_cookies_gr", "0"),
        ),
    )


bot.polling(none_stop=True)
