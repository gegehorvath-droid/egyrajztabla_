# Egy rajztábla

## Készítő neve
Név: Horváth Gergő  
Neptun kód: JKFHTS

## Feladat rövid leírása
Az egérrel lehet a vászonra rajzolni, a színt gombokkal lehet váltani, a vászon törölhető, és véletlen szín is választható.

## Fájlok és modulok

- `main.py`  
  - A program indító modulja.
  - Fő feladata: a `RajzApp` példányosítása és futtatása.

- `rajztabla.py`  
  - Saját modul.
  - Tartalmazza a `RajzApp` osztályt és a rajzoláshoz kapcsolódó függvényeket.

## Használt modulok

- **Beépített / tanult modulok:**
  - `tkinter` – grafikus felület:
    - `Tk()` – főablak létrehozása
    - `Canvas` – rajzfelület
    - `Button` – gombok
    - `Frame` – gombok csoportosítása
    - `bind()` – eseménykezelés
    - `mainloop()` – eseménykezelő ciklus

  - `random` – véletlen szín kiválasztása:
    - `random.choice(lista)`

- **Saját modul:**
  - `rajztabla`:
    - Osztály: `RajzApp`
    - Függvények / metódusok:
      - `__init__(self)`
      - `_felulet_letrehozas(self)`
      - `_esemenyek_hozzaadasa(self)`
      - `szin_valtas(self, uj_szin)`
      - `veletlen_szin(self)`
      - `vaszon_torles(self)`
      - `egerkattintas(self, event)`
      - `egermozgas(self, event)`
      - `eger_fel(self, event)`
      - `run(self)`

**Működés röviden:**

A program a main.py fájlból indul (app = RajzApp()).
A RajzApp létrehozza a főablakot (root) és a grafikus elemeket, az egér mozgatásával a felhasználó rajzolhat.

**A gombok:**
      - `színváltás`
      - `véletlenszín`
      - `teljes törlés`
      
Az **eseménykezelések** `canvas.bind()`-del vannak hozzárendelve.
