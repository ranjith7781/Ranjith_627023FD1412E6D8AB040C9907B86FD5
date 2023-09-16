class player:
    def play():
        print("The player is playing cricket")

class Batsman(player):
    def play():
        print("Batsman is batting...")

class Bowler(player):
    def play():
        print("Bowler is bowling...")

Batsman.play()
Bowler.play()