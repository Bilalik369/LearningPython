
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score



data = {
    "study_hours": [2, 4, 6, 8, 10, 3, 5, 7, 9, 1],
    "absences":   [5, 3, 2, 1, 0, 6, 3, 2, 1, 7],
    "participation": [40, 60, 70, 80, 90, 50, 65, 75, 85, 30],
    "final_grade":   [8, 11, 13, 15, 18, 9, 12, 14, 16, 7]
}

df = pd.DataFrame(data)

print("Dataset :")
print(df)




X = df[["study_hours", "absences", "participation"]]  
y = df["final_grade"]                                



X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


model = LinearRegression()

model.fit(X_train, y_train)





y_pred = model.predict(X_test)




mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\nRésultats :")
print("MSE :", mse)
print("R² :", r2)




new_student = np.array([[6, 2, 70]])

predicted_grade = model.predict(new_student)

print("\nNote prédite :", round(predicted_grade[0], 2))




plt.scatter(y_test, y_pred)
plt.xlabel("Vraie Note")
plt.ylabel("Note Prédite")
plt.title("Prédiction vs Réalité")
plt.show()
