class SuperHero():
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def print_name(self):
        print(f"name: {self.name}")

    def hp2(self):
        print(f"health_points: {self.health_points * 2}")

    def __str__(self):
        return f"nickname: {self.nickname},\n" \
               f"superpower: {self.superpower}\n" \
               f"health_points: {self.health_points}"

    def __len__(self):
        print("catchphrase: ",len(self.catchphrase))


Hero = SuperHero(name='Чёрная_Пантера', nickname='Пантера', superpower='Сила', health_points=100,catchphrase='Ваканда навеки!')
Hero.print_name()
Hero.hp2()
Hero.__len__()
print(Hero)