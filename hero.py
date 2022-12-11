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
        print(f"health_points * 2: {self.health_points * 2}")

    def __str__(self):
        return f"nickname: {self.nickname},\n" \
               f"superpower: {self.superpower}\n" \
               f"health_points: {self.health_points}"

    def __len__(self):
        print("catchphrase: ", len(self.catchphrase))


Hero = SuperHero(name='Чёрная_Пантера', nickname='Пантера', superpower='Сила', health_points=100,
                 catchphrase='Ваканда навеки!')
Hero.print_name()
Hero.hp2()
Hero.__len__()
print(Hero)

#new_hw
class SuperHero2(SuperHero):
    siski = 'siski'

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage, fly=False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = fly

    def hp2(self):
        self.fly = True
        print(f"health_points ** 2: {self.health_points ** 2}")


superhero2 = SuperHero2(name='Joker', nickname='Artur', superpower='Smile', health_points=50, catchphrase='AXAXAXAXAXA', damage=20)
superhero2.hp2()
print(superhero2)


class SuperHero3(SuperHero):
    jopa = 'jopa'

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage, fly=False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = fly

    def hp2(self):
        self.fly = True
        print(f"health_points ** 2: {self.health_points ** 2}")

    def print_phrase(self):
        print('fly in the True_phrase')


superhero3 = SuperHero3(name='Flash', nickname='Barry_Allen', superpower='speed', health_points=100,
                        catchphrase='Я-скорость!', damage=20)
superhero3.hp2()
print(superhero3)
superhero3.print_phrase()


class Villain(SuperHero3):
    people = "monster"

    def gen_x(self):
        pass

    def crit(self, damage):
        print(f'damage ** 3: {damage ** 2}')


villain = Villain(name='Thanos', nickname='Titan', superpower='Сверхчеловеческая', health_points=50,
                  catchphrase='Не смогли смириться с поражением!', damage=20)

print(villain)
villain.gen_x()
villain.crit(superhero3.damage)