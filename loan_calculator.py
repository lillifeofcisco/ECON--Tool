def calculate_monthly_payment(principal, annual_rate, years):
    """
    Calculates the monthly repayment for a loan.

    Args:
        principal (float): The loan amount.
        annual_rate (float): The annual interest rate as a percentage (e.g., 5 for 5%).
        years (float): The duration of the loan in years.

    Returns:
        float: The monthly payment amount.
    """
    # Convert annual rate percentage to a monthly decimal rate
    monthly_rate = annual_rate / 100 / 12
    num_payments = years * 12

    if monthly_rate == 0:
        return principal / num_payments

    # Formula: M = P [ i(1 + i)^n ] / [ (1 + i)^n – 1 ]
    payment = principal * (monthly_rate * (1 + monthly_rate)**num_payments) / ((1 + monthly_rate)**num_payments - 1)
    return payment

def main():
    print("Loan Repayment Calculator")
    print("-------------------------")
    try:
        principal_input = input("Enter the Principal (in Cedis): ")
        principal = float(principal_input)

        rate_input = input("Enter the Annual Interest Rate (e.g., 5 for 5%): ")
        annual_rate = float(rate_input)

        years_input = input("Enter the Duration in years: ")
        years = float(years_input)

        if years <= 0:
            print("Duration must be greater than 0.")
            return

        payment = calculate_monthly_payment(principal, annual_rate, years)

        print(f"The monthly payment is: {payment:.2f} Cedis")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()
