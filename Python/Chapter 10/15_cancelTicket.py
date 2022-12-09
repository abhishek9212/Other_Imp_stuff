class Train:
    def __init__(self, name, seats, fare):
        self.Tname = name
        self.fare = fare
        self.listSeats = []
        for i in range(1,seats+1):
            self.listSeats.append(i)

    def getStatus(self):
        numSeats = len(self.listSeats)
        print("************")
        print(f"The name of the Train is {self.Tname}.\nNumber of seats available in {self.Tname} are {numSeats}")
        print("************")

    def getFare(self):
        print(f"The price of the ticket is: Rs. {self.fare}")

    def bookTicket(self):
        if(len(self.listSeats) > 0):
            num = self.listSeats.pop()
            print(f"You got a seat!! Your seat number is {num}")     
        else:
            print("There is no seat available :(  Please try Tatkal.")

    def cancelTicket(self, seatNo):
        print(f"Your ticket has been successfully cancelled and your seat {seatNo} has been vacated:)")
        self.listSeats.append(seatNo)


train1 = Train("Rajdhani Express", 5, 300)
train1.getStatus()
train1.getFare()
train1.bookTicket()
train1.cancelTicket(14)
train1.bookTicket()
train1.bookTicket()
train1.bookTicket()
train1.bookTicket()
train1.bookTicket()
train1.bookTicket()
# train1.bookTicket()
# train1.getStatus()
# train1.bookTicket()
# train1.bookTicket()
# train1.getStatus()
# train1.bookTicket()