# © 2025 M26I - For educational/portfolio use only

from pipeline.load_data import load_data
from pipeline.preprocess import preprocess_data
from pipeline.train_model import train_model
from pipeline.evaluate import evaluate_model
from pipeline.save_model import save_model
import logging
import os
import yaml

# Load config from YAML
with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)
    
# Logging config
logging.basicConfig(
    filename='pipeline.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def main():
    try:
        logging.info("Pipeline started.")
        
        # Use path from config
        data = load_data(config["data_path"])

        # Basic validation
        if data.isnull().sum().sum() > 0:
            logging.warning("Missing values found in dataset.")

        # Use target column from config
        X_train, X_test, y_train, y_test = preprocess_data(data, target_column=config["target_column"])

        model = train_model(X_train, y_train)
        accuracy = evaluate_model(model, X_test, y_test)

        logging.info(f"Model trained. Accuracy: {accuracy:.2f}")

        # Use model output path from config
        save_model(model, config["model_output"])

        logging.info("Pipeline completed successfully.")
    except Exception as e:
        logging.error(f"Pipeline failed: {e}")

if __name__ == "__main__":
    main()
