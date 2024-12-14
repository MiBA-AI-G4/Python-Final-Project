import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

df = pd.read_csv('hotel_bookings.csv')

features = ['lead_time', 'previous_cancellations', 'adr', 'booking_changes']
target = 'is_canceled'

X = df[features]
y = df[target]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), features)
    ])

pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', LogisticRegression())
])

pipeline.fit(X_train, y_train)

scaler = pipeline.named_steps['preprocessor'].transformers_[0][1]
found_means = scaler.mean_
found_std_devs = scaler.scale_

model = pipeline.named_steps['classifier']
coefficients = model.coef_
intercept = model.intercept_

for i, feature in enumerate(features):
    print(f"\nFeature: {feature}")
    print(f"Coefficient: {coefficients[0][i]}")
    print(f"Mean: {found_means[i]}")
    print(f"Standard Deviation: {found_std_devs[i]}")
    print(f'Intercept: {intercept}')