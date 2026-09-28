import csv
from sklearn.model_selection import train_test_split

features = []
answers = []

with open("practice_credit_data.csv", newline="") as file:
    reader = csv.DictReader(file)

    for person in reader:
        income = int(person["Income"])
        debt = int(person["Debt"])

        if person["PaymentHistory"] == "Good":
            payment_history = 1
        else:
            payment_history = 0

        debt_to_income = debt / income

        features.append([income, debt, payment_history, debt_to_income])
        answers.append(int(person["Creditworthy"]))

X_train, X_test, y_train, y_test = train_test_split(
    features,
    answers,
    test_size=0.2,
    random_state=42,
    stratify=answers
)

print("Total examples:", len(features))
print("Examples for learning:", len(X_train))
print("Examples for testing:", len(X_test))

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score
)

model = DecisionTreeClassifier(max_depth=3, random_state=42)
model.fit(X_train, y_train)

predictions = model.predict(X_test)
probabilities = model.predict_proba(X_test)[:, 1]

print("Accuracy:", accuracy_score(y_test, predictions))
print("Precision:", precision_score(y_test, predictions, zero_division=0))
print("Recall:", recall_score(y_test, predictions, zero_division=0))
print("F1-score:", f1_score(y_test, predictions, zero_division=0))
print("ROC-AUC:", roc_auc_score(y_test, probabilities))
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score

model = DecisionTreeClassifier(max_depth=3, random_state=42)
model.fit(X_train, y_train)

predictions = model.predict(X_test)
probabilities = model.predict_proba(X_test)[:, 1]

print("Accuracy:", accuracy_score(y_test, predictions))
print("Precision:", precision_score(y_test, predictions, zero_division=0))
print("Recall:", recall_score(y_test, predictions, zero_division=0))
print("F1-score:", f1_score(y_test, predictions, zero_division=0))
print("ROC-AUC:", roc_auc_score(y_test, probabilities))