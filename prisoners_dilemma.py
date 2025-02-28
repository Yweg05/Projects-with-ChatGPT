"""

Mirei un vídeo sobre o dilema do prisioneiro e quedei maravillado xd.
É un xogo para dúas personas que recrea este dilema, está feito así rápido, pola noite e malamente.

By Migel

"""

from snippets import *
import tkinter as tk
from tkinter import ttk


player1_choice = None
player2_choice = None
player1_score = 0
player2_score = 0


ventana = tk.Tk()
ventana.title("Dilema do prisioneiro")
ventana.geometry("300x150")


def update_choices(player, action):
    global player1_choice, player2_choice

    if player == 1:
        if action == 1:
            player1_choice = 1
        else:
            player1_choice = 0
    else:
        if action == 1:
            player2_choice = 1
        else:
            player2_choice = 0


def player1_gameplay():
    clean(ventana)
    space1 = ttk.Label(ventana, text="Xogador 1").pack()

    b_good1 = ttk.Button(
        ventana, text="Boa acción", command=lambda: update_choices(1, 1)
    ).pack()
    b_bad1 = ttk.Button(
        ventana, text="Mala acción", command=lambda: update_choices(1, 0)
    ).pack()

    b_continue1 = ttk.Button(ventana, text="Confirmar", command=player2_gameplay).pack()


def player2_gameplay():
    clean(ventana)
    space2 = ttk.Label(ventana, text="Xogador 2").pack()

    b_good2 = ttk.Button(
        ventana, text="Boa acción", command=lambda: update_choices(2, 1)
    ).pack()
    b_bad2 = ttk.Button(
        ventana, text="Mala acción", command=lambda: update_choices(2, 0)
    ).pack()

    b_continue2 = ttk.Button(ventana, text="Confirmar", command=result).pack()


def result():
    global player1_score, player2_score, player1_choice, player2_choice

    clean(ventana)

    if player1_choice == 1 and player2_choice == 1:
        clean(ventana)
        le_win_win1 = ttk.Label(ventana, text="").pack()
        le_win_win2 = ttk.Label(ventana, text="").pack()
        le_win_win3 = ttk.Label(ventana, text="Ambos ganastes 100 puntos").pack()
        b_menu.pack()

        player1_score += 100
        player2_score += 100

    elif player1_choice == 1 and player2_choice == 0:
        clean(ventana)
        le_defeat_win1 = ttk.Label(ventana, text="").pack()
        le_defeat_win2 = ttk.Label(ventana, text="").pack()
        le_defeat_win3 = ttk.Label(
            ventana, text="O xogador 1 perdeu 400 puntos e o xogador 2 gañou 400 puntos"
        ).pack()
        b_menu.pack()

        player1_score -= 400
        player2_score += 400

    elif player1_choice == 0 and player2_choice == 1:
        clean(ventana)
        le_win_defeat1 = ttk.Label(ventana, text="").pack()
        le_win_defeat2 = ttk.Label(ventana, text="").pack()
        le_win_defeat3 = ttk.Label(
            ventana, text="O xogador 1 gañou 400 puntos\nO xogador 2 perdeu 400 puntos"
        ).pack()
        b_menu.pack()

        player1_score += 400
        player2_score -= 400

    elif player1_choice == 0 and player2_choice == 0:
        clean(ventana)
        le_defeat_defeat1 = ttk.Label(ventana, text="").pack()
        le_defeat_defeat2 = ttk.Label(ventana, text="").pack()
        le_defeat_defeat3 = ttk.Label(ventana, text="Ambos perdestes 200 puntos").pack()
        b_menu.pack()

        player1_score -= 200
        player2_score -= 200


def show_scores():
    clean(ventana)

    clean(ventana)
    le_show_results1 = ttk.Label(ventana, text=f"Xogador 1: {player1_score}").pack()
    le_show_results2 = ttk.Label(ventana, text=f"Xogador 2: {player2_score}").pack()

    b_menu.pack()


def menu():
    clean(ventana)

    b_start = ttk.Button(
        ventana, text="Comezar o xogo", command=player1_gameplay
    ).pack()
    b_show_scores = ttk.Button(
        ventana, text="Ver puntuacións", command=show_scores
    ).pack()


b_menu = ttk.Button(ventana, text="Volver ó menú", command=menu)

menu()
ventana.mainloop()
