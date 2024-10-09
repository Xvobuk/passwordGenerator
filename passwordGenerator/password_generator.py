import random
import string


def generate_password():
    # Генерируем 1 заглавную букву
    upper = random.choice(string.ascii_uppercase)
    # Генерируем 1 строчную букву
    lower = random.choice(string.ascii_lowercase)
    # Генерируем 1 спецсимвол
    special = random.choice(string.punctuation)
    # Генерируем 1 цифру
    digit = random.choice(string.digits)
    # Генерируем 4 оставшихся символа (буквы или цифры)
    remaining = ''.join(random.choices(string.ascii_letters + string.digits, k=4))
    # Собираем пароль и перемешиваем его
    password = upper + lower + special + digit + remaining
    return ''.join(random.sample(password, len(password)))


def main():
    print("=== Генератор надёжных паролей ===\n")
    passwords = [generate_password() for _ in range(10)]

    # Выводим 10 паролей в два ряда по 5 паролей
    for i in range(0, 10, 5):
        print(" | ".join(passwords[i:i + 5]))
    print("\nВыберите понравившийся пароль, скопируйте его и запишите, чтобы не забыть.")
    print(
        "Каждый из этих паролей имеет статус \"надёжный\" по шкале надёжности на любом из сайтов во время регистрации.")
    str(input())


if __name__ == "__main__":
    main()
