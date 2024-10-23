#Program 3 – Auto Insurance
#Write a program that computes monthly insurance according to the provided schedule. 

#Student #:     
#Student Name:  Mathew Akunyili

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)
    # Title
    print("Auto Insurance")
    print("")

    # Ask user to  enter there sex, age, and price of vehicle

    sex = input("Are you 'Male' or 'Female': ").lower()
    age = int(input("Enter your age: "))
    price = float(input("Enter the purchase price of the vehicle: $"))

    # Perform calculationd
    # These shows the rates requires for each sex and age groups
    if sex == "male" and (age >= 15 and age < 25):
        rate = 0.25 / 12
    elif sex == "male" and (age >= 25 and age < 40):
        rate = 0.17 / 12
    elif (sex == "male" or sex == "female") and (age >= 40 and age < 70):
        rate = 0.1 / 12
    elif sex == "female" and (age >= 15 and age < 25):
        rate = 0.2 / 12
    elif sex == "female" and (age >= 25 and age < 40):
        rate = 0.15 / 12

    insurance = price * (rate) # This calculates the insurance taking the price of the vehicle the mutiply by the required rte

    print(f"Your monthly insurance will be ${insurance:.2f}")
    









    # YOUR CODE ENDS HERE

main()