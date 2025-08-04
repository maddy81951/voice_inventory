# 🗣️ Voice-Controlled Inventory Management System with QR Archiving

A smart and accessible inventory system that allows users (e.g., warehouse staff) to **speak inventory commands**, automatically **transcribe and parse** them using **speech recognition** and **NLP**, then generate **QR codes** for tagging items and archive them. The system also features a modern **Streamlit-based dashboard** to visualize inventory and filter QR history.

---

## 🚀 Features

- 🎙️ Voice-controlled inventory entry using speech recognition (`SpeechRecognition` + `NLP`)
- 📦 Automatically extracts:
  - **Item**
  - **Quantity**
  - **Location**
- 🧠 NLP-powered command parsing (`add 5 bags of rice to Section A`)
- 🕒 Timestamped records
- 🧾 SQLite database for persistent storage
- 📸 Auto-generates QR codes per item/location
- 📂 Organized `qr_codes` folder with date-wise subfolders
- 🌐 Frontend dashboard with:
  - 📊 Inventory table (ID, Item, Quantity, Location, Timestamp)
  - ✅ Filter panel
  - 🖼️ Toggle switch to preview full QR archive

---

## 🧠 Example Voice Command

> **"Add 10 boxes of pens to Section B"**

### ✅ Parsed Output:
```json
{
  "item": "pens",
  "quantity": "10 boxes",
  "location": "Section B"
}
