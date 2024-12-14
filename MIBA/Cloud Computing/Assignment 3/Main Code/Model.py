import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

data = pd.read_csv('hotel_bookings.csv')

feature_columns = ['lead_time', 'previous_cancellations', 'adr', 'booking_changes']
target_variable = 'is_canceled'

X = data[feature_columns]
y = data[target_variable]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler_transformer = ColumnTransformer(
    transformers=[
        ('num_scaler', StandardScaler(), feature_columns)
    ])

model_pipeline = Pipeline(steps=[
    ('scaling', scaler_transformer),
    ('logistic_regression', LogisticRegression())
])

model_pipeline.fit(X_train, y_train)

scaler = model_pipeline.named_steps['scaling'].transformers_[0][1]
means = scaler.mean_
std_devs = scaler.scale_

logistic_model = model_pipeline.named_steps['logistic_regression']
coeffs = logistic_model.coef_
intercept_value = logistic_model.intercept_

for idx, column in enumerate(feature_columns):
    print(f"\nFeature: {column}")
    print(f"Coefficient: {coeffs[0][idx]}")
    print(f"Mean: {means[idx]}")
    print(f"Standard Deviation: {std_devs[idx]}")
print(f"\nIntercept: {intercept_value}")
