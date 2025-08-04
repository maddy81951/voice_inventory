import qrcode
import os
from datetime import datetime

def generate_qr(data, timestamp):
    item = data["item"]
    quantity = data["quantity"]
    location = data["location"]

    qr_data = f"Item: {item}\nQuantity: {quantity}\nLocation: {location}\nTimestamp: {timestamp}"
    qr = qrcode.make(qr_data)

    folder = f"qr_codes/{datetime.now().strftime('%Y-%m-%d')}"
    os.makedirs(folder, exist_ok=True)

    filename = f"qr_{item}_{quantity}_{location.replace(' ', '_')}.png"
    path = os.path.join(folder, filename)

    qr.save(path)
    print(f"QR code saved as {path}")
    return path