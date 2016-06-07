name = input("what is your name?")
print(" (H)ello\n","(G)oodbye\n","(Q)uit")
choice = input()
while choice != "Q":
    if choice == "H":
        print("Hello",name)
        print(" (H)ello\n","(G)oodbye\n","(Q)uit")
        choice = input()

    if choice == "G":
        print("Goodbye",name)
        print(" (H)ello\n","(G)oodbye\n","(Q)uit")
        choice = input()

    if choice == "Q":
        print("Finished")
    else:
        print("Invalid choice")
        print(" (H)ello\n","(G)oodbye\n","(Q)uit")
        choice = input() #######