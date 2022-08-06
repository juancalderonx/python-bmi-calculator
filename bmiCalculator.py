print("¡Hi! Let's calculate your BMI")

def calculateBMI(weight, height):
    bmi = weight / height**2
    return bmi

def getData():
    height = int(input("Please, type your height in cm "))
    weight = int(input("Please type your weight in kg "))
    heightInMt = height * 0.01

    bmi = calculateBMI(weight, heightInMt)

    if bmi < 20:
        print("You've thinness")
    elif bmi >= 20 and bmi < 26:
        print("Your weight is normal")
    elif bmi >= 26 and bmi < 30:
        print("You're overweight")
    else:
        print("You're obese")

getData()