class Robot:
    def __init__(self, name, version):
        self.name = name
        self.version = version

    def move_forward(self):
        print(f'{self.name}-{self.version} is moving Forward.')
        # return f'{self.name}-{self.version} is moving Forward.'

    def move_backward(self):
        return f'{self.name}-{self.version} is moving Backward.'

    def move_left(self):
        return f'{self.name}-{self.version} is moving Left.' 

    def move_right(self):
        return f'{self.name}-{self.version} is moving Right.'               


class HouseBot(Robot):
    def __init__(self, name, version, activation_date, area_covered):
        Robot.__init__(self, name, version)
        self.activation_date = activation_date
        self.area_covered = area_covered

    def check_test(self):
        return f'BOT Activation Date: {self.activation_date}'

    def cleaned_area(self):
        if self.area_covered > 0:
            print(f'{self.name} is Cleaning The House!')
            self.area_covered -= 10
            if self.area_covered < 0:
                self.area_covered = 0
        else:
            print('RESET The Area Cover Value!')

    # @classmethod        
    def set_area_cover(self, area):
        if self.area_covered == 0:
            self.area_covered = area
        else:
            print('I can CLEAN More!')

    # method overriding

    def move_forward(self):
        print('I am from Another Class.')
        super().move_forward()                                 

hbot = HouseBot('ROBO', '1.1.1', '26/11/21', 20)
hbot1 = HouseBot('ROBO', '1.1.1', '28/11/21', 20)
robo = Robot('Stan Le', '1.1.2')
# print(hbot.move_forward())
# hbot.move_forward()
# print(hbot.check_test())
# print(hbot.area_covered)
# hbot.cleaned_area()
# hbot.cleaned_area()
# hbot.cleaned_area()
# hbot.area_covered = 30
# HouseBot.area_covered = 30
# print(hbot.area_covered)
# print(hbot1.area_covered)

# print(robo.name)
# print(help(hbot))
print(issubclass(HouseBot, Robot))
print(isinstance(Robot, object))
