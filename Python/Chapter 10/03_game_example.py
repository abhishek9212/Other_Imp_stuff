class Remote():
    pass

class Player:
    def moveRight(self):  # encapsulation ---> Means we are wrapping one entity's things into one class i.e. all Player's methods are in Player class
        pass

    def moveLeft(self):
        pass

    def moveTop(self):
        pass

remote1 = Remote()
player1 = Player()

if(remote1.isLeftPressed()):  # abstraction ---> we got a layer of abstraction because we don't know what this function isLeftPressed() actually does.
    player1.moveLeft()   # oops is making this come close to the real world language that we use i.e. closer to the real world