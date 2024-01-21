import time

class TextAdventureGame:
    def __init__(self):
        self.choices = ['left', 'right']
        self.paths = ['mountainous', 'cavernous']
        self.behavior=['confront','seek']
        self.actions = ['solve', 'find', 'approach', 'continue']

    def print_slow(self, text):
        for char in text:
            print(char, end='', flush=True)
            time.sleep(0.03)
        print("\n")

    def get_choice(self, choices):
        while True:
            choice = input("Enter your choice: ").strip().lower()
            print()
            if choice in choices:
                return choice
            else:
                print("Invalid choice. Try again.")

    def game_intro(self):
        self.print_slow("Welcome to the Text Adventure Game!")
        self.print_slow("You find yourself in a dark, mysterious forest.")
        self.print_slow("You have two paths ahead of you.")
        self.print_slow("Will you take the 'left' path or the 'right' path?")

    def left_path(self):
        self.print_slow("You chose the left path.")
        self.print_slow("You encounter a friendly squirrel.")
        self.print_slow("The squirrel gives you a magical map.")

    def right_path(self):
        self.print_slow("You chose the right path.")
        self.print_slow("You discover an ancient altar surrounded by mystical energy.")
        self.print_slow("As you approach, the altar grants you a vision of a hidden temple.")
        self.print_slow("You decide to seek out this hidden temple and uncover its secrets.")

    def confront_darkness(self):
        self.print_slow("You decide to confront the darkness directly, harnessing your mystical powers and courage.")
        self.print_slow("The ensuing battle is fierce, as you face off against dark entities threatening the forest's existence.")
        self.print_slow("After a relentless struggle, you emerge victorious, dispelling the darkness and restoring peace to the land.")
        self.print_slow("Your bravery and sacrifice cement your place as a true legend, celebrated by all living beings in the forest.")
        self.print_slow("You find a sacred map next.")

    def seek_allies(self):
        self.print_slow("You choose to seek allies to join your cause, understanding the importance of unity in the face of darkness.")
        self.print_slow("You form alliances with ancient forest guardians, mystical creatures, and wise beings from distant realms.")
        self.print_slow("Together, you launch a strategic campaign, combining your unique strengths to combat the encroaching darkness.")
        self.print_slow("Through unity and cooperation, you successfully repel the dark forces and safeguard the forest's magic for future generations.")
        self.print_slow("You find a sacred map next.")

    def move_forward_with_map(self):
        self.print_slow("You decide to use the map you found and navigate through the forest.")
        self.print_slow("The map leads you through winding paths and past various obstacles.")
        self.print_slow("You come to a fork in the road.")
        self.print_slow("Do you choose the 'mountainous' path or the 'cavernous' path?")

    def mountainous_path(self):
        self.print_slow("You choose the mountainous path.")
        self.print_slow("You begin a steep climb up the rugged terrain, facing challenges along the way.")
        self.print_slow("As you reach the summit, you are rewarded with a breathtaking view of the entire forest.")

    def cavernous_path(self):
        self.print_slow("You opt for the cavernous path.")
        self.print_slow("You descend into the depths of the earth, navigating through dark, twisting tunnels.")
        self.print_slow("You find yourself in a chamber filled with glowing crystals, illuminating the darkness with a mystical light.")

    def continue_journey_after_chamber(self):
        self.print_slow("After the chamber, you continue your journey, following the guidance of the map.")
        self.print_slow("The path leads you to a clearing where you see a mysterious old house in the distance.")
        self.print_slow("Do you 'approach' the house or 'continue' on your journey?")

    def approach_house(self):
        self.print_slow("You decide to approach the house.")
        self.print_slow("As you get closer, you hear strange whispers and feel a cold breeze emanating from the house.")
        self.print_slow("You cautiously enter and discover a room filled with ancient artifacts and a cryptic message.")

    def continue_journey_after_house(self):
        self.print_slow("After the house, you resume your journey, the map guiding you closer to the edge of the forest.")
        self.print_slow("As you near the exit, you encounter a final challenge.")
        self.print_slow("A mystical gate appears before you, requiring a special incantation to open.")
        self.print_slow("Do you attempt to 'solve' the incantation or 'find' another way out?")

    def solve_incantation(self):
        self.print_slow("You concentrate and decipher the cryptic riddle, speaking the incantation aloud.")
        self.print_slow("The gate begins to glow and slowly opens, allowing you to step through and emerge from the forest.")

    def find_alternate_exit(self):
        self.print_slow("You decide not to risk the incantation and search for an alternative exit.")
        self.print_slow("Your journey ends here.")
        self.print_slow("Thanks for playing")

    def play_game(self):
        self.game_intro()
        choice = self.get_choice(self.choices)

        if choice == 'left':
            self.left_path()
            self.move_forward_with_map()
            path_choice = self.get_choice(self.paths)
            if path_choice == 'mountainous':
                self.mountainous_path()
            else:
                self.cavernous_path()
            self.continue_journey_after_chamber()
            approach_choice = self.get_choice(self.actions)
            if approach_choice == 'approach':
                self.approach_house()
                self.continue_journey_after_house()
                gate_choice = self.get_choice(self.actions)
                if gate_choice == 'solve':
                    self.solve_incantation()
                    self.print_slow("You emerge victorious")
                    self.print_slow("Thanks for playing!")
                else:
                    self.find_alternate_exit()

            elif approach_choice=='continue':
                self.print_slow("Since you decided to not approach the mysterious old house.")
                self.print_slow("The forest succumbed to the dark forces, and your journey ends here.")
                self.print_slow("Thanks for playing!")

        else:
            self.right_path()
            self.print_slow("As the guardian of the forest, you are faced with a crucial decision.")
            self.print_slow("To protect the forest, will you directly 'confront' the darkness or 'seek allies' to aid you in your mission?")
            choice = self.get_choice(['confront', 'seek'])
            if choice == 'confront':
                self.confront_darkness()
            else:
                self.seek_allies()
            self.move_forward_with_map()
            path_choice = self.get_choice(self.paths)
            if path_choice == 'mountainous':
                self.mountainous_path()
            else:
                self.cavernous_path()
            self.continue_journey_after_chamber()
            approach_choice = self.get_choice(self.actions)
            if approach_choice == 'approach':
                self.approach_house()
                self.continue_journey_after_house()
                gate_choice = self.get_choice(self.actions)
                if gate_choice == 'solve':
                    self.solve_incantation()
                    self.print_slow("You successfully navigated through the forest and emerged safely!")
                    self.print_slow("Thanks for playing!")
                else:
                    self.print_slow("Despite your best efforts, you were unable to overcome the darkness.")
                    self.print_slow("The forest succumbed to the dark forces, and your journey ends here.")
                    self.print_slow("Thanks for playing!")
            else:
                self.print_slow("You decided not to approach the mysterious old house.")
                self.print_slow("This lead to the failure of your journey.")
                self.print_slow("Thanks for playing")  


if __name__ == "__main__":
    game = TextAdventureGame()
    game.play_game()
