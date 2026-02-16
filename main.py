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

vstup_uzivatel = input("Enter your username: ")     
vstup_heslo = input("Enter your password: ")

if vstup_uzivatel in uzivatele and uzivatele[vstup_uzivatel] == vstup_heslo:        
    print("-"*40)
    print("Welcome to the app,", vstup_uzivatel)  
    print("We have 3 texts to be analyzed.")
    print("-"*40)
else:
    print("Unregistered user, terminating the program.")     
    quit()

#Prace s texty
vstup_cislo_textu = (input("Enter a number btw. 1 and 3 to select: "))

#Zajisti bezchybny prubeh
if not vstup_cislo_textu.isdigit():
    print("Invalid text number, terminating the program.") 
    quit() 

vstup_cislo_textu_int = int(vstup_cislo_textu)

if 1 <= vstup_cislo_textu_int <= len(TEXTS):
    vybrany_text = TEXTS[vstup_cislo_textu_int - 1]
    #print("Selected text: ", vybrany_text)
else:
    print("Invalid input, terminating the program.")
    quit()

#Vystup analyzy textu
slova = vybrany_text.split()
pocet_slov = len(slova)
print("-"*40)
print("There are", pocet_slov, "words in the selected text.")

pocet_velkych_pismen = 0
for slovo in slova:
    if slovo[0].isupper():
        pocet_velkych_pismen +=1
print("There are", pocet_velkych_pismen, "titlecase words.")

pocet_velkych_slov = 0
for slovo in slova:
    if slovo.isupper():
        pocet_velkych_slov +=1 
print("There are", pocet_velkych_pismen, "uppercase words.")

pocet_malych_slov = 0
for slovo in slova:
    if slovo.islower():
        pocet_malych_slov +=1 
print("There are", pocet_malych_slov, "lowercase words.")

pocet_cisel = 0
for slovo in slova:
    if slovo.isdigit():
        pocet_cisel +=1 
print("There are", pocet_cisel, "numeric strings.")

soucet_cisel = 0
for slovo in slova:
    if slovo.isdigit():
        soucet_cisel += int(slovo) 
print("The sum of all the numbers is", soucet_cisel)
print("-"*40)
print("LEN| ", "OCCUENCES   |", "NR.")
print("-"*40)

slova = vybrany_text.split()
ciste_slova = []
for slovo in slova:
    ciste_slova.append(slovo.strip(".,':;!?"))

graf = {}
delka_cisteho_slova = 1

for ciste_slovo in ciste_slova:
    delka_cisteho_slova = len(ciste_slovo)
    if delka_cisteho_slova in graf:
        graf[delka_cisteho_slova] = graf[delka_cisteho_slova] + 1
    else:
        graf[delka_cisteho_slova] = 1

for delka_cisteho_slova in sorted(graf):
    print(delka_cisteho_slova, "|", "*" * graf[delka_cisteho_slova])