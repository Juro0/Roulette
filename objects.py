class Slot:

    def __init__(self, name, color):
        self.name = name
        self.color = color
    
    def get_value(self):
        return self.name
    
    def get_color(self):
        return self.color

class Player:

    def __init__(self, name='Juri'):
        self.score = 0
        self.name = name
        self.cash = 1000
    
    def set_name(self, name):
        self.name = name

    def get_cash(self):
        return self.cash
    
    def sub_cash(self, amount):
        self.cash -= amount

    def add_cash(self, amount):
        self.cash += amount

    def get_name(self):
        return self.name

    def add_score(self, score):
        self.score += score
    
    def get_score(self):
        return self.score
    
    def select_play(self, puntata):
        self.puntata = puntata
    
    def get_play(self):
        return self.puntata
    
    def select_scommessa(self, scommessa):
        self.scommessa = scommessa
    
    def get_scommessa(self):
        return self.scommessa

uno = Slot("1","rosso")
due = Slot("2","nero")
tre = Slot("3","rosso")
quattro = Slot("4","nero")
cinque = Slot("5","rosso")
sei = Slot("6","nero")
sette = Slot("7","rosso")
otto = Slot("8","nero")
nove = Slot("9","rosso")
dieci = Slot("10","nero")
undici = Slot("11","rosso")
dodici = Slot("12","nero")
tredici = Slot("13","rosso")
quattordici = Slot("14","nero")
quindici = Slot("15","rosso")
sedici = Slot("16","nero")
diciasette = Slot("17","rosso")
diciotto = Slot("18","nero")
diciannove = Slot("19","rosso")
venti = Slot("20","nero")
ventuno = Slot("21","rosso")
ventidue = Slot("22","nero")
ventitre = Slot("23","rosso")
ventiquattro = Slot("24","nero")
venticinque = Slot("25","rosso")
ventisei = Slot("26","nero")
ventisette = Slot("27","rosso")
ventotto = Slot("28","nero")
ventinove = Slot("29","nero")
trenta = Slot("30","rosso")
trentuno = Slot("31","nero")
trentadue = Slot("32","rosso")
trentatre = Slot("33","nero")
trentaquattro = Slot("34","rosso")
trentacinque = Slot("35","nero")
trentasei = Slot("36","rosso")