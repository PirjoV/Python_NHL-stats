#Python-kurssin olioharjoitus NHL-tilastoilla
#tiedosto kaikki.json - hakua alkaa suorittamalla tiedosto

import json

#tarvitaan
#class Tiedostonkäsittelijä, joka avaa json-tiedoston ja palauttaa sanakirjan
#class Tilastopaketti, josta haetaan ja lisätään pelaajiin liittyviä tietoja
#class Pelaaja
# class Tilastosovellus, sisältää ohje- ja suorita, haku, lisäys,  

class Tilastosovellus:
    def __init__(self):
        self.tilasto = Tilastopaketti()

    def ohje(self):
        print("komennot: ")
        print("0 lopeta")
        print("1 hae pelaaja")
        print("2 joukkueet")
        print("3 maat")
        print("4 joukkueen pelaajat")
        print("5 maan pelaajat")
        print("6 eniten pisteitä")
        print("7 eniten maaleja")
       


    def suorita(self):
        self.ohje()
        while True:
            print("")
            komento = input("komento: ")
            if komento == "0":
                break
            elif komento =="1":
                self.hae_pelaaja()
            elif komento =="2":
                self.hae_joukkueet()

            elif komento == "3":
                self.hae_maat()

            elif komento == "4":
                self.hae_joukkueen_pelaajat()

            elif komento == "5":
                self.hae_maan_pelaajat()

            elif komento == "6":
                self.hae_pisteet()

            elif komento == "7":
                self.maalimaarat()

           

    def hae_pelaaja(self):
        self.tilasto.hae_tiedot()

    def hae_joukkueet(self):
        joukkueet=sorted(set(self.tilasto.hae_joukkue_lyhenteet()))

        for joukkue in joukkueet:
            print(joukkue)

    def hae_maat(self):
        maat = sorted(set(self.tilasto.hae_maat()))
        for maa in maat:
            print(maa)
        
    def hae_joukkueen_pelaajat(self):
        pelaajat = self.tilasto.hae_joukkueen_pelaajat()
        lisat = ["+", "="]
        for pelaaja in pelaajat:

            print(f"{pelaaja['nimi']:21}{pelaaja['joukkue']:3}{pelaaja['maalit']:>4}{lisat[0]:>2}{pelaaja['syotot']:>3}{lisat[1]:>2}{pelaaja['maalit']+pelaaja['syotot']:>4}")
            #f"{self.name:21} {self.team:3} {self.goals:>4} +{self.assists:>3} ={self.hae_pisteet():>4}"
        
    def hae_maan_pelaajat(self):
        pelaajat = self.tilasto.hae_maan_pelaajat()
        lisat = ["+", "="]

        for pelaaja in pelaajat:
            print(f"{pelaaja['nimi']:21}{pelaaja['joukkue']:3}{pelaaja['maalit']:>4}{lisat[0]:>2}{pelaaja['syotot']:>3}{lisat[1]:>2}{pelaaja['maalit']+pelaaja['syotot']:>4}")
    def hae_pisteet(self):
        montako = int(input("kuinka monta: "))
        pistejarjestys = self.tilasto.jarjesta_pisteiden_mukaan()
        i = 0
        lisat = ["+", "="]

        while i < montako:
            pelaaja = pistejarjestys[i]
            print(f"{pelaaja['nimi']:21}{pelaaja['joukkue']:3}{pelaaja['maalit']:>4}{lisat[0]:>2}{pelaaja['syotot']:>3}{lisat[1]:>2}{pelaaja['maalit']+pelaaja['syotot']:>4}")

            i+=1


    def maalimaarat(self):
        montako = int(input("kuinka monta: "))
        maalijarjestys = self.tilasto.jarjesta_maalien_mukaan()
        i = 0
        lisat = ["+", "="]

        while i < montako:
            pelaaja = maalijarjestys[i]

            print(f"{pelaaja['nimi']:21}{pelaaja['joukkue']:3}{pelaaja['maalit']:>4}{lisat[0]:>2}{pelaaja['syotot']:>3}{lisat[1]:>2}{pelaaja['maalit']+pelaaja['syotot']:>4}")
            i+=1

class Tilastopaketti:
    def __init__(self):
        self.pelaajat = {}
        self.pelaajalista = []
        self.lue_tilastot()

    def lue_tilastot(self):
        #tiedosto = input("tiedosto: ")
        #with open("tiedosto") as tiedosto:
        with open("kaikki.json") as tiedosto:
            data = tiedosto.read()
            tilastot = json.loads(data)
            #print(tilastot)
        #tilastot = pelurit
        for i in range(len(tilastot)):
            
            pelaaja_listaan = {"nimi": tilastot[i]["name"], "maa": tilastot[i]["nationality"], "syotot": tilastot[i]["assists"], "maalit": tilastot[i]["goals"], "jaahyt": tilastot[i]["penalties"], "joukkue": tilastot[i]["team"], "ottelut": tilastot[i]["games"]}
            self.pelaajalista.append(pelaaja_listaan)
            pelaaja = Pelaaja(tilastot[i]["name"], tilastot[i]["nationality"], tilastot[i]["assists"], tilastot[i]["goals"], tilastot[i]["penalties"], tilastot[i]["team"], tilastot[i]["games"])
            self.pelaajat[tilastot[i]["name"]] = pelaaja
        print()
        print(f"luettiin {len(tilastot)} pelaajan tiedot")

    def hae_joukkue_lyhenteet(self):
        pelaajat = self.pelaajalista
        joukkueet = []
        for pelaaja in pelaajat:
            #print(pelaaja["joukkue"], "j")
            joukkueet.append(pelaaja["joukkue"])
        #return joukkueet
        #print(sorted(set(joukkueet)))
        return joukkueet
    
    def hae_maat(self):
        pelaajat = self.pelaajalista
        maat = []
        for pelaaja in pelaajat:
            maat.append(pelaaja["maa"])

        return maat

    def hae_joukkueen_pelaajat(self):
        joukkue = input("joukkue: ")
        joukkueen_pelaajat = []
        for pelaaja in self.pelaajalista:
            if pelaaja["joukkue"] == joukkue:
                joukkueen_pelaajat.append(pelaaja)
        #tehdään tähän sama sorttausfunktio kuin järjestä maalien mukaan
        def pistejarjestys(alkio:dict):
            return (alkio["maalit"] + alkio["syotot"], alkio["maalit"])

        return sorted(joukkueen_pelaajat, key=pistejarjestys, reverse= True)

        #return joukkueen_pelaajat

    def hae_maan_pelaajat(self):
        maa = input("maa: ")
        maan_pelaajat = []
        for pelaaja in self.pelaajalista:
            if pelaaja["maa"] == maa:
                maan_pelaajat.append(pelaaja)

        def pistejarjestys(alkio:dict):
            return (alkio["maalit"] + alkio["syotot"], alkio["maalit"])
        return sorted(maan_pelaajat, key=pistejarjestys, reverse=True)



    def hae_tiedot(self):
        nimi = input("nimi: ")
        name = self.pelaajat[nimi]
        print(name)
        return name   

    def jarjesta_pisteiden_mukaan(self):
        pelaajat = self.pelaajalista
        def pistejarjestys(alkio:dict):
            return (alkio["maalit"] + alkio["syotot"], alkio["maalit"])
        return sorted(pelaajat, key=pistejarjestys, reverse=True)
        
    def jarjesta_maalien_mukaan(self):
        pelaajat = self.pelaajalista
        def maalijarjestys(alkio:dict):
            return (alkio["maalit"], -alkio["ottelut"])
        return sorted(pelaajat, key=maalijarjestys, reverse=True)
    
        #def kausi_jarjestys(alkio:dict):
            #return alkio["kausia"]

        #return sorted(alkiot, key=kausi_jarjestys)
        #käydään jokainen rivi läpi ja luodaan pelaaja-olioita tiedoista

class Pelaaja:
    def __init__(self, name:str, nationality:str, assists:int, goals:int, penalties:int, team:str, games:int):
        self.name = name
        self.nationality = nationality
        self.assists = assists
        self.goals = goals
        self.penalties = penalties
        self.team = team
        self.games = games

    def hae_syotot(self):
        return self.assists

    def hae_maalit(self):
        return self.goals

    def hae_pisteet(self):
        return (self.goals + self.assists)

    def hae_joukkue(self):
        return self.team

    def __str__(self):
        lisat = ["+", "="]
        return f"{self.name:21}{self.team:3}{self.goals:>4}{lisat[0]:>2}{self.assists:>3}{lisat[1]:>2}{self.hae_pisteet():>4}"
        


sovellus = Tilastosovellus()
sovellus.suorita()
