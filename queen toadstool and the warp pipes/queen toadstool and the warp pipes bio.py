# Queen Toadstool & The Warp Pipes Member Profiles
# Group: Emoji Band sub-unit, signed to YG Entertainment

qt_twp = ["Yoshi", "Mario", "Luigi", "Toad"]

member_data = {
    "Yoshi": {
        "emoji_band": "emojiband2019",
        "queen_role": "John Deacon",
        "instrument": "Bass",
        "trait": "dinosaur hype",
        "birthdate": "July 24, 2003"
    },
    "Mario": {
        "emoji_band": "Gene Meh",
        "queen_role": "Freddie Mercury",
        "instrument": "Lead vocals",
        "trait": "star power",
        "birthdate": "August 9, 2004"
    },
    "Luigi": {
        "emoji_band": "Hi-5",
        "queen_role": "Brian May",
        "instrument": "Guitar",
        "trait": "high harmonies + maknae",
        "birthdate": "August 22, 2005"
    },
    "Toad": {
        "emoji_band": "Ice Cream",
        "queen_role": "Roger Taylor",
        "instrument": "Drums",
        "trait": "Toadstool energy + shortest",
        "birthdate": "August 17, 2004"
    }
}

group_info = {
    "current_name": "Queen Toadstool & The Warp Pipes",
    "former_name": "Emoji Band K — Emoji Band Korean Unit",
    "group_active": "2019-present",
    "name_change_date": "April 1, 2026",
    "former_era": "2019 to March 31, 2026",
    "current_era": "April 1, 2026 to present",
    "parent_group": "Emoji Band (sub unit)",
    "label": "YG Entertainment",
    "concept": "Queen-inspired band with Mushroom Kingdom characters"
}

def print_bio(name):
    data = member_data[name]
    print(f"\n{'='*45}")
    print(f"** {name} — {group_info['current_name']} **")
    print(f"{'='*45}")
    print(f"Emoji Band Character: {data['emoji_band']}")
    print(f"Queen Counterpart: {data['queen_role']}")
    print(f"Position: {data['instrument']}")
    print(f"Key Trait: {data['trait']}")
    print(f"Birthdate: {data['birthdate']}")
    print(f"{'='*45}\n")

def print_back_page():
    print(f"\n{'*'*50}")
    print(f"** GROUP PROFILE: BACK PAGE **")
    print(f"{'*'*50}")
    print(f"Group Name: {group_info['current_name']}")
    print(f"Formerly Known As: {group_info['former_name']}")
    print(f"Parent Group: {group_info['parent_group']}")
    print(f"Active Since: {group_info['group_active']}")
    print(f"Name Changed: {group_info['name_change_date']}")
    print(f"")
    print(f"Timeline:")
    print(f" {group_info['former_era']} - {group_info['former_name']}")
    print(f" {group_info['current_era']} - {group_info['current_name']}")
    print(f"")
    print(f"Label: {group_info['label']}")
    print(f"Concept: {group_info['concept']}")
    print(f"")
    print(f"Members (L to R):")
    for i, member in enumerate(qt_twp, 1):
        data = member_data[member]
        print(f" {i}. {member} - {data['instrument']}, {data['queen_role']}")
    print(f"{'*'*50}\n")

# Main menu
while True:
    print("\nQueen Toadstool & The Warp Pipes — Profile Viewer")
    print("1-4: View member bio")
    print("5: View group back page")
    print("6: View all")
    print("0: Exit")

    for i, member in enumerate(qt_twp, 1):
        print(f"{i}. {member}")
    print("5. Back Page / Group Info")

    choice = input("\nEnter option: ")

    try:
        choice_num = int(choice)
        if 1 <= choice_num <= 4:
            selected_member = qt_twp[choice_num - 1]
            print_bio(selected_member)
        elif choice_num == 5:
            print_back_page()
        elif choice_num == 6:
            print_back_page()
            for member in qt_twp:
                print_bio(member)
        elif choice_num == 0:
            print("Thanks for visiting Queen Toadstool & The Warp Pipes!")
            break
        else:
            print("Invalid option. Please pick 0-6.")
    except ValueError:
        print("Please enter a number.")
