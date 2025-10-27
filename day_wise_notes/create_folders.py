import os

# --- Configuration ---

# The main directory where you want to create the 100 folders.
# '.' means the current directory where you run the script.
# You can change this to a specific path, for example:
# BASE_DIR = "C:/Users/YourUser/Desktop/My_100_Day_Project"
BASE_DIR = "."

# The total number of days/folders you want to create.
TOTAL_DAYS = 100

# The formatting pattern for the folder name.
# {day} will be replaced by the day number (1, 2, 3...).
# Your example "15_day_15" matches the pattern f"{day}_day_{day}"
# If you wanted "Day_001", "Day_002", you could use:
# FOLDER_PATTERN = "Day_{day:03d}"
FOLDER_PATTERN = "{day}_day_{day}"

# --- End of Configuration ---


def create_day_folders():
    """
    Creates a series of numbered day folders in the BASE_DIR.
    """
    
    # Gets the full, absolute path for cleaner print messages
    base_path = os.path.abspath(BASE_DIR)
    print(f"Starting to create {TOTAL_DAYS} folders in: {base_path}")
    
    # Loop from 1 up to and including TOTAL_DAYS
    for day_num in range(1, TOTAL_DAYS + 1):
        
        # Format the folder name using the pattern
        # e.g., "1_day_1", "2_day_2", ... "100_day_100"
        folder_name = FOLDER_PATTERN.format(day=day_num)
        
        # Create the full path by joining the base directory and the new folder name
        # os.path.join handles path separators (like / or \) correctly
        folder_path = os.path.join(base_path, folder_name)
        
        try:
            # os.makedirs() creates the directory.
            # exist_ok=True prevents the script from crashing if the
            # folder already exists. It will just skip it.
            os.makedirs(folder_path, exist_ok=True)
            
            print(f"Successfully created or found: {folder_path}")
            
        except OSError as e:
            # Catch other potential errors (e.g., permission denied)
            print(f"Error creating directory {folder_path}: {e}")

    print(f"\nFolder creation process complete for {TOTAL_DAYS} days.")

# This common Python pattern allows the script to be run
# directly from the command line.
if __name__ == "__main__":
    create_day_folders()
