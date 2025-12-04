#!/usr/bin/env python3
# main.py
# Entry point for Arabic Morphology Analyzer

"""
Arabic Morphology Analyzer
===========================
A GUI application for analyzing Arabic text morphology using Qalsadi.
Supports user corrections stored in MongoDB.

Author: Mini Project FTP
"""

from gui_main import ArabicMorphologyGUI


def main():
    """Main entry point"""
    app = ArabicMorphologyGUI()
    app.run()


if __name__ == "__main__":
    main()