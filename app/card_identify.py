def cardType(number):
    number = str(number)
    cardtype = ""
    if len(number) == 15:
        if number[:2] == "34" or number[:2] == "37":
            cardtype = "American Express"
    if len(number) == 13:
        if number[:1] == "4":
            cardtype = "Visa"
    if len(number) == 16:
        if number[:4] == "6011":
            cardtype = "Discover"
        if int(number[:2]) >= 51 and int(number[:2]) <= 55:
            cardtype = "Master Card"
        if number[:1] == "4":
            cardtype = "Visa"
        if number[:4] == "3528" or number[:4] == "3529":
            cardtype = "JCB"
        if int(number[:3]) >= 353 and int(number[:3]) <= 359:
            cardtype = "JCB"
    if len(number) == 14:
        if number[:2] == "36":
            cardtype = "DINERS"
        if int(number[:3]) >= 300 and int(number[:3]) <= 305:
            cardtype = "DINERS"
    return cardtype