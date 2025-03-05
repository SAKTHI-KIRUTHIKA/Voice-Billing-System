from flask import Flask, jsonify
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend requests

EXCEL_FILE_PATH = "D:/final_yr_proj/original_db.xlsx"

@app.route('/api/excel', methods=['GET'])
def read_excel():
    try:
        df = pd.read_excel(EXCEL_FILE_PATH, engine='openpyxl')

        # Fill NaN values with appropriate defaults
        df = df.fillna({"Item Name": "Unknown", "Price": 0, "Quantity": 0, "Units": "N/A"})

        # Ensure numeric columns are properly formatted
        df["Price"] = pd.to_numeric(df["Price"], errors='coerce').fillna(0).astype(float)
        df["Quantity"] = pd.to_numeric(df["Quantity"], errors='coerce').fillna(0).astype(int)

        # Convert DataFrame to list of dictionaries
        data = df.to_dict(orient='records')
        print(data)  # Debugging: Check the processed data

        return jsonify(data)
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5001)  # Run on port 5001 to avoid conflicts
