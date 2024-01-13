# TRANSLATORGUI (SUN VALLEY EDITION)

from tkinter import (
    Tk,
    StringVar,
    Text,
    LabelFrame,
    Label,
    HORIZONTAL,
    WORD,
    DISABLED,
    CENTER,
    END,
    NORMAL,
)
import UnlimitedAutoTranslate as auto
from tkinter import messagebox
import tkinter.ttk as ttk
import threading
import pyperclip
import sv_ttk


# H = 0x0067C0  # MAGIC NUMBER THAT DOES NOTHING
LANGUAGES = (
    "amharic",
    "english",
    "oromo",
    "tigrinya",
    "french",
    "spanish",
)  # add more languages you want i got lazy


THEMES = ("dark", "light")  # we need a vaporwave windows11 theme


# fonts
FONT_12 = ("Consolas", 13)
FONT_10 = ("Consolas", 11)
FONT_8 = ("Consolas", 9)


class translator(Tk):
    # CLASS CLASS CLASS F*CKING CLASSES!!!
    def __init__(self):
        super().__init__()
        self.geometry("675x575")  # pretty big
        self.title("T.L.S. Translator")
        self.resizable(False, False)  # NO WAY I'M GOING TO LET THIS THING GO FULLSCREEN
        self.style = ttk.Style(self)
        self.iconbitmap("./icon.ico")

        self.option_var = StringVar()
        self.theme_var = StringVar()

        self.input_box = Text(
            self,
            height=10,
            width=30,
            wrap=WORD,
            font=FONT_12,
            highlightbackground="#0067c0",
            highlightcolor="#0067c0",
        )

        self.result_box = Text(
            self,
            height=10,
            width=30,
            state=DISABLED,
            wrap=WORD,
            font=FONT_12,
        )

        self.control_grid = LabelFrame(
            self,
            text="Translate Options",
            font=FONT_10,
            fg="#aaaaaa",  # THE AIRPLAINE IS COMING
        )

        self.settings_grid = LabelFrame(
            self, text="Settings", font=FONT_10, fg="#aaaaaa"
        )

        self.language_perf = ttk.OptionMenu(
            self.control_grid,
            self.option_var,
            LANGUAGES[0],
            *LANGUAGES,
        )

        self.translatebutton = ttk.Button(
            self.control_grid,
            text="Translate",
            width=10,
            command=lambda: threading.Thread(
                target=self.translate,
                name="GET_THREAD",  # Threads are really cool stuff. no more being stuck unresponsive
            ).start(),
        )

        self.copybutton = ttk.Button(
            self.settings_grid, text="Copy", width=10, command=self.copy_text
        )

        self.aboutbutton = ttk.Button(
            self.settings_grid, text="About", width=10, command=self.about
        )

        self.theme_perf = ttk.OptionMenu(
            self.settings_grid,
            self.theme_var,
            "dark",
            *THEMES,
            command=self.change_theme,
        )

        #  I HATE THIS
        # WHY WON'T SOMEONE MAKE A CSS-LIKE STYLE DECLARATION FOR DESKTOP APPS?!
        #  I DON'T WANT TO LEARN QT JUST PLEASE PLEASE SOMEONE ANYONE!!!
        # F*CK PYTHON EEL IT'S GRABAGE I CAN'T CALL A JS FUNCTION FROM PYTHON
        # I HAVE TO INVOKE IT USING AN EVENT HANDLER IN THE HTML WHICH IS A LOT OF BUTTONS

        # anyway...

        self.language_perf.grid(row=0, column=0, padx=15, pady=15)
        self.translatebutton.grid(row=0, column=1, padx=15, pady=15)
        self.copybutton.grid(row=0, column=0, padx=15, pady=15)
        self.aboutbutton.grid(row=0, column=1, padx=15, pady=15)
        self.theme_perf.grid(row=1, column=1, padx=0, pady=15)
        self.input_box.place(relx=0.25, rely=0.22, anchor=CENTER)
        self.result_box.place(relx=0.25, rely=0.66, anchor=CENTER)
        self.control_grid.place(relx=0.7, rely=0.12, anchor=CENTER)
        self.settings_grid.place(relx=0.7, rely=0.32, anchor=CENTER)
        self.about_frame = LabelFrame(self, text="About", font=FONT_10, fg="#aaaaaa")
        Label(self.settings_grid, font=FONT_12, text="Theme: ").place(
            relx=0.475, rely=0.735, anchor=CENTER
        )

        self.lable = Label(
            self.about_frame,
            text="Translator Version 2.0\nMade by The Sundowner\nPublished by The Lunar Surface\n\nTranslator Module code from:\n BaseMax/UnlimitedAutoTranslate:main ",
            font=FONT_10,
            fg="#aaaaaa",
        )
        self.lable.pack()

        # self.loading_diag = None     // unsued variable

        sv_ttk.set_theme("dark")
        self.style.configure("TButton", font=FONT_10)

        self.bind(
            "<Control-Return>",
            lambda event: threading.Thread(
                target=self.translate,
                name="GET_THREAD",
            ).start(),
        )

    # Cool Windows 11 rendition for a 30-year old framework
    def change_theme(self, event):
        theme = self.theme_var.get()
        if theme == "light":
            self.lable.configure(fg="#000")
        else:
            self.lable.configure(fg="#aaaaaa")  # THE AIRPLANE

        return sv_ttk.set_theme(theme)

    def about(self):
        self.about_frame.place(relx=0.7, rely=0.720, anchor=CENTER)

    # THIS IS WHERE THE REAL WORK HAPPENS
    def translate(self):
        try:
            self.pb = ttk.Progressbar(
                self, orient=HORIZONTAL, mode="indeterminate", length=250
            )
            self.pb.place(relx=0.25, rely=0.66, anchor=CENTER)
            self.pb.start()
            text = str(self.input_box.get("1.0", END)).strip()
            option = self.option_var.get()
            self.title("Translating...")
            self.result_box.configure(state=NORMAL)
            self.result_box.delete("1.0", "end-1c")
            self.result_box.insert("1.0", auto.translate(text, None, option))
            self.result_box.configure(state=DISABLED)
            self.pb.destroy()
            self.title("T.L.S. Translator")
        except Exception as e:
            self.pb.destroy()
            self.result_box.configure(state=DISABLED)
            self.title("T.L.S. Translator")
            messagebox.showerror(title="Error", message=e)

    def copy_text(self):
        if self.result_box.get("1.0", END):
            pyperclip.copy(self.result_box.get("1.0", END))


if (
    __name__ == "__main__"
):  # Python has a weird way of addressing main functions. like wtf is __name__?
    translator().mainloop()
# end main
