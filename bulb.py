'''
'''
import avea
from flask import Flask, request, jsonify

app = Flask(__name__)

# Replace with the MAC address of your Avea bulb
AVEA_BULB_MAC = "78:A5:04:50:D6:53"

# Function to set bulb color (RGB format)
def set_avea_color(r, g, b):
    bulb = avea.Bulb(AVEA_BULB_MAC)
    if not bulb:
        return False

    try:
        bulb.set_rgb(r, g, b)
        return True
    except Exception as e:
        print("Error setting color:", e)
        return False

@app.route("/set_color", methods=["POST"])
def change_color():
    data = request.get_json()
    r = data.get("r", 255)  # Default: White
    g = data.get("g", 255)
    b = data.get("b", 255)

    success = set_avea_color(r, g, b)
    return jsonify({"success": success})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)