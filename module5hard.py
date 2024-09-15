import hashlib
import time

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hashlib.sha256(password.encode()).hexdigest()
        self.age = age

    def __str__(self):
        return self.nickname

    def __eq__(self, other):
        return other.nickname == self.nickname

class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title   #заголовок, строка
        self.duration = duration   #продолжительность, секунды?
        self.time_now = time_now       #секунда остановки (изначально 0)?
        self.adult_mode = adult_mode # ограничение по возрасту, bool (False по умолчанию)?
        #time.sleep(time_now)

class UrTube():

    def __init__(self):
        self.users = []              #список объектов User
        self.videos = []    #список объектов Video
        self.current_user = None     #текущий пользователь
        self.age = int


    def log_in(self, nickname, password): #авторизоваться
        self.password = hashlib.sha256(password.encode()).hexdigest()
        for user in self.users:
            if current_user.nickname == nickname and current_user.password == self.password:
                self.current_user = user
            else:
                print("Неверный логин или пароль")

    def register(self, nickname, password, age):  # зарегистрироваться
        new_user = User(nickname, password, age)
        if new_user not in self.users:
            # if self.current_user == nickname:
            self.current_user = new_user
            self.users.append(new_user)
            # print('Вход выполнен, регистрация прошла успешно')
        else:
            print(f"Пользователь {nickname} уже существует")

    def log_out(self): # выход из системы
        self.current_user = None

    def add(self, *videos):
        for video in videos:
            if all(v.title != video.title for v in self.videos):
                self.videos.append(video)

    def get_videos(self, search_word): #search_word - поисковое слово
        return [video.title for video in self.videos if search_word.lower() in video.title.lower()]

    def watch_video(self, title):
        if self.current_user is None:
            print('Войдите в аккаунт чтобы смотреть видео')
            return
        for video in self.videos:
            if title == video.title:
                if video.adult_mode and self.current_user.age >= 18:
                    while video.time_now < video.duration:
                        video.time_now += 1
                        print(video.time_now, end=' ')
                        time.sleep(1)
                    video.time_now = 0
                    print('Конец видео')
                else:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                break

ur = UrTube()
ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# print(v1)

# Добавление видео
ur.add(v1, v2)
# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')



