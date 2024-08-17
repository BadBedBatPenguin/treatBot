class UserSettings:
    main_menu = [
        ("Наличие", "items"),
    ]
    welcome_message = (
        "Добро пожаловать в TreatsBot!\n\n"
        "Телеграм-бот, в котором Вы сможете заказать сушеные лакомства для своих питомцев."
    )
    welcome_menu_text = "Заказать лакомства"
    beef_lung_big = "Говяжье лёгкое крупное"
    beef_lung_small = "Говяжье лёгкое мелкое"
    beef_liver = "Говяжья печень"
    beef_heart = "Говяжье сердце"
    beef_mix = "Говяжий микс"
    liver_cookies = "Печёночное печенье"
    buttons_names = {
        "beef_lung_big": beef_lung_big,
        "beef_lung_small": beef_lung_small,
        "beef_liver": beef_liver,
        "beef_heart": beef_heart,
        "beef_mix": beef_mix,
        "liver_cookies": liver_cookies,
    }
    add_items_buttons = {
        "unchecked": {
            "beef_lung_big": f"⬜️{beef_lung_big}",
            "beef_lung_small": f"⬜️{beef_lung_small}",
            "beef_liver": f"⬜️{beef_liver}",
            "beef_heart": f"⬜️{beef_heart}",
            "beef_mix": f"⬜️{beef_mix}",
            "liver_cookies": f"⬜️{liver_cookies}",
        },
        "checked": {
            "beef_lung_big": f"✅{beef_lung_big}",
            "beef_lung_small": f"✅{beef_lung_small}",
            "beef_liver": f"✅{beef_liver}",
            "beef_heart": f"✅{beef_heart}",
            "beef_mix": f"✅{beef_mix}",
            "liver_cookies": f"✅{liver_cookies}",
        },
    }
    main_menu_title = "Выберите товар"
    buy_button_text = "Заказать"
    buy_report = "Ваш заказ принят.\nМы с вами свяжемся для уточнения деталей"
    accept_button_name = "Подтвердить"
    buy_form = [
        "Сколько грамм говяжьего лёгкого крупного вы хотите заказать?",
        "Сколько грамм говяжьего лёгкого мелкого вы хотите заказать?",
        "Сколько грамм говяжьей печени вы хотите заказать?",
        "Сколько грамм говяжьего сердца вы хотите заказать?",
        "Сколько грамм говяжьего микса вы хотите заказать?",
        "Сколько грамм печёночного печенья вы хотите заказать?",
        "В каком городе вы находитесь?",
    ]
    accept_form_report = "Ваш заказ принят"
    buy_message = (
        "Заявка на покупку:\nПользователь: @{username}\n"
        "Город: {city}\n"
        "Говяжье лёгкое крупное: {beef_lung_big} гр.\n"
        "Говяжье лёгкое мелкое: {beef_lung_small} гр.\n"
        "Говяжья печень: {beef_liver} гр.\n"
        "Говяжье сердце: {beef_heart} гр.\n"
        "Говяжий микс: {beef_mix} гр.\n"
        "Печёночное печенье: {liver_cookies} гр."
    )


class CommonSettings:
    manager_chat_id = 629909066
    # manager_chat_id = 569791598
    default_photo = ""
    back_button_text = "Назад"
    no_item_selected = (
        "Вы не выбрали ни одного товара. Пожалуйста, выберите хотя бы один товар."
    )
    error_message = "Произошла ошибка"


user_settings = UserSettings()
common_settings = CommonSettings()
