import random

def games_choices():
    p_choice = input("Pilihlah (gunting, batu, kertas): ")
    choice = ["gunting","batu","kertas"]
    ai_choice = random.choice(choice)
    choices = {"pemain": p_choice, "musuh": ai_choice}
    return choices

def sistem_win(pemain, musuh):
    print(f"Kamu memilih {pemain}, Musuh memilih{musuh}")
    if pemain == musuh: 
        return "Hasilnya seri!"
    elif pemain == "batu":
        if musuh == "gunting":
            return "Batu menghancurkan gunting! Kamu menang!"
        else:
            return "Kertas membungkus batu! Kamu kalah."
    elif pemain == "gunting":
        if musuh == "kertas":
            return "Gunting memotong kertas! Kamu menang!"
        else:
            return "Batu menghancurkan gunting! Kamu kalah."
    elif pemain == "kertas":
        if musuh == "batu":
            return "Kertas membungkus batu! Kamu menang!"
        else:
            return "Gunting memotong kertas! Kamu kalah."

choices = games_choices()
hasil = sistem_win(choices["pemain"], choices["musuh"])
print(hasil)
