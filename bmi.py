# BMi Calculator
def bmi(x,y):
    y = y/100
    return x / (y**2)

def main( ):
    x = int(input("Enter the Weight(Kg):  "))
    y = int(input("Enter the Height(Cm): "))
    bmiv = bmi(x,y)
    if bmiv < 18.5:
        print("Under Weight ",bmiv)
    elif bmiv <= 24.9:
        print("Normal Weight ",bmiv)
    elif bmiv <= 29.9:
        print("Over Weight ",bmiv)
    else:
        print("Obese")

main( )
