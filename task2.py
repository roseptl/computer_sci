time24 = float(input('Provide the time in the form 18.25: '))
if time24 < 13.0:
    print(time24)
else:
    time12 = time24 - 12
    print(time12)