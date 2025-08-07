#TODO: Create a letter using starting_letter.txt

replace = ["[name]", "noob"]

with open("./Input/Names/invited_names.txt") as f:
    h = f.readlines()
    print(h)

for i in h:
    with open("./Input/Letters/starting_letter.txt") as n:
        g = n.read()
        e = g.replace(replace[0],i.strip())

        with open(f"./Output/ReadyToSend/{i.strip()}.txt", "w") as l:
            l.write(e)



