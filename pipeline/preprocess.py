from sklearn.model_selection import train_test_split

def validate_data(df, target_column):
    if target_column not in df.columns:
        raise ValueError(f"Target column '{target_column}' not found in the dataset.")
    
    # Check for missing values
    if df.isnull().any().any():
        raise ValueError("Dataset contains missing values.")
    
    print("Data validation passed.")

def preprocess_data(df, target_column):
    validate_data(df, target_column)
    X = df.drop(columns=[target_column])
    y = df[target_column]
    return train_test_split(X, y, test_size=0.2, random_state=42)

