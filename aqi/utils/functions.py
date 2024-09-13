# Function to fit the series of predefined model formulas
def fit_models(data, formulas):
    models = {}
    for i, formula in enumerate(formulas):
        model_name = f"model{i}"  # Generate model names dynamically
        print(f"Fitting {model_name} with formula: {formula}")
        models[model_name] = Lmer(formula, data=data, family='binomial').fit()
    return models

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