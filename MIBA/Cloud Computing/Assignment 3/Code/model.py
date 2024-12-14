import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

df = pd.read_csv("/Users/alexanderlange/Desktop/Github/hotel_bookings.csv")

df = df.dropna()
X = df[["lead_time", "previous_cancellations", "days_in_waiting_list", "booking_changes"]]
y = df["is_canceled"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = LogisticRegression()
model.fit(X_train_scaled, y_train)

print("Model Coefficients (weights):", model.coef_)
print("Model Intercept (bias):", model.intercept_)

# Evaluate the model
y_pred = model.predict(X_test_scaled)
accuracy = accuracy_score(y_test, y_pred)
print("Model Accuracy:", accuracy)

mean_std = X_train.agg(["mean", "std"])

# Display the mean and standard deviation
print("Mean and Standard Deviation of Training Features:")
print(mean_std)