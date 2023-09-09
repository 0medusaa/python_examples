import random

bots = ['bot_1', 'bot_2', 'bot_3', 'bot_4', 'bot_5']
users = {
    'medusa': {
        'password': '123',
        'safe': 1000
    },
}

def roll_dice():
    return random.randint(1, 6), random.randint(1, 6)


def login():
    while True:
        username = input("Kullanıcı adınızı giriniz: ")
        password = input("Şifrenizi giriniz: ")

        if username in users and users[username]['password'] == password:
            print(f"Hoşgeldin {username}")
            play_game(username)
            break
        else:
            print("Geçersiz kullanıcı adı veya şifre! Lütfen tekrar deneyin.")


def play_game(username):
    bot = random.choice(bots)
    print(f"{bot} ile oynayacaksınız")

    while True:
        bet = float(input("Bahis miktarınızı girin: "))

        if bet > users[username]['safe']:
            print("Sahip olduğunuzdan daha fazla bahis yapamazsınız!")
            continue

        dice_roll = roll_dice()
        print(f"Atılan zarlar: {dice_roll}")

        if sum(dice_roll) in [7, 11]:
            print("Tebrikler, kazandınız!")
            users[username]['safe'] += bet
        else:
            print("Üzgünüm, kaybettiniz.")
            users[username]['safe'] -= bet

        print(f"Yeni bakiyeniz: {users[username]['safe']}")

        play_again = input("Devam etmek istiyor musunuz? (Evet/Hayır): ")
        if play_again.lower() != 'evet':
            break


login()