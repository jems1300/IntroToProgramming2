class TV:
    def __init__(self, channel= None, volumeLevel = None, on =None):
        self.channel = channel
        self.volumeLevel = volumeLevel
        self.on = on

    #These are void
    def turnOn(self):
        if self.on == False and self.on == None:
            self.on = True

    def turnOff(self):
        if self.on == True:
            self.on =False

    def setChannel(self, newChannel):
        if 1 < newChannel < 120:
            self.channel = newChannel

    def channelUp(self):
        if self.channel == 120:
            self.channel = 1
        else:
            self.channel += 1

    def channelDown(self):
        if self.channel == 1:
            self.channel = 120
        else:
            self.channel -= 1

    # def volumeUp(self):
    #     self.volumeLevel += 10
    #     print("You turned up the TV volume by 10")
    #
    # def volumeDown(self):
    #     self.volumeLevel -= 10
    #     print("You turned down the TV volume by 10")
