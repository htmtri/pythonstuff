#The game HORSE is a popular basketball shooting game.
#It can be played with any number of players. One-by-one,
#each player takes a shot from anywhere they want. If they
#make the shot, the next person must make the same shot.
#If they do not, they receive a letter: H, then O, then R,
#then S, then E. Once a player receives all 5 letters, they
#are out of the game.
#
#The game continues until all but one player has all five
#letters.
#
#Write a function called check_horse_winner. This function
#will take as input a tuple of at least two, but potentially
#more, strings. 
#
#check_horse_winner should return the following:
#
# - If only one player is left with fewer than 5 letters,
#   return "Player X wins!", where X is the index of the
#   player in the list (which could be 0).
# - If more than one player has fewer than 5 letters,
#   return "Players X, Y: keep playing!", where X, Y, and
#   potentially more numbers are the indices of all players
#   who have not yet been eliminated.
# - If no player has 5 letters, return "Everyone: keep
#   playing!"

def check_horse_winner(str_tuple):
    count = 0
    playlist_str = ''
    winlist = []
    for i in range(0,len(str_tuple)):
        if len(str_tuple[i]) < 5:
            count += 1
            playlist_str += (' '+str(i)+',')
            winlist.append(str_tuple[i])
    if count == len(str_tuple):
        return "Everyone: keep playing!"
    elif 0 < count < len(str_tuple):
        if len(winlist) == 1:
            return 'Player ' + str(str_tuple.index(winlist[0])) + ' wins!'
        else:
            return 'Players' + playlist_str[:-1] + ': keep playing!'
        
#If your function works correctly, this will originally
#print:
#Everyone: keep playing!
#Players 1, 2: keep playing!
#Player 2 wins!
print(check_horse_winner(("HOR", "HORS", "H", "HO")))
print(check_horse_winner(("HORSE", "HOR", "HORS", "HORSE")))
print(check_horse_winner(("HORSE", "HORSE", "HORS", "HORSE")))