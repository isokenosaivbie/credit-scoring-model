import csv
import random

random.seed(42)

with open("practice_credit_data.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Income", "Debt", "PaymentHistory", "Creditworthy"])

    for _ in range(100):
        income = random.randint(80000, 500000)
        debt = random.randint(0, income)
        payment_history = random.choice(["Good", "Poor"])

        if payment_history == "Good" and debt / income <= 0.4:
            creditworthy = 1
        else:
            creditworthy = 0

        writer.writerow([income, debt, payment_history, creditworthy])

print("Created 100 fictional practice records.")
