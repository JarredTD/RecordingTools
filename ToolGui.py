from pathlib import Path
from src.RootWindow import RootWindow

### Constants
CWD = Path.cwd()
PARENT_DIR = CWD.parent # Move out of the Scripts Dir





# Debugging
if __name__ == "__main__":
    rw = RootWindow()
    rw.mainloop()