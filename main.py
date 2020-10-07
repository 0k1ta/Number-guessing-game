import random

answer = random.randint(1, 10)

while True:
    print("1〜10の中から1つ正解の数値を予想してください", end="")
    guess = int(input())
    
    if answer == guess:
        print("Bingo!")
        break
    elif answer > guess:
        print("Bigger!")
    else:
        print("Smaller!")
