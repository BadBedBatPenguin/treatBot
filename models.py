import telebot

from settings import user_settings


class CallBackData:
    def __init__(
        self,
        action: str | None = None,
        items: str | None = None,
        user_id: str | None = None,
        from_str: str | None = None,
    ) -> None:
        if from_str:
            data = from_str.split(":")
            self.action = data[0] if data[0] else None
            self.items = data[1] if data[1] else None
            self.user_id = data[2] if data[2] else None
            return
        self.action = action
        self.items = items
        self.user_id = user_id if user_id else ""

    def str(self) -> str:
        return f"{self.action if self.action else ''}:{self.items if self.items else ''}::{self.user_id if self.user_id else ''}"


class Menu:
    title: str
    action: str
    buttons: list
    prev_action: str | None


class WelcomeMenu(Menu):
    def __init__(self) -> None:
        self.action = "welcome"
        self.title = user_settings.welcome_message
        self.buttons = [
            telebot.types.InlineKeyboardButton(
                user_settings.welcome_menu_text,
                callback_data=CallBackData(action="main_menu").str(),
            )
        ]


class MainMenu(Menu):
    def __init__(
        self,
        beef_lung_big: bool = False,
        beef_lung_small: bool = False,
        beef_liver: bool = False,
        beef_heart: bool = False,
        beef_mix: bool = False,
        liver_cookies: bool = False,
    ) -> None:
        self.action = "main_menu"
        self.prev_action = None
        self.title = user_settings.main_menu_title
        beef_lung_big_str = "1" if beef_lung_big else "0"
        beef_lung_small_str = "1" if beef_lung_small else "0"
        beef_liver_str = "1" if beef_liver else "0"
        beef_heart_str = "1" if beef_heart else "0"
        beef_mix_str = "1" if beef_mix else "0"
        liver_cookies_str = "1" if liver_cookies else "0"
        not_beef_lung_big_str = "1" if not beef_lung_big else "0"
        not_beef_lung_small_str = "1" if not beef_lung_small else "0"
        not_beef_liver_str = "1" if not beef_liver else "0"
        not_beef_heart_str = "1" if not beef_heart else "0"
        not_beef_mix_str = "1" if not beef_mix else "0"
        not_liver_cookies_str = "1" if not liver_cookies else "0"
        self.buttons = [
            telebot.types.InlineKeyboardButton(
                user_settings.add_items_buttons[
                    "checked" if beef_lung_big else "unchecked"
                ]["beef_lung_big"],
                callback_data=CallBackData(
                    action=self.action,
                    items=f"{not_beef_lung_big_str} {beef_lung_small_str} {beef_liver_str} {beef_heart_str} {beef_mix_str} {liver_cookies_str}",
                ).str(),
            ),
            telebot.types.InlineKeyboardButton(
                user_settings.add_items_buttons[
                    "checked" if beef_lung_small else "unchecked"
                ]["beef_lung_small"],
                callback_data=CallBackData(
                    action=self.action,
                    items=f"{beef_lung_big_str} {not_beef_lung_small_str} {beef_liver_str} {beef_heart_str} {beef_mix_str} {liver_cookies_str}",
                ).str(),
            ),
            telebot.types.InlineKeyboardButton(
                user_settings.add_items_buttons[
                    "checked" if beef_liver else "unchecked"
                ]["beef_liver"],
                callback_data=CallBackData(
                    action=self.action,
                    items=f"{beef_lung_big_str} {beef_lung_small_str} {not_beef_liver_str} {beef_heart_str} {beef_mix_str} {liver_cookies_str}",
                ).str(),
            ),
            telebot.types.InlineKeyboardButton(
                user_settings.add_items_buttons[
                    "checked" if beef_heart else "unchecked"
                ]["beef_heart"],
                callback_data=CallBackData(
                    action=self.action,
                    items=f"{beef_lung_big_str} {beef_lung_small_str} {beef_liver_str} {not_beef_heart_str} {beef_mix_str} {liver_cookies_str}",
                ).str(),
            ),
            telebot.types.InlineKeyboardButton(
                user_settings.add_items_buttons["checked" if beef_mix else "unchecked"][
                    "beef_mix"
                ],
                callback_data=CallBackData(
                    action=self.action,
                    items=f"{beef_lung_big_str} {beef_lung_small_str} {beef_liver_str} {beef_heart_str} {not_beef_mix_str} {liver_cookies_str}",
                ).str(),
            ),
            telebot.types.InlineKeyboardButton(
                user_settings.add_items_buttons[
                    "checked" if liver_cookies else "unchecked"
                ]["liver_cookies"],
                callback_data=CallBackData(
                    action=self.action,
                    items=f"{beef_lung_big_str} {beef_lung_small_str} {beef_liver_str} {beef_heart_str} {beef_mix_str} {not_liver_cookies_str}",
                ).str(),
            ),
            telebot.types.InlineKeyboardButton(
                user_settings.buy_button_text,
                callback_data=CallBackData(
                    action="buy",
                    items=f"{beef_lung_big_str} {beef_lung_small_str} {beef_liver_str} {beef_heart_str} {beef_mix_str} {liver_cookies_str}",
                ).str(),
            ),
        ]
