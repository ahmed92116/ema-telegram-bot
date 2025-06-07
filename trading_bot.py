from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print("🚨 Trading Signal Received 🚨")
    print(json.dumps(data, indent=4))

    msg = data.get('message', '').upper()

    if "LONG" in msg:
        print(f"📈 Signal: {data['ticker']} is going UP (LONG)")
    elif "SHORT" in msg:
        print(f"📉 Signal: {data['ticker']} is going DOWN (SHORT)")
    else:
        print("⚠️ Unknown signal")

    return 'Signal received', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
