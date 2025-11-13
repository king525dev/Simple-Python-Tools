import random
import time
import copy
import sys

# Try to import Tkinter
try:
    import tkinter as tk
    from tkinter import font
except ImportError:
    print("Tkinter is not installed. GUI mode will not work.")
    sys.exit()

# --- Default Configuration ---
DEFAULT_WIDTH = 60
DEFAULT_HEIGHT = 20
CELL_SIZE = 20 

# ==========================================
# PART 1: The Command Line Logic
# ==========================================
def run_cli_version():
    """Runs the original text-based version of the game."""
    print("\n" * 50) 
    print("Initializing Command Line Mode...")
    time.sleep(1)
    
    # Local variables for CLI to keep it isolated from GUI resizing
    cli_width = 60
    cli_height = 20

    nextCells = []
    for x in range(cli_width):
        column = [] 
        for y in range(cli_height):
            if random.randint(0, 1) == 0:
                column.append('#') 
            else:
                column.append(' ') 
        nextCells.append(column) 

    try:
        while True: 
            print('\n\n\n----------\n\n\n') 
            currentCells = copy.deepcopy(nextCells) 

            for y in range(cli_height): 
                for x in range(cli_width): 
                    print(currentCells[x][y], end='') 
                print() 

            for x in range(cli_width): 
                for y in range(cli_height): 
                    leftCoord  = (x - 1) % cli_width 
                    rightCoord = (x + 1) % cli_width 
                    aboveCoord = (y - 1) % cli_height 
                    belowCoord = (y + 1) % cli_height 
        
                    numNeighbors = 0 
                    if currentCells[leftCoord][aboveCoord] == '#': numNeighbors += 1 
                    if currentCells[x][aboveCoord] == '#': numNeighbors += 1 
                    if currentCells[rightCoord][aboveCoord] == '#': numNeighbors += 1 
                    if currentCells[leftCoord][y] == '#': numNeighbors += 1 
                    if currentCells[rightCoord][y] == '#': numNeighbors += 1 
                    if currentCells[leftCoord][belowCoord] == '#': numNeighbors += 1 
                    if currentCells[x][belowCoord] == '#': numNeighbors += 1 
                    if currentCells[rightCoord][belowCoord] == '#': numNeighbors += 1 
        
                    if currentCells[x][y] == '#' and (numNeighbors == 2 or numNeighbors == 3): 
                        nextCells[x][y] = '#' 
                    elif currentCells[x][y] == ' ' and numNeighbors == 3: 
                        nextCells[x][y] = '#' 
                    else: 
                        nextCells[x][y] = ' ' 
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nSimulation Stopped.")

# ==========================================
# PART 2: The Game GUI Logic
# ==========================================
class RetroLifeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Conway's Game of Life - Simulation")
        
        # Dynamic Dimensions (Starts with default, changes on fullscreen)
        self.cols = DEFAULT_WIDTH
        self.rows = DEFAULT_HEIGHT
        
        # Retro Colors
        self.bg_color = "#c0c0c0" 
        self.cell_alive = "#000080" # Navy
        self.cell_dead = "#ffffff"
        
        self.root.configure(bg=self.bg_color)
        self.running = False
        
        self.canvas = None
        self.cells = []
        self.rects = []

        self.setup_controls()
        self.create_grid() # Draws the initial default grid

    def setup_controls(self):
        # Header
        header_font = font.Font(family="Courier", size=12, weight="bold")
        tk.Label(self.root, text="SIMULATION WINDOW", bg="#000080", fg="white", 
                 font=header_font, pady=5).pack(fill=tk.X)

        # Controls Frame
        self.control_frame = tk.Frame(self.root, bg=self.bg_color, bd=3, relief="raised")
        self.control_frame.pack(pady=10, fill=tk.X)
        
        # Center the buttons inside the frame using a sub-frame
        btn_area = tk.Frame(self.control_frame, bg=self.bg_color)
        btn_area.pack()

        self.btn_text = tk.StringVar(value="START")
        tk.Button(btn_area, textvariable=self.btn_text, command=self.toggle_sim,
                  bg=self.bg_color, relief="raised", width=8).grid(row=0, column=0, padx=5)

        tk.Button(btn_area, text="CLEAR", command=self.clear_grid,
                  bg=self.bg_color, relief="raised", width=8).grid(row=0, column=1, padx=5)

        tk.Button(btn_area, text="RANDOM", command=self.randomize_grid,
                  bg=self.bg_color, relief="raised", width=8).grid(row=0, column=2, padx=5)

        # New Fullscreen Button
        tk.Button(btn_area, text="FULL SCR", command=self.go_fullscreen,
                  bg=self.bg_color, relief="raised", width=8).grid(row=0, column=3, padx=5)

        tk.Label(btn_area, text="SPEED:", bg=self.bg_color).grid(row=0, column=4, padx=5)
        self.speed_scale = tk.Scale(btn_area, from_=500, to=10, orient=tk.HORIZONTAL, 
                                    bg=self.bg_color, length=100, showvalue=0)
        self.speed_scale.set(100) 
        self.speed_scale.grid(row=0, column=5, padx=5)
        
        # Exit Fullscreen binding (Esc key)
        self.root.bind("<Escape>", self.exit_fullscreen)

    def create_grid(self):
        """Creates (or recreates) the grid based on current self.cols and self.rows"""
        # Remove old canvas if it exists
        if self.canvas:
            self.canvas.destroy()
            
        # Stop simulation if running
        self.running = False
        self.btn_text.set("START")

        # Reset Data Structures
        self.cells = [[0 for _ in range(self.rows)] for _ in range(self.cols)]
        self.rects = [[None for _ in range(self.rows)] for _ in range(self.cols)]

        # Calculate Canvas Size
        canvas_width = self.cols * CELL_SIZE
        canvas_height = self.rows * CELL_SIZE

        # Create New Canvas
        self.canvas = tk.Canvas(self.root, width=canvas_width, height=canvas_height, 
                                bg="white", highlightthickness=2, highlightbackground="#808080")
        self.canvas.pack(padx=15, pady=10)

        # Draw Rectangles
        for x in range(self.cols):
            for y in range(self.rows):
                x1, y1 = x * CELL_SIZE, y * CELL_SIZE
                x2, y2 = x1 + CELL_SIZE, y1 + CELL_SIZE
                self.rects[x][y] = self.canvas.create_rectangle(x1, y1, x2, y2, 
                                                       fill=self.cell_dead, outline="#d0d0d0")

        # Re-bind inputs
        self.canvas.bind("<Button-1>", self.handle_click)
        self.canvas.bind("<B1-Motion>", self.handle_click)

    def go_fullscreen(self):
        """Calculates screen size and rebuilds grid to fill it."""
        # 1. Enable Window Fullscreen
        self.root.attributes('-fullscreen', True)
        self.root.update_idletasks() # Update to get correct screen dims
        
        # 2. Get Screen Dimensions
        screen_w = self.root.winfo_screenwidth()
        screen_h = self.root.winfo_screenheight()
        
        # 3. Calculate space available (Screen Height - Control Panel Height)
        # We estimate control panel + padding is about 120px
        available_h = screen_h - 120 
        
        # 4. Calculate new grid dimensions
        self.cols = (screen_w - 40) // CELL_SIZE # -40 for side padding
        self.rows = available_h // CELL_SIZE
        
        # 5. Rebuild Grid
        self.create_grid()

    def exit_fullscreen(self, event=None):
        """Optional: Press ESC to leave fullscreen and return to default."""
        self.root.attributes('-fullscreen', False)
        self.cols = DEFAULT_WIDTH
        self.rows = DEFAULT_HEIGHT
        self.create_grid()

    def handle_click(self, event):
        if self.running: return
        x, y = event.x // CELL_SIZE, event.y // CELL_SIZE
        if 0 <= x < self.cols and 0 <= y < self.rows:
            self.cells[x][y] = 1
            self.update_single_cell(x, y)

    def update_single_cell(self, x, y):
        color = self.cell_alive if self.cells[x][y] == 1 else self.cell_dead
        self.canvas.itemconfig(self.rects[x][y], fill=color)

    def update_all_visuals(self):
        for x in range(self.cols):
            for y in range(self.rows):
                self.update_single_cell(x, y)

    def randomize_grid(self):
        self.running = False
        self.btn_text.set("START")
        for x in range(self.cols):
            for y in range(self.rows):
                self.cells[x][y] = 1 if random.randint(0, 1) == 0 else 0
        self.update_all_visuals()

    def clear_grid(self):
        self.running = False
        self.btn_text.set("START")
        self.cells = [[0 for _ in range(self.rows)] for _ in range(self.cols)]
        self.update_all_visuals()

    def toggle_sim(self):
        if self.running:
            self.running = False
            self.btn_text.set("RESUME")
        else:
            self.running = True
            self.btn_text.set("PAUSE")
            self.run_step()

    def run_step(self):
        if not self.running: return
        new_cells = copy.deepcopy(self.cells)
        
        for x in range(self.cols):
            for y in range(self.rows):
                left, right = (x - 1) % self.cols, (x + 1) % self.cols
                above, below = (y - 1) % self.rows, (y + 1) % self.rows
                neighbors = 0
                if self.cells[left][above]: neighbors += 1
                if self.cells[x][above]: neighbors += 1
                if self.cells[right][above]: neighbors += 1
                if self.cells[left][y]: neighbors += 1
                if self.cells[right][y]: neighbors += 1
                if self.cells[left][below]: neighbors += 1
                if self.cells[x][below]: neighbors += 1
                if self.cells[right][below]: neighbors += 1

                if self.cells[x][y] == 1 and (neighbors == 2 or neighbors == 3):
                    new_cells[x][y] = 1
                elif self.cells[x][y] == 0 and neighbors == 3:
                    new_cells[x][y] = 1
                else:
                    new_cells[x][y] = 0
        
        self.cells = new_cells
        self.update_all_visuals()
        self.root.after(self.speed_scale.get(), self.run_step)

# ==========================================
# PART 3: New Module Placeholders
# ==========================================
def run_alternative_mode():
    # TODO: Add your code for Alternative Mode here
    print("\n[!] Running Alternative Mode...")
    print("    (No logic has been added to this module yet.)")
    input("    Press Enter to exit...")

def run_initial_mode():
    # TODO: Add your code for Initial Mode here
    print("\n[!] Running Initial Mode...")
    print("    (No logic has been added to this module yet.)")
    input("    Press Enter to exit...")

# ==========================================
# PART 4: The Launcher (Main Entry Point)
# ==========================================
class Launcher:
    def __init__(self, root):
        self.root = root
        self.root.title("System Launcher")
        self.root.geometry("400x350") 
        self.root.configure(bg="#c0c0c0") 

        # Styling
        title_font = font.Font(family="Courier", size=16, weight="bold")
        btn_font = font.Font(family="MS Sans Serif", size=10, weight="bold")

        # Frame
        frame = tk.Frame(root, bg="#c0c0c0", bd=5, relief="raised")
        frame.place(relx=0.5, rely=0.5, anchor="center")

        # Title
        tk.Label(frame, text="SELECT MODULE", bg="#000080", fg="white", 
                 font=title_font, padx=20, pady=10).pack(pady=10, fill=tk.X)

        # Buttons
        tk.Button(frame, text="GRAPHICAL (GUI)", font=btn_font, 
                  command=lambda: self.select_mode("GUI"), 
                  bg="#c0c0c0", relief="raised", bd=3).pack(pady=5, ipadx=10, ipady=5, fill=tk.X)

        tk.Button(frame, text="COMMAND LINE (CLI)", font=btn_font, 
                  command=lambda: self.select_mode("CLI"), 
                  bg="#c0c0c0", relief="raised", bd=3).pack(pady=5, ipadx=10, ipady=5, fill=tk.X)
        
        tk.Button(frame, text="ALTERNATIVE MODE", font=btn_font, 
                  command=lambda: self.select_mode("ALT"), 
                  bg="#c0c0c0", relief="raised", bd=3).pack(pady=5, ipadx=10, ipady=5, fill=tk.X)

        tk.Button(frame, text="INITIAL MODE", font=btn_font, 
                  command=lambda: self.select_mode("INIT"), 
                  bg="#c0c0c0", relief="raised", bd=3).pack(pady=5, ipadx=10, ipady=5, fill=tk.X)

        self.mode = None 

    def select_mode(self, mode_type):
        self.mode = mode_type
        self.root.destroy() 

def main():
    root = tk.Tk()
    launcher = Launcher(root)
    root.mainloop()

    if launcher.mode == "GUI":
        game_root = tk.Tk()
        # Start maximize if possible (not full screen yet)
        try: game_root.state('zoomed') 
        except: pass
        app = RetroLifeGUI(game_root)
        game_root.mainloop()
        
    elif launcher.mode == "CLI":
        run_cli_version()
    elif launcher.mode == "ALT":
        run_alternative_mode()
    elif launcher.mode == "INIT":
        run_initial_mode()

if __name__ == "__main__":
    main()