# AutoML Pipeline

AutoML Pipeline is an automated machine learning tool designed to streamline the process of data loading, model training, and evaluation. With minimal setup, you can train various models like Random Forest and XGBoost and evaluate their performance.

🔍 **What It Does**
Run the AutoML pipeline to:

✅ **Load Data**  
Upload your own dataset (CSV) for model training.

✅ **Train Models**  
Train models with one simple command. Supported models include:
- Random Forest (default)
- XGBoost

✅ **Evaluate Models**  
Evaluate model performance using accuracy or other metrics.

🛠️ **Built With**
- Python
- scikit-learn – Machine learning algorithms
- XGBoost – Gradient boosting model
- pandas – Data manipulation
- argparse – Command-line argument parsing

📁 **Dataset**
 I used [Kaggle Iris Dataset](https://www.kaggle.com/datasets/vijayaadithyanvg/iris-dataset), but the app works with any CSV dataset. Ensure your dataset contains a target column that you want to predict.


📦 **Installation**

### Clone the repo:
```bash
git clone https://github.com/M26I/AutoMlPipeline
cd AutoMlPipeline
```
### Install dependencies:
```bash
pip install -r requirements.txt
```
### Run the pipeline:
-Load Data & Train Model:
```bash
python main.py --data path/to/your/dataset.csv --target target_column --model rf
```

-Evaluate Model:
```bash
python main.py --data path/to/your/dataset.csv --target target_column --model rf --evaluate
```

⚠️ **Limitations**
Model Suggestions: Currently, you must specify the model type (rf for Random Forest, xgb for XGBoost).

Dataset Requirement: The dataset must have a target column for the pipeline to predict.

👤 **Author**
[M26I](https://github.com/M26I)

---
© 2025 Your M26I – For educational/portfolio use only.  
Unauthorized use or redistribution without credit is prohibited.





