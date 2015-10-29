# coding=utf-8
__author__ = 'ujarc'

attempts = 0

number = 7


while attempts < 3:
    guess = raw_input(Ugani stevilko!)
    guess = int(guess)

    attempts = attempts + 1

    if guess < number:
       print('Probaj visijo stevilko')

    if guess > number:
       print('Probaj manjso stevilko')

    if guess == number:
        break

if guess == number:
    attempts = str(attempts)
    print('Čestitam številko si uganil v' + attempts + ' poiskusih!')

if guess != number:
    number = str(number)
    print('To ni številka' + number)









