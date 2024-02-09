from random import randint
import requests
from datetime import datetime, timedelta
import time

class Pokemon:
    pokemons = {}
    # Инициализация объекта (конструктор)
    def _init_(self, pokemon_trainer):

        self.pokemon_trainer = pokemon_trainer

        self.pokemon_number = randint(1,1000)
        self.img = self.get_img()
        self.name = self.get_name()
        self.last_feed_time = datetime.now()

        self.hp = randint(25,100)
        self.power = randint(5,15)

        Pokemon. pokemons [pokemon_trainer] = self

    # Метод для получения картинки покемона через API
    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['forms'][0]['name'])
        else:
            return "Pikachu"
    
    # Метод для получения имени покемона через API
    def get_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['sprites']['other']['home']['front_default'])
        else:
            return "Pikachu"


    # Метод класса для получения информации
    def info(self):
        return f"""Имя твоего покеомона: {self.name}
силы покемона: {self.power}
здоровье покемона: {self.hp}"""
    
    def attack(self, enemy):
        if isinstance(enemy, Wizard): # Проверка на то, что enemy является типом данных Wizard (является экземпляром класса Волшебник)
            chance = randint(1,5)
            if chance == 1:
                return "Покемон-волшебник применил щит в сражении"
        if enemy.hp > self.power:
            enemy.hp -= self.power
            return f"Сражение @{self.pokemon_trainer} с @{enemy.pokemon_trainer}"
        else:
            enemy.hp = 0
            return f"Победа @{self.pokemon_trainer} над @{enemy.pokemon_trainer}! "

    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img
    
    def feed(self):
        #логика кормления покемона
        self.satiety_level += 1

        #обновлени евремни последнего кормления
        self.last_fed = datetime.datetime.now()


class Fighter(Pokemon):
    def attack(self, enemy):
        super_power = randint(5,15)
        self.power += super_power
        result = super().attack(enemy)
        self.power -= super_power
        return result + f"\n Боец применил супер-атаку силой:{super_power}"

class Wizard(Pokemon):
    def feed(self):
        return super(). feed(10)

p = Pokemon("user1")
time.sleep(11)
print(p.feed())


