import random


def recommended_doctor(age):

    if(age > 18):
        print("Proceed to room no : 2 ")
    else:
        print("Proceed to room no : 1 ")


def token_number():
    n = random.randint(0, 50)

    # print(n)
    return n


def pharmacy(age):

    if(age == 1):
        cash = 100
    else:
        cash = 200

    return cash


def doctor_rate(age):
    if (age < 18):
        doctor_fee = 150
    else:
        doctor_fee = 200
    return doctor_fee


print("--------------------- WELCOME TO HOSPITAL --------------")

print("\n")

patient_name = input("Name : ")
patient_age = int(input("Age : "))
patient_mobile_number = int(input("Mobile number : "))

print("\n")

recommended_doctor(patient_age)

token = token_number()

print("Your token number is : ", token)

total_cash = doctor_rate(patient_age) + pharmacy(patient_age)

# print("Your recepit >>>> " + )

print("""--------------------------------------
                                               
            HOSPITAL                           
           ----------                           
                                            
Name :  """ + str(patient_name) + "\n" +

      "Age :  " + str(patient_age) + "\n" +

      "Mobile Number :  " + str(patient_mobile_number) + "\n" +

      "Total fees :  " + str(total_cash) + "\n\n" +

      "THANK YOU FOR VISITING US  " + "\n" + "\n" + "--------------------------------------")
