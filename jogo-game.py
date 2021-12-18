jogo = [["", "", ""], ["", "", ""], ["", "", ""]]

flag = 0
count = 0

while True:
    while flag == 0:
        print(f'"X"')
        x_i = int(input("Linha:"))
        x_j = int(input("Coluna:"))
        if jogo[x_i][x_j] != "":
            print("local preenchido.")
            continue
        else:
            jogo[x_i][x_j] = "X"
            flag += 1
            count += 1
        for i in range(0, len(jogo)):
            print()
            for j in range(0, len(jogo[i])):
                print(f'| {jogo[i][j]} |', end=" ")

    for ii in jogo:
        for jj in ii:
            if jogo[0][0] == "X" and jogo[0][1] == "X" and jogo[0][2] == "X":
                print(f'\nVencedor: X')
                exit(1)
            elif jogo[0][0] == "X" and jogo[1][0] == "X" and jogo[2][0] == "X":
                print(f'\nVencedor: X')
                exit(1)
            elif jogo[0][0] == "X" and jogo[1][1] == "X" and jogo[1][2] == "X":
                print(f'\nVencedor: X')
                exit(1)
            elif jogo[1][0] == "X" and jogo[1][1] == "X" and jogo[1][2] == "X":
                print(f'\nVencedor: X')
                exit(1)
            elif jogo[0][1] == "X" and jogo[1][1] == "X" and jogo[2][1] == "X":
                print(f'\nVencedor: X')
                exit(1)
            elif jogo[0][2] == "X" and jogo[1][1] == "X" and jogo[2][0] == "X":
                print(f'\nVencedor: X')
                exit(1)
            elif jogo[2][0] == "X" and jogo[2][1] == "X" and jogo[2][2] == "X":
                print(f'\nVencedor: X')
                exit(1)
            elif jogo[0][2] == "X" and jogo[1][2] == "X" and jogo[2][2] == "X":
                print(f'\nVencedor: X')
                exit(1)
            elif count == 9:
                print("\nVelha.")
                exit(1)

    flag = 0

    while flag == 0:
        print(f'\n\n"O"')
        o_i = int(input("Linha:"))
        o_j = int(input("Coluna:"))
        if jogo[o_i][o_j] != "":
            print("local preenchido.")
        else:
            jogo[o_i][o_j] = "O"
            flag += 1
            count += 1
        for i in range(0, len(jogo)):
            print()
            for j in range(0, len(jogo[i])):
                print(f'| {jogo[i][j]} |', end=" ")
        print()

    for kk in jogo:
        for ll in kk:
            if jogo[0][0] == "O" and jogo[0][1] == "O" and jogo[0][2] == "O":
                print(f'\nVencedor: O')
                exit(1)
            elif jogo[0][0] == "O" and jogo[1][0] == "O" and jogo[2][0] == "O":
                print(f'\nVencedor: O')
                exit(1)
            elif jogo[0][0] == "O" and jogo[1][1] == "O" and jogo[1][2] == "O":
                print(f'\nVencedor: O')
                exit(1)
            elif jogo[1][0] == "O" and jogo[1][1] == "O" and jogo[1][2] == "O":
                print(f'\nVencedor: O')
                exit(1)
            elif jogo[0][1] == "O" and jogo[1][1] == "O" and jogo[2][1] == "O":
                print(f'\nVencedor: O')
                exit(1)
            elif jogo[0][2] == "O" and jogo[1][1] == "O" and jogo[2][0] == "O":
                print(f'\nVencedor: O')
                exit(1)
            elif jogo[2][0] == "O" and jogo[2][1] == "O" and jogo[2][2] == "O":
                print(f'\nVencedor: O')
                exit(1)
            elif jogo[0][2] == "O" and jogo[1][2] == "O" and jogo[2][2] == "O":
                print(f'\nVencedor: O')
                exit(1)
            elif count == 9:
                print("\nVelha.")
                exit(1)

    flag = 0
