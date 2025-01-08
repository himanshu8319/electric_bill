name = str(input("Enter your name:"))
age = int(input("Enter your age:"))
userid = int(input("Enter your UserID:"))
unit = int(input("Enter your unit use:"))
amt=unit*6
fc= 150
pa= amt + fc
 
f=open(f"kescoBill/{name}.txt","a")
f.write("=========KESCO==========\n")
f.write(f"Name: {name}\n")
f.write(f"Age: {age}\n")
f.write(f"UserID: {userid}\n")
f.write(f"Unit Use: {unit}\n")
f.write("--------------------------\n")
f.write(f"Amount : {amt}\n")
f.write(f"Fix Charges: {fc}\n")
f.write(f"--------------------------\n")
f.write(f"Payable Amount: {pa}\n")
f.close()