import tkinter as tk
import joblib
import numpy as np

model = joblib.load("models/overload_model.pkl")


def predict():
    inputs = np.array([[ 
        float(entry_total.get()),
        float(entry_avg.get()),
        float(entry_std.get()),
        float(entry_delay.get())
    ]])

    prob = model.predict_proba(inputs)[0][1]
    pred = model.predict(inputs)[0]

    result_label.config(text=f"Prediction: {pred} | Probability: {prob:.2f}")


root = tk.Tk()
root.title("Overload Risk Predictor")

tk.Label(root, text="Total Clicks").pack()
entry_total = tk.Entry(root)
entry_total.pack()

tk.Label(root, text="Avg Clicks").pack()
entry_avg = tk.Entry(root)
entry_avg.pack()

tk.Label(root, text="Click Std").pack()
entry_std = tk.Entry(root)
entry_std.pack()

tk.Label(root, text="Avg Delay").pack()
entry_delay = tk.Entry(root)
entry_delay.pack()

tk.Button(root, text="Predict", command=predict).pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
