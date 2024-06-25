from RPS_game import play, quincy, mrugesh, abbey, kris, human
from RPS import player

# Play 1000 games against each bot and print the result
print("Playing against quincy...")
play(player, quincy, 1000, verbose=True)

print("Playing against mrugesh...")
play(player, mrugesh, 1000, verbose=True)

print("Playing against abbey...")
play(player, abbey, 1000, verbose=True)

print("Playing against kris...")
play(player, kris, 1000, verbose=True)
