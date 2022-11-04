'''
3. create a body mass Index(BMI) calculator. The BMI calculator should be able to tell
the user this infiormation after calculation

Less than 18.5 = Underweight
between 18.5 - 24.9 = healthy weight
between 25 - 29.9 = overweight
over 30 = obese
      steps
1. prompt the user to input his or her weight
2. prompt the user to input his/her height
3. the program should calculate the BMI and print out the result
4. should tell the user his or her condition


   Fomula for BMI is (weight / height ** 2)

'''
we = float(input("Enter your weight:"))
he = float(input("Enter your height:"))

bmi = float(we / (he **2))
print(f'our BMI is {bmi}')

if bmi <=18.5:
    print("you are under weight")
elif bmi == 18.6 or bmi <24.9:
    print("you are helathy")
elif bmi ==25 or bmi <29.9:
    print("you are over weight")

else:
    print("you are Obese, kindly see your doctor")
           
