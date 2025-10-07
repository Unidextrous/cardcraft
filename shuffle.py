print("Select Deck: ")
def choose_deck(cancel_option = False):
    while True:
        print("""1. ByteDeck
2. Rider-Waite Deck
3. Singularity Deck\n""")
        if cancel_option:
            print("Type X to Cancel")
        
        selection = input(">>> ")

        if cancel_option and selection == "X":
            return
        elif selection in ["1", "1."]:
            import bytedeck
            return bytedeck.bytedeck
            break
        elif selection in ["2", "2."]:
            import rider_waite
            return rider_waite.rider_waite
            break
        elif selection in ["3", "3."]:
            import singularity_deck
            return singularity_deck.singularity
            break
        else:
            print("Invalid Selection\n")

deck = choose_deck()

helpscreen = """1. Draw
2. Rotate Deck
3. Cut
4. Randomize
5. Overhand Shuffle
6. Messy Overhand Shuffle
7. Bridge Shuffle
8. Bridge Shuffle (Rotate Bottom Deck)
9. Faro Shuffle
10. Reset Order
11. See all cards
12. Choose New Deck
Type QUIT to exit
Type HELP to see this menu again\n"""

print(helpscreen)

while True:
    action = input(">>> ")
    if action.upper() == "HELP":
        print(helpscreen)
        continue
    if action.upper() == "QUIT":
        break
    try:
        action = int(action)
    except:
        try:
            action = int(f"{action}.")
        except:
            print("Invalid Selection\n")
    if action not in range(1, 13):
        print("Invalid Selection\n")
    
    if action == 1:
        while True:
            draw_selection = input("Draw How Many?\n\n>>> ")
            try:
                draw_num = int(draw_selection)
                break
            except:
                print("Invalid Selection\n")
        
        drawn_cards = deck.draw(draw_num)
        print(drawn_cards, "\n")
    
    elif action == 2:
        deck.rotate()
    
    elif action == 3:
        while True:
            cut_index_str = input("Cut Where? (Type ? for Random)\n\n>>> ")
            if cut_index_str == "?":
                cut_index = None
                break
            else:
                try:
                    cut_index = int(cut_index_str)
                    break
                except:
                    print("Invalid Selection\n")
        deck.cut(cut_index)
        print()
    
    elif action == 4:
        deck.randomize()
        print()
    
    elif action == 5:
        deck.overhand_shuffle()
        print()
    
    elif action == 6:
        print(deck.overhand_shuffle(messy=True))
        print()
    
    elif action == 7:
        deck.bridge_shuffle()
        print()
    
    elif action == 8:
        deck.bridge_shuffle(rotate=True)
        print()
    
    elif action == 9:
        deck.faro_shuffle()
        print()
    
    elif action == 10:
        deck.reset_order()
        print()
    
    elif action == 11:
        print(deck.cards, "\n")
    
    elif action == 12:
        print("Select New Deck (Type X to cancel)")
        choose_deck(cancel_option=True)