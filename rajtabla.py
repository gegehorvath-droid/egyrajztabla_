import tkinter as tk
import random


class RajzApp:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Egyszerű Rajztábla")

        self.aktualis_szin = "black"

        self.elozo_x = None
        self.elozo_y = None

        self._felulet_letrehozas()
        self._esemenyek_hozzaadasa()

    def _felulet_letrehozas(self):
        self.canvas = tk.Canvas(self.root, width=600, height=400, bg="white")
        self.canvas.pack()

        gomb_frame = tk.Frame(self.root)
        gomb_frame.pack(pady=5)

        self.fekete_gomb = tk.Button(
            gomb_frame, text="Fekete", command=lambda: self.szin_valtas("black")
        )
        self.fekete_gomb.pack(side=tk.LEFT, padx=2)

        self.piros_gomb = tk.Button(
            gomb_frame, text="Piros", command=lambda: self.szin_valtas("red")
        )
        self.piros_gomb.pack(side=tk.LEFT, padx=2)

        self.kek_gomb = tk.Button(
            gomb_frame, text="Kék", command=lambda: self.szin_valtas("blue")
        )
        self.kek_gomb.pack(side=tk.LEFT, padx=2)

        self.veletlen_gomb = tk.Button(
            gomb_frame, text="Véletlen szín", command=self.veletlen_szin
        )
        self.veletlen_gomb.pack(side=tk.LEFT, padx=2)

        self.torles_gomb = tk.Button(
            gomb_frame, text="Törlés", command=self.vaszon_torles
        )
        self.torles_gomb.pack(side=tk.LEFT, padx=2)

    def _esemenyek_hozzaadasa(self):
        self.canvas.bind("<Button-1>", self.egerkattintas)

        self.canvas.bind("<B1-Motion>", self.egermozgas)

        self.canvas.bind("<ButtonRelease-1>", self.eger_fel)

    def szin_valtas(self, uj_szin: str):
        self.aktualis_szin = uj_szin

    def veletlen_szin(self):
        szinek = ["red", "blue", "green", "black", "purple", "orange"]
        self.aktualis_szin = random.choice(szinek)

    def vaszon_torles(self):
        self.canvas.delete("all")

    def egerkattintas(self, event):
        self.elozo_x = event.x
        self.elozo_y = event.y

    def egermozgas(self, event):
        if self.elozo_x is not None and self.elozo_y is not None:
            self.canvas.create_line(
                self.elozo_x,
                self.elozo_y,
                event.x,
                event.y,
                fill=self.aktualis_szin,
                width=3
            )

        self.elozo_x = event.x
        self.elozo_y = event.y

    def eger_fel(self, event):
        self.elozo_x = None
        self.elozo_y = None

    def run(self):
        self.root.mainloop()
