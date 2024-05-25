import tkinter as tk
import random
from tkinter import messagebox

# List of questions and their answers
questions = {
    "Quotes": [
        ("The greatest glory in living lies not in never falling, but in rising every time we fall.", "Nelson Mandela"),
        ("The way to get started is to quit talking and begin doing.", "Walt Disney"),
        ("If life were predictable it would cease to be life, and be without flavor.", "Eleanor Roosevelt"),
        ("Spread love everywhere you go. Let no one ever come to you without leaving happier.", "Mother Teresa"),
        ("When you reach the end of your rope, tie a knot in it and hang on.", "Franklin D. Roosevelt"),
        ("Always remember that you are absolutely unique. Just like everyone else.", "Margaret Mead"),
        ("Don't judge each day by the harvest you reap but by the seeds that you plant.", "Robert Louis Stevenson"),
        ("The future belongs to those who believe in the beauty of their dreams.", "Eleanor Roosevelt"),
        ("Tell me and I forget. Teach me and I remember. Involve me and I learn.", "Benjamin Franklin"),
        ("The best and most beautiful things in the world cannot be seen or even touched - they must be felt with the heart.", "Helen Keller"),
        ("It is during our darkest moments that we must focus to see the light.", "Aristotle"),
        ("Whoever is happy will make others happy too.", "Anne Frank"),
        ("Do not go where the path may lead, go instead where there is no path and leave a trail.", "Ralph Waldo Emerson"),
        ("You will face many defeats in life, but never let yourself be defeated.", "Maya Angelou"),
        ("In the end, it's not the years in your life that count. It's the life in your years.", "Abraham Lincoln"),
        ("Life is either a daring adventure or nothing at all.", "Helen Keller"),
        ("What we achieve inwardly will change outer reality.", "Plutarch"),
        ("Success is not how high you have climbed, but how you make a positive difference to the world.", "Roy T. Bennett"),
        ("Life is what happens when you're busy making other plans.", "John Lennon"),
        ("The purpose of our lives is to be happy.", "Dalai Lama"),
        ("Get busy living or get busy dying.", "Stephen King"),
        ("You have within you right now, everything you need to deal with whatever the world can throw at you.", "Brian Tracy"),
        ("Believe you can and you're halfway there.", "Theodore Roosevelt"),
        ("Act as if what you do makes a difference. It does.", "William James"),
        ("When you have a dream, you've got to grab it and never let go.", "Carol Burnett"),
        ("It is our choices that show what we truly are, far more than our abilities.", "J.K. Rowling"),
        ("It does not matter how slowly you go as long as you do not stop.", "Confucius"),
        ("Everything you’ve ever wanted is on the other side of fear.", "George Addair"),
        ("Success is not final, failure is not fatal: It is the courage to continue that counts.", "Winston Churchill"),
        ("Hardships often prepare ordinary people for an extraordinary destiny.", "C.S. Lewis"),
    ],
    "Riddles": [
        ("I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?", "Echo"),
        ("You measure my life in hours and I serve you by expiring. I die in just a few hours. What am I?", "Candle"),
        ("I have keys but no locks. I have space but no room. You can enter, but you can’t go outside. What am I?", "Keyboard"),
        ("The more of this there is, the less you see. What is it?", "Darkness"),
        ("What has many keys but can't open a single lock?", "Piano"),
        ("What has a heart that doesn’t beat?", "Artichoke"),
        ("I am not alive, but I grow; I don’t have lungs, but I need air; I don’t have a mouth, and I can drown. What am I?", "Fire"),
        ("I’m light as a feather, yet the strongest man can’t hold me for more than 5 minutes. What am I?", "Breath"),
        ("What comes once in a minute, twice in a moment, but never in a thousand years?", "M"),
        ("What disappears as soon as you say its name?", "Silence"),
        ("What has one eye, but can’t see?", "Needle"),
        ("What has to be broken before you can use it?", "Egg"),
        ("I’m tall when I’m young, and I’m short when I’m old. What am I?", "Candle"),
        ("What month of the year has 28 days?", "All of them"),
        ("What is full of holes but still holds water?", "Sponge"),
        ("What question can you never answer yes to?", "Are you asleep yet?"),
        ("What is always in front of you but can’t be seen?", "Future"),
        ("There’s a one-story house in which everything is yellow. Yellow walls, yellow doors, yellow furniture. What color are the stairs?", "There aren’t any"),
        ("What can you break, even if you never pick it up or touch it?", "Promise"),
        ("What goes up but never comes down?", "Age"),
    ],
    "General Knowledge": [
        ("What is the largest planet in our solar system?", "Jupiter"),
        ("What is the capital city of France?", "Paris"),
        ("Which element has the chemical symbol 'O'?", "Oxygen"),
        ("How many continents are there on Earth?", "Seven"),
        ("What is the smallest country in the world?", "Vatican City"),
        ("What is the hardest natural substance on Earth?", "Diamond"),
        ("Who wrote 'Hamlet'?", "William Shakespeare"),
        ("What is the main ingredient in guacamole?", "Avocado"),
        ("What is the capital of Australia?", "Canberra"),
        ("Which planet is known as the Red Planet?", "Mars"),
        ("Who painted the Mona Lisa?", "Leonardo da Vinci"),
        ("What is the longest river in the world?", "Nile"),
        ("Which ocean is the largest?", "Pacific"),
        ("What is the capital of Japan?", "Tokyo"),
        ("What is the smallest ocean in the world?", "Arctic"),
        ("What is the largest desert in the world?", "Sahara"),
        ("What is the tallest mountain in the world?", "Mount Everest"),
        ("Who is known as the father of computers?", "Charles Babbage"),
        ("What is the speed of light?", "299,792 km per second"),
        ("What is the currency of Japan?", "Yen"),
    ],
    "Historical Facts": [
        ("Who was the first President of the United States?", "George Washington"),
        ("In which year did the Titanic sink?", "1912"),
        ("Who discovered penicillin?", "Alexander Fleming"),
        ("Which ancient civilization built the Machu Picchu complex in Peru?", "Inca"),
        ("What year did the Berlin Wall fall?", "1989"),
        ("Who was the first person to walk on the moon?", "Neil Armstrong"),
        ("What was the name of the ship that brought the Pilgrims to America in 1620?", "Mayflower"),
        ("Who was the ancient Greek god of the sun?", "Apollo"),
        ("In which year did World War I begin?", "1914"),
        ("Who was the longest reigning British monarch?", "Queen Elizabeth II"),
        ("Which empire was known for having an efficient road system?", "Roman Empire"),
        ("Who was the leader of the Soviet Union during World War II?", "Joseph Stalin"),
        ("Which U.S. state was once an independent country?", "Texas"),
        ("In which year did the United States declare its independence?", "1776"),
        ("Who was the first female Prime Minister of India?", "Indira Gandhi"),
        ("What was the name of the last queen of France before the French Revolution?", "Marie Antoinette"),
        ("Who was the first emperor of China?", "Qin Shi Huang"),
        ("In which year did the United States land the first man on the moon?", "1969"),
        ("Who was the famous Egyptian queen who married Julius Caesar?", "Cleopatra"),
        ("What is the name of the first artificial Earth satellite launched by the Soviet Union in 1957?", "Sputnik"),
        ("Who was the German dictator during World War II?", "Adolf Hitler"),
        ("Who was the British Prime Minister during World War II?", "Winston Churchill"),
        ("Which ancient civilization is known for its pyramids?", "Egyptian"),
        ("What year did the American Civil War end?", "1865"),
        ("Who was the first female aviator to fly solo across the Atlantic Ocean?", "Amelia Earhart"),
    ]
}

class QuoteGuessingGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Quote and Riddle Guessing Game")
        self.master.configure(bg="#f0f0f0")
        self.score = 0
        self.high_score = 0
        self.time_limit = 30  # seconds
        self.time_remaining = self.time_limit
        self.hint_used = 0
        self.max_hints = 3
        self.asked_questions = set()

        self.frame = tk.Frame(self.master, bg="#f0f0f0")
        self.frame.pack(padx=20, pady=20)

        self.create_main_menu()

    def create_main_menu(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

        self.title_label = tk.Label(self.frame, text="Welcome to the Quote and Riddle Guessing Game!", font=("Helvetica", 24, "bold"), bg="#f0f0f0", fg="#333333")
        self.title_label.grid(row=0, columnspan=4, pady=20)

        self.category_label = tk.Label(self.frame, text="Choose a category to play:", font=("Helvetica", 18, "bold"), bg="#f0f0f0", fg="#333333")
        self.category_label.grid(row=1, columnspan=4, pady=10)

        self.quote_button = tk.Button(self.frame, text="Quotes", command=lambda: self.start_game("Quotes"), font=("Helvetica", 16, "bold"), bg="#4caf50", fg="white", padx=10, pady=5)
        self.quote_button.grid(row=2, column=0, padx=10, pady=10)

        self.riddle_button = tk.Button(self.frame, text="Riddles", command=lambda: self.start_game("Riddles"), font=("Helvetica", 16, "bold"), bg="#2196f3", fg="white", padx=10, pady=5)
        self.riddle_button.grid(row=2, column=1, padx=10, pady=10)

        self.general_knowledge_button = tk.Button(self.frame, text="General Knowledge", command=lambda: self.start_game("General Knowledge"), font=("Helvetica", 16, "bold"), bg="#ff9800", fg="white", padx=10, pady=5)
        self.general_knowledge_button.grid(row=2, column=2, padx=10, pady=10)

        self.historical_facts_button = tk.Button(self.frame, text="Historical Facts", command=lambda: self.start_game("Historical Facts"), font=("Helvetica", 16, "bold"), bg="#9c27b0", fg="white", padx=10, pady=5)
        self.historical_facts_button.grid(row=2, column=3, padx=10, pady=10)

    def start_game(self, category):
        self.selected_category = category
        self.asked_questions = set()
        self.time_remaining = self.time_limit
        self.score = 0
        self.create_game_widgets()
        self.new_question()
        self.update_timer()

    def create_game_widgets(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

        self.question_label = tk.Label(self.frame, text="", font=("Helvetica", 16, "bold"), wraplength=600, justify="center", bg="#f0f0f0", fg="#333333")
        self.question_label.grid(row=0, columnspan=3, pady=20)

        self.entry = tk.Entry(self.frame, font=("Helvetica", 16), justify="center")
        self.entry.grid(row=1, columnspan=3, pady=10, ipadx=10, ipady=5)

        self.check_button = tk.Button(self.frame, text="Check Answer", command=self.check_answer, font=("Helvetica", 14, "bold"), bg="#4caf50", fg="white", padx=10, pady=5)
        self.check_button.grid(row=2, column=0, pady=10)

        self.hint_button = tk.Button(self.frame, text="Hint", command=self.show_hint, font=("Helvetica", 14, "bold"), bg="#2196f3", fg="white", padx=10, pady=5)
        self.hint_button.grid(row=2, column=1, pady=10)

        self.new_question_button = tk.Button(self.frame, text="New Question", command=self.new_question, font=("Helvetica", 14, "bold"), bg="#ff9800", fg="white", padx=10, pady=5)
        self.new_question_button.grid(row=2, column=2, pady=10)

        self.result_label = tk.Label(self.frame, text="", font=("Helvetica", 16, "bold"), bg="#f0f0f0", fg="#333333")
        self.result_label.grid(row=3, columnspan=3, pady=10)

        self.score_label = tk.Label(self.frame, text=f"Score: {self.score}", font=("Helvetica", 16, "bold"), bg="#f0f0f0", fg="#333333")
        self.score_label.grid(row=4, column=0, pady=10, sticky='w')

        self.high_score_label = tk.Label(self.frame, text=f"High Score: {self.high_score}", font=("Helvetica", 16, "bold"), bg="#f0f0f0", fg="#333333")
        self.high_score_label.grid(row=4, column=2, pady=10, sticky='e')

        self.timer_label = tk.Label(self.frame, text=f"Time: {self.time_remaining}", font=("Helvetica", 16, "bold"), bg="#f0f0f0", fg="#333333")
        self.timer_label.grid(row=5, columnspan=3, pady=10)

        self.pause_button = tk.Button(self.frame, text="Pause", command=self.pause_timer, font=("Helvetica", 14, "bold"), bg="#f44336", fg="white", padx=10, pady=5)
        self.pause_button.grid(row=6, column=0, pady=10)

        self.resume_button = tk.Button(self.frame, text="Resume", command=self.resume_timer, font=("Helvetica", 14, "bold"), bg="#4caf50", fg="white", padx=10, pady=5)
        self.resume_button.grid(row=6, column=1, pady=10)

        self.restart_button = tk.Button(self.frame, text="Restart Game", command=self.restart_game, font=("Helvetica", 14, "bold"), bg="#9c27b0", fg="white", padx=10, pady=5)
        self.restart_button.grid(row=6, column=2, pady=10)

        self.home_button = tk.Button(self.frame, text="Home", command=self.create_main_menu, font=("Helvetica", 14, "bold"), bg="#ff9800", fg="white", padx=10, pady=5)
        self.home_button.grid(row=7, columnspan=3, pady=10)

    def display_question(self):
        self.question_label.config(text=self.question)
        self.entry.delete(0, tk.END)
        self.result_label.config(text="")
        self.hint_used = 0
        self.hint_positions = []

    def check_answer(self):
        user_answer = self.entry.get().strip().lower()
        if user_answer == self.answer.lower():
            self.result_label.config(text="Correct!", fg="green")
            self.score += 1
        else:
            self.result_label.config(text=f"Incorrect. The correct answer was {self.answer}.", fg="red")
        self.update_score()
        self.new_question()

    def new_question(self):
        if len(self.asked_questions) >= len(questions[self.selected_category]):
            messagebox.showinfo("Game Over", "No more questions available in this category.")
            return
        while True:
            self.question, self.answer = random.choice(questions[self.selected_category])
            if self.question not in self.asked_questions:
                break
        self.asked_questions.add(self.question)
        self.display_question()

    def show_hint(self):
        if self.hint_used < self.max_hints:
            available_positions = [i for i in range(len(self.answer)) if i not in self.hint_positions and self.answer[i].isalpha()]
            if available_positions:
                position = random.choice(available_positions)
                self.hint_positions.append(position)
                hint = self.answer[position]
                self.result_label.config(text=f"Hint: The letter at position {position+1} is '{hint}'.", fg="blue")
                self.hint_used += 1
            else:
                self.result_label.config(text="No more hints available.", fg="blue")
        else:
            self.result_label.config(text="Maximum number of hints used.", fg="blue")

    def update_score(self):
        self.score_label.config(text=f"Score: {self.score}")
        if self.score > self.high_score:
            self.high_score = self.score
            self.high_score_label.config(text=f"High Score: {self.high_score}")

    def update_timer(self):
        if self.time_remaining > 0 and not self.timer_paused:
            self.time_remaining -= 1
            self.timer_label.config(text=f"Time: {self.time_remaining}")
            self.master.after(1000, self.update_timer)
        elif self.time_remaining == 0:
            self.result_label.config(text="Time's up!", fg="red")
            self.check_button.config(state="disabled")
            self.hint_button.config(state="disabled")
            self.new_question_button.config(state="disabled")

    def pause_timer(self):
        self.timer_paused = True

    def resume_timer(self):
        self.timer_paused = False
        self.update_timer()

    def restart_game(self):
        self.score = 0
        self.time_remaining = self.time_limit
        self.asked_questions = set()
        self.update_score()
        self.start_game(self.selected_category)

def main():
    root = tk.Tk()
    game = QuoteGuessingGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
