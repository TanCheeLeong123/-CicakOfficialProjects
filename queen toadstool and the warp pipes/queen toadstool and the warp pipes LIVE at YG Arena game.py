import random
import time

class WarpPipesGame:
    def __init__(self):
        self.members = {
            "Yoshi": {"stage_name": "emojiband2019", "role": "John Deacon", "skill": 85},
            "Mario": {"stage_name": "Gene Meh", "role": "Freddie Mercury", "skill": 95},
            "Luigi": {"stage_name": "Hi-5", "role": "Brian May", "skill": 88},
            "Toad": {"stage_name": "Ice Cream", "role": "Roger Taylor", "skill": 90}
        }
        self.setlist = ["Fear", "VERY NICE", "HIT", "God Of Music", "HOT", "Rock With You"]
        
    def reset_game(self):
        """Reset score and fan energy for a new run"""
        self.score = 0
        self.fan_energy = 100
        
    def start_concert(self):
        self.reset_game()
        print("🍄 Queen Toadstool & The Warp Pipes LIVE at YG Arena game 🍄")
        print("Members: Yoshi | Mario | Luigi | Toad")
        print("-" * 50)
        
        for song in random.sample(self.setlist, 3):
            self.play_song(song)
            time.sleep(1)
            
        self.show_results()
    
    def play_song(self, song):
        print(f"\nNow Playing: {song}")
        chart = [random.choice(list(self.members.keys())) for _ in range(8)]
        
        for i, note in enumerate(chart):
            input(f"Beat {i+1}: {note} takes the spotlight! Press Enter: ")
            hit_chance = self.members[note]["skill"] + random.randint(-10, 10)
            
            if hit_chance > 80:
                print(f"Perfect! {self.members[note]['stage_name']} nailed it!")
                self.score += 100
                self.fan_energy = min(100, self.fan_energy + 5)
            elif hit_chance > 60:
                print(f"Good! Crowd is vibing.")
                self.score += 50
            else:
                print(f"Oops... {note} missed. Fan energy -10")
                self.fan_energy = max(0, self.fan_energy - 10)
        
        print(f"Song complete! Current score: {self.score} | Fan Energy: {self.fan_energy}%")
    
    def show_results(self):
        print("\n" + "=" * 50)
        print("CONCERT RESULTS")
        print("=" * 50)
        print(f"Final Score: {self.score}")
        print(f"Fan Energy: {self.fan_energy}%")
        
        if self.score > 600 and self.fan_energy > 70:
            rank = "S - Power Star Legends"
        elif self.score > 400:
            rank = "A - Warp Pipe Certified"
        else:
            rank = "B - Needs more practice"
        print(f"Rank: {rank}")
        print("\nThanks for playing! Queen Toadstool & The Warp Pipes forever!")

    def run(self):
        """Main game loop with play again option"""
        playing = True
        while playing:
            # Replace _ with your actual engine init, e.g. pygame.init()
            # _.init()
            self.start_concert()
            
            again = input("\nEncore? Play again? [y/n]: ").lower().strip()
            if again!= 'y' and again!= 'yes':
                playing = False
                print("\nTour’s over! Queen Toadstool & The Warp Pipes signing off 🍄🎤")
            else:
                print("\n" + "🎵" * 25)
                print("SETTING UP THE NEXT STAGE...")
                print("🎵" * 25 + "\n")
                time.sleep(1)

if __name__ == "__main__":
    game = WarpPipesGame()
    game.run()
