from tkinter import StringVar , Text , Frame ,messagebox , WORD , END , NORMAL , DISABLED , CENTER
from tkinter.ttk import Button , OptionMenu
from ttkthemes import ThemedTk
import pyperclip
import UnlimitedAutoTranslate as auto


DARK_0 = "#222"
DARK_1 = "#333"
DARK_2 = "#444"
WHITE_1 = "#fff"
WHITE_2 = "#ddd"


# Write the languages you want to translate to
LANGUAGES = ("amharic", "english", "french", "oromo", "tigrinya")


class translator(ThemedTk):
    def __init__(self):
        super().__init__(theme="black")
        self.geometry("300x575")
        self.title("Translator")
        self.resizable(False, False)
        self["bg"] = DARK_1

        self.option_var = StringVar()
        self.textbox = Text(
            self,
            height=10,
            width=30,
            font=("Cascadia Mono", 12),
            background=DARK_2,
            foreground=WHITE_1,
            borderwidth=1,
            wrap=WORD,
            insertbackground="white",
        )

        self.result = Text(
            self,
            height=10,
            width=30,
            font=("Cascadia Mono", 12),
            state=DISABLED,
            background=DARK_2,
            foreground=WHITE_2,
            borderwidth=1,
            wrap=WORD,
        )

        self.grid = Frame(self)
        self.grid["bg"] = self["bg"]

        self.outLang = OptionMenu(
            self.grid, self.option_var, LANGUAGES[0], *LANGUAGES
        )

        self.translatebutton = Button(
            self.grid, text="Translate", width=15, command=self.translate
        )

        self.copybutton = Button(
            self.grid, text="Copy", width=15, command=self.copy_text
        )

        self.aboutbutton = Button(
            self.grid, text="About", width=15, command=self.about
        )

        self.outLang.grid(row=0, column=1, padx=10, pady=10)
        self.translatebutton.grid(row=0, column=0, padx=10, pady=10)

        self.aboutbutton.grid(row=1, column=1, padx=10, pady=10)
        self.copybutton.grid(row=1, column=0, padx=10, pady=0)

        self.textbox.place(relx=0.5, rely=0.22, anchor=CENTER)
        self.result.place(relx=0.5, rely=0.66, anchor=CENTER)

        self.grid.place(relx=0.5, rely=0.925, anchor=CENTER)

        self.bind("<Control-Return>", lambda event: self.translate())

    def copy_text(self):
        if self.result.get("1.0", END):
            pyperclip.copy(self.result.get("1.0", END))

    def about(self):
        messagebox.showinfo(
            title="About",
            message="""\
        Translator 1.0
        Made by Bigg Smoke
        Original code forked from: BaseMax/UnlimitedAutoTranslate:main
        (C) 2016/24
        """,
        )

    def translate(self):
        text = str(self.textbox.get("1.0", END)).strip()
        option = self.option_var.get()
        self.title("Translating...")
        self.result.configure(state=NORMAL)
        self.result.delete("1.0", "end-1c")

        try:
            self.result.insert("1.0", auto.translate(text, None, option))
            self.result.configure(state=DISABLED)
        except Exception as e:
            messagebox.showerror(title="Error", message=e)

        self.title("Translator")


if __name__ == "__main__":
    app = translator()
    app.mainloop()

# end main
