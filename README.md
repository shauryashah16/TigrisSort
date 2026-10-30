# TigrisSort

A lightweight, automated file organization utility written in Python using modern filesystem pathways.

## Features
- **Automatic Classification:** Groups files instantly by extension into clean, uppercase subdirectories.
- **Dynamic Safeguards:** Includes a modular safelist system to protect active scripts and critical system files.
- **Turnkey Revert Engine:** Generates a persistent state log allowing users to reverse all actions and instantly undo the entire sorting process.
- **Zero Dependencies:** Built entirely using native Python standard libraries (`pathlib`, `shutil`).

## How to Run
1. Place `TigrisSort.py` into your target directory.
2. Open your terminal in the workspace directory.
3. Run the organization loop:
   ```bash
   python TigrisSort.py
   ```

## Reverting Changes
To completely reverse the organization process, uncomment the `undo_organization` method at the bottom of the script and execute the file again.
