import random
import sys
import os
os.system("pip install colorama termcolor")
import colorama
colorama.init()
from termcolor import cprint

numbers = [
    ['cero', ' 0'],
    ['uno', '1'],
    ['dos', '2'],
    ['tres', '3'],
    ['cuatro', '4'],
    ['cinco', '5'],
    ['seis', '6'],
    ['siete', '7'],
    ['ocho', '8'],
    ['nueve', '9'],
    ['diez', '10'],
    ['once', '11'],
    ['dose', '12'],
    ['trece', '13'],
    ['catorce', '14'],
    ['quince', '15'],
    ['dieciseis', '16'],
    ['diecisiete', '17'],
    ['dieciocho', '18'],
    ['diecinueve', '19'],
    ['veinte', '20'],
    ['veintiuno', '21'],
    ['veintidos', '22'],
    ['veintitres', '23'],
    ['veinticuatro', '24'],
    ['veinticinco', '25'],
    ['veintiseis', '26'],
    ['veintisiete', '27'],
    ['veintiocho', '28'],
    ['veintinueve', '29'],
    ['treinta', '30'],
    ['treinta y uno', '31'],
    ['treinta y dos', '32'],
    ['treinta y tres', '33'],
    ['treinta y cuatro', '34'],
    ['treinta y cinco', '35'],
    ['treinta y seis', '36'],
    ['treinta y siete', '37'],
    ['treinta y ocho', '38'],
    ['treinta y nueve', '39'],
    ['cuarenta', '40'],
    ['cuarenta y uno', '41'],
    ['cuarenta y dos', '42'],
    ['cuarenta y tres', '43'],
    ['cuarenta y cuatro', '44'],
    ['cuarenta y seis', '46'],
    ['cuarenta y cinco', '45'],
    ['cuarenta y siete', '47'],
    ['cuarenta y ocho', '48'],
    ['cuarenta y nueve', '49'],
    ['cincuenta', '50'],
    ['cincuenta y uno', '51'],
    ['cincuenta y dos', '52'],
    ['cincuenta y tres', '53'],
    ['cincuenta y cuatro', '54'],
    ['cincuenta y cinco', '55'],
    ['cincuenta y seis', '56'],
    ['cincuenta y cinco', '55'],
    ['cincuenta y siete', '57'],
    ['cincuenta y ocho', '58'],
    ['cincuenta y nueve', '59'],
    ['sesenta', '60'],
    ['sesenta y uno', '61'],
    ['sesenta y dos', '62'],
    ['sesenta y tres', '63'],
    ['sesenta y cuatro', '64'],
    ['sesenta y cinco', '65'],
    ['sesenta y seis', '66'],
    ['sesenta y siete', '67'],
    ['sesenta y ocho', '68'],
    ['sesenta y nueve', '69'],
    ['setenta', '70'],
    ['setenta y uno', '71'],
    ['setenta y dos', '72'],
    ['setenta y tres', '73'],
    ['setenta y cuatro', '74'],
    ['setenta y cinco', '75'],
    ['setenta y seis', '76'],
    ['setenta y siete', '77'],
    ['setenta y ocho', '78'],
    ['setenta y nueve', '79'],
    ['ochenta', '80'],
    ['ochenta y uno', '81'],
    ['ochenta y dos', '82'],
    ['ochenta y tres', '83'],
    ['ochenta y cuatro', '84'],
    ['ochenta y cinco', '85'],
    ['ochenta y seis', '86'],
    ['ochenta y siete', '87'],
    ['ochenta y ocho', '88'],
    ['ochenta y nueve', '89'],
    ['noventa', '90'],
    ['noventa y uno', '91'],
    ['noventa y dos', '92'],
    ['noventa y tres', '93'],
    ['noventa y cuatro', '94'],
    ['noventa y cinco', '95'],
    ['noventa y seis', '96'],
    ['noventa y siete', '97'],
    ['noventa y ocho', '98'],
    ['noventa y nueve', '99'],
    ['cien', '100']
]


try:
    os.system("clear")
except:
    os.system("clear")

CORRECT_MESSAGE = "\n"*5 + "."*10 + "\n¡Correcto!\nBuen trabajo\n" + "."*10 + "\n"*5
WRONG_MESSAGE = "\n"*5 + "¡Incorrecto!" + "\n"*5

while True:
    qnum = random.choice(numbers)
    question = "what is \"{}\" in English? >> ".format(qnum[0])

    player = input(question)

    if "q" in player.lower() or "quit" in player.lower():
        sys.exit()
    elif player == qnum[1]:
        cprint(CORRECT_MESSAGE, color="green")
    else:
        print("\n#HINT#")
        hints = [qnum[1],
         random.choice(numbers)[1]]


        hint1 = random.choice([0, 1])

        hint2 = 0 if hint1 is 1 else 1
        player = input("Is it {} or {}? >> ".format(hints[hint1],
         hints[hint2])
        )
        
        if "q" in player.lower() or "quit" in player.lower():
            sys.exit()
        elif player == qnum[1]:

            cprint(CORRECT_MESSAGE, color="green")
        else: cprint(WRONG_MESSAGE, color="red")
