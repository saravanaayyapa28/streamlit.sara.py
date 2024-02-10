pip install scikit-learn

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import LabelEncoder

# Load dataset (you can replace this with your own dataset)
url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-02-11/hotels.csv"
df = pd.read_csv(url)

# Data preprocessing
df = df.drop(["reservation_status_date", "reservation_status"], axis=1)
df["agent"] = df["agent"].fillna(0)
df["children"] = df["children"].fillna(0)
df["country"] = df["country"].fillna(df["country"].mode()[0])

# Label encoding for categorical features
le = LabelEncoder()
df["hotel"] = le.fit_transform(df["hotel"])
df["meal"] = le.fit_transform(df["meal"])
df["country"] = le.fit_transform(df["country"])
df["market_segment"] = le.fit_transform(df["market_segment"])
df["distribution_channel"] = le.fit_transform(df["distribution_channel"])
df["reserved_room_type"] = le.fit_transform(df["reserved_room_type"])
df["assigned_room_type"] = le.fit_transform(df["assigned_room_type"])
df["deposit_type"] = le.fit_transform(df["deposit_type"])
df["customer_type"] = le.fit_transform(df["customer_type"])

# Target variable
y = df["is_canceled"]

# Features
X = df.drop(["is_canceled"], axis=1)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the RandomForestClassifier
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
classification_rep = classification_report(y_test, y_pred)

# Print results
print(f"Accuracy: {accuracy:.2f}")
print("Classification Report:\n", classification_rep)
