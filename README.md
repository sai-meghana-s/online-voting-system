# 🗳️ Online Voting System

This project is a **GUI-based Online Voting System** built using **Python (CustomTkinter)**. It allows users to register, login, cast their vote, and view the voting results. This project is ideal for learning **GUI development** and implementing **voting logic** in Python.

their vote, and view the voting results. This project is ideal for learning **GUI development** and implementing **voting logic** in Python.

## 🎬 Demo  
You can **download and run** the `.exe` file **directly** without installing Python! 🚀  
👉 [**Download EXE File**](https://github.com/sai-meghana-s/online-voting-system/releases/download/v1.0.0/voting.exe)  

## Features
## Features
- ✅ **User Registration**: Allows users to register with a username and password.
- ✅ **User Login**: Registered users can log in to cast their vote.
- ✅ **Vote Casting**: Users can cast their vote for any one of four candidates.
- ✅ **Vote Count**: Displays the total number of votes each candidate received.
- ✅ **Leading Candidate**: Displays the leading candidate or shows a tie if applicable.
- ✅ **Prevent Multiple Voting**: Ensures that each user can only vote once.

## Key Libraries
- `CustomTkinter`: Used for creating modern GUI applications in Python.
- `tkinter.messagebox`: Used for displaying pop-up messages and alerts.
- `pyinstaller` (Optional): Converts the Python script into an executable file (`.exe`).

## 💻 How It Works
The system follows these steps:

### 1. **User Registration**
- Users can enter a username and password to register.
- The system prevents duplicate usernames during registration.
- Upon successful registration, the user can immediately vote.

### 2. **User Login**
- Registered users can log in using their credentials.
- If the username or password is incorrect, an error message is displayed.
- Once logged in, users can proceed to cast their vote.

### 3. **Cast Vote**
- Users will see 4 candidates to vote for:
```
1. Candidate A  
2. Candidate B  
3. Candidate C  
4. Candidate D
```
- After selecting a candidate, the vote count increases, and a success message is shown.
- Users are restricted from voting multiple times.

### 4. **View Vote Count**
- Users can view the total number of votes for each candidate.
- Example output:
```
Candidate A: 3 votes  
Candidate B: 5 votes  
Candidate C: 2 votes  
Candidate D: 1 vote
```

### 5. **Leading Candidate**
- The system identifies and shows the leading candidate based on the vote count.
- In case of a tie, it displays all the candidates tied with the highest votes.

### 6. **Prevent Duplicate Voting**
- If a user tries to log in again and cast another vote, it shows:
```
You have already voted!
```

## 📂 Project Structure
The project directory is structured as follows:
```
Online Voting System/
│
├── voting_system.py       <-- Main Python file
├── requirements.txt       <-- Dependencies file
├── README.md              <-- Documentation
├── dist/                  <-- EXE file (if built)
```

## 📦 Installation

### ✅ Step 1: Clone the Repository
Clone this project to your local machine using:
```bash
git clone https://github.com/your-username/online-voting-system.git
cd online-voting-system
```

### ✅ Step 2: Install Required Libraries
Install the required libraries using pip:
```bash
pip install customtkinter
```
OR install from the requirements.txt file:
```bash
pip install -r requirements.txt
```

### ✅ Step 3: Run the Application
Run the Python file using:
```bash
python voting_system.py
```

OR double-click the `voting_system.py` file.

## 📊 Vote Results Example
The output of votes may look like this:
```
Candidate A - 4 votes  
Candidate B - 5 votes  
Candidate C - 2 votes  
Candidate D - 1 vote
```
The system will automatically identify the leading candidate or notify if there's a tie:
```
Leading Candidate: Candidate B
```
or
```
Tie between: Candidate A and Candidate B
```

## 🛡️ Preventing Multiple Votes
The system ensures that:
- **One user can only vote once.**
- If a user tries to vote again, they get the message:
```
You have already voted!
```

## 🗳️ Creating EXE File (Optional)
If you want to convert this Python file into a **standalone executable (.exe)**, follow these steps:

### ✅ Step 1: Install PyInstaller
```bash
pip install pyinstaller
```

### ✅ Step 2: Build EXE File
Run this command:
```bash
pyinstaller --onefile --windowed voting_system.py
```
- `--onefile`: Creates a single executable file.
- `--windowed`: Prevents the command prompt from appearing.

### ✅ Step 3: Run EXE File
Your `.exe` file will be located in the `dist/` folder:
```
dist/voting_system.exe
```
Double-click the file to run your voting system without Python installed.

## 🚀 Future Enhancements
Here are some features we can add in the future:
1. ✅ **Admin Panel** to add/remove candidates.
2. ✅ **Database Integration (SQLite/MongoDB)** to store votes persistently.
3. ✅ **Real-time Graphs** using Matplotlib to display voting trends.
4. ✅ **Email Notifications** to notify voters after registration.

## 💡 Troubleshooting
If you face any issues while running the project:
- Ensure **Python 3.10+** is installed.
- Make sure `customtkinter` is installed.
- If creating an EXE, check the `dist/` folder.

## 📬 Contact
For any queries or collaboration:
- **GitHub**: [https://github.com/sai-meghana-s]
- **LinkedIn**: [www.linkedin.com/in/sai-meghana-s]

## ⭐ Support the Project
If you find this project helpful:
- ⭐ Star the repository.
- 💻 Fork the project.
- 🗳️ Share with your friends.

