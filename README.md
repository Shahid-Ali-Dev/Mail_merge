# 📬 Mail Merge Project

A simple and effective Python script that automates the generation of personalized invitation letters using a letter template and a list of names.

---

## ✨ Features

- 📂 Reads invitee names from a `.txt` file
- 📝 Replaces the `[name]` placeholder in a letter template with each name
- 📄 Outputs a personalized `.txt` letter for each invitee
- 🔄 Easily adaptable for other use-cases (certificates, emails, etc.)

---

## 📁 Project Structure

- `starting_letter.txt`: Contains the template letter with `[name]` placeholder  
- `invited_names.txt`: Contains one name per line  
- `ReadyToSend/`: Contains the generated personalized letters  

---

## 🧠 How It Works

1. The script reads all names from `invited_names.txt`.
2. For each name:
   - It loads the `starting_letter.txt`.
   - Replaces `[name]` with the actual name.
   - Saves the new letter as `<name>.txt` inside the `Output/ReadyToSend/` folder.

---


## ▶️ How to Run

Make sure you have Python 3 installed.

```bash
python main.py
