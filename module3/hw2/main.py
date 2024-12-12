import re


def send_email(
    message: str, recipient: str, sender="university.help@gmail.com"
) -> None:
    if not (is_valid_email(recipient) and is_valid_email(sender)):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    elif sender == recipient:
        print("Нельзя отправить письмо самому себе!")
    elif sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(
            f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо успешно отправлено с адреса {sender} на адрес {recipient}."
        )


def is_valid_email(email: str) -> bool:
    if re.search("@", email) and re.search(r"\.(com|net|ru)$", email):
        return True
    return False


if __name__ == "__main__":
    send_email("Это сообщение для проверки связи", "vasyok1337@gmail.com")
    send_email(
        "Вы видите это сообщение как лучший студент курса!",
        "urban.fan@mail.ru",
        sender="urban.info@gmail.com",
    )
    send_email(
        "Пожалуйста, исправьте задание",
        "urban.student@mail.ru",
        sender="urban.teacher@mail.uk",
    )
    send_email(
        "Напоминаю самому себе о вебинаре",
        "urban.teacher@mail.ru",
        sender="urban.teacher@mail.ru",
    )
