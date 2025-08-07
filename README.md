📬 Mail Merge Project
A simple Python script to automatically generate personalized invitation letters by merging names into a letter template. This is a practical implementation of file handling and string replacement using Python.

✨ Features
Reads a list of invitee names from a .txt file.

Replaces a placeholder (e.g., [name]) in a letter template with each actual name.

Saves a personalized letter for each invitee in a specified output folder.

Clean and easy to modify for other mail merge tasks (e.g., emails, certificates).

🗂️ Project Structure
pgsql
Copy
Edit
MailMergeProject/
├── Input/
│   ├── Letters/
│   │   └── starting_letter.txt        # Template letter with placeholder [name]
│   └── Names/
│       └── invited_names.txt          # List of names to send letters to
│
├── Output/
│   └── ReadyToSend/                   # Folder where personalized letters are saved
│
└── main.py                            # Main script to perform the mail merge
🧠 How It Works
The script reads all names from invited_names.txt.

For each name, it opens starting_letter.txt, replaces [name] with the actual name, and writes the personalized letter to a .txt file inside the Output/ReadyToSend/ folder.

🧾 Example
If invited_names.txt contains:

nginx
Copy
Edit
Angela
John
Marco
And starting_letter.txt contains:

css
Copy
Edit
Dear [name],

You are invited to my birthday party this Saturday!

Sincerely,
Shahid
The script will generate:

Angela.txt

John.txt

Marco.txt

Each containing the personalized version of the letter.

▶️ How to Run
Ensure your folder structure matches the one shown above.

Run the script:

bash
Copy
Edit
python main.py
Check the Output/ReadyToSend/ folder for the generated letters.

✅ Requirements
Python 3.x

No external libraries required

🧑‍💻 Author
Shahid
Practicing file handling and automation using Python.
