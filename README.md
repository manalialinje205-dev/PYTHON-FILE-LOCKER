Project Overview

This Python File Locker is a lightweight security utility designed to protect sensitive data through AES-based symmetric encryption. It utilizes the cryptography library's Fernet implementation to ensure that files are encrypted with a high standard of security, making them inaccessible without the unique master key.

How It Works

The application combines a user-friendly command-line menu with a Tkinter-based GUI file explorer. Upon execution, it automatically manages your encryption keys; it will generate a secret.key file if one isn't present or load the existing one to process files. Users can quickly select any file from their system via a popup window to either lock it (encrypt) or unlock it (decrypt) in place.

Security & Usage

Built with safety in mind, the script includes logic to prevent users from accidentally encrypting the key file itself, which would result in a permanent lockout. Because this tool overwrites the original file during the process, it serves as an efficient way to secure private documents, images, or data logs directly on local storage.
