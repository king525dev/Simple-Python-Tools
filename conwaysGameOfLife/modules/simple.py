import random
import time
import copy
import sys

# Try to import Tkinter for the GUI
try:
    import tkinter as tk
    from tkinter import font
except ImportError:
    print("Tkinter is not installed. GUI mode will not work.")

# --- Configuration ---
WIDTH = 60
HEIGHT = 20
CELL_SIZE = 20  # Pixel size for GUI squares

def run_cli_version():
    """Runs the original text-based version of the game."""
    print("Starting Command Line Version...")
    
    # Create a list of list for the cells:
    nextCells = []
    for x in range(WIDTH):
        column = [] # Create a new column.
        for y in range(HEIGHT):
            if random.randint(0, 1) == 0:
                column.append('#') # Add a living cell.
            else:
                column.append(' ') # Add a dead cell.
        nextCells.append(column) # nextCells is a list of column lists.

    try:
        while True: # Main program loop.
            print('\n\n\n----------\n\n\n\n\n----------\n\n\n') # Separate each step with newlines.
            currentCells = copy.deepcopy(nextCells)

            # Print currentCells on the screen:
            for y in range(HEIGHT):
                for x in range(WIDTH):
                    print(currentCells[x][y], end='') # Print the # or space.
                print() # Print a newline at the end of the row.

            # Calculate the next step's cells based on current step's cells:
            for x in range(WIDTH):
                for y in range(HEIGHT):
                    # Get neighboring coordinates:
                    leftCoord  = (x - 1) % WIDTH
                    rightCoord = (x + 1) % WIDTH
                    aboveCoord = (y - 1) % HEIGHT
                    belowCoord = (y + 1) % HEIGHT

                    # Count number of living neighbors:
                    numNeighbors = 0
                    if currentCells[leftCoord][aboveCoord] == '#': numNeighbors += 1
                    if currentCells[x][aboveCoord] == '#': numNeighbors += 1
                    if currentCells[rightCoord][aboveCoord] == '#': numNeighbors += 1
                    if currentCells[leftCoord][y] == '#': numNeighbors += 1
                    if currentCells[rightCoord][y] == '#': numNeighbors += 1
                    if currentCells[leftCoord][belowCoord] == '#': numNeighbors += 1
                    if currentCells[x][belowCoord] == '#': numNeighbors += 1
                    if currentCells[rightCoord][belowCoord] == '#': numNeighbors += 1

                    # Set cell based on Conway's Game of Life rules:
                    if currentCells[x][y] == '#' and (numNeighbors == 2 or numNeighbors == 3):
                        nextCells[x][y] = '#'
                    elif currentCells[x][y] == ' ' and numNeighbors == 3:
                        nextCells[x][y] = '#'
                    else:
                        nextCells[x][y] = ' '
            time.sleep(1) 
    except KeyboardInterrupt:
        print("\nExiting CLI mode.")

class RetroLifeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Conway's Game of Life - Retro Edition")
        
        # Retro Colors
        self.bg_color = "#c0c0c0"  # Classic Windows Gray
        self.grid_bg = "#ffffff"
        self.cell_alive = "#000080" # Navy Blue
        self.cell_dead = "#ffffff"
        self.grid_line = "#808080"
        
        self.root.configure(bg=self.bg_color)
        self.running = False
        
        # Data Structure (x, y)
        # 0 is dead, 1 is alive
        self.cells = [[0 for _ in range(HEIGHT)] for _ in range(WIDTH)]
        self.rects = [[None for _ in range(HEIGHT)] for _ in range(WIDTH)]

        self.setup_ui()

    def setup_ui(self):
        # --- Header ---
        header_font = font.Font(family="Courier", size=14, weight="bold")
        title_lbl = tk.Label(self.root, text="SIMULATION: LIFE.EXE", 
                             bg="#000080", fg="white", font=header_font, pady=5)
        title_lbl.pack(fill=tk.X)

        # --- Controls Frame ---
        control_frame = tk.Frame(self.root, bg=self.bg_color, bd=3, relief="raised")
        control_frame.pack(pady=10)

        # Start/Stop Button
        self.btn_text = tk.StringVar(value="START")
        tk.Button(control_frame, textvariable=self.btn_text, command=self.toggle_sim,
                  bg=self.bg_color, relief="raised", width=10).grid(row=0, column=0, padx=5)

        # Clear Button
        tk.Button(control_frame, text="CLEAR", command=self.clear_grid,
                  bg=self.bg_color, relief="raised", width=10).grid(row=0, column=1, padx=5)

        # Randomize Button
        tk.Button(control_frame, text="RANDOM", command=self.randomize_grid,
                  bg=self.bg_color, relief="raised", width=10).grid(row=0, column=2, padx=5)

        # Speed Slider
        tk.Label(control_frame, text="SPEED:", bg=self.bg_color).grid(row=0, column=3, padx=5)
        self.speed_scale = tk.Scale(control_frame, from_=500, to=10, orient=tk.HORIZONTAL, 
                                    bg=self.bg_color, length=150, showvalue=0)
        self.speed_scale.set(100) # Default speed
        self.speed_scale.grid(row=0, column=4, padx=5)

        # --- The Grid (Canvas) ---
        canvas_width = WIDTH * CELL_SIZE
        canvas_height = HEIGHT * CELL_SIZE
        self.canvas = tk.Canvas(self.root, width=canvas_width, height=canvas_height, 
                                bg="white", highlightthickness=2, highlightbackground="#808080")
        self.canvas.pack(padx=20, pady=20)

        # Initialize Grid Rectangles
        for x in range(WIDTH):
            for y in range(HEIGHT):
                x1 = x * CELL_SIZE
                y1 = y * CELL_SIZE
                x2 = x1 + CELL_SIZE
                y2 = y1 + CELL_SIZE
                # Create rectangle and store ID
                rect_id = self.canvas.create_rectangle(x1, y1, x2, y2, 
                                                       fill=self.cell_dead, outline="#d0d0d0")
                self.rects[x][y] = rect_id

        # Bind Mouse Click
        self.canvas.bind("<Button-1>", self.handle_click)
        self.canvas.bind("<B1-Motion>", self.handle_click) # Allow dragging to draw

        # Instructions
        tk.Label(self.root, text="> CLICK GRID TO EDIT | PRESS START TO RUN", 
                 bg=self.bg_color, font=("Courier", 10)).pack(pady=5)

    def handle_click(self, event):
        """Toggle cell state on click."""
        if self.running: return # Don't edit while running
        
        x = event.x // CELL_SIZE
        y = event.y // CELL_SIZE

        if 0 <= x < WIDTH and 0 <= y < HEIGHT:
            # Toggle logic: If dead make alive
            self.cells[x][y] = 1
            self.update_single_cell(x, y)

    def update_single_cell(self, x, y):
        color = self.cell_alive if self.cells[x][y] == 1 else self.cell_dead
        self.canvas.itemconfig(self.rects[x][y], fill=color)

    def update_all_visuals(self):
        for x in range(WIDTH):
            for y in range(HEIGHT):
                self.update_single_cell(x, y)

    def randomize_grid(self):
        self.running = False
        self.btn_text.set("START")
        for x in range(WIDTH):
            for y in range(HEIGHT):
                self.cells[x][y] = 1 if random.randint(0, 1) == 0 else 0
        self.update_all_visuals()

    def clear_grid(self):
        self.running = False
        self.btn_text.set("START")
        self.cells = [[0 for _ in range(HEIGHT)] for _ in range(WIDTH)]
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

        # Create a copy for calculation
        new_cells = copy.deepcopy(self.cells)

        for x in range(WIDTH):
            for y in range(HEIGHT):
                # Calculate Neighbors (Using Modulo for Wrapping)
                left  = (x - 1) % WIDTH
                right = (x + 1) % WIDTH
                above = (y - 1) % HEIGHT
                below = (y + 1) % HEIGHT

                neighbors = 0
                if self.cells[left][above] == 1: neighbors += 1
                if self.cells[x][above] == 1: neighbors += 1
                if self.cells[right][above] == 1: neighbors += 1
                if self.cells[left][y] == 1: neighbors += 1
                if self.cells[right][y] == 1: neighbors += 1
                if self.cells[left][below] == 1: neighbors += 1
                if self.cells[x][below] == 1: neighbors += 1
                if self.cells[right][below] == 1: neighbors += 1

                # Apply Rules
                if self.cells[x][y] == 1 and (neighbors == 2 or neighbors == 3):
                    new_cells[x][y] = 1
                elif self.cells[x][y] == 0 and neighbors == 3:
                    new_cells[x][y] = 1
                else:
                    new_cells[x][y] = 0
        
        self.cells = new_cells
        self.update_all_visuals()
        
        # Schedule next frame based on slider speed
        delay = self.speed_scale.get()
        self.root.after(delay, self.run_step)

def main():
    print("Conway's Game of Life Simulator")
    print("-------------------------------")
    print("1. Graphical Interface (GUI)")
    print("2. Command Line (Text Only)")
    
    choice = input("\nEnter choice (1 or 2): ").strip()

    if choice == '1':
        root = tk.Tk()
        app = RetroLifeGUI(root)
        root.mainloop()
    elif choice == '2':
        run_cli_version()
    else:
        print("Invalid selection. Defaulting to GUI.")
        root = tk.Tk()
        app = RetroLifeGUI(root)
        root.mainloop()

if __name__ == "__main__":
    main()