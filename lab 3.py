print("=== Secure notes app ===")


while True:
    choice = input("choose add / view / done /: ").strip().lower()
    if choice == "add":
        note = input("enter note: ").strip().lower()
              
        if not note:
            print("ERROR, Please enter a valid note")

            encrypted = " "
            for ch in note:
                encrypted = encrypted + chr(ord(ch)+1)

            file = open("secure_notes.txt", "a")
            file.write(encrypted + "\n")
            file.close()

        print("note saved securly. ")

    elif choice == "view":
        file = open("secure_notes.txt", "r")

        count = 0 
        for line in file:
            decrypted = " "
            for ch in line.strip():
                decrypted = decrypted + chr(ord(ch)-1)

            
            print("- " + decrypted)
            count = count + 1
        file.close()
        print("total notes:", count)
    else:
        if choice != "done":
            print("invalid option")

    if choice == "done":
        break


