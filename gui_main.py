# gui_main.py
# Main GUI application window

import tkinter as tk
from tkinter import scrolledtext, messagebox
from config import *
from database import Database
from analyzer import MorphologyAnalyzer
from gui_widgets import style_button, create_label_entry_pair


class ArabicMorphologyGUI:
    """Main GUI application for Arabic Morphology Analyzer"""
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title(WINDOW_TITLE)
        self.root.configure(bg=BG)
        self.root.minsize(MIN_WIDTH, MIN_HEIGHT)
        
        # Initialize components
        self.db = Database()
        self.analyzer = MorphologyAnalyzer()
        
        # Data storage
        self.words = []
        self.current_index = 0
        
        # Build UI
        self._create_header()
        self._create_main_layout()
        self._create_input_panel()
        self._create_results_panel()
        self._create_correction_panel()
        self._create_status_panel()
        
        # Initial refresh
        self.refresh_results()
    
    def _create_header(self):
        """Create header section"""
        header = tk.Frame(self.root, bg=ACCENT, height=HEADER_HEIGHT)
        header.pack(fill="x")
        header.pack_propagate(False)
        
        tk.Label(
            header,
            text="MINI PROJECT FTP",
            bg=ACCENT,
            fg="white",
            font=HEADER_FONT
        ).pack(anchor="e", padx=20, pady=15)
    
    def _create_main_layout(self):
        """Create main layout grid"""
        self.main_frame = tk.Frame(self.root, bg=BG)
        self.main_frame.pack(fill="both", expand=True, padx=10, pady=10)
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(1, weight=1)
    
    def _create_input_panel(self):
        """Create input panel (right side)"""
        # Right side frame
        right_frame = tk.Frame(self.main_frame, bg=BG)
        right_frame.grid(row=0, column=1, sticky="nsew", padx=(8, 0))
        
        # Input panel
        input_panel = tk.Frame(right_frame, bg=PANEL)
        input_panel.pack(fill="x", pady=(0, 10))
        
        tk.Label(
            input_panel,
            text="أدخل الجملة:",
            bg=PANEL,
            fg=TEXT,
            font=LABEL_FONT
        ).pack(anchor="e", padx=10, pady=5)
        
        # Input text box
        self.input_box = scrolledtext.ScrolledText(
            input_panel,
            height=4,
            font=FONT,
            wrap=tk.WORD
        )
        self.input_box.pack(fill="x", padx=10, pady=(0, 10))
        self.input_box.tag_configure("rtl", justify="right")
        self.input_box.tag_add("rtl", "1.0", "end")
        
        # Buttons
        button_frame = tk.Frame(input_panel, bg=PANEL)
        button_frame.pack(fill="x", padx=10, pady=5)
        
        analyze_btn = tk.Button(
            button_frame,
            text="تحليل",
            command=self.analyze_text
        )
        style_button(analyze_btn)
        analyze_btn.pack(side="right")
        
        clear_btn = tk.Button(
            button_frame,
            text="مسح",
            bg="#f0ad4e",
            fg="white",
            bd=0,
            padx=10,
            pady=6,
            command=self.clear_input
        )
        clear_btn.pack(side="right", padx=8)
        clear_btn.bind("<Enter>", lambda e: clear_btn.config(bg="#d48806"))
        clear_btn.bind("<Leave>", lambda e: clear_btn.config(bg="#f0ad4e"))
        
        # Results panel
        self.results_frame = right_frame
    
    def _create_results_panel(self):
        """Create results display panel"""
        results_panel = tk.Frame(self.results_frame, bg=PANEL)
        results_panel.pack(fill="both", expand=True)
        
        tk.Label(
            results_panel,
            text="النتائج:",
            bg=PANEL,
            fg=TEXT,
            font=LABEL_FONT
        ).pack(anchor="e", padx=10, pady=5)
        
        self.results_box = scrolledtext.ScrolledText(
            results_panel,
            height=20,
            font=FONT,
            wrap=tk.WORD,
            state=tk.DISABLED
        )
        self.results_box.pack(fill="both", expand=True, padx=10, pady=10)
        self.results_box.tag_configure("word", foreground=ACCENT_DARK, font=WORD_FONT, justify="right")
        self.results_box.tag_configure("meta", foreground=META, justify="right")
        self.results_box.tag_configure("sep", foreground=SEPARATOR, justify="right")
    
    def _create_correction_panel(self):
        """Create correction panel (left side)"""
        left_frame = tk.Frame(self.main_frame, bg=BG)
        left_frame.grid(row=0, column=0, sticky="nsew")
        
        correction_panel = tk.Frame(left_frame, bg=PANEL)
        correction_panel.pack(fill="x")
        
        tk.Label(
            correction_panel,
            text="التصحيح",
            bg=PANEL,
            fg=TEXT,
            font=LABEL_FONT
        ).pack(anchor="e", padx=10, pady=5)
        
        # Form
        form_frame = tk.Frame(correction_panel, bg=PANEL)
        form_frame.pack(padx=10, pady=8, fill="x")
        
        # Word display
        self.word_var = tk.StringVar()
        tk.Label(form_frame, text="الكلمة:", bg=PANEL).grid(row=0, column=1, sticky="e", padx=5)
        tk.Label(
            form_frame,
            textvariable=self.word_var,
            bg=PANEL,
            fg=ACCENT_DARK,
            font=WORD_FONT
        ).grid(row=0, column=0, sticky="e", padx=5)
        
        # Entry fields
        _, self.pos_entry = create_label_entry_pair(form_frame, "النوع:", 1)
        _, self.i3rab_entry = create_label_entry_pair(form_frame, "الإعراب:", 2)
        _, self.gender_entry = create_label_entry_pair(form_frame, "الجنس:", 3)
        
        # Navigation buttons
        nav_frame = tk.Frame(correction_panel, bg=PANEL)
        nav_frame.pack(padx=10, pady=10, fill="x")
        
        prev_btn = tk.Button(nav_frame, text="« السابق", command=self.prev_word)
        style_button(prev_btn)
        prev_btn.pack(side="right")
        
        next_btn = tk.Button(nav_frame, text="التالي »", command=self.next_word)
        style_button(next_btn)
        next_btn.pack(side="right", padx=8)
        
        save_btn = tk.Button(nav_frame, text="حفظ", command=self.save_correction)
        style_button(save_btn)
        save_btn.pack(side="left")
        
        self.correction_frame = left_frame
    
    def _create_status_panel(self):
        """Create status panel"""
        status_panel = tk.Frame(self.correction_frame, bg=PANEL)
        status_panel.pack(fill="both", expand=True, pady=10)
        
        tk.Label(
            status_panel,
            text="الحالة:",
            bg=PANEL,
            fg=TEXT,
            font=LABEL_FONT
        ).pack(anchor="e", padx=10, pady=5)
        
        db_status = "متصل بــ MongoDB" if self.db.is_online() else "غير متصل بـ MongoDB"
        tk.Label(
            status_panel,
            text=db_status,
            bg=PANEL,
            fg=ACCENT_DARK
        ).pack(anchor="e", padx=10, pady=2)
        
        self.count_var = tk.StringVar(value="الكلمات: 0")
        tk.Label(
            status_panel,
            textvariable=self.count_var,
            bg=PANEL,
            fg=META,
            font=STATUS_FONT
        ).pack(anchor="e", padx=10, pady=5)
    
    def analyze_text(self):
        """Analyze input text"""
        text = self.input_box.get("1.0", tk.END).strip()
        if not text:
            messagebox.showwarning("تنبيه", "أدخل نصاً للتحليل.")
            return
        
        # Analyze text
        self.words = self.analyzer.analyze_text(text)
        
        # Get user corrections from database
        for word in self.words:
            user_correction = self.db.get_user_correction(word["mot"])
            if user_correction:
                word["user"] = user_correction
        
        self.current_index = 0
        self.refresh_results()
        self.load_current_word()
    
    def clear_input(self):
        """Clear input box"""
        self.input_box.delete("1.0", tk.END)
    
    def refresh_results(self):
        """Refresh results display"""
        self.results_box.config(state=tk.NORMAL)
        self.results_box.delete("1.0", tk.END)
        
        if not self.words:
            self.results_box.insert(tk.END, "لا نتائج.\n", "meta")
            self.count_var.set("الكلمات: 0")
        else:
            for word_data in self.words:
                mot = word_data["mot"]
                system = word_data["system"]
                user = word_data["user"]
                
                # Use user correction if available, otherwise system
                pos = user.get("pos") if user else system["pos"]
                i3rab = user.get("i3rab") if user else system["i3rab"]
                gender = user.get("gender") if user else system["gender"]
                
                self.results_box.insert(tk.END, f"{mot}\n", "word")
                self.results_box.insert(tk.END, f"  • النوع: {pos}\n", "meta")
                self.results_box.insert(tk.END, f"  • الإعراب: {i3rab}\n", "meta")
                self.results_box.insert(tk.END, f"  • الجنس: {gender}\n", "meta")
                self.results_box.insert(tk.END, "-" * 45 + "\n", "sep")
            
            self.count_var.set(f"الكلمات: {len(self.words)}")
        
        self.results_box.config(state=tk.DISABLED)
    
    def load_current_word(self):
        """Load current word into correction form"""
        if not self.words:
            self.word_var.set("")
            self.pos_entry.delete(0, tk.END)
            self.i3rab_entry.delete(0, tk.END)
            self.gender_entry.delete(0, tk.END)
            return
        
        word_data = self.words[self.current_index]
        self.word_var.set(word_data["mot"])
        
        system = word_data["system"]
        user = word_data["user"]
        
        self.pos_entry.delete(0, tk.END)
        self.i3rab_entry.delete(0, tk.END)
        self.gender_entry.delete(0, tk.END)
        
        if user:
            self.pos_entry.insert(0, user["pos"])
            self.i3rab_entry.insert(0, user["i3rab"])
            self.gender_entry.insert(0, user["gender"])
        else:
            self.pos_entry.insert(0, system["pos"])
            self.i3rab_entry.insert(0, system["i3rab"])
            self.gender_entry.insert(0, system["gender"])
    
    def prev_word(self):
        """Navigate to previous word"""
        if self.words and self.current_index > 0:
            self.current_index -= 1
            self.load_current_word()
    
    def next_word(self):
        """Navigate to next word"""
        if self.words and self.current_index < len(self.words) - 1:
            self.current_index += 1
            self.load_current_word()
    
    def save_correction(self):
        """Save user correction"""
        if not self.words:
            return
        
        word_data = self.words[self.current_index]
        pos = self.pos_entry.get().strip()
        i3rab = self.i3rab_entry.get().strip()
        gender = self.gender_entry.get().strip()
        
        if not pos and not i3rab and not gender:
            messagebox.showwarning("تنبيه", "أدخل تصحيحاً واحداً على الأقل.")
            return
        
        # Save to database
        success = self.db.save_correction(word_data["mot"], pos, i3rab, gender)
        
        if not success:
            messagebox.showerror("خطأ", "لا يوجد اتصال بقاعدة البيانات.")
            return
        
        # Update local data
        word_data["user"] = {
            "pos": pos,
            "i3rab": i3rab,
            "gender": gender
        }
        
        self.refresh_results()
        self.load_current_word()
        messagebox.showinfo("تم", "تم الحفظ.")
    
    def run(self):
        """Start the application"""
        self.root.mainloop()