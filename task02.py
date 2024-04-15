from solution import NavalBattle_2


NavalBattle_2.playing_field = [[0, 1, 1, 1, 0, 0, 0, 0, 0, 1],
                             [0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
                             [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
                             [1, 1, 1, 0, 0, 1, 0, 0, 1, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 1, 1, 0, 0, 1, 0, 0]]

player1 = NavalBattle_2('#')
player2 = NavalBattle_2('*')
NavalBattle_2.show()
player1.shot(6, 2)
player1.shot(6, 1)
player2.shot(6, 3)
player2.shot(6, 4)
player2.shot(6, 5)
player2.shot(3, 3)
player2.show()
player1.shot(1, 1)
NavalBattle_2.show()
