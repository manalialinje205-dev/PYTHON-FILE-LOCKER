from cryptography.fernet import Fernet
import os
import sys
import time
import tkinter as tk
from tkinter import filedialog

KEY_FILE = "secret.key"

def generate_key():
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as key_file:
        key_file.write(key)
    print(f" New key generated and saved as {KEY_FILE}")

def load_key():
    return open(KEY_FILE, "rb").read()

def select_file():
    """Opens a file dialog to select a file."""
    root = tk.Tk()
    root.withdraw() 
    file_path = filedialog.askopenfilename(
        title="Select a file to Encrypt/Decrypt",
        filetypes=[("All Files", "*.*")]
    )
    root.destroy()
    return file_path

def process_file(filename, key, mode):
    f = Fernet(key)
    try:
        with open(filename, "rb") as file:
            data = file.read()

        if mode == 'encrypt':
            processed_data = f.encrypt(data)
            action = "Encrypted"
        else:
            processed_data = f.decrypt(data)
            action = "Decrypted"

        with open(filename, "wb") as file:
            file.write(processed_data)
        
        print(f"\n SUCCESS: '{os.path.basename(filename)}' has been {action}.")
        time.sleep(2) 
    except Exception as e:
        print(f"\n ERROR: Could not {mode} the file. (Invalid key or file corrupted)")
        time.sleep(2)

def main():
    if not os.path.exists(KEY_FILE):
        generate_key()
    
    key = load_key()

    while True:
        print("\n" + "="*30)
        print("FILE LOCKER MENU")
        print("="*30)
        print("1. Encrypt a file")
        print("2. Decrypt a file")
        print("3. Exit Program")
        print("-"*30)
        
        choice = input("Select an option (1-3): ")

        if choice == '3':
            print("\n Closing File Locker. Stay safe!")
            break 

        if choice in ['1', '2']:
            print("\n Please select a file in the popup window...")
            filename = select_file()
            
            if not filename:
                print("No file selected. Returning to menu.")
                continue

            if os.path.basename(filename) == KEY_FILE:
                print("Permission Denied: You cannot encrypt the key file!")
                continue

            mode = 'encrypt' if choice == '1' else 'decrypt'
            process_file(filename, key, mode)
        else:
            print("Invalid choice! Please pick 1, 2, or 3.")

if __name__ == "__main__":
    main()
