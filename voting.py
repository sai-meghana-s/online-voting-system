import customtkinter as ctk
from tkinter import messagebox

CANDIDATE1 = "A"
CANDIDATE2 = "B"
CANDIDATE3 = "C"
CANDIDATE4 = "D"

votesCount1 = 0
votesCount2 = 0
votesCount3 = 0
votesCount4 = 0
numVoters = 0
num = 1

class Voter:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class Member:
    def __init__(self, username):
        self.username = username

mem = [Member("") for _ in range(20)]
voters = [Voter("", "") for _ in range(100)]

def registerVoter(username, password):
    global numVoters
    
    for i in range(numVoters):
        if voters[i].username == username:
            messagebox.showerror("Error", "Username already exists. Please choose another one.")
            return
    
    voters[numVoters] = Voter(username, password)
    numVoters += 1
    messagebox.showinfo("Success", "Voter registered successfully!")
    openVotingWindow(username)
 

def voted(username):
    for j in range(1, num):
        if mem[j].username == username:
            return j
    return 0

def login(username, password):
    for i in range(numVoters):
        if voters[i].username == username and voters[i].password == password:
            return i
    messagebox.showerror("Error", "Invalid username or password.")
    return -1

def castVote(username, choice):
    global num, votesCount1, votesCount2, votesCount3, votesCount4, nota
    
    if voted(username):
        messagebox.showerror("Error", "You have already voted!")
        return
    
    mem[num] = Member(username)
    num += 1
    
    if choice == 1:
        votesCount1 += 1
        messagebox.showinfo("Success", f"You voted for {CANDIDATE1}!")
    elif choice == 2:
        votesCount2 += 1
        messagebox.showinfo("Success", f"You voted for {CANDIDATE2}!")
    elif choice == 3:
        votesCount3 += 1
        messagebox.showinfo("Success", f"You voted for {CANDIDATE3}!")
    elif choice == 4:
        votesCount4 += 1
        messagebox.showinfo("Success", f"You voted for {CANDIDATE4}!")
    else:
        messagebox.showerror("Error", "Invalid choice. Please try again.")

def votesCount():
    result = f"""
    {CANDIDATE1} - {votesCount1}
    {CANDIDATE2} - {votesCount2}
    {CANDIDATE3} - {votesCount3}
    {CANDIDATE4} - {votesCount4}
    """
    messagebox.showinfo("Vote Count", result)

def getLeadingCandidate():
    maxVotes = max(votesCount1, votesCount2, votesCount3, votesCount4)
    leading_candidates = []
    
    if votesCount1 == maxVotes:
        leading_candidates.append(CANDIDATE1)
    if votesCount2 == maxVotes:
        leading_candidates.append(CANDIDATE2)
    if votesCount3 == maxVotes:
        leading_candidates.append(CANDIDATE3)
    if votesCount4 == maxVotes:
        leading_candidates.append(CANDIDATE4)

    if len(leading_candidates) == 1:
        messagebox.showinfo("Leading Candidate", f"Leading Candidate: {leading_candidates[0]}")
    else:
        messagebox.showwarning("Tie", f"Tie between: {', '.join(leading_candidates)}")

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.geometry("500x450")
root.title("Online Voting System")
root.configure(fg_color="#1f1f1f")

title = ctk.CTkLabel(root, text="Online Voting System", font=("Arial", 24, "bold"))
title.pack(pady=15)

ctk.CTkLabel(root, text="Username:", font=("Arial", 14)).pack()
entry_username = ctk.CTkEntry(root, width=300, height=40, corner_radius=10)
entry_username.pack(pady=5)

ctk.CTkLabel(root, text="Password:", font=("Arial", 14)).pack()
entry_password = ctk.CTkEntry(root, width=300, height=40, corner_radius=10, show="*")
entry_password.pack(pady=5)

def handleRegister():
    username = entry_username.get()
    password = entry_password.get()
    if username and password:
        registerVoter(username, password)
        entry_username.delete(0, 'end')  
        entry_password.delete(0, 'end')
        root.after(100, lambda: entry_username.focus_set())
    else:
        messagebox.showerror("Error", "Username and Password cannot be empty!")

def handleLogin():
    username = entry_username.get()
    password = entry_password.get()
    voterIndex = login(username, password)
    if voterIndex != -1:
        entry_username.delete(0, 'end')  
        entry_password.delete(0, 'end')
        root.after(100, lambda: entry_username.focus_set())
        openVotingWindow(username)

def openVotingWindow(username):
    voting_window = ctk.CTkToplevel(root)
    voting_window.geometry("800x1000")
    voting_window.title("Cast Your Vote")
    
    ctk.CTkLabel(voting_window, text=f"Welcome, {username}!\nCast your vote or choose any one of the options below!", font=("Arial", 18)).pack(pady=10)
    
    def handleVote(choice):
        castVote(username, choice)
    
    options = [CANDIDATE1, CANDIDATE2, CANDIDATE3, CANDIDATE4]
    for i, option in enumerate(options, 1):
        ctk.CTkButton(voting_window, text=f"{i}. {option}", width=250, height=40,
                      corner_radius=10, fg_color="#0078D7", hover_color="#005a9e",
                      command=lambda c=i: handleVote(c)).pack(pady=5)

    ctk.CTkButton(voting_window, text="Show Vote Count", width=250, height=40,
                  fg_color="#6C757D", hover_color="#5A6268", command=votesCount).pack(pady=5)

    ctk.CTkButton(voting_window, text="Leading Candidate", width=250, height=40,
                  fg_color="#17A2B8", hover_color="#138496", command=getLeadingCandidate).pack(pady=5)

    ctk.CTkButton(voting_window, text="New Login / Register ", width=250, height=40,
                  fg_color="#218828", hover_color="#218858", command=voting_window.destroy).pack(pady=5)

    ctk.CTkButton(voting_window, text="Exit", width=250, height=40,
                  fg_color="#DC3545", hover_color="#C82333", command=root.quit).pack(pady=5)

ctk.CTkButton(root, text="Register", width=150, height=40, corner_radius=12,
              fg_color="#0078D7", hover_color="#005a9e", command=handleRegister).pack(pady=5)

ctk.CTkButton(root, text="Login", width=150, height=40, corner_radius=12,
              fg_color="#28A745", hover_color="#218838", command=handleLogin).pack(pady=5)

root.mainloop()
