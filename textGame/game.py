import time
import random

class Game:
     DEFAULT_HEALTH = 100;
     
     ENVIRONMENTS = {
          "Dark Forest": ["Wolf", "Goblin Scout", "Forest Spider"],
          "Cave": ["Cave Troll", "Bat Swarm", "Rock Golem"],
          "Ruins": ["Skeleton", "Dark Knight", "Goblin Shaman"],
          "Frozen Wastes": ["Ice Wolf", "Frost Giant"],
          "Volcanic Depths": ["Fire Imp", "Lava Beast", "Dragon"]
     }
     
     ENEMIES = {
          "Wolf": (50, 15),
          "Goblin Scout": (40, 12),
          "Forest Spider": (35, 10),

          "Cave Troll": (90, 13),
          "Bat Swarm": (30, 8),
          "Rock Golem": (120, 17),

          "Skeleton": (45, 14),
          "Dark Knight": (100, 25),
          "Goblin Shaman": (60, 17),

          "Ice Wolf": (60, 16),
          "Frost Giant": (140, 20),

          "Fire Imp": (45, 15),
          "Lava Beast": (130, 27),
          "Dragon": (200, 35)
     }

     ASCII_ENEMIES = {
          "Goblin Scout": r"""
  (._.)
  <| |>
   / \
Goblin Scout
          """,
          "Cave Troll": r"""
   (####)
  /|    |\
   | || |
  /_|____|_\
Cave Troll
          """,
          "Dragon": r"""
                    🔥🔥!!D R A G O N !!🔥🔥
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣤⣤⣤⡼⠀⢀⡀⣀⢱⡄⡀⠀⠀⠀⢲⣤⣤⣤⣤⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣾⣿⣿⣿⣿⣿⡿⠛⠋⠁⣤⣿⣿⣿⣧⣷⠀⠀⠘⠉⠛⢻⣷⣿⣽⣿⣿⣷⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣴⣞⣽⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠠⣿⣿⡟⢻⣿⣿⣇⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣟⢦⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⣿⡾⣿⣿⣿⣿⣿⠿⣻⣿⣿⡀⠀⠀⠀⢻⣿⣷⡀⠻⣧⣿⠆⠀⠀⠀⠀⣿⣿⣿⡻⣿⣿⣿⣿⣿⠿⣽⣦⡀⠀⠀⠀⠀
⠀⠀⠀⠀⣼⠟⣩⣾⣿⣿⣿⢟⣵⣾⣿⣿⣿⣧⠀⠀⠀⠈⠿⣿⣿⣷⣈⠁⠀⠀⠀⠀⣰⣿⣿⣿⣿⣮⣟⢯⣿⣿⣷⣬⡻⣷⡄⠀⠀⠀
⠀⠀⢀⡜⣡⣾⣿⢿⣿⣿⣿⣿⣿⢟⣵⣿⣿⣿⣷⣄⠀⣰⣿⣿⣿⣿⣿⣷⣄⠀⢀⣼⣿⣿⣿⣷⡹⣿⣿⣿⣿⣿⣿⢿⣿⣮⡳⡄⠀⠀
⠀⢠⢟⣿⡿⠋⣠⣾⢿⣿⣿⠟⢃⣾⢟⣿⢿⣿⣿⣿⣾⡿⠟⠻⣿⣻⣿⣏⠻⣿⣾⣿⣿⣿⣿⡛⣿⡌⠻⣿⣿⡿⣿⣦⡙⢿⣿⡝⣆⠀
⠀⢯⣿⠏⣠⠞⠋⠀⣠⡿⠋⢀⣿⠁⢸⡏⣿⠿⣿⣿⠃⢠⣴⣾⣿⣿⣿⡟⠀⠘⢹⣿⠟⣿⣾⣷⠈⣿⡄⠘⢿⣦⠀⠈⠻⣆⠙⣿⣜⠆
⢀⣿⠃⡴⠃⢀⡠⠞⠋⠀⠀⠼⠋⠀⠸⡇⠻⠀⠈⠃⠀⣧⢋⣼⣿⣿⣿⣷⣆⠀⠈⠁⠀⠟⠁⡟⠀⠈⠻⠀⠀⠉⠳⢦⡀⠈⢣⠈⢿⡄
⣸⠇⢠⣷⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⠿⠿⠋⠀⢻⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢾⣆⠈⣷
⡟⠀⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣶⣤⡀⢸⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡄⢹
⡇⠀⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠈⣿⣼⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠃⢸
⢡⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⠶⣶⡟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼
⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡁⢠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣼⣀⣠⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
     """
     }

     ASCII_ENV = {
          "Dark Forest": [r"""
 D A R K   
 F O R E S T
 🌲🌲🌲🌲🌲
  🌲  🌲
 🌲🌲🌲🌲🌲
          """,
          r"""
               ^  ^  ^   ^      ^
              / \/ \/ \ / \    / \
             /           \ \  /   \
            /             \ \/     \
            """
          ],
          "Cave": [r"""
 C A V E S
  ________
 /  ____  \
|  |    |  |
|__|____|__|
          """,
          r"""
             _________________
            /  ____________   \
           /  /            \   \
          |  |    (  )      |   |
          |__|______________|___|
            """],
          "Ruins": [r"""
 R U I N S

 ███   ███
 █  █ █  █
 ███   ███
          """,
          r"""
              _  _   _____   _  _
             | || | |     | | || |
             | || | |     | | || |
             | || | |_____| | || |
            """],
          "Frozen Wastes": [r"""
 F R O Z E N
 W A S T E S
 ❄️ ❄️ ❄️ ❄️
 ❄️  ❄️  ❄️
     """, 
     r"""
              * .    * .   *
                .   ❄️    * .
              * .   * ❄️   .
            """],
          "Volcanic Depths": r"""
 V O L C A N I C
 D E P T H S
 🌋 🌋 🌋
  🔥🔥🔥
          """
     }

     def __init__(self):
          self.inventory = [];
          self.health = Game.DEFAULT_HEALTH;
          self.gold = 20;
          self.level = 1;
          self.exp = 0;
          self.player_class = None;
          self.environment = "Dark Forest"
          self.current_location = "start";
          self.game_over = False;
          self.enemies_defeated = 0;
          self.WELCOME_LOGO = r"""
        ______  ___  ______ _   __  ______ ___________ _____ _____ _____ 
        |  _  \/ _ \ | ___ \ | / /  |  ___|  _  | ___ \  ___/  ___|_   _|
        | | | / /_\ \| |_/ / |/ /   | |_  | | | | |_/ / |__ \ `--.  | |  
        | | | |  _  ||    /|    \   |  _| | | | |    /|  __| `--. \ | |  
        | |/ /| | | || |\ \| |\  \  | |   \ \_/ / |\ \| |___/\__/ / | |  
        |___/ \_| |_/\_| \_\_| \_/  \_|    \___/\_| \_\____/\____/  \_/  
        """

     def print_slowly(self, text):
          for char in text:
               print(char, end='', flush=True);
               time.sleep(0.034);
          print();

     def choose_class(self):
          self.print_slowly("Choose your class:");
          print("1. Warrior (more health)");
          print("2. Rogue (high crit chance)");
          print("3. Mage (powerful attacks)");

          choice = input("> ");

          if choice == "1":
               self.player_class = "Warrior";
               self.health += 30;
          elif choice == "2":
               self.player_class = "Rogue";
          else:
               self.player_class = "Mage";

          self.print_slowly(f"You are now a {self.player_class}!");

     def show_status(self):
          print("\n" + "=" * 50);
          print(f"Class: {self.player_class}");
          print(f"Health: {self.health}");
          print(f"Level: {self.level} | EXP: {self.exp}");
          print(f"Gold: {self.gold}");
          print(f"Location: {self.environment}");
          print(f"Inventory: {', '.join(self.inventory) if self.inventory else 'Empty'}");
          print("=" * 50);

     def choose_environment(self):
          print("\nWhere do you want to go?");
          for i, env in enumerate(self.ENVIRONMENTS.keys(), 1):
               print(f"{i}. {env}");

          choice = input("> ");
          envs = list(self.ENVIRONMENTS.keys());
          if choice.isdigit() and 1 <= int(choice) <= len(envs):
               self.environment = envs[int(choice) - 1];
               self.print_slowly(f"You travel to the {self.environment}...\n");
               self.print_slowly(self.ASCII_ENV[self.environment][random.randint(0, len(self.ASCII_ENV[self.environment]) - 1)]);

     def level_up(self):
          if self.exp >= self.level * 50:
               self.level += 1;
               self.health += 20;
               self.exp = 0;
               self.print_slowly("✨ You leveled up! Your power grows!");

     def spawn_enemy(self):
          enemy_name = random.choice(self.ENVIRONMENTS[self.environment]);
          health, damage = self.ENEMIES[enemy_name];
          return enemy_name, health, damage;

     def random_event(self):
          events = ["trap", "treasure", "nothing", "nothing"];
          event = random.choice(events);

          if event == "trap":
               dmg = random.randint(5, 15);
               self.health -= dmg;
               self.print_slowly(f"A hidden trap hits you for {dmg} damage!");
          elif event == "treasure":
               gold = random.randint(10, 30);
               self.gold += gold;
               self.print_slowly(f"You found a hidden stash with {gold} gold!");
          else:
               self.print_slowly("The area is eerily quiet...");

     def handle_combat(self, enemy_name, enemy_health, enemy_damage):
          self.print_slowly(f"\n⚔️ A {enemy_name} attacks!");
          
          if enemy_name in self.ASCII_ENEMIES:
               print(self.ASCII_ENEMIES[enemy_name]);

          while enemy_health > 0:
               print("\n1. Attack");
               print("2. Use Item");
               print("3. Run");

               choice = input("> ");

               if choice == "1":
                    base_damage = random.randint(10, 25) + (self.level * 2);
                    crit = False;
                    
                    if self.player_class == "Rogue" and random.random() < 0.3:
                         crit = True;
                         base_damage *= 2;

                    if self.player_class == "Mage":
                         base_damage += 5;

                    enemy_health -= base_damage;

                    if crit:
                         self.print_slowly(f"💥 CRITICAL HIT! You deal {base_damage} damage!");
                    else:
                         self.print_slowly(f"You hit for {base_damage} damage!");

                    if enemy_health <= 0:
                         self.print_slowly(f"You defeated the {enemy_name}!");
                         self.exp += 20;
                         self.enemies_defeated += 1;
                         self.gold += random.randint(5, 10)
                         self.level_up();

                         if random.random() < 0.5:
                              self.inventory.append("Health Potion");
                              self.print_slowly("You found a Health Potion!");

                         return True;

                    enemy_hit = random.randint(5, enemy_damage);
                    self.health -= enemy_hit;
                    self.print_slowly(f"The {enemy_name} hits you for {enemy_hit}!");

               elif choice == "2":
                    if "Bomb" in self.inventory:
                         self.inventory.remove("Bomb");
                         self.print_slowly("💣 You throw a bomb!");
                         enemy_health -= 40;
                    else:
                         self.print_slowly("You have no usable items!");

               elif choice == "3":
                    if random.random() < 0.5:
                         self.print_slowly("You escaped!");
                         return True;
                    else:
                         self.print_slowly("Escape failed!");

               if self.health <= 0:
                    self.game_over = True;
                    return False;

     def shop(self):
          self.print_slowly("\n🧙 A shady merchant appears...");
          print("1. Health Potion (10 gold)");
          print("2. Bomb (15 gold)");
          print("3. Leave");

          choice = input("> ");

          if choice == "1" and self.gold >= 10:
               self.gold -= 10;
               self.inventory.append("Health Potion");
          elif choice == "2" and self.gold >= 15:
               self.gold -= 15;
               self.inventory.append("Bomb");

     def use_potion(self):
          if "Health Potion" in self.inventory:
               self.inventory.remove("Health Potion");
               heal = random.randint(30, 50);
               self.health = min(100, self.health + heal);
               self.print_slowly(f"You recover {heal} health!");
          else:
               self.print_slowly("No potions left!");
               
     def explore(self):
          if random.random() < 0.3:
               enemy, hp, dmg = self.spawn_enemy();
               self.handle_combat(enemy, hp, dmg);
          else:
               self.random_event();

     def play(self):
          print(self.WELCOME_LOGO);
          self.print_slowly("🌲 Welcome to the Dark Forest Adventure!\n");
          self.choose_class();
          
          self.print_slowly(self.ASCII_ENV[self.environment][random.randint(0, len(self.ASCII_ENV[self.environment]) - 1)]);

          while not self.game_over:
               self.show_status();

               print("\n1. Travel to a new location");
               print("2. Explore current location");
               print("3. Visit merchant");
               print("4. Use potion");
               print("5. Quit");

               choice = input("> ");

               if choice == "1":
                    self.choose_environment();
               elif choice == "2":
                    self.explore();
               elif choice == "3":
                    self.shop();
               elif choice == "4":
                    self.use_potion();
               elif choice == "5":
                    break;
               
               if self.enemies_defeated >= 7:
                         self.print_slowly("🔥 A DRAGON descends from the sky!");
                         self.handle_combat("Dragon", 200, 35);
                         self.print_slowly("🏆 You beat the game! Legend status achieved!");
                         break;

               if self.health <= 0:
                    self.print_slowly("💀 You have fallen. Game Over.");
                    break;


if __name__ == "__main__":
     Game().play();
