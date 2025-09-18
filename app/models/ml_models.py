import os
import pickle

# Chemin vers le dossier models à la racine (backend/models)
MODELS_DIR = os.path.normpath(os.path.join(os.path.dirname(__file__), "../../models"))

def _load_model(filename):
    path = os.path.join(MODELS_DIR, filename)
    if not os.path.exists(path):
        raise FileNotFoundError(f"Model file not found: {path}")
    with open(path, "rb") as f:
        return pickle.load(f)

# Charger les modèles (va lever une erreur si le fichier n'existe pas)
random_forest_model = _load_model("random_forest_model.pkl")
xgboost_model = _load_model("linear_regression_model.pkl")
logistic_model = _load_model("logistic regression.pkl")
svm_model = _load_model("resume_screen_model.pkl")

# Fonctions de prédiction — attention : features doit être une liste/array au bon format
def predict_turnover_rf(features):
    """Random Forest"""
    prediction = random_forest_model.predict([features])
    return float(prediction[0])

def predict_turnover_xgb(features):
    """linear_regression_model"""
    prediction = xgboost_model.predict([features])
    return float(prediction[0])

def predict_turnover_logistic(features):
    """Logistic Regression"""
    prediction = logistic_model.predict([features])
    return float(prediction[0])

def predict_turnover_svm(features):
    """resume_screen_model"""
    prediction = svm_model.predict([features])
    return float(prediction[0])
