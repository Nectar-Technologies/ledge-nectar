import os
import pickle
from tqdm import tqdm
from pymer4.models import Lmer

# Function to fit the series of predefined model formulas
def fit_models(data, formulas):
    models = {}
    summaries = {}
    
    for i, formula in tqdm(enumerate(formulas), total=len(formulas), desc="Fitting Models"):
        
        model_name = f"model{i}"
        print(f"Fitting {model_name} with formula: {formula}")
        
        # Create the Lmer model object and store
        # Fit the model
        model = Lmer(formula, data=data, family='binomial')
        fitted_model = model.fit()
        
        # Store the full model object and the summary
        models[model_name] = model
        summaries[model_name] = fitted_model
        
    return models, summaries


# Save the dictionary of fitted models in the "outputs" folder
def save_fitted_models(fitted_models, filename="fitted_models.pkl"):
    
    # Path to the 'outputs' folder
    project_root = os.path.dirname(os.getcwd())
    output_dir = os.path.join(project_root, 'outputs')
    
    filepath = os.path.join(output_dir, filename)

    # Save the models to the specified file
    with open(filepath, 'wb') as f:
        pickle.dump(fitted_models, f)
    print(f"Models saved to {filepath}.")


# Load the dictionary of fitted models from the "outputs" folder in the parent directory
def load_fitted_models(filename="fitted_models.pkl"):
    
    # Path to the 'outputs' folder
    project_root = os.path.dirname(os.getcwd())
    output_dir = os.path.join(project_root, 'outputs')
    
    filepath = os.path.join(output_dir, filename)

    # Load the models from the specified file
    with open(filepath, 'rb') as f:
        fitted_models = pickle.load(f)
    print(f"Models loaded from {filepath}.")
    return fitted_models