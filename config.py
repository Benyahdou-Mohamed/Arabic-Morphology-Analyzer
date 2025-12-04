# config.py
# Configuration file for Arabic Morphology Analyzer

# ======================== UI Colors ========================
BG = "#f5f7fa"
PANEL = "#ffffff"
ACCENT = "#0f6464"
ACCENT_DARK = "#084b4b"
BUTTON_BG = "#1fa3a3"
BUTTON_HOVER = "#168787"
TEXT = "#222"
META = "#0a6fbf"
SEPARATOR = "#dddddd"

# ======================== Fonts ========================
FONT = ("Segoe UI", 11)
HEADER_FONT = ("Segoe UI", 20, "bold")
LABEL_FONT = ("Segoe UI", 12, "bold")
WORD_FONT = ("Segoe UI", 12, "bold")
STATUS_FONT = ("Segoe UI", 11)

# ======================== Window Settings ========================
WINDOW_TITLE = "تحليل الكلمات العربية"
MIN_WIDTH = 960
MIN_HEIGHT = 680
HEADER_HEIGHT = 70

# ======================== MongoDB Settings ========================
MONGO_URI = "mongodb://localhost:27017"
MONGO_TIMEOUT = 1500
DB_NAME = "arabic_morphology_db"
COLLECTION_NAME = "lexicon_simple"