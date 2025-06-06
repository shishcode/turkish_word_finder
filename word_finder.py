import tkinter as tk
from tkinter import ttk, scrolledtext
import os

class WordFinderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Word Finder")
        self.root.geometry("800x600")
        
        # Configure style
        style = ttk.Style()
        style.configure("TButton", padding=6, relief="flat", background="#2196F3")
        style.configure("TLabel", padding=6)
        style.configure("TEntry", padding=6)
        
        # Create main frame
        main_frame = ttk.Frame(root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Include letters
        ttk.Label(main_frame, text="Include Letters (comma-separated):").grid(row=0, column=0, sticky=tk.W)
        self.include_entry = ttk.Entry(main_frame, width=40)
        self.include_entry.grid(row=0, column=1, padx=5, pady=5)
        
        # Exclude letters
        ttk.Label(main_frame, text="Exclude Letters (comma-separated):").grid(row=1, column=0, sticky=tk.W)
        self.exclude_entry = ttk.Entry(main_frame, width=40)
        self.exclude_entry.grid(row=1, column=1, padx=5, pady=5)
        
        # Search button
        search_button = ttk.Button(main_frame, text="Search", command=self.search_words)
        search_button.grid(row=2, column=0, columnspan=2, pady=10)
        
        # Results area
        ttk.Label(main_frame, text="Results:").grid(row=3, column=0, sticky=tk.W)
        self.results_text = scrolledtext.ScrolledText(main_frame, width=70, height=20)
        self.results_text.grid(row=4, column=0, columnspan=2, pady=5)
        
        # Load words
        self.words = self.load_words()
        
    def load_words(self):
        try:
            with open('words.txt', 'r', encoding='utf-8') as file:
                return [word.strip() for word in file.readlines()]
        except FileNotFoundError:
            self.results_text.insert(tk.END, "Error: words.txt file not found!")
            return []
    
    def search_words(self):
        include_letters = [letter.strip() for letter in self.include_entry.get().split(',') if letter.strip()]
        exclude_letters = [letter.strip() for letter in self.exclude_entry.get().split(',') if letter.strip()]
        
        self.results_text.delete(1.0, tk.END)
        
        if not self.words:
            self.results_text.insert(tk.END, "No words loaded!")
            return
        
        filtered_words = []
        for word in self.words:
            # Check if word contains all include letters
            if include_letters and not all(letter in word for letter in include_letters):
                continue
                
            # Check if word contains any exclude letters
            if exclude_letters and any(letter in word for letter in exclude_letters):
                continue
                
            filtered_words.append(word)
        
        if filtered_words:
            self.results_text.insert(tk.END, f"Found {len(filtered_words)} words:\n\n")
            self.results_text.insert(tk.END, "\n".join(filtered_words))
        else:
            self.results_text.insert(tk.END, "No words found matching the criteria.")

if __name__ == "__main__":
    root = tk.Tk()
    app = WordFinderApp(root)
    root.mainloop() 