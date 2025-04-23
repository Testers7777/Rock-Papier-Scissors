import random

choices = {'Papier', 'Pierre', 'Ciseaux'}

score = {
    "Pierre Papier": "Papier",
    "Papier Ciseaux": "Ciseaux",
    "Ciseaux Pierre": "Pierre",
    "Papier Papier": "Rematch",
    "Pierre Pierre": "Rematch",
    "Ciseaux Ciseaux": "Rematch"
}

mapping = {
    "P": "Pierre",
    "Pa": "Papier",
    "C": "Ciseaux",
    "p": "Pierre",
    "pa": "Papier",
    "c": "Ciseaux"
}

def play():
    while True:
        userInput = input('👊 Pierre (P) ✋ Papier (Pa) ou ✌️ Ciseaux (C) ? ').capitalize()
        
        userChoice = mapping.get(userInput, userInput.capitalize())

        if userChoice not in choices:
            print('❌ Choix invalide.')
        else:
            botChoice = random.choice(list(choices))
            print(f"🤖 Bot a choisi : {botChoice}")

            key1 = f"{userChoice} {botChoice}"
            key2 = f"{botChoice} {userChoice}"

            if key1 in score:
                winner = score[key1]
            elif key2 in score:
                winner = score[key2]
            else:
                winner = "Erreur"

            if winner == "Rematch":
                print("🔁 Match nul")
            else:
                print(f"🏆 {winner} gagne !")
                
        playAgain = str(input('Voulez-vous rejouer ? (Y/N)')).upper()
        if playAgain == "Y":
            play()
        else:
            print('Bonne journée !')
            break

play()