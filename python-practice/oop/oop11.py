class Dancer:
    def __init__(self, style):
        self.style = style

    def dance(self):
        print(f'Dancing in {self.style}.')


class Singer:
    def __init__(self, genere):
        self.genere = genere

    def sing(self):
        print(f'Singing {self.genere} music.')   


class Artist:
    def __init__(self, painting_material):
        self.painting_material = painting_material

    def paint(self):
        print(f'Painting with {self.painting_material}')                         

class SuperHuman(Dancer, Singer, Artist):
    def __init__(self, style, genere, painting_material, sport):
        Dancer.__init__(self, style)
        Singer.__init__(self, genere)
        Artist.__init__(self, painting_material)
        self.sport = sport

    def play_sport(self):
        print(f'Playing {self.sport}.')

    def dance(self, competition):
        print(f'Dancing with {self.style} style in {competition} competition.')    


sh1 = SuperHuman('Hiphop', 'Classical', 'Acrolyc', 'Cricket')
sh1.dance('District Level')
sh1.play_sport()
sh1.paint()
