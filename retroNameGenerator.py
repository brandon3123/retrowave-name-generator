import random

retroWavePhrases = ["Cassette", "Photon",
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


bigBanner =   "************************************************************ "
smallBanner = "*************************** "

knight = "                    _.--.    .--._\n"\
"                  .'  .'      '.  '.\n" \
"                 ;  .'    /\    '.  ;\n" \
"                 ;  '._,-/  \-,_.`  ;\n" \
"                 \  ,`  / /\ \  `,  /\n" \
"                  \/    \/  \/    \/\n" \
"                  ,=_    \/\/    _=,\n" \
"                  |  '_   \/   _'  |\n" \
"                  |_   ''-..-''   _|\n" \
"                  | '-.        .-' |\n" \
"                  |    '\    /'    |\n" \
"                  |      |  |      |\n" \
"          ___     |      |  |      |     ___\n" \
"      _,-',  ',   '_     |  |     _'   ,'  ,'-,_\n" \
"    _(  \  \   \=-- -.  |  |  .- --= /   /  /  )_\n" \
" ,   \  \  \   \       -'--'-       /   /  /  /   .\n" \
"!     \  \  \   \                  /   /  /  /     !\n" \
":      \  \  \   \                /   /  /  /      TK\n"\

superCar ="                    ___..............._\n"\
"          __.. ' _'.'''''''''\\'''''''''- .`-._\n"\
" ______.-'         (_) |      \\           ` \\`-. _\n"\
"/_       --------------'-------\\---....______\\__`.`  -..___\n"\
"| T      _.----._           Xxx|x...           |          _.._`--. _\n"\
"| |    .' ..--.. `.         XXX|XXXXXXXXXxx==  |       .'.---..`.     -._\n"\
"\_j   /  /  __  \  \        XXX|XXXXXXXXXXX==  |      / /  __  \ \        `-.\n"\
" _|  |  |  /  \  |  |       XXX|""'            |     / |  /  \  | |          |\n"\
"|__\_j  |  \__/  |  L__________|_______________|_____j |  \__/  | L__________J\n"\
"     `'\ \      / ./__________________________________\ \      / /___________\n"\
"        `.`----'.'   dp                                `.`----'.'\n"\
"          `'''''                                         `'''''\n"\

cassette ="      ___________________________________________\n"\
"      |  _______________________________________  |\n"\
"      | / .-----------------------------------. \ |\n"\
"      | | | /\ :                        90 min| | |\n"\
"      | | |/--\:....................... NR [ ]| | |\n"\
"      | | `-----------------------------------' | |\n"\
"      | |      //- \   |         |   //- \      | |\n"\
"      | |     ||( )||  |_________|  ||( )||     | |\n"\
"      | |      \ -//   :....:....:   \ -//      | |\n"\
"      | |       _ _ ._  _ _ .__|_ _.._  _       | |\n"\
"      | |      (_(_)| |(_(/_|  |_(_||_)(/_      | |\n"\
"      | |               low noise   |           | |\n"\
"      | `______ ____________________ ____ ______' |\n"\
"      |        /    []             []    \        |\n"\
"      |       /  ()                   ()  \       |\n"\
"      !______/_____________________________\______!\n"\


retroWaveAsciiList = [knight, superCar, cassette]

## generates a RetroWave name
def generateRetroName():

    firstName = fetchPhraseFromList()
    secondName = fetchPhraseFromList()

    while secondName == firstName:
        secondName = fetchPhraseFromList()

    return firstName + " " + secondName

## Randomly select a retro wave phrase
def fetchPhraseFromList():
    return retroWavePhrases[random.randint(0, len(retroWavePhrases) - 1)]

## Randomly select a finishing slogan
def fetchSloganFromList():
    return slogans[random.randint(1, len(slogans) - 1)]

## Randomly select an ascii art image
def fetchAsciiArtFromList():
    return retroWaveAsciiList[random.randint(0, len(retroWaveAsciiList) - 1)]

print(logo + "\n" + "\n")

userInput = ""

while userInput != "0":
    userInput = raw_input("Press 'Enter' to generate a RetroWave name or input '0' to terminate program.....")
    if userInput != "0":
        print("\n\n"
              + "\n\n "
              + fetchAsciiArtFromList()
              + "\n         "
              + fetchSloganFromList()
              + "....." + generateRetroName() + "!"
              + "            \n"
              + "\n\n")
