class Train:
    def __init__(self, name, seats, fare):
        self.Tname = name
        self.seats = seats
        self.fare = fare

    def getStatus(self):
        print("************")
        print(f"The name of the Train is {self.Tname}.\nNumber of seats available in {self.Tname} are {self.seats}")
        print("************")

    def getFare(self):
        print(f"The price of the ticket is: Rs. {self.fare}")

    def bookTicket(self):
        if(self.seats > 0):
            print(f"You got a seat!! Your seat number is {self.seats}")
            self.seats = self.seats - 1
        else:
            print("There is no seat available :(  Please try Tatkal.")

    def cancelTicket(self, seatNo):
        pass


train1 = Train("Rajdhani Express", 3, 300)
train1.getStatus()
train1.getFare()
train1.bookTicket()
train1.getStatus()
train1.bookTicket()
train1.bookTicket()
train1.getStatus()
train1.bookTicket()