from methods_v2 import *
from tkinter import *
# ###############################################################################
BUTTON_FONT = ('Courier', 12, 'bold')
BUTTON_FONT2 = ('Helvetica', 12, 'bold')
# ###############################################################################


# ################### SCANNER #################################################
def scan():
    text_to_check = text1.get("1.0", END)  # Gets current value in textbox at line 1, character 0
    print(text_to_check)
    words_list = text_to_check.lower().split()
    dictionary = get_dictionary()
    mispelled_words = get_misspelled(dictionary, words_list)
    reprint_text(text1, words_list, mispelled_words)
    suggestions = get_suggestions(dictionary, mispelled_words)
    print_suggestions(text2, words_list, mispelled_words, suggestions)


# ############################## UI SETUP ################################################
window = Tk()
# window.geometry('950x700')
window.title("Spell Checker")
window.config(padx=50, pady=20, bg='gainsboro')
# ----------------- IMAGE --------------------------------------------------------------
canvas = Canvas(width=500, height=160, bg='gainsboro', highlightthickness=0)
logo_img = PhotoImage(file="logo.png")                        # ######
canvas.create_image(330, 190, image=logo_img)                  # ######
canvas.grid(column=1, row=0)                                   # ######
# --------------------------------------------------------------------------------------
# ----------------- TEXT ---------------------------------------------------------------
text1 = Text(height=9, width=80)                                # ######
text1.focus()  # Puts cursor in textbox.                        # ######
text1.grid(column=1, row=1, columnspan=2)                       # ######
text1.config(padx=20, pady=10)                                  # ######

text2 = Text(height=9, width=80)                                # ######
text2.grid(column=1, row=3, columnspan=2)                       # ######
text2.config(padx=20, pady=10)                                  # ######
# --------------------------------------------------------------------------------------
# ----------------- BUTTON -------------------------------------------------------------
scanner_button = Button(text="Scan", command=scan, fg='black', bg='silver', font=BUTTON_FONT)
scanner_button.grid(column=1, row=2, columnspan=2, pady=10)     # ######
scanner_button.config(padx=200, pady=5)                         # ######

window.mainloop()
