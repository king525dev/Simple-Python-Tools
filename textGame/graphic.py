import tkinter as tk
from tkinter import messagebox, scrolledtext
import random

class GameGUI:
     def __init__(self, root):
          self.root = root
          self.root.title("Dark Forest Adventure")
          self.root.geometry("900x800")
          self.root.configure(bg="#121212")

          # ==== ASCII ART DATA ====
          self.WELCOME_LOGO = r"""
        ______  ___  ______ _   __  ______ ___________ _____ _____ _____ 
        |  _  \/ _ \ | ___ \ | / /  |  ___|  _  | ___ \  ___/  ___|_   _|
        | | | / /_\ \| |_/ / |/ /   | |_  | | | | |_/ / |__ \ `--.  | |  
        | | | |  _  ||    /|    \   |  _| | | | |    /|  __| `--. \ | |  
        | |/ /| | | || |\ \| |\  \  | |   \ \_/ / |\ \| |___/\__/ / | |  
        |___/ \_| |_/\_| \_\_| \_/  \_|    \___/\_| \_\____/\____/  \_/  
        """

          self.ENV_ART = {
               "Dark Forest": r"""
               ^  ^  ^   ^      ^
              / \/ \/ \ / \    / \
             /           \ \  /   \
            /             \ \/     \
            """,
               "Cave": r"""
             _________________
            /  ____________   \
           /  /            \   \
          |  |    (  )      |   |
          |__|______________|___|
            """,
               "Ruins": r"""
              _  _   _____   _  _
             | || | |     | | || |
             | || | |     | | || |
             | || | |_____| | || |
            """,
               "Frozen Wastes": r"""
              * .    * .   *
                .   ❄️    * .
              * .   * ❄️   .
            """,
               "Volcanic Depths": r"""
               /\      /\    /\
              /  \    /  \  /  \
             /    \  /    \/    \
            🌋🌋🌋🌋🌋🌋🌋🌋🌋🌋🌋
            """
        }

          # ==== GAME STATE ====
          self.max_health = 100
          self.health = 100
          self.gold = 20
          self.level = 1
          self.exp = 0
          self.inventory = []
          self.player_class = "None"
          self.environment = "Dark Forest"
          self.enemies_defeated = 0

          # ==== DATA ====
          self.environments = {
               "Dark Forest": ["Wolf", "Goblin Scout", "Forest Spider"],
               "Cave": ["Cave Troll", "Bat Swarm", "Rock Golem"],
               "Ruins": ["Skeleton", "Dark Knight", "Goblin Shaman"],
               "Frozen Wastes": ["Ice Wolf", "Frost Giant"],
               "Volcanic Depths": ["Fire Imp", "Lava Beast", "Dragon"]
          }
          self.enemies = {
               "Wolf": (50, 15), "Goblin Scout": (40, 12), "Forest Spider": (35, 10),
               "Cave Troll": (90, 13), "Bat Swarm": (30, 8), "Rock Golem": (120, 17),
               "Skeleton": (45, 14), "Dark Knight": (100, 25), "Goblin Shaman": (60, 17),
               "Ice Wolf": (60, 16), "Frost Giant": (140, 20), "Fire Imp": (45, 15),
               "Lava Beast": (130, 27), "Dragon": (200, 35)
          }

          self.create_widgets()
          self.show_welcome()

     def create_widgets(self):
          # Header Status Frame
          self.status_frame = tk.Frame(self.root, bg="#1e1e1e", padx=10, pady=10)
          self.status_frame.pack(fill="x")

          # Health Bar
          self.hp_label = tk.Label(self.status_frame, text="HP:", bg="#1e1e1e", fg="white", font=("Courier", 12, "bold"))
          self.hp_label.grid(row=0, column=0, padx=5)
          
          self.hp_canvas = tk.Canvas(self.status_frame, width=200, height=20, bg="#333", highlightthickness=0)
          self.hp_canvas.grid(row=0, column=1, padx=5)
          self.hp_bar = self.hp_canvas.create_rectangle(0, 0, 200, 20, fill="#00ff00")

          self.stats_text = tk.Label(self.status_frame, text="", bg="#1e1e1e", fg="#aaa", font=("Courier", 11))
          self.stats_text.grid(row=0, column=2, padx=20)

          # Game Log Area
          self.log_area = scrolledtext.ScrolledText(self.root, height=25, bg="black", fg="#00ff00", 
                                                  font=("Courier", 10), insertbackground="white", state='disabled')
          self.log_area.pack(pady=10, padx=15, fill="both", expand=True)

          # Action Button Frame
          self.buttons = tk.Frame(self.root, bg="#121212")
          self.buttons.pack(pady=20)

     def log(self, msg):
          self.log_area.configure(state='normal')
          self.log_area.insert(tk.END, msg + "\n")
          self.log_area.see(tk.END)
          self.log_area.configure(state='disabled')

     def show_welcome(self):
          self.log(self.WELCOME_LOGO)
          self.log("\n" + "="*60)
          self.log("Welcome, traveler. Your legend begins in the shadows.")
          self.log("="*60 + "\n")
          self.choose_class()

     def update_status(self):
          self.stats_text.config(
               text=f"LVL: {self.level} | EXP: {self.exp} | GOLD: {self.gold}\nCLASS: {self.player_class} | LOC: {self.environment}"
          )
          ratio = max(0, min(1, self.health / self.max_health))
          self.hp_canvas.coords(self.hp_bar, 0, 0, 200 * ratio, 20)
          
          # Color transition
          color = "#00ff00" if ratio > 0.6 else "#ffff00" if ratio > 0.3 else "#ff0000"
          self.hp_canvas.itemconfig(self.hp_bar, fill=color)

     def clear_buttons(self):
          for w in self.buttons.winfo_children():
               w.destroy()

     # ================= GAME FLOW =================

     def choose_class(self):
          self.log("Select your class to enter the forest:")
          self.clear_buttons()
          for name in ["Warrior", "Rogue", "Mage"]:
               tk.Button(self.buttons, text=name, width=12, command=lambda n=name: self.set_class(n)).pack(side="left", padx=10)

     def set_class(self, cls):
          self.player_class = cls
          if cls == "Warrior": self.max_health = 130; self.health = 130
          self.log(f"\n[ SYSTEM ] You are now a {cls}.")
          self.log(self.ENV_ART["Dark Forest"])
          self.main_menu()
          self.update_status()

     def main_menu(self):
          self.clear_buttons()
          actions = [("Explore", self.explore), ("Travel", self.travel_menu), 
                    ("Shop", self.shop), ("Use Potion", self.use_potion)]
          for text, cmd in actions:
               tk.Button(self.buttons, text=text, width=12, bg="#222", fg="white", command=cmd).pack(side="left", padx=5)

     def travel_menu(self):
          self.clear_buttons()
          self.log("\nWhere shall you travel next?")
          for env in self.environments:
               tk.Button(self.buttons, text=env, command=lambda e=env: self.travel(e)).pack(side="left", padx=2)

     def travel(self, env):
          self.environment = env
          self.log("\n" + "="*30)
          self.log(f"Entering the {env}...")
          self.log(self.ENV_ART.get(env, ""))
          self.log("="*30)
          self.update_status()
          self.main_menu()

     # (Keep existing explore, attack, shop, and use_potion methods from previous code)
     def explore(self):
          if random.random() < 0.4:
               enemy = random.choice(self.environments[self.environment])
               self.start_combat(enemy, self.enemies[enemy][0], self.enemies[enemy][1])
          else:
               self.random_event()

     def random_event(self):
          event = random.choice(["trap", "treasure", "nothing"])
          if event == "trap":
               dmg = random.randint(5, 15)
               self.health -= dmg
               self.log(f"⚠️ A trap dealt {dmg} damage!")
          elif event == "treasure":
               gold = random.randint(10, 30)
               self.gold += gold
               self.log(f"💰 You found {gold} gold!")
          else:
               self.log("It's quiet here...")
          self.update_status()
          if self.health <= 0: messagebox.showerror("Game Over", "You died!"); self.root.quit()

     def start_combat(self, enemy, hp, dmg):
          self.enemy_name, self.enemy_hp, self.enemy_dmg = enemy, hp, dmg
          self.log(f"\n⚔️ A {enemy} attacks!")
          self.clear_buttons()
          tk.Button(self.buttons, text="ATTACK", bg="#800", fg="white", command=self.attack).pack(side="left", padx=5)
          tk.Button(self.buttons, text="FLEE", command=self.main_menu).pack(side="left", padx=5)

     def attack(self):
          dmg = random.randint(10, 25) + self.level * 2
          self.enemy_hp -= dmg
          self.log(f"You hit {self.enemy_name} for {dmg} damage.")
          if self.enemy_hp <= 0:
               self.log(f"🏆 {self.enemy_name} defeated!")
               self.exp += 25; self.gold += 10; self.enemies_defeated += 1
               self.check_level_up(); self.main_menu(); self.update_status()
               return
          e_hit = random.randint(5, self.enemy_dmg)
          self.health -= e_hit
          self.log(f"{self.enemy_name} hits you for {e_hit}!")
          self.update_status()
          if self.health <= 0: messagebox.showerror("Game Over", "You died!"); self.root.quit()

     def check_level_up(self):
          if self.exp >= self.level * 50:
               self.level += 1; self.max_health += 20; self.health = self.max_health; self.exp = 0
               self.log("✨ LEVEL UP! Health restored.")

     def shop(self):
          self.log("\n🧙 Merchant: 'Buy a potion for 10g?'")
          self.clear_buttons()
          tk.Button(self.buttons, text="Buy Potion", command=self.buy_potion).pack(side="left", padx=5)
          tk.Button(self.buttons, text="Leave", command=self.main_menu).pack(side="left", padx=5)

     def buy_potion(self):
          if self.gold >= 10: self.gold -= 10; self.inventory.append("Potion"); self.log("Bought potion.")
          else: self.log("Not enough gold!")
          self.update_status()

     def use_potion(self):
          if "Potion" in self.inventory:
               self.inventory.remove("Potion"); self.health = min(self.max_health, self.health + 40)
               self.log("🧪 Healed 40 HP."); self.update_status()
          else: self.log("No potions!")

if __name__ == "__main__":
     root = tk.Tk()
     GameGUI(root)
     root.mainloop()