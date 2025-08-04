from speech_to_text import recognize_speech
from nlp_parser import parse_inventory_command
from db import create_db, save_to_db
from qr_generator import generate_qr
import datetime

def main():
    create_db()
    while True:
        print("\nSpeak your inventory command or say 'exit' to quit:")
        command = recognize_speech()
        if not command:
            continue
        if "exit" in command.lower():
            break

        data = parse_inventory_command(command)
        print("Parsed Data:", data)

        item = data.get("item")
        quantity = data.get("quantity")
        location = data.get("location")

        if all(data.values()):
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            qr_path = generate_qr(data, timestamp)
            save_to_db(item, quantity, location, timestamp, qr_path)
            print("Inventory recorded and QR code generated.")
        else:
            print("Could not parse the command properly.")

if __name__ == "__main__":
    main()