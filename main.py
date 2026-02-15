TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

#prihlaseni uzivatele
uzivatele = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

vstup_uzivatel = input("Napis uzivatelske jmeno: ")     
vstup_heslo = input("Napis heslo: ")

if vstup_uzivatel in uzivatele and uzivatele[vstup_uzivatel] == vstup_heslo:        
    print("Ahoj", vstup_uzivatel, "prihlaseni probehlo uspesne")     
else:
    print("Nespravne uzivatelske jmeno nebo heslo")     
    quit()

#Prace s texty
vstup_cislo_textu = (input("Zadej cislo vybraneho textu(1,2,3):" ))

#Zajisti bezchybny prubeh
if not vstup_cislo_textu.isdigit():
    print("Neplatne cislo textu, ukoncuji program.") 
    quit() 

vstup_cislo_textu_int = int(vstup_cislo_textu)

if 1 <= vstup_cislo_textu_int <= len(TEXTS):
    vybrany_text = TEXTS[vstup_cislo_textu_int - 1]
    print("Vybrany text: ", vybrany_text)
else:
    print("Neplatny vstup, ukoncuji program.")
    quit()

#Vystup analyzy textu
slova = vybrany_text.split()
pocet_slov = len(slova)
print("There are", pocet_slov, "words in the selected text")

slova_cap = slova.c