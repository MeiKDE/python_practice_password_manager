# Password Manager Application

This is a **Password Manager Application** built using Python and `tkinter` for GUI. The app provides an easy and secure way to manage and generate passwords, store them in a file, and directly copy the generated password to the clipboard.

---

## Features

### 1. Password Generation

- Randomly generates secure passwords with:
  - **Letters** (uppercase and lowercase)
  - **Numbers**
  - **Symbols**
- Randomized lengths for letters, numbers, and symbols ensure strong passwords.
- Copies the generated password directly to the clipboard.

### 2. Data Management

- Allows users to enter:
  - **Website**
  - **Email/Username**
  - **Password**
- Saves the entered data into a local `data.txt` file.
- Validates input fields to ensure no fields are left blank.
- Displays a confirmation dialog before saving data.

### 3. Graphical User Interface (GUI)

- Built using `tkinter`, featuring:
  - **Labels** for website, email/username, and password.
  - **Entry Widgets** for user input.
  - **Buttons** for generating passwords and saving data.
  - **Canvas** displaying an app logo.

---

## Requirements

### Dependencies

- **Python 3.x**
- **Required Libraries**:
  - `tkinter`: Built-in Python library for GUI.
  - `pyperclip`: For copying passwords to the clipboard. Install via:

    ```bash
    pip install pyperclip
    ```
