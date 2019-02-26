import tkinter as tk
import tkinter.messagebox
import sqlite3

def insert_into_db(path_to_db_file, values):
    # povezi se na bazu preko putanje do datoteke u kojoj je spremljena baza
    # buduci da je sqlite baza onda je i tako jednostavno povezivanje preko datoteke
    connection = sqlite3.connect(path_to_db_file)

    # pomocu kursora se izvode naredbe za rad s bazom podataka
    cursor = connection.cursor()

    # naredba u kojoj se u tablicu Knjiga stavljaju odgovarajuce vrijednosti
    # upitnici ce se u pozadini zamijeniti s vrijednostima koje su definirane u values argumentu koji je poslan ovoj funkciji
    sql = "INSERT INTO Knjiga (naslov, autor, godinaIzdanja, izdavackaKuca, brojStranica) VALUES (?, ?, ?, ?, ?)"

    # izvrsava se naredba s predanim values, ali jos nije trajno pohranjena
    # mora se pozvati commit kako bi pohrana bila trajna
    cursor.execute(sql, values)

    # trajna pohrana promjena
    connection.commit()

    # (gotovo) uvijek nakon rada s bazom se zatvara konekcija
    connection.close()


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # ====================================== #
        # kreira se labela naslovLabel koja nema drugu funkcionalnost osim da se znaju razlikovati text boxovi
        # to vrijedi i za sve ostale labele
        self.naslovLabel = tk.Label(self, text="Naslov:")
        # svaka pack naredba s parametrom tk.X slaze komponente jednu ispod druge
        # to vrijedi za sve ostale .pack(fill=tk.X) naredbe
        self.naslovLabel.pack(fill=tk.X)
        # text box u koji se unosi vrijednost koja predstavlja naslov knjige
        # visina text boxa je postavljena na 2
        self.naslovTextBox = tk.Text(self, height=2)
        self.naslovTextBox.pack(fill=tk.X)
        # ====================================== #

        # ====================================== #
        self.autorLabel = tk.Label(self, text="Autor:")
        self.autorLabel.pack(fill=tk.X)
        self.autorTextBox = tk.Text(self, height=2)
        self.autorTextBox.pack(fill=tk.X)
        # ====================================== #

        # ====================================== #
        self.godinaIzdanjaLabel = tk.Label(self, text="Godina izdanja:")
        self.godinaIzdanjaLabel.pack(fill=tk.X)
        self.godinaIzdanjaTextBox = tk.Text(self, height=2)
        self.godinaIzdanjaTextBox.pack(fill=tk.X)
        # ====================================== #

        # ====================================== #
        self.izdavackaKucaLabel = tk.Label(self, text="Izdavacka kuca:")
        self.izdavackaKucaLabel.pack(fill=tk.X)
        self.izdavackaKucaTextBox = tk.Text(self, height=2)
        self.izdavackaKucaTextBox.pack(fill=tk.X)
        # ====================================== #

        # ====================================== #
        self.brojStranicaLabel = tk.Label(self, text="Broj stranica:")
        self.brojStranicaLabel.pack(fill=tk.X)
        self.brojStranicaTextBox = tk.Text(self, height=2)
        self.brojStranicaTextBox.pack(fill=tk.X)
        # ====================================== #

        # ====================================== #
        # gumb na ciji se pritisak podaci spremaju u bazu podataka
        self.insert = tk.Button(self, bg="green")
        self.insert["text"] = "Pohrani u bazu"
        # tu mu se predaje funkcija koja predstavlja njegovu funkcionalnost, odnosno spremanje podataka u bazu
        self.insert["command"] = self.insertButtonFunction
        self.insert.pack(fill=tk.X)

    # pomocna funkcija u kojoj se samo provjerava jesu li uneseni svi podaci
    def validateUserInput(self, naslov, autor, godinaIzdanja, izdavackaKuca, brojStranica):
        if naslov.strip() == "":
            tk.messagebox.showerror("Pogreska", "Naslov knjige mora biti zadan!")
            return False
        if autor.strip() == "":
            tk.messagebox.showerror("Pogreska", "Autor knjige mora biti zadan!")
            return False
        if godinaIzdanja.strip() == "":
            tk.messagebox.showerror("Pogreska", "Godina izdanja knjige mora biti zadana!")
            return False
        if izdavackaKuca.strip() == "":
            tk.messagebox.showerror("Pogreska", "Izdavacka kuca knjige mora biti zadana!")
            return False
        if brojStranica.strip() == "":
            tk.messagebox.showerror("Pogreska", "Broj stranica knjige mora biti zadan!")
            return False

        return True

    # funkcija koja izvlaci unesene podatke u poziva funkciju koja se spaja na bazu i sprema te podatke
    def insertButtonFunction(self):
        path_to_db = "MiniBaza.db"

        # ovaj dodatak "1.0", tk.END imas na ovom linku objasnjen: https://stackoverflow.com/questions/14824163/how-to-get-the-input-from-the-tkinter-text-box-widget
        naslov = self.naslovTextBox.get("1.0", tk.END)
        autor = self.autorTextBox.get("1.0", tk.END)
        godinaIzdanja = self.godinaIzdanjaTextBox.get("1.0", tk.END)
        izdavackaKuca = self.izdavackaKucaTextBox.get("1.0", tk.END)
        brojStranica = self.brojStranicaTextBox.get("1.0", tk.END)

        # ako input ne valja, ne spremaj u bazu
        if not self.validateUserInput(naslov, autor, godinaIzdanja, izdavackaKuca, brojStranica):
            return

        # input je prosao, podaci se mogu spremiti
        insert_into_db(path_to_db, (naslov, autor, godinaIzdanja, izdavackaKuca, brojStranica))

        tk.messagebox.showinfo("Info", "Knjiga je uspjesno pohranjena u bazu!")

root = tk.Tk()
root.minsize(width=200, height=200)
app = Application(master=root)
app.mainloop()