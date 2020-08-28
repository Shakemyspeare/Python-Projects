#parent class
class Home:
    rooms = 4
    sqft = 1500
    entrances = 1
    def homeConfig(self):
        print('Your house has {} rooms, is {} square feet, and has {} entrance!'.format(self.rooms, self.sqft, self.entrances))


#child class
class House(Home):
    entrances = 2
    floors = 2
    basement = False
    def homeConfig(self):
        print('Your house has {} rooms, is {} square feet, has {} entrance, \nand is {} stories tall!'.format(self.rooms, self.sqft, self.entrances, self.floors))


#another child class
class Condo(Home):
    sqft = 1100
    renting = True
    floorNumber = 2
    def homeConfig(self):
        print('Your house has {} rooms, is {} square feet, has {} entrance, \nand you live on floor number {}!'.format(self.rooms, self.sqft, self.entrances, self.floorNumber))
    
if __name__ == "__main__":

    home1 = Home()
    home2 = House()
    home3 = Condo()

    home1.homeConfig()
    home2.homeConfig()
    home3.homeConfig()
    
