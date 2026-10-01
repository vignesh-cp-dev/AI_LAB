def vc(status,cr):
    if status[cr]=="dirty":
        return "Cleaning "+cr
    elif cr=="A":
        return "Moving Right"
    else:
        return "Moving Left"
roomA=input("Enter the status(clean or dirty) of room A: ").lower()
roomB=input("Enter the status(clean or dirty) of room B: ").lower()
cr=input("Enter the current location of Vacuum Cleaner (A/B): ").upper()
status ={
    "A":roomA,
    "B":roomB
}

while(status["A"]!="clean" or status["B"]!="clean"):
    text=vc(status,cr)
    if text==("Cleaning "+cr):
        status[cr]="clean"
    elif text=="Moving Right":
        cr="B"
    else:
        cr="A"
    print(text)
