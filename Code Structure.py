# import module
import os
import random
import pygame
import sys  # sys.exit을 이용한 게임 종료 코드
from pygame.locals import *  # import 는 Pygame

print("""
──────────────▐█████───────
──────▄▄████████████▄──────
────▄██▀▀────▐███▐████▄────
──▄██▀───────███▌▐██─▀██▄──
─▐██────────▐███─▐██───██▌─
─██▌────────███▌─▐██───▐██─
▐██────────▐███──▐██────██▌
██▌────────███▌──▐██────▐██
██▌───────▐███───▐██────▐██
██▌───────███▌──▄─▀█────▐██
██▌──────▐████████▄─────▐██
██▌──────█████████▀─────▐██
▐██─────▐██▌────▀─▄█────██▌
─██▌────███─────▄███───▐██─
─▐██▄──▐██▌───────────▄██▌─
──▀███─███─────────▄▄███▀──
──────▐██▌─▀█████████▀▀────
──────███──────────────────

FakeVengers Game """)
print()

name = input("What is your name? : ")
print("Welcome to FakeVengers game, {}!".format(name))

running = True
while running:
    to_play = input("This is a main room. Do you wanna continue? (yes or no) : ")
    if to_play == "yes":
        while True:
            choose_rooms = input("choose a room btw 1 to 4 (1-4) : ")
            ######################################################
            if choose_rooms == '1':
                ans = input("Good, do you wanna play car racing? (yes or no) : ")
                if ans == "yes":
                    print("Let's play car racing!")
                    ######################################################
                    # Car racing game
                    ######################################################
                    print("Game is over. Back to the main room")
                    break

                elif ans == "no":
                    print("Then we go back to the main room")
                    break

            if choose_rooms == '2':
                ans = input("Good, do you wanna play shooting game? (yes or no) : ")
                if ans == "yes":
                    print("Let's play shooting game!")
                    ######################################################
                    # Shooting game
                    ######################################################
                    print("Game is over. Back to the main room")
                    break

                elif ans == "no":
                    print("Then we go back to the main room")
                    break

            if choose_rooms == '3':
                ans = input("Good, do you wanna play flappy bird? (yes or no) : ")
                if ans == "yes":
                    print("Let's play flappy bird!")
                    ######################################################
                    # flappy bird game
                    ######################################################
                    print("Game is over. Back to the main room")
                    break

                elif ans == "no":
                    print("Then we go back to the main room")
                    break

            if choose_rooms == '4':
                ans = input("Good, do you wanna play T-REX game? (yes or no) : ")
                if ans == "yes":
                    print("Let's play T-REX game!")
                    ######################################################
                    # T-REX game
                    ######################################################
                    print("Game is over. Back to the main room")
                    break

                elif ans == "no":
                    print("Then we go back to the main room")
                    break

            else:
                print("Please answer correctly")


    elif to_play == "no":
        while True:
            quit_ans = input("Do you really wanna quit? : (yes or no) ")
            if quit_ans == "yes":
                print("Goodbye, {}".format(name))
                running = False
                break
            elif quit_ans == "no":
                break
            else:
                print("Please answer 'yes or 'no'")

    else:
        print("Please answer 'yes or 'no'")