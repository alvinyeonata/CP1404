"""

weight= float(input("Please enter your weight in kg:"))
height= float(input("Please enter your height in m:"))

bmi= weight/(height * height)
print("Therefore, your BMI value is:", bmi)
print("Thank you!")
"""

def get_weight_height():
    weight= float(input("enter weight: "))
    height =float(input("enter height: "))
    return weight,height

def main():
    weight, height = get_weight_height()
    bmi = weight/(height * height)
    print("Therefore, your BMI value is:",bmi)

main()