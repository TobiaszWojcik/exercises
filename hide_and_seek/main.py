from random import randint
from time import sleep
import os
map_row = 200
map_col = 48
map = []
start = [30, 150]
end = [22, 13]

for x in range(0, map_col):
    rowfields=[]
    for y in range(0, map_row):
        fieldtype = randint(3,8)
        rowfields.append([fieldtype,[0,0]])
    map.append(rowfields)

map[start[0]][start[1]][0] = 11
map[end[0]][end[1]][0] = 10
def print_map_value():
    for x in map:
        for y in x:
            print(y, end=" ")

        print("")

def print_map(step=0, back=False):
    print(f'This is step:{step}')
    print("-" * (map_row+2))
    for x in map:
        print("|", end="")
        for y in x:
            if y[0] == 11:
                print("O", end="")
            elif y[0] == 12:
                print("*", end="")
            elif y[0] == 10:
                print("X", end="")
            elif y[0] == 9:
                if back:
                    print(" ",end="")
                else:
                    print("+", end="")
            elif y[0] < 7:
                print(" ",end="")
            else:
                print("█",end="")
        print("|")
    print("-" * (map_row+2))
def do_step_back(end):
    print(end)
    if not map[end[0]][end[1]][0] == 10:
        map[end[0]][end[1]][0] = 12
    end = map[end[0]][end[1]][1]
    return end
def do_step():
    change_list = []
    for x in range(0, map_col):
        for y in range(0, map_row):
            if map[x][y][0] == 11 or map[x][y][0] == 9:
                if y > 0:
                    if map[x][y-1][0] < 7 or map[x][y-1][0] == 10:
                        map[x][y - 1][1][0] = x
                        map[x][y - 1][1][1] = y
                        change_list.append([x, y - 1])
                if y < map_row-1:
                    if map[x][y + 1][0] < 7 or map[x][y+1][0] == 10:
                        map[x][y + 1][1][0] = x
                        map[x][y + 1][1][1] = y
                        change_list.append([x, y + 1])
                if x > 0:
                    if map[x - 1][y][0] < 7 or map[x - 1][y][0] == 10:
                        map[x - 1][y][1][0] = x
                        map[x - 1][y][1][1] = y
                        change_list.append([x - 1, y])
                if x < map_col - 1:
                    if map[x + 1][y][0] < 7 or map[x + 1][y][0] == 10:
                        map[x + 1][y][1][0] = x
                        map[x + 1][y][1][1] = y
                        change_list.append([x + 1, y])
    for field in change_list:

        if map[field[0]][field[1]][0] == 10:
            return 2
        # if map[field[0]][field[1]] < 7:
        map[field[0]][field[1]][0] = 9

    print(f'Zajęte pola {len(change_list)}')
    if len(change_list) == 0:
        return 1
    return 0
i = 0
while True:
    i += 1

    os.system("clear")
    finish = do_step()

    print_map(i)
    if finish:
        if finish == 1:
            print("Brak dalszego ruchu - koniec poszukiwań")
        else:
            print(f'Wytropiony w {i} krokach. Teraz powrót')
            sleep(1)
            while True:
                os.system("clear")
                end = do_step_back(end)
                if end == start:
                    print_map(i, True)
                    print("Koniec!")
                    break
                print_map(i, True)
                sleep(0.02)

        break
    sleep(0.05)

