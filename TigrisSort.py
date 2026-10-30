import os
import shutil
from pathlib import Path

# Define the local database text file to log all movements
LOG_FILE_NAME = "tigrissort_history.log"

def organize_folder(target_folder_path):
    target_path = Path(target_folder_path)
    
    if not target_path.exists():
        print(f"Error: The folder '{target_folder_path}' does not exist.")
        return
        
    SAFELIST_FILES = ["TigrisSort.py", "LICENSE", "README.md", ".git", LOG_FILE_NAME]
    SAFELIST_EXTENSIONS = ["ini", "sys"]
    
    log_path = target_path / LOG_FILE_NAME
    
    print(f"[INFO] Scanning folder: {target_path.resolve()}")
    
    # Open the log file in 'append' mode to record movements
    with open(log_path, "a", encoding="utf-8") as log:
        for item in target_path.iterdir():
            if item.is_dir():
                continue
                
            if item.name in SAFELIST_FILES or item.suffix.lower().replace('.', '') in SAFELIST_EXTENSIONS:
                print(f"Skipped (Safelist): {item.name}")
                continue
                
            file_extension = item.suffix.lower().replace('.', '')
            if not file_extension:
                file_extension = "unknown"
                
            destination_folder = target_path / file_extension.upper()
            
            if not destination_folder.exists():
                destination_folder.mkdir()
                print(f"Created subfolder: {destination_folder.name}")
                
            destination_file_path = destination_folder / item.name
            
            try:
                # Record the movement in the log: "Old_Location -> New_Location"
                log.write(f"{item.name},{destination_folder.name}/{item.name}\n")
                
                shutil.move(str(item), str(destination_file_path))
                print(f"Moved: {item.name} -> {destination_folder.name}/")
            except Exception as e:
                print(f"Failed to move {item.name}: {e}")

def undo_organization(target_folder_path):
    """Reads the log history file and reverses every file movement execution."""
    target_path = Path(target_folder_path)
    log_path = target_path / LOG_FILE_NAME
    
    if not log_path.exists():
        print("[ERROR] No history log found. Nothing to undo!")
        return
        
    print(f"\n[INFO] Activating Undo Engine...")
    
    # Read all logged movements
    with open(log_path, "r", encoding="utf-8") as log:
        lines = log.readlines()
        
    # Process the lines in reverse order (Last In, First Out)
    for line in reversed(lines):
        line = line.strip()
        if not line or "," not in line:
            continue
            
        original_name, current_relative_path = line.split(",")
        
        current_file_path = target_path / current_relative_path
        restored_file_path = target_path / original_name
        
        if current_file_path.exists():
            try:
                shutil.move(str(current_file_path), str(restored_file_path))
                print(f"Restored: {original_name} back to root workspace")
                
                # Clean up the folder if it is now empty
                parent_dir = current_file_path.parent
                if parent_dir.exists() and not any(parent_dir.iterdir()):
                    parent_dir.rmdir()
                    print(f"Removed empty directory: {parent_dir.name}")
            except Exception as e:
                print(f"Failed to restore {original_name}: {e}")
                
    # Delete the log file since history is now completely cleared
    os.remove(log_path)
    print("[SUCCESS] Workspace completely restored to original state.")

# --- CONTROL PANEL ---
folder_to_clean = r"."

# Action 1: To organize your folder, leave this active:
organize_folder(folder_to_clean)

# Action 2: To UNDO everything, uncomment the line below (remove the #) and comment out organize_folder!
# undo_organization(folder_to_clean)
