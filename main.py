from tkinter import *
from tkinter import messagebox
from pickwords import Pick_word

BACKGROUND_COLOR = "#B1DDC6"


class FlashcardApp:
    def __init__(self, window):
        self.pkword= Pick_word()
        self.window = window
        self.window.title("Flashcard App")
        self.window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)



        # 设置窗口大小
        # self.window.geometry("800x400")

        self.flip_timer = self.window.after(3000,func=self.flip_card)

        self.canvas = Canvas(width=800, height=526)
        self.card_front_img = PhotoImage(file="images/card_front.png")
        self.card_back_ing = PhotoImage(file="images/card_back.png")
        # self.logo_img = PhotoImage(file="images/card_front.png")
        self.card_background = self.canvas.create_image(400, 263, image=self.card_front_img)
        # 创建文本并保存它们的ID
        self.title = self.canvas.create_text(400,150,text="Title",font=("Ariel",40,"italic"))
        self.word = self.canvas.create_text(400, 265, text="word", font=("Ariel", 60, "bold"))

        self.canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
        self.canvas.grid(column=1, row=0, columnspan=2)

        # 创建按钮
        self.known_image = PhotoImage(file="images/right.png")
        self.known_button = Button(window, image=self.known_image,text="认识, highlightthickness=0",command=self.pickword)
        self.known_button.grid(column=1, row=1)

        self.forget_image = PhotoImage(file="images/wrong.png")
        self.forget_button = Button(image=self.forget_image,text="aa", highlightthickness=0,command=self.pickword)
        self.forget_button.grid(column=2, row=1)
        self.pickword()

    def pickword(self):
        self.window.after_cancel(self.flip_timer)
        self.word_fr, self.word_en=self.pkword.pick_random_word()
        self.canvas.itemconfig(self.card_background, image=self.card_front_img)
        self.canvas.itemconfig(self.word,text=self.word_en,fill="black")
        self.canvas.itemconfig(self.title,text="English",fill="black")
        self.window.after(3000, func=self.flip_card)

    def flip_card(self):

        self.canvas.itemconfig(self.title,text="Franch",fill="white")
        self.canvas.itemconfig(self.word,text=self.word_fr,fill="white")
        self.canvas.itemconfig(self.card_background,image=self.card_back_ing)



if __name__ == "__main__":
    window = Tk()
    app = FlashcardApp(window)
    window.mainloop()
