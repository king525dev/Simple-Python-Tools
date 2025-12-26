# Conway's Game of Life - CLI + GUI version
import random, time, copy, tkinter as tk
from tkinter import messagebox

# === CONFIGURATION ===
WIDTH = 60
HEIGHT = 20

def run_cli():
    """Run Conway's Game of Life in the console."""
    nextCells = []
    for x in range(WIDTH):
        column = []
        for y in range(HEIGHT):
            if random.randint(0, 1) == 0:
                column.append('#')
            else:
                column.append(' ')
        nextCells.append(column)

    while True:
        print('\n\n\n----------\n\n\n')
        currentCells = copy.deepcopy(nextCells)

        # Print currentCells on screen
        for y in range(HEIGHT):
            for x in range(WIDTH):
                print(currentCells[x][y], end='')
            print()

        # Calculate next step
        for x in range(WIDTH):
            for y in range(HEIGHT):
                leftCoord  = (x - 1) % WIDTH
                rightCoord = (x + 1) % WIDTH
                aboveCoord = (y - 1) % HEIGHT
                belowCoord = (y + 1) % HEIGHT

                numNeighbors = 0
                if currentCells[leftCoord][aboveCoord] == '#':
                    numNeighbors += 1
                if currentCells[x][aboveCoord] == '#':
                    numNeighbors += 1
                if currentCells[rightCoord][aboveCoord] == '#':
                    numNeighbors += 1
                if currentCells[leftCoord][y] == '#':
                    numNeighbors += 1
                if currentCells[rightCoord][y] == '#':
                    numNeighbors += 1
                if currentCells[leftCoord][belowCoord] == '#':
                    numNeighbors += 1
                if currentCells[x][belowCoord] == '#':
                    numNeighbors += 1
                if currentCells[rightCoord][belowCoord] == '#':
                    numNeighbors += 1

                # Game of Life rules
                if currentCells[x][y] == '#' and (numNeighbors == 2 or numNeighbors == 3):
                    nextCells[x][y] = '#'
                elif currentCells[x][y] == ' ' and numNeighbors == 3:
                    nextCells[x][y] = '#'
                else:
                    nextCells[x][y] = ' '
        time.sleep(0.5)


# === GUI VERSION ===
CELL_SIZE = 20
GRID_WIDTH = 30
GRID_HEIGHT = 20

class GameOfLifeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Conway's Game of Life - Retro Edition")
        self.root.config(bg="#c0c0c0")  # Windows 2000 gray aesthetic

        self.running = False
        self.speed = 500  # milliseconds

        # Title
        title = tk.Label(root, text="Conway's Game of Life", bg="#000080", fg="white",
                            font=("Courier", 14, "bold"), relief="ridge", width=40, pady=5)
        title.pack(pady=5)

        # Canvas grid
        self.canvas = tk.Canvas(root, width=GRID_WIDTH * CELL_SIZE,
                                height=GRID_HEIGHT * CELL_SIZE, bg="#f0f0f0", highlightthickness=2, highlightbackground="#808080")
        self.canvas.pack(padx=10, pady=10)

        # Draw grid
        self.cells = {}
        for x in range(GRID_WIDTH):
            for y in range(GRID_HEIGHT):
                rect = self.canvas.create_rectangle(
                    x*CELL_SIZE, y*CELL_SIZE,
                    (x+1)*CELL_SIZE, (y+1)*CELL_SIZE,
                    fill="#f0f0f0", outline="#a0a0a0")
                self.cells[(x, y)] = {"rect": rect, "alive": False}

        self.canvas.bind("<Button-1>", self.toggle_cell)

        # Controls
        control_frame = tk.Frame(root, bg="#c0c0c0")
        control_frame.pack(pady=5)

        self.start_button = tk.Button(control_frame, text="▶ Start", width=10, command=self.start, bg="#e0e0e0")
        self.start_button.grid(row=0, column=0, padx=5)

        self.stop_button = tk.Button(control_frame, text="⏹ Stop", width=10, command=self.stop, bg="#e0e0e0")
        self.stop_button.grid(row=0, column=1, padx=5)

        clear_btn = tk.Button(control_frame, text="🧹 Clear", width=10, command=self.clear, bg="#e0e0e0")
        clear_btn.grid(row=0, column=2, padx=5)

        tk.Label(control_frame, text="Speed (ms):", bg="#c0c0c0").grid(row=1, column=0, pady=5)
        self.speed_entry = tk.Entry(control_frame, width=8)
        self.speed_entry.insert(0, str(self.speed))
        self.speed_entry.grid(row=1, column=1)

        apply_btn = tk.Button(control_frame, text="Apply", command=self.set_speed, bg="#e0e0e0")
        apply_btn.grid(row=1, column=2)

    def toggle_cell(self, event):
        x = event.x // CELL_SIZE
        y = event.y // CELL_SIZE
        cell = self.cells.get((x, y))
        if cell:
            cell["alive"] = not cell["alive"]
            color = "#00cc00" if cell["alive"] else "#f0f0f0"
            self.canvas.itemconfig(cell["rect"], fill=color)

    def set_speed(self):
        try:
            val = int(self.speed_entry.get())
            self.speed = max(100, val)
        except ValueError:
            messagebox.showerror("Invalid Input", "Speed must be a number.")

    def clear(self):
        for c in self.cells.values():
            c["alive"] = False
            self.canvas.itemconfig(c["rect"], fill="#f0f0f0")

    def start(self):
        if not self.running:
            self.running = True
            self.update_game()

    def stop(self):
        self.running = False

    def update_game(self):
        if not self.running:
            return

        new_state = {}
        for (x, y), cell in self.cells.items():
            neighbors = 0
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if dx == 0 and dy == 0:
                        continue
                    nx = (x + dx) % GRID_WIDTH
                    ny = (y + dy) % GRID_HEIGHT
                    if self.cells[(nx, ny)]["alive"]:
                        neighbors += 1
            # Apply rules
            if cell["alive"]:
                new_state[(x, y)] = neighbors in [2, 3]
            else:
                new_state[(x, y)] = neighbors == 3

        # Update cells visually
        for (x, y), alive in new_state.items():
            self.cells[(x, y)]["alive"] = alive
            color = "#000080" if alive else "#f0f0f0"
            self.canvas.itemconfig(self.cells[(x, y)]["rect"], fill=color)

        self.root.after(self.speed, self.update_game)


def run_gui():
    root = tk.Tk()
    app = GameOfLifeGUI(root)
    root.mainloop()


# === MAIN CHOICE ===
if __name__ == "__main__":
    print("Conway's Game of Life")
    print("1. Run in Command Line")
    print("2. Run in GUI (Retro Mode)")
    choice = input("Choose mode (1 or 2): ")

    if choice == "1":
        run_cli()
    else:
        run_gui()
