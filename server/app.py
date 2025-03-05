# # from flask import Flask, jsonify, request
# # import re
# # import speech_recognition as sr
# # from googletrans import Translator
# # from word2number import w2n  
# # from flask_cors import CORS




# # app = Flask(__name__)

# # CORS(app)



# # UNITS = ["kg", "g", "l", "ml", "piece", "pieces", "dozen", "pack", "packet", "bottle", "can", "box", "kilo","kilogram"]
# # FRACTION_MAP = {"half": 0.5, "one and a half": 1.5, "quarter": 0.25}

# # def convert_word_to_number(text):
# #     try:
# #         return w2n.word_to_num(text)
# #     except ValueError:
# #         return text

# # def separate_number_and_unit(text):
# #     match = re.match(r"(\d+\.?\d*)([a-zA-Z]+)", text)
# #     if match:
# #         num, unit = match.groups()
# #         try:
# #             num = float(num) if "." in num else int(num)  # Convert to int or float
# #         except ValueError:
# #             return None, None
# #         return num, unit.lower() if unit.lower() in UNITS else None
# #     return None, None

# # def extract_details(text):
# #     text = text.lower().strip()
# #     words = text.split()
# #     if words[0] in ["a", "an"]:
# #         words[0] = "one"

# #     quantity = None
# #     unit = None
# #     item_name = text  

# #     if len(words) >= 2 and f"{words[0]} {words[1]}" in FRACTION_MAP:
# #         quantity = FRACTION_MAP[f"{words[0]} {words[1]}"]
# #         words.pop(0)
# #         words.pop(0)
# #     elif words[0] in FRACTION_MAP:
# #         quantity = FRACTION_MAP[words[0]]
# #         words.pop(0)

# #     elif words:
# #         num, extracted_unit = separate_number_and_unit(words[0])
# #         if num and extracted_unit in UNITS:
# #             quantity = num
# #             unit = extracted_unit
# #             words.pop(0)

# #     elif words:
# #         converted = convert_word_to_number(words[0])
# #         if isinstance(converted, (int, float)):  
# #             quantity = converted
# #             words.pop(0)  

# #     if words and words[0] in UNITS:
# #         unit = words.pop(0)  

# #     if words and words[0] == "of":
# #         words.pop(0)

# #     item_name = " ".join(words).strip()
# #     return quantity, item_name, unit

# # def takecommand(): 
# #     r = sr.Recognizer()
# #     with sr.Microphone() as source: 
# #         print("Listening for Tamil speech...") 
# #         r.pause_threshold = 1
# #         audio = r.listen(source) 

# #     try: 
# #         print("Recognizing Tamil Speech...") 
# #         query = r.recognize_google(audio, language='ta-IN')  
# #         print(f"The User said (Tamil): {query}\n") 
# #     except Exception as e: 
# #         print("Couldn't recognize, please try again...") 
# #         return "None"
    
# #     return query  

# # def translate_text(text):
# #     translator = Translator()
# #     translation = translator.translate(text, dest='en')
# #     return translation.text

# # @app.route('/voice', methods=['GET'])
# # def voice():
# #     query = takecommand()
# #     while query == "None":
# #         query = takecommand()

# #     translated_text = translate_text(query)  
# #     quantity, item_name, unit = extract_details(translated_text)
# #     print(quantity,item_name, unit)

# #     return jsonify({
# #         "Translated Text": translated_text,
# #         "Quantity": quantity,
# #         "Item name": item_name,
# #         "Units": unit
# #     })

# # if __name__ == "__main__":
# #     app.run(debug=True)


# from flask import Flask, jsonify, request
# import re
# import speech_recognition as sr
# from googletrans import Translator
# from word2number import w2n  
# from flask_cors import CORS
# import pymongo  # MongoDB integration
# from bson import ObjectId  # Import ObjectId for type conversion

# app = Flask(__name__)
# CORS(app)

# # MongoDB Connection
# client = pymongo.MongoClient("mongodb://localhost:27017/")
# db = client["voice_bill_db"]
# collection = db["store_groceries"]


# UNITS = ["kg", "g", "l", "ml", "piece", "pieces", "dozen", "pack", "packet", "bottle", "can", "box", "kilo","kilogram"]
# FRACTION_MAP = {"half": 0.5, "one and a half": 1.5, "quarter": 0.25}


# def convert_word_to_number(text):
#     try:
#         return w2n.word_to_num(text)
#     except ValueError:
#         return text

# def separate_number_and_unit(text):
#     match = re.match(r"(\d+\.?\d*)([a-zA-Z]+)", text)
#     if match:
#         num, unit = match.groups()
#         try:
#             num = float(num) if "." in num else int(num)
#         except ValueError:
#             return None, None
#         return num, unit.lower() if unit.lower() in UNITS else None
#     return None, None

# def extract_details(text):
#     text = text.lower().strip()
#     words = text.split()
#     if words[0] in ["a", "an"]:
#         words[0] = "one"
    
#     quantity, unit = None, None
    
#     if len(words) >= 2 and f"{words[0]} {words[1]}" in FRACTION_MAP:
#         quantity = FRACTION_MAP[f"{words[0]} {words[1]}"]
#         words = words[2:]
#     elif words[0] in FRACTION_MAP:
#         quantity = FRACTION_MAP[words[0]]
#         words = words[1:]
#     elif words:
#         num, extracted_unit = separate_number_and_unit(words[0])
#         if num:
#             quantity = num
#             if extracted_unit in UNITS:
#                 unit = extracted_unit
#                 words = words[1:]
#         else:
#             converted = convert_word_to_number(words[0])
#             if isinstance(converted, (int, float)):
#                 quantity = converted
#                 words = words[1:]
    
#     if words and words[0] in UNITS:
#         unit = words.pop(0)
    
#     if words and words[0] == "of":
#         words.pop(0)
    
#     item_name = " ".join(words).strip()
#     return quantity, item_name, unit

# def takecommand(): 
#     r = sr.Recognizer()
#     with sr.Microphone() as source: 
#         print("Listening for Tamil speech...") 
#         r.pause_threshold = 1
#         audio = r.listen(source) 
    
#     try: 
#         print("Recognizing Tamil Speech...") 
#         query = r.recognize_google(audio, language='ta-IN')  
#         print(f"The User said (Tamil): {query}\n") 
#     except Exception as e: 
#         print("Couldn't recognize, please try again...") 
#         return "None"
    
#     return query  

# def translate_text(text):
#     translator = Translator()
#     translation = translator.translate(text, dest='en')
#     return translation.text

# def get_item_from_db(item_name):
#     item = collection.find_one({"ItemName": {"$regex": f"^{re.escape(item_name)}$", "$options": "i"}})
    
#     if item:
#         item["_id"] = str(item["_id"])
#         return {
#             "Item Name": item.get("ItemName", ""),
#             "Price": item.get("Price", 0),
#             "Available Quantity": item.get("Quantity", 0),
#             "Units": item.get("Units", "")
#         }
    
#     return None

# def convert_units(requested_qty, requested_unit, db_unit, price_per_unit):
#     if requested_unit and db_unit and requested_unit in UNITS and db_unit in UNITS:
#         if UNITS[requested_unit] < UNITS[db_unit]:
#             converted_qty = requested_qty / (UNITS[db_unit] / UNITS[requested_unit])
#         else:
#             converted_qty = requested_qty * (UNITS[requested_unit] / UNITS[db_unit])
#         return converted_qty * price_per_unit
#     return requested_qty * price_per_unit

# @app.route('/voice', methods=['GET'])
# def voice():
#     query = takecommand()
#     while query == "None":
#         query = takecommand()

#     translated_text = translate_text(query)  
#     quantity, item_name, unit = extract_details(translated_text)  
#     print("data", quantity, item_name, unit)

#     item_data = get_item_from_db(item_name)

#     if item_data:
#         # Ensure Available Quantity is treated as a string before regex operation
#         available_quantity_str = str(item_data.get("Available Quantity", "0"))

#         # Extract numeric value from available quantity (default to 1 if extraction fails)
#         match = re.search(r'\d+(\.\d+)?', available_quantity_str)
#         db_quantity = float(match.group()) if match else 1  
#         db_unit = item_data.get("Units", "").lower()

#         # Convert user input quantity to match DB unit
#         if unit and db_unit and unit != db_unit:
#             if unit == "g" and db_unit == "kg":
#                 quantity /= 1000  # Convert grams to kg
#             elif unit == "kg" and db_unit == "g":
#                 quantity *= 1000  # Convert kg to grams

#         # Ensure price conversion if DB stores price per kg but user enters g
#         if unit == "g" and db_unit == "kg":
#             price_per_unit = item_data["Price"] / 1000  # Convert price per kg to price per gram
#         elif unit == "kg" and db_unit == "g":
#             price_per_unit = item_data["Price"] * 1000  # Convert price per gram to price per kg
#         else:
#             price_per_unit = item_data["Price"]  # No conversion needed

#         # Calculate total cost
#         if quantity:
#             total_cost = price_per_unit * quantity
#         else:
#             total_cost = "Quantity not specified"

#         response_data = {
#             "Translated Text": translated_text,
#             "Item Name": item_data["Item Name"],
#             "Price per Unit": item_data["Price"],
#             "Available Quantity": quantity,
#             "Units": unit if unit else db_unit,
#             "Total Cost": round(total_cost, 2) if isinstance(total_cost, (int, float)) else total_cost
#         }
#     else:
#         response_data = {
#             "Translated Text": translated_text,
#             "Available Quantity": quantity if quantity else "Not specified",
#             "Item Name": item_name,
#             "Units": unit if unit else "Not specified",
#             "Message": "Item not found in database"
#         }

#     print(response_data)
#     return jsonify(response_data)


# if __name__ == "__main__":
#     app.run(debug=True)

from flask import Flask, jsonify, request
import re
import speech_recognition as sr
from googletrans import Translator
from word2number import w2n  
from flask_cors import CORS
import pymongo  # MongoDB integration
from bson import ObjectId  # Import ObjectId for type conversion

app = Flask(__name__)
CORS(app)

# MongoDB Connection
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["voice_bill_db"]
collection = db["store_groceries"]

UNITS = {"kg": 1000, "g": 1, "l": 1000, "ml": 1, "piece": 1, "pieces": 1, "dozen": 12, "pack": 1, "packet": 1, "bottle": 1, "can": 1, "box": 1, "kilo": 1000, "kilogram": 1000}
FRACTION_MAP = {"half": 0.5, "one and a half": 1.5, "quarter": 0.25}

def convert_word_to_number(text):
    try:
        return w2n.word_to_num(text)
    except ValueError:
        return text

def separate_number_and_unit(text):
    match = re.match(r"(\d+\.?\d*)([a-zA-Z]+)", text)
    if match:
        num, unit = match.groups()
        try:
            num = float(num) if "." in num else int(num)
        except ValueError:
            return None, None
        return num, unit.lower() if unit.lower() in UNITS else None
    return None, None

def extract_details(text):
    text = text.lower().strip()
    words = text.split()
    if words[0] in ["a", "an"]:
        words[0] = "one"
    
    quantity, unit = None, None
    
    if len(words) >= 2 and f"{words[0]} {words[1]}" in FRACTION_MAP:
        quantity = FRACTION_MAP[f"{words[0]} {words[1]}"]
        words = words[2:]
    elif words[0] in FRACTION_MAP:
        quantity = FRACTION_MAP[words[0]]
        words = words[1:]
    elif words:
        num, extracted_unit = separate_number_and_unit(words[0])
        if num:
            quantity = num
            if extracted_unit in UNITS:
                unit = extracted_unit
                words = words[1:]
        else:
            converted = convert_word_to_number(words[0])
            if isinstance(converted, (int, float)):
                quantity = converted
                words = words[1:]
    
    if words and words[0] in UNITS:
        unit = words.pop(0)
    
    if words and words[0] == "of":
        words.pop(0)
    
    item_name = " ".join(words).strip()
    return quantity, item_name, unit

def takecommand(): 
    r = sr.Recognizer()
    with sr.Microphone() as source: 
        print("Listening for Tamil speech...") 
        r.pause_threshold = 1
        audio = r.listen(source) 
    
    try: 
        print("Recognizing Tamil Speech...") 
        query = r.recognize_google(audio, language='ta-IN')  
        print(f"The User said (Tamil): {query}\n") 
    except Exception as e: 
        print("Couldn't recognize, please try again...") 
        return "None"
    
    return query  

def translate_text(text):
    translator = Translator()
    translation = translator.translate(text, dest='en')
    return translation.text

def get_item_from_db(item_name):
    item = collection.find_one({"ItemName": {"$regex": f"^{re.escape(item_name)}$", "$options": "i"}})
    
    if item:
        item["_id"] = str(item["_id"])
        return {
            "Item Name": item.get("ItemName", ""),
            "Price": item.get("Price", 0),
            "Available Quantity": item.get("Quantity", 0),
            "Units": item.get("Units", "")
        }
    
    return None

def calculate_price(requested_qty, requested_unit, db_qty, db_unit, price_per_unit):
    if requested_unit and db_unit and requested_unit in UNITS and db_unit in UNITS:
        requested_qty = requested_qty * UNITS[requested_unit] / UNITS[db_unit]
    return requested_qty * price_per_unit

@app.route('/voice', methods=['GET'])
def voice():
    query = takecommand()
    while query == "None":
        query = takecommand()

    translated_text = translate_text(query)  
    quantity, item_name, unit = extract_details(translated_text)  
    print("data", quantity, item_name, unit)

    item_data = get_item_from_db(item_name)

    if item_data:
        # Ensure Available Quantity is treated as a string before regex operation
        available_quantity_str = str(item_data.get("Available Quantity", "0"))

        # Extract numeric value from available quantity (default to 1 if extraction fails)
        match = re.search(r'\d+(\.\d+)?', available_quantity_str)
        db_quantity = float(match.group()) if match else 1  
        db_unit = item_data.get("Units", "").lower()

        # Convert user input quantity to match DB unit
        if unit and db_unit and unit != db_unit:
            if unit == "g" and db_unit == "kg":
                quantity /= 1000  
            elif unit == "kg" and db_unit == "g":
                quantity *= 1000  

        if quantity:
            total_cost = (item_data["Price"] / db_quantity) * quantity
        else:
            total_cost = "Quantity not specified"

        response_data = {
            "Translated Text": translated_text,
            "Item Name": item_data["Item Name"],
            "Price per Unit": item_data["Price"],
            "Available Quantity": quantity,
            "Units": unit if unit else db_unit,
            "Total Cost": round(total_cost, 2) if isinstance(total_cost, (int, float)) else total_cost
        }
    else:
        response_data = {
            "Translated Text": translated_text,
            "Available Quantity": quantity if quantity else "Not specified",
            "Item Name": item_name,
            "Units": unit if unit else "Not specified",
            "Message": "Item not found in database"
        }

    print(response_data)
    return jsonify(response_data)


if __name__ == "__main__":
    app.run(debug=True)
