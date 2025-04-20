
# Iris Flower Classification with Flask

This project predicts the species of an iris flower based on user input features using a machine learning model.

## How to Run

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Train the model:
   ```
   python model_training.py
   ```

3. Run the Flask app:
   ```
   python app.py
   ```

4. Open in browser:
   ```
   http://127.0.0.1:5000/
   ```

## Files
- `model_training.py`: Trains and saves the ML model.
- `app.py`: Flask web app.
- `templates/index.html`: Web UI.
- `static/style.css`: Styling.
- `iris_model.pkl`: Saved ML model.
