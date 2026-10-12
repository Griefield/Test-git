# Initialization of variables
sliced_bread = ["bottom crust", "middle piece1", "middle piece2", "middle piece3", "middle piece4", "middle piece5", "top crust"]
ACTIONS = ["check if empty", "check amount", "check top", "check hand", "take bread", "exit"]
running = True
hand = ""

# functions
def notempty(stack):
    if len(stack) == 0:
        print("there's no more bread!")
        return False
    return True

def amount(stack):
    pieces = len(stack)
    print("there are ", pieces, "pieces of bread!")

def checktop(stack):
    top_item = stack[-1] if stack else None
    print("Top item:", top_item)

print("\nThis program simulates a loaf of bread in a one-hole container")
while running:
    print("\n                   Actions available:\n", ACTIONS)
    action = str(input("select action: "))
    print()

    match action:

        # actions for the loaf
        case "check amount":
            if notempty(sliced_bread):
                amount(sliced_bread)

        case "check if empty":
            if notempty(sliced_bread):
                print("there's still bread!")
            else:
                ACTIONS.pop(1)

        case "check top":
            if notempty(sliced_bread):
                checktop(sliced_bread)

        case "take bread":
            if hand == "":
                if notempty(sliced_bread):
                    ACTIONS.insert(4, "put back bread")
                    ACTIONS.insert(4, "eat bread")
                    hand = sliced_bread[-1]
                    print("taking", hand, "out of the loaf...")
                    sliced_bread.pop()
            else:
                print("theres already bread in your hand")

        # actions for the hand and loaf
        case "check hand":
            if hand == "":
                print("theres no bread in your hand")
            else:
                print("youre holding", hand)

        case "put back bread":
            if hand == "":
                print("theres no bread in your hand")
            else:
                sliced_bread.append(hand)
                ACTIONS.remove("put back bread")
                ACTIONS.remove("eat bread")
                print("putting bread back...")
                print("theres no more bread in your hand")
                hand = ""

        case "eat bread":
            if hand == "":
                print("theres no bread in your hand")
            else:
                hand = ""
                print("eating bread...")
                print("theres no more bread in your hand")
                ACTIONS.remove("eat bread")
                ACTIONS.remove("put back bread")

        case "exit":
            running = False

        case _:
            print("Wrong input, try again.")

print("bye.")
