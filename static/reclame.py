from algemene_functies import mijn_functie_2

def aanbieding_1(smaak, prijs, korting):
    aanbieding_prijs = prijs * (1 - korting)
    return f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {aanbieding_prijs:.2f} euro."

print(aanbieding_1("aardbei", 4, 0.1))

def inkomsten_totaal(inkomsten, btw):
    totaal = sum(inkomsten)
    btw_bedrag = totaal * btw
    return f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {btw_bedrag:.2f} euro btw betaald dient te worden."

inkomsten_per_week = [220, 430, 125, 160, 205, 90, 345]
btw_percentage = 0.09

print(inkomsten_totaal(inkomsten_per_week, btw_percentage))

def laag_en_hoog(mijn_lijst):
    laagste = min(mijn_lijst)
    hoogste = max(mijn_lijst)
    return [laagste, hoogste]

resultaat = laag_en_hoog(inkomsten_per_week)
print(resultaat)

def gemiddelde(mijn_lijst):
    gemiddeld_bedrag = sum(mijn_lijst) / len(mijn_lijst)
    return f"De gemiddelde inkomsten deze week zijn {gemiddeld_bedrag:.2f} euro."

print(gemiddelde(inkomsten_per_week))

def meervoudig(invoer_lijst):
    return laag_en_hoog(invoer_lijst)

mijn_lijst = [10, 5, 3, 2, 1, 2, 9]
resultaat = meervoudig(mijn_lijst)
print(resultaat)


def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    return mijn_functie_2(korte_lijst[0])

resultaat = combinatie(inkomsten_per_week)
print(resultaat)