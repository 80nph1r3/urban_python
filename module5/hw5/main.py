from time import sleep


class User:
    def __init__(self, nickname: str, password: str, age: int) -> None:
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __eq__(self, value: object | str) -> bool:
        return self.__str__() == str(value)

    def __str__(self) -> str:
        return self.nickname


class Video:
    def __init__(self, title: str, duration: int, time_now=0, adult_mode=False) -> None:
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __eq__(self, value: object | str) -> bool:
        return self.__str__() == str(value)

    def __str__(self) -> str:
        return self.title

    def __contains__(self, item: str) -> bool:
        return item in self.__str__().lower()


class UrTube:
    def __init__(self) -> None:
        self.users = []
        self.videos = []
        self.current_user = None

    def register(self, nickname: str, password: str, age: int):
        if nickname in self.users:
            print(f"Пользователь {nickname} уже существует")
            return
        self.users.append(User(nickname, password, age))
        self.log_in(nickname, password)

    def log_in(self, nickname: str, password: str) -> None:
        try:
            user_index = self.users.index(nickname)
        except ValueError:
            print("Пользователь не найден")
            return
        if self.users[user_index].password == hash(password):
            self.current_user = self.users[user_index]

    def log_out(self) -> None:
        self.current_user = None

    def add(self, *videos: Video) -> None:
        for new_video in videos:
            if new_video in self.videos:
                continue
            self.videos.append(new_video)

    def get_videos(self, search_query: str) -> list[Video]:
        result = []
        for video in self.videos:
            if search_query.lower() in video:
                result.append(str(video))
        return result

    def watch_video(self, title: str) -> None:
        if not self.current_user:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return

        try:
            watched_video = self.videos[self.videos.index(title)]
        except ValueError:
            watched_video = None

        if not watched_video:
            return

        if watched_video.adult_mode and self.current_user.age < 18:
            print("Вам нет 18 лет, пожалуйста покиньте страницу")
            return

        for i in range(watched_video.time_now, watched_video.duration):
            print(i + 1, end=" ")
            sleep(1)
        print("Конец видео")
        watched_video.time_now = 0


if __name__ == "__main__":
    ur = UrTube()
    v1 = Video("Лучший язык программирования 2024 года", 200)
    v2 = Video("Для чего девушкам парень программист?", 10, adult_mode=True)

    # Добавление видео
    ur.add(v1, v2)

    # Проверка поиска
    print(ur.get_videos("лучший"))
    print(ur.get_videos("ПРОГ"))

    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video("Для чего девушкам парень программист?")
    ur.register("vasya_pupkin", "lolkekcheburek", 13)
    ur.watch_video("Для чего девушкам парень программист?")
    ur.register("urban_pythonist", "iScX4vIJClb9YQavjAgF", 25)
    v2.time_now = 5
    ur.watch_video("Для чего девушкам парень программист?")
    ur.watch_video("Для чего девушкам парень программист?")

    # Проверка входа в другой аккаунт
    ur.register("vasya_pupkin", "F8098FM8fjm9jmi", 55)
    print(ur.current_user)

    # Попытка воспроизведения несуществующего видео
    ur.watch_video("Лучший язык программирования 2024 года!")
