# Written by Aidan Holloway
# Date Written March 21 2023

# One Stop Insurance company project QAP #4

import datetime
# Open the OSICDef.dat file and read the data

with open('OSICDef.dat', 'r') as f:
    NEXT_POLICY_NUM_RATE = int(f.readline())
    BASIC_PREM = float(f.readline())
    DISCOUNT_PER_CAR = float(f.readline())
    EXTRA_LIABILITY = float(f.readline())
    GLASS_COVERAGE = float(f.readline())
    CAR_LOAN_COVERAGE = float(f.readline())
    HST_RATE = float(f.readline())
    PROCESS_FEE_MON = float(f.readline())



# Set up list of valid provinces
Valid_provinces = ['AB', 'BC', 'MB', 'NB', 'NL', 'NT', 'NS', 'NU', 'ON', 'PE', 'QC', 'SK', 'YT']

# Loop to get multiple polices
while True:
    # Get customer information
    First_name = input('Enter customer first name: ').title()
    Last_name = input('Enter customer last name: ').title()
    Address = input('Enter customer address: ')
    City = input('Enter customer city: ').title()
    Province = input('Enter customer province (2 letter abbreviation): ').upper()

    while Province not in Valid_provinces:
        province = input('Invalid province. Enter customer province (2 letter abbreviation): ').upper()
    Postal_code = input('Enter customer postal code (A1A 1A1 format): ').upper()
    Phone_number = input('Enter customer phone number: ')

# Get number of cars and options
    Num_cars = int(input('Enter number of cars being insured: '))
    Extra_liability_option = input('Extra liability coverage up to $1,000,000 (Y/N): ').upper()
    Glass_coverage_option = input('Glass coverage (Y/N): ').upper()
    Loaner_car_option = input('Loaner car (Y/N): ').upper()

# Get payment method
    payment_method = input('Payment method (F for full payment, M for monthly): ').upper()

# Calculate total premium and costs
    Total_premium = BASIC_PREM + (DISCOUNT_PER_CAR * (Num_cars - 1))
    Total_costs = 0

    if Extra_liability_option == 'Y':
        Total_costs += EXTRA_LIABILITY * Num_cars
    elif Glass_coverage_option == 'Y':
        Total_costs += GLASS_COVERAGE * Num_cars
    elif Loaner_car_option == 'Y':
        Total_costs += CAR_LOAN_COVERAGE * Num_cars
    Total_premium += Total_costs

    Hst = Total_premium * HST_RATE
    Total_cost = Total_premium + Hst

    Invoice_Date = datetime.date.today()
    Payment_Date = datetime.date.today().replace(day=1) + datetime.timedelta(days=32)

# Calculate monthly payment
    Processing_fee = 39.99
    Monthly_payment = (Total_cost + Processing_fee) / 8

    Total_cost = Total_premium + Hst
# Print receipt
    print()
    print('--------------------------------------------')
    print('                 INVOICE                     ')
    print('--------------------------------------------')
    print(f'Customer: {First_name} {Last_name}')
    print(f'Address: {Address}, {City}, {Province} {Postal_code}')
    print(f'Phone: {Phone_number}')
    print(f'Number of cars: {Num_cars}')
    if Extra_liability_option == 'Y':
        print(f'Extra liability coverage: ${EXTRA_LIABILITY * Num_cars:.2f}')
    if Glass_coverage_option == 'Y':
        print(f'Glass coverage: ${GLASS_COVERAGE * Num_cars:.2f}')
    if Loaner_car_option == 'Y':
        print(f'Invoice Date:    {Invoice_Date}')
        print(f'Payment Date:    {Payment_Date}')

    print("Total premium: $%.2f" % Total_premium)
    print("HST: $%.2f" % Hst)
    print("Total cost: $%.2f" % Total_cost)

        # Display monthly payment if user selected monthly payment method
    if payment_method == "M":
        print("Monthly payment: $%.2f" % Monthly_payment)



    print('--------------------------------------------')
    print("One Stop Insurance Company Policy Information".center(40))
    print('--------------------------------------------')
    print(f"Policy Number: {NEXT_POLICY_NUM_RATE}")

# Open the file in Write mode
    with open("Policies.dat", "a") as file:
        file.write("{}," .format(str(NEXT_POLICY_NUM_RATE)))
        file.write("{},".format(Invoice_Date))
        file.write("{},".format(First_name))
        file.write("{},".format(Last_name))
        file.write("{},".format(Address))
        file.write("{},".format(City))
        file.write("{},".format(Province))
        file.write("{},".format(Postal_code))
        file.write("{},".format(Phone_number))
        file.write("{},".format(Num_cars))
        file.write("{},".format(Extra_liability_option))
        file.write("{},".format(GLASS_COVERAGE))
        file.write("{}\n".format(str(Total_premium)))
        f.close()
        NEXT_POLICY_NUM_RATE += 1
        print()
        print("Policy information processed and saved.")