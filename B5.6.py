markup = list(range(1, 10))

def draw_board(markup):
    for i in range(3):
        print(" ", markup[0+i*3], " ", markup[1+i*3], " ", markup[2+i*3], " ")


def take_input(player_token):
    valid = False
    while not valid:
        player_answer = input("Куда поставим " + player_token+"? ")
        try:
            player_answer = int(player_answer)
        except:
            print ("Некорректный ввод. Вы уверены, что ввели число?")
            continue
        if player_answer >= 1 and player_answer <= 9:
            if (str(board[player_answer-1]) not in "XO"):
                markup[player_answer-1] = player_token
                valid = True
            else:
                print("Эта клеточка уже занята")
        else:
            print("Некорректный ввод. Введите число от 1 до 9 чтобы походить.")

def check_win(markup):
    win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for each in win_coord:
        if markup[each[0]] == markup[each[1]] == markup[each[2]]:
            return markup[each[0]]
    return False

def main(board):
    counter = 0
    win = False
    while not win:
        draw_board(board)
        if counter % 2 == 0:
            take_input("X")
        else:
            take_input("O")
        counter += 1
        if counter > 4:
            tmp = check_win(board)
            if tmp:
                print (tmp, "выиграл!")
                win = True
                break
        if counter == 9:
            print ("Ничья!")
            break
    draw_board(board)

main(markup)