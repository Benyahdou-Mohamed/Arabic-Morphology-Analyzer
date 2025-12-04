# Arabic Morphology Analyzer

A modern GUI application for analyzing Arabic text morphology with support for user corrections.

## Features ✨

- **Morphological Analysis**: Analyze Arabic text using Qalsadi
- **Part of Speech Detection**: Automatically detect word types (فعل، اسم، حرف)
- **Grammatical Case**: Identify إعراب (مرفوع، منصوب، مجرور، مجزوم)
- **Gender Detection**: Determine word gender (مذكر، مؤنث)
- **User Corrections**: Save and manage custom corrections in MongoDB
- **RTL Support**: Full right-to-left text layout for Arabic
- **Clean UI**: Modern, intuitive interface

## Installation 🚀

### Prerequisites

- Python 3.8+
- MongoDB (running on localhost:27017)

### Setup

1. **Clone or download the project**

2. **Install dependencies**:
```bash
pip install -r requirements.txt
```

3. **Start MongoDB**:
```bash
# Make sure MongoDB is running
mongod
```

4. **Run the application**:
```bash
python main.py
```

## Project Structure 📁

```
arabic_morphology_analyzer/
├── main.py              # Entry point
├── config.py            # Configuration (colors, fonts, settings)
├── database.py          # MongoDB operations
├── analyzer.py          # Morphology analysis logic
├── gui_main.py          # Main GUI window
├── gui_widgets.py       # Reusable UI components
├── requirements.txt     # Python dependencies
└── README.md           # This file
```

## Usage 📖

1. **Enter Text**: Type or paste Arabic text in the input box
2. **Analyze**: Click "تحليل" to perform morphological analysis
3. **Review Results**: View analysis in the results panel
4. **Make Corrections**: Navigate through words and edit analysis
5. **Save**: Click "حفظ" to save corrections to database

## Database Schema 💾

MongoDB Collection: `lexicon_simple`

```json
{
  "mot": "الكلمة",
  "user": {
    "pos": "فعل",
    "i3rab": "مرفوع",
    "gender": "مذكر"
  }
}
```

## Configuration ⚙️

Edit `config.py` to customize:
- UI colors and fonts
- Window dimensions
- MongoDB connection settings

## Dependencies 📦

- **pymongo**: MongoDB driver
- **qalsadi**: Arabic morphological analyzer
- **pyarabic**: Arabic language processing tools
- **tkinter**: GUI framework (built-in with Python)

## Troubleshooting 🔧

**MongoDB Connection Failed?**
- Ensure MongoDB is running: `mongod`
- Check connection URI in `config.py`
- Default: `mongodb://localhost:27017`

**Import Errors?**
- Install requirements: `pip install -r requirements.txt`

**Display Issues?**
- Ensure you have Arabic fonts installed
- Try changing FONT in `config.py`

## License 📄

Educational/Academic Project

## Author 👨‍💻
- HOCEINI Mohammed
- DEGHEM Boubakar Seddik
- Horri Mourad
- Khene Yacine
- Dahou Mohammed Amine
- Benyahdou Mohammed

Mini Project FTP
