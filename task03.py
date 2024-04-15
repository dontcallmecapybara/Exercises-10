from solution import NavalBattle_3


player1 = NavalBattle_3('#')
player1.shot(6, 2)
NavalBattle_3.playing_field = [[0, 1, 1, 1, 0, 0, 0, 0, 0, 1],
                               [0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
                               [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
                               [1, 1, 1, 0, 0, 1, 0, 0, 1, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                               [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 1, 1, 0, 0, 1, 0, 0]]
player1.shot(6, 2)
player1.shot(6, 2)
NavalBattle_3.show()
player1.shot(1,1)
player1.shot(1,1)
NavalBattle_3.new_game()
NavalBattle_3.show()
player1.shot(6, 2)
