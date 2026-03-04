import os
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression


def train(features):

    X = features[['total_clicks', 'avg_clicks', 'click_std', 'avg_delay']]
    y = features['overload']

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)

    os.makedirs("models", exist_ok=True)
    joblib.dump(model, "models/overload_model.pkl")

    return model, X_test, y_test
