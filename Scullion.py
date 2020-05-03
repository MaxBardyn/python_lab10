class Scullion(object):

    def __init__(self, water_consumption=580, number_of_programs=1, brand="Unknown",
                 weight=100, id_number=10000, name="None", color="white"):
        self.water_consumption = water_consumption
        self.number_of_programs = number_of_programs
        self.brand = brand
        self.weight = weight
        self.id = id_number
        self.name = name
        self.color = color
        Scullion.number += 1

    def __del__(self):
        print(self.name + ' sold')

    def __str__(self):
        return 'water_consumption=' + str(self.water_consumption) + ', water_consumption=' + str(
            self.water_consumption) + ', brand=' + str(
            self.brand) + ', weight=' + str(self.weight) + ", model=" + str(self.id) + ', name=' + str(
            self.name) + ', color=' + str(self.color) + ')'

    number = 0

    @staticmethod
    def get_number():
        return Scullion.number


if __name__ == '__main__':
    first_scullion = Scullion(water_consumption=100, number_of_programs=2, brand="Opel",
                              weight=234, id_number=10010, name="Petro", color="red")
    print(first_scullion)
    print(Scullion.get_number())
    second_scullion = Scullion(water_consumption=500, number_of_programs=3, brand="Intel",
                               weight=50, id_number=10210, name="btr", color="black")
    print(second_scullion)
    print(Scullion.get_number())
    third_scullion = Scullion(water_consumption=300, number_of_programs=9, brand="LG",
                              weight=32, id_number=11111, name="s-700", color="orange")
    print(third_scullion)
    print(Scullion.get_number())
