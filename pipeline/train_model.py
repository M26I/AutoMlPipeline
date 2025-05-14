from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score

def train_model(X_train, y_train):
    model = RandomForestClassifier()
    scores = cross_val_score(model, X_train, y_train, cv=5)
    print(f"Cross-validation scores: {scores}")
    return model.fit(X_train, y_train)
