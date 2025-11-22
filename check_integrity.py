import os
import hashlib
from datetime import datetime

HASH_FILE = "hashes.txt"
LOG_FILE = "check_log.txt"

def calculate_hash(filename):
    """Calculate SHA-256 hash of a file"""
    with open(filename, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()

def load_hashes():
    """Load saved hashes from HASH_FILE"""
    hashes = {}
    if os.path.exists(HASH_FILE):
        with open(HASH_FILE, "r") as f:
            for line in f:
                name, saved_hash = line.strip().split(",")
                hashes[name] = saved_hash
    return hashes

def save_hashes(hashes):
    """Save hashes to HASH_FILE"""
    with open(HASH_FILE, "w") as f:
        for name, h in hashes.items():
            f.write(f"{name},{h}\n")

def log_change(message):
    """Log every check in LOG_FILE"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as f:
        f.write(f"[{timestamp}] {message}\n")

def check_file(filename, hashes):
    if not os.path.exists(filename):
        print(f"❌ File '{filename}' does NOT exist.")
        return hashes

    current_hash = calculate_hash(filename)
    if filename in hashes:
        if hashes[filename] == current_hash:
            print(f"✅ '{filename}' is unchanged.")
            log_change(f"{filename} unchanged")
        else:
            print(f"⚠️ '{filename}' has been MODIFIED!")
            log_change(f"{filename} modified")
    else:
        print(f"ℹ️ First time checking '{filename}'. Hash saved.")
        log_change(f"{filename} first check")
    
    hashes[filename] = current_hash
    return hashes

def check_all_files(hashes):
    for filename in os.listdir():
        if filename.endswith(".py"):
            hashes = check_file(filename, hashes)
    return hashes

def main():
    print("=== Simple File Integrity Checker ===")
    hashes = load_hashes()

    while True:
        print("\nMenu:")
        print("1. Check a single file")
        print("2. Check all .py files in folder")
        print("3. Exit")
        choice = input("Enter choice (1/2/3): ")

        if choice == "1":
            filename = input("Enter file name: ")
            hashes = check_file(filename, hashes)
        elif choice == "2":
            hashes = check_all_files(hashes)
        elif choice == "3":
            break
        else:
            print("❌ Invalid choice. Please enter 1, 2, or 3.")

    save_hashes(hashes)
    print("\nAll done! Hashes saved in 'hashes.txt'.")

if __name__ == "__main__":
    main()
