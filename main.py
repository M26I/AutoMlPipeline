from pipeline.load_data import load_data
from pipeline.preprocess import preprocess_data
from pipeline.train_model import train_model
from pipeline.evaluate import evaluate_model
from pipeline.save_model import save_model
import logging
import json

with open('config.json') as f:
    config = json.load(f)

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    try:
        logging.info("Starting data loading.")
        data = load_data("data/iris.csv")
        
        logging.info("Starting data preprocessing.")
        X_train, X_test, y_train, y_test = preprocess_data(data, target_column="species")
        
        logging.info("Starting model training.")
        model = train_model(X_train, y_train)
        
        logging.info("Evaluating model.")
        accuracy = evaluate_model(model, X_test, y_test)
        logging.info(f"Model Accuracy: {accuracy:.2f}")
        
        logging.info("Saving the trained model.")
        save_model(model, "models/random_forest_model.joblib")
        
    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()