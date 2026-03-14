import tkinter as tk
from tkinter import messagebox
import sys

try:
     from game import Game as CLI_Game
     from graphic import GameGUI
except ImportError as e:
     print(f"Error: Could not find the game files. {e}")
     sys.exit()


class Launcher:
     def __init__(self, root):
          self.root = root
          self.root.title("Adventure Launcher")
          self.root.geometry("400x250")
          self.root.configure(bg="#1a1a1a")

          # Title
          tk.Label(
               root, text="DARK FOREST", 
               fg="#00ff00", bg="#1a1a1a", 
               font=("Courier", 24, "bold")
          ).pack(pady=20)

          tk.Label(
               root, text="Select your interface:", 
               fg="white", bg="#1a1a1a", 
               font=("Arial", 10)
          ).pack(pady=5)

          # Buttons
          tk.Button(
               root, text="Terminal Version (CLI)", 
               width=25, command=self.launch_cli,
               bg="#333", fg="white"
          ).pack(pady=10)

          tk.Button(
               root, text="Graphic Version (GUI)", 
               width=25, command=self.launch_gui,
               bg="#005500", fg="white"
          ).pack(pady=10)

     def launch_cli(self):
          """Closes the GUI and starts the terminal game."""
          self.root.destroy()
          print("\n" * 20) # Clear some space in terminal
          game = CLI_Game()
          game.play()

     def launch_gui(self):
          """Closes the launcher and starts the graphic game."""
          self.root.destroy()
          new_root = tk.Tk()
          GameGUI(new_root)
          new_root.mainloop()

if __name__ == "__main__":
     root = tk.Tk()
     app = Launcher(root)
     root.mainloop()