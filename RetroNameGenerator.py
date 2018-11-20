import random

retroWaveNameList = ["Cassette", "Photon",
                     "Mega", "Omega", "Shine", "Tape", "Ninja", "Captain", "Force", "Drive", "Synth",
                     "Laser", "Max", "Night", "Cruise", "Star", "Captain", "Cyber", "Droid", "Boom",
                     "Neon", "Grid", "Electro", "Rocket", "Dynamic", "Edge", "Thunder", "Major",
                     "Magnum", "Tech", "Guy", "System", "Burner", "Rouge", "Velvet", "Future", "Nitro",
                     "Matrix", "FM", "AC", "Glove", "Slash", "Energy", "Maverick", "Gun", "Groove",
                     "Bishop", "Wave", "Turbo", "Sunset", "Racer", "Killer", "87", "88", "Vice", "Runner",
                     "Arcade", "Player", "Disco", "64", "12", "City", "Midnight", "Horizon", "Beach" 
                     "Blue", "Style", "Viper", "Panther", "Snake", "Razor", "Track", "44", "Finisher",
                     "Groovy", "Sharp", "Miami", "Fuel", "Cosmic", "Space", "Renegade", "Tune", "Retro", "Throwback",
                     "Outcast", "Dancer"]

slogans = ["Welcome to the fight", "Brave the front", "The hero we need", "Prepare yourself", "Destiny has found you",
           "The worlds fate is yours", "Enter at your own risk"]

logo = "*******************************************************************"\
"\n** ________     _____             ___       __                    **"\
"\n** ___  __ \______  /_______________ |     / /_____ ___   ______  **"\
"\n** __  /_/ /  _ \  __/_  ___/  __ \_ | /| / /_  __ `/_ | / /  _ \\ **"\
"\n** _  _, _//  __/ /_ _  /   / /_/ /_ |/ |/ / / /_/ /__ |/ //  __/ **"\
"\n** /_/ |_| \___/\__/ /_/    \____/____/|__/  \__,_/ _____/ \___/  ** " \
"\n**                                                                **" \
"\n*******************************************************************"\


banner = "************************************************************ " \

# During name generation, I need to make sure that both names arent a number.....look this up at home.
def generateRetroName():

    firstName = fetchNameFromList()
    secondName = fetchNameFromList()

    while secondName == firstName:
        secondName = fetchNameFromList()

    return firstName + " " + secondName



def fetchNameFromList():
    return retroWaveNameList[random.randint(1, len(retroWaveNameList) - 1)]

def fetchSloganFromList():
    return slogans[random.randint(1, len(slogans) - 1)]

print(logo)
userInput = ""
while userInput != "0":
    userInput = input("Press enter to generate a RetroWave name or input '0' to terminate program.....")
    if userInput != "0":
        print(banner
              + "\n         "
              + fetchSloganFromList()
              + "....." + generateRetroName() + "!"
              + "            \n"
              + banner)
