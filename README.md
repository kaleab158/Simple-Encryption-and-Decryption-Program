🔐 Simple Encryption & Decryption Program (Python)

A simple Python-based encryption and decryption tool that transforms readable text into encrypted ciphertext and restores it back using a shuffled character key.

This project demonstrates core concepts of:
Character mapping

Randomization

Symmetric encryption logic

Python string handling


📌 Features

 Random key generation using random.shuffle()

 Symmetric encryption & decryption

 Uses letters, digits, punctuation, and spaces

Simple command-line interface

Lightweight and beginner-friendly

⚙️ How It Works (Process)

1️ Character Set Creation

The program creates a list of characters including:
Uppercase letters

Lowercase letters

Numbers

Symbols

Spaces

Chars = "  " + string.ascii_letters + string.digits + string.punctuation

2️ Key Generation

A copy of the character list is shuffled randomly:
key = Chars.copy()
random.shuffle(key)
This shuffled list acts as the encryption key.

3️ Encryption Process
The program asks the user to enter a message.

Each character in the message is replaced with its corresponding shuffled character.

The result becomes the encrypted message (ciphertext).

4️ Decryption Process

The encrypted text is entered.

The program finds each character in the shuffled key.

It maps it back to the original character list.

The original message is restored.


🚀 How To Run The Project
Step 1: Clone the Repository
git clone https://github.com/your-username/Simple-Encryption-and-Decryption-Program.git
Step 2: Navigate into the Project
cd Simple-Encryption-and-Decryption-Program
Step 3: Run the Program
python your_filename.py

Make sure Python is installed on your system.

⚠️ Limitations

The encryption key changes every time the program runs.

 You must encrypt and decrypt within the same session.

 Not suitable for real-world secure communication.

 No persistent key storage.

No error handling for unsupported characters.

This project is designed for learning purposes only.
📚 What This Project Teaches
Basic encryption concepts
List indexing and mapping
Randomization in Python
Symmetric key logic
CLI interaction


🧠 Future Improvements
Save the key to a file
Add file encryption support
Implement stronger encryption algorithms
Add GUI interface
Add error handling
