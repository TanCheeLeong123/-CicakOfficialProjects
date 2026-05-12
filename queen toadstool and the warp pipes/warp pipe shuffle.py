import random

# Your band data
band = {
    "Yoshi": {"member": "emojiband2019", "queen_role": "John Deacon", "instrument": "Bass"},
    "Mario": {"member": "Gene Meh", "queen_role": "Freddie Mercury", "instrument": "Vocals"},
    "Luigi": {"member": "Hi-5", "queen_role": "Brian May", "instrument": "Guitar"},
    "Toad": {"member": "Ice Cream", "queen_role": "Roger Taylor", "instrument": "Drums"}
}

def play_round():
    print("\n🍄 Queen Toadstool & The Warp Pipes got shuffled in the Warp Zone!")
    characters = list(band.keys())
    shuffled_roles = list(band.keys())
    random.shuffle(shuffled_roles)
    
    # Create the mixed-up lineup
    round_matchup = dict(zip(characters, shuffled_roles))
    
    # Pick one to quiz the player on
    quiz_character = random.choice(characters)
    correct_answer = round_matchup[quiz_character]
    
    print(f"\nThis round: {quiz_character} is now playing the role of...?")
    print(f"Hint: Their real Queen role is {band[correct_answer]['queen_role']} on {band[correct_answer]['instrument']}")
    
    guess = input("Type your guess (Yoshi/Mario/Luigi/Toad): ").strip().title()
    
    if guess == correct_answer:
        print(f"🎵 Correct! {quiz_character} warped into {correct_answer}'s role. 'We Are The Champions' plays!")
        return 1
    else:
        print(f"💥 Game Over! {quiz_character} was actually {correct_answer}. The real {guess} is {band[guess]['member']}.")
        return 0

def main():
    score = 0
    print("=== WARP PIPE SHUFFLE ===")
    print("Signed to YG Entertainment. Active since Apr 1, 2026.")
    print("Guess who warped into whose role. Type 'quit' to exit.")
    
    while True:
        score += play_round()
        again = input("\nWarp again? (y/n): ").lower()
        if again!= 'y':
            break
    
    print(f"\nFinal Score: {score} correct warps!")
    print("Thanks for playing with Queen Toadstool & The Warp Pipes 🎮")

if __name__ == "__main__":
    main()
