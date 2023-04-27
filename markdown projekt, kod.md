# Cantorov dijagonalni argument
**Autor:** *Dino Žagar i Lucia Labinjan*

**Sveučilište:** *Sveučilište Jurja Dobrile*

**Fakultet:** *Tehnički fakultet Pula, Fakultet informatike u Puli*

**Datum:** *26.6 2023*

## Sažetak
Georg Cantorov revolucionarni rad u teoriji skupova predstavio je svijetu koncept različitih veličina beskonačnosti. U središtu ovog otkrića nalazi se Cantorov dijagonalni argument, dokaz kontradikcijom koji pokazuje neizbrojivost skupa realnih brojeva. Ovaj projekt proučava složenosti Cantorovog dokaza, pružajući korak po korak objašnjenje argumenta i ističući njegovu važnost u razvoju suvremene matematike. Istražit ćemo osnovne koncepte teorije skupova, kardinaliteta, prebrojivih i neprebrojivih skupova te implikacije Cantorovog dijagonalnog argumenta na razne grane matematike kao što su analiza, topologija i temelji matematike. Nadalje, raspravljat ćemo o početnom prihvaćanju i kritikama Cantorovih ideja te njihovom dugotrajnom utjecaju na naše razumijevanje beskonačnosti. Projekt također povezuje Cantorov dijagonalni argument s povezanim konceptima i generalizacijama, kao što su Hilbertov hotel, problem zaustavljanja i Gödelovi teoremi o nepotpunosti, pokazujući svestranost dijagonalizacije kao matematičkog alata. Ovo sveobuhvatno istraživanje Cantorovog dijagonalnog argumenta nastoji razjasniti duboke uvide koje nudi u prirodu beskonačnosti i njegov trajni utjecaj na matematičku misao.


## Dijelovi projekta
- 1. [Uvod](#1)
- 2. [Osnovni koncepti](#2)
    - 2.1 [skupovi i kardinalnosti](#2.1)
    - 2.2 [ Prebrojivi i neprebrojivi skupovi ](#2.2)
    - 2.3 [Beskonačni skupovi i različite veličine beskonačnosti](#2.3)
- 3. [Cantorova dijagonalna argumentacija ](#3)
    - 3.1 [ Pretpostavke i postavljanje ](#3.1)
    - 3.2 [Teorem i dokaz ](#3.2)
- 4. [Primjene i posljedice ](#4)
    - 4.1 [Posljedice u teoriji skupova](#4.1)
    - 4.2 [Veze s analizom i topologijom ](#4.2)
    - 4.3 [Odnos s kontinuumskom hipotezom](#4.3)
- 5. [Kritike i kontroverze](#5)
    - 5.1 [Početni prijem Cantorovih ideja ](#5.1)
    - 5.2 [Kritike suvremenika](#5.2)
    - 5.3 [ Moderni pogledi na Cantorov rad](#5.3)
- 6. [Povezani koncepti i generalizacije ](#6)
    - 6.1. [ Hilbertov hotel i koncept beskonačnih skupova](#6.1)
    - 6.2. [Problem zaustavljanja i veze s računljivošću ](#6.2)
    - 6.3. [ Gödelove teoreme nepotpunosti i granice formalnih sustava](#6.3)
- 7. [Zaključak](#7)
- 8. [Kod](#8)
- 9. [Reference](#9)


## 1. Uvod
Georg Cantor, njemački matematičar rođen 1845. godine, dao je značajan doprinos matematici, posebno u teoriji skupova. Jedan od njegovih najinovativnijih rezultata bio je Cantorov dijagonalni argument, dokazivanje proturječjem koji je pokazao postojanje različitih veličina beskonačnosti. Dijagonalni argument pokazao je da je skup realnih brojeva neprebrojiv i stoga veći od skupa prirodnih brojeva. Ovo otkriće izazvalo je dugogodišnja uvjerenja o prirodi beskonačnosti i imalo duboke posljedice na različita područja matematike, uključujući analizu, topologiju i temelje matematike. Ovaj projekt ima za cilj istražiti Cantorov dijagonalni argument, njegove implikacije i veze s drugim matematičkim konceptima.


## 2.Osnovni koncepti 
### 2.1 skupovi i kardinalnosti 
U matematici, skup je zbir različitih objekata, često nazvanih elementima ili članovima. Skupovi su temeljni koncept u mnogim područjima matematike i osnova su za razumijevanje složenijih struktura. Veličina skupa naziva se kardinalitet skupa, što predstavlja broj elemenata u skupu. Na primjer, kardinalitet skupa {1, 2, 3} je 3, jer sadrži tri različita elementa.


### 2.2  Brojivi i nebrojivi skupovi 
Skupovi se mogu klasificirati u dvije kategorije na temelju njihovog kardinaliteta: prebrojivi i neprebrojivi skupovi. Prebrojivi skup je onaj koji se može staviti u jedan prema jedan odnos s prirodnim brojevima, što znači da je moguće stvoriti popis svih elemenata u skupu. Neprebrojivi skup, s druge strane, ne može se staviti u jedan prema jedan odnos s prirodnim brojevima, što implicira da je “veći” na neki način od prebrojivih skupova.

### 2.3 Beskonačni skupovi i različite veličine beskonačnosti 
Beskonačni skupovi su skupovi s neograničenim brojem elemenata. Iako su beskonačni, nije da   svi beskonačni skupovi imaju isti kardinalitet. Cantorov dijagonalni argument pokazuje da postoje različite veličine beskonačnosti, posebno uspoređivanjem kardinaliteta skupa prirodnih brojeva i skupa realnih brojeva. Skup prirodnih brojeva je prebrojivo beskonačan, dok je skup realnih brojeva neprebrojiv, što ukazuje na postojanje različitih veličina beskonačnosti.

## 3. Cantorov dijagonalni argument 
### 3.1   Pretpostavke i postavljanje 
Cantorov dijagonalni argument je dokaz proturječjem koji pokazuje neprebrojivost skupa realnih brojeva. Argument počinje pretpostavkom da je skup realnih brojeva prebrojiv, što implicira postojanje jedan-na-jedne korespondencije između skupa prirodnih brojeva i skupa realnih brojeva. Ova pretpostavka dovodi do stvaranja tablice koja nabraja sve realne brojeve, pri čemu svaki red sadrži decimalnu ekspanziju odgovarajućeg realnog broja. Konstruiranjem novog realnog broja “d” od dijagonalnih elemenata ove tablice i mijenjanjem svake znamenke, Cantorov dijagonalni argument dokazuje da je početna pretpostavka lažna, jer novi broj “d” nije na popisu, uspostavljajući prebrojivost skupa realnih brojeva.


### 3.2 Teorem i dokaz 
Teorem: Skup realnih brojeva je neprebrojiv, što znači da ne postoji jedan prema jedan odnos između skupa realnih brojeva i skupa prirodnih brojeva.
Dokaz:
Cantorov dijagonalni argument je dokaz proturječnosti. Pretpostavimo, radi argumenta, da je skup realnih brojeva između 0 i 1 sabrojiv. Ako bi to bilo istinito, mogli bismo sve realne brojeve u ovom rasponu navesti kao niz, pri čemu svaki broj odgovara jedinstvenom prirodnom broju:
1 -> r_1 = 0.a11 a12 a13 a14 …
 2 -> r_2 = 0.a21 a22 a23 a24 … 
3 -> r_3 = 0.a31 a32 a33 a34 … 
4 -> r_4 = 0.a41 a42 a43 a44 … 
…

Ovdje je svaki r_i realni broj između 0 i 1, a a_ij predstavlja j-tu decimalnu znamenku i-tog broja u nizu.
Sada ćemo konstruirati novi realni broj R tako da uzmemo dijagonalu liste i promijenimo svaku znamenku:
R = 0.b1 b2 b3 b4 …
gdje se b_i određuje prema:
b_i = a_ii + 1 ako a_ii nije 9 ,b_i = 0 ako je a_ii jednak 9

Konstrukcijom se R razlikuje od svakog broja u nizu barem za jednu znamenku. Drugim riječima, R nije jednak nijednom r_i u našem nizu. Budući da smo pretpostavili da naš niz sadrži sve realne brojeve između 0 i 1, došli smo do proturječnosti. To znači da je naša početna pretpostavka da je skup realnih brojeva između 0 i 1 sabrojiv netočna.
Stoga je skup realnih brojeva neprebrojiv.


## 4. Cantorov dijagonalni argument 
### 4.1  Posljedice u teoriji skupova
Cantorov dijagonalni argument imao je dubok utjecaj na teoriju skupova, jer je uspostavio postojanje različitih veličina beskonačnosti. Ovo otkriće dovelo je do razvoja naprednijih koncepata u teoriji skupova, poput pojma kardinalnih brojeva, koji se koriste za uspoređivanje veličine beskonačnih skupova.

### 4.2 Veze s analizom i topologijom 

Cantorove ideje također su imale posljedice u područjima analize i topologije. Na primjer, razumijevanje neprebrojivih skupova doprinijelo je razvoju Lebesgueove mjere i teorije integracije, koja proširuje klasičnu Riemannovu integraciju kako bi se rukovala širim nizom funkcija. U topologiji je koncept različitih veličina beskonačnosti utjecao na proučavanje svojstava kompaktnosti i povezanosti topoloških prostora.

### 4.3 Odnos s kontinuumskom hipotezom
Kontinuum hipoteza je blisko povezana s Cantorovim dijagonalnim argumentom. Hipoteza tvrdi da ne postoji skup s kardinalitetom strogo između prirodnih brojeva i realnih brojeva1. Iako dijagonalni argument dokazuje da je kardinalitet realnih brojeva veći od kardinaliteta prirodnih brojeva, on ne rješava Kontinuum hipotezu izravno. Hipoteza ostaje neovisna o standardnim aksiomima teorije skupova (Zermelo-Fraenkelova teorija skupova s aksiomom izbora), što su dokazali Kurt Gödel i Paul Cohen u 20. stoljeću


## 5. Kritike i kontroverze 
### 5.1  Početni prijem Cantorovih ideja 
Cantorove ideje o beskonačnim skupovima i dijagonalnom argumentu, koji su se prvi put pojavili krajem 19. stoljeća, suočili su se s miješanim prijemom. Dok su neki matematičari poput Davida Hilberta prihvatili i promovirali Cantorov rad, drugi su bili skeptični ili čak neprijateljski raspoloženi. Koncept različitih veličina beskonačnosti bio je kontroverzan jer je izazvao široko prihvaćeno uvjerenje da je beskonačnost jedinstveni i uniformni koncept. Mnogi matematičari su smatrali da je teško prihvatiti ove revolucionarne ideje, što je dovelo do rasprava i diskusija u matematičkoj zajednici.

### 5.2  Kritike suvremenika
Cantorov rad suočio se s nekoliko kritika od njegovih suvremenika. Jedan od značajnih kritičara bio je Leopold Kronecker, koji se protivio Cantorovim idejama jer su previše odstupale od konkretnih “konstruktivnih” matematika. Kronecker je vjerovao da bi matematika trebala biti temeljena na konačnom skupu objekata i operacija te je smatrao Cantorov rad kao odstupanje od ovog principa. Henri Poincaré, drugi poznati matematičar, nazvao je Cantorove ideje “bolest” od koje će se matematika na kraju oporaviti. Ove kritike potaknule su daljnje rasprave i kontroverze oko Cantorova rada.

### 5.3  Moderni pogledi na Cantorov rad
Cantorov rad o beskonačnim skupovima i dijagonalnom argumentu danas se široko priznaje kao temelj modernoj teoriji skupova i matematičkoj logici. Iako su kontroverze oko njegovog rada uglavnom utihnule, rasprave o filozofskim implikacijama njegovih ideja nastavljaju se. Neki matematičari tvrde da Cantorov rad ističe važnost istraživanja apstraktnih pojmova, dok drugi tvrde da bi se trebalo usredotočiti na konkretnu, konstruktivnu matematiku. Ipak, Cantorov rad sada se smatra neodvojivim dijelom matematičkog krajolika.

## 6. Povezani koncepti i generalizacije
### 6.1   Hilbertov hotel i koncept beskonačnih skupova
Hilbertov hotel je misaoni eksperiment koji je predložio David Hilbert kako bi ilustrirao kontraintuitivna svojstva beskonačnih skupova. Hotel ima beskonačan broj soba, svaka zauzeta gostom. Unatoč tome što je potpuno popunjen, hotel još uvijek može primiti nove goste tako što će svakog trenutnog gosta premjestiti u sobu s brojem dva puta većim od njihove trenutne sobe. To stvara beskonačan broj praznih soba s neparnim brojevima. Hilbertov hotel demonstrira paradoksalnu prirodu beskonačnih skupova i pojačava značaj Cantorovog rada.
![ilustracija paradoksa Hilbertov hotel](https://jpmacmanus.me/assets/images/blog/hilbert/hilbert-np1.png "Hilbertov hotel")
-Ova slika prikazuje sobe u hotelu. Svaki put kada novi gosti dođe, vlasnik hotela  treba organizirati da svi prijašnji gosti se presele u sobu s brojem većim za 1,  soba 1 je onda slobodna za novog gosta.
![ilustracija paradoksa Hilbertov hotel](https://jpmacmanus.me/assets/images/blog/hilbert/hilbert-2n.png "Hilbertov hotel")
Čak i za beskonačan broj novih gostiju, moguće je napraviti mjesta. Na primjer, neka svaki od starih gostiju koji su izvorno imali sobu s brojem n sada preseli u onu s brojem 2n, nakon čega beskonačan broj soba s neparnim brojevima postaje dostupan novim gostima.


### 6.2  Problem zaustavljanja i veze s računljivošću 

Halting problem je odlučivački problem u području teorije izračunljivosti, koji je formulirao Alan Turing 1936. godine. Pita se hoće li program nakon nekog vremena završiti ili nastaviti raditi beskonačno dugo, dajući opis proizvoljnog računalnog programa i ulaz. Turing je dokazao da nijedan opći algoritam ne može riješiti Halting Problem, utvrdivši granice izračunljivosti. Cantorov dijagonalni argument odigrao je ključnu ulogu u Turingovom dokazu, ističući dalekosežne implikacije Cantorovog rada izvan teorije skupova.

-Dano je računalni program i ulazni niz w, problem je odrediti hoće li program s vremenom zaustaviti kad se pokrene s ulazom w ili će se nastaviti izvoditi neograničeno2. U početku ćemo pretpostaviti da postoji takav Turingov stroj koji rješava ovaj problem, a zatim ćemo pokazati da se sam proturječi. Ovaj Turingov stroj nazivat ćemo Strojem za zaustavljanje koji proizvodi 'da' ili 'ne' u konačnom vremenu2. Ako stroj za zaustavljanje završi u konačnom vremenu, izlaz dolazi kao 'da', inače kao 'ne'. Slijedi blok dijagram Stroja za zaustavljanje 
![prikaz Halting machine](https://www.tutorialspoint.com/automata_theory/images/halting_machine.jpg  "Halting machine")
-Sada ćemo dizajnirati inverzni stroj za zaustavljanje (HM)' kao - Ako H vraća DA, tada se izvodi beskonačna petlja. Ako H vraća NE, tada zaustavi. Slijedi blok dijagram 'Inverznog stroja za zaustavljanje' 
![prikaz Halting machine](https://www.tutorialspoint.com/automata_theory/images/inverted_halting_machine.jpg "Halting machine")
 Nadalje, konstruira se stroj (HM)2 koji sam sebi daje ulaz kako slijedi - Ako (HM)2 zaustavi na ulazu, izvoditi beskonačnu petlju. Inače, zaustaviti se. Ovdje smo dobili proturječje. Dakle, problem zaustavljanja je nerazlučiv

### 6.3   Gödelove teoreme nepotpunosti i granice formalnih sustava 
Gödelovi teoremi nepotpunosti su dva temeljna rezultata u matematičkoj logici koje je dokazao Kurt Gödel 1931. godine i koji demonstriraju ograničenja formalnih aksiomatskih sustava. Teoremi tvrde da je svaki dovoljno moćan formalni sustav ili nepotpun (postoje istinite izjave koje se ne mogu dokazati unutar sustava) ili neusklađen (i izjava i njegova negacija mogu se dokazati unutar sustava). Gödelovi dokazi oslanjaju se na tehnike povezane s Cantorovim dijagonalnim argumentom, pokazujući širi utjecaj Cantorovog rada na naše razumijevanje ograničenja formalnih sustava u matematici




## 7. Zaključak
U zaključku, Cantorov dijagonalni argument je revolucionarni dokaz koji pokazuje postojanje različitih veličina beskonačnosti, pokazujući da je skup realnih brojeva neprebrojiv i veći od skupa prirodnih brojeva. Argument koristi dokazivanje proturječjem otkrivajući da je nemoguće uspostaviti jedan-na-jedan odnos između skupa realnih brojeva i skupa prirodnih brojeva.Cantorov dijagonalni argument imao je trajni utjecaj na matematiku oblikujući naše razumijevanje beskonačnih skupova i njihovih kardinalnosti. Dokaz je utjecao na različita područja matematike, uključujući teoriju skupova, analizu, topologiju i temelje matematike.Kako nastavljamo istraživati prirodu beskonačnosti i implikacije Cantorovog dijagonalnog argumenta, pojavljuju se novi smjerovi i otvorena pitanja. Na primjer, hipoteza kontinuuma ostaje nedeterminirana unutar standardnog okvira teorije skupova, predstavljajući stalni izazov za matematičare. Nadalje, veze dokaza s računalnošću i granicama formalnih sustava nastavljaju inspirirati istraživače, potičući interdisciplinarno istraživanje i razvoj novih matematičkih koncepata.

## 8. Kod

Ovaj kod generira popis n slučajnih decimala, svaka s 10 znamenki. Zatim primjenjuje Cantorov dijagonalni argument za konstrukciju novog decimalnog broja koji se razlikuje od svih decimala na popisu. Izlaz pokazuje da je novi decimalni broj zaista različit od svih decimala na popisu i ilustrira koncept Cantorovog dijagonalnog argumenta.
``` python
import random


def generate_random_decimal(digits=10):
    return [random.randint(0, 9) for _ in range(digits)]


def create_list_of_decimals(n, digits=10):
    decimals = [generate_random_decimal(digits) for _ in range(n)]
    return decimals


def cantors_diagonal_argument(decimals):
    diagonal = [decimals[i][i] for i in range(len(decimals))]
    new_number = [(digit + 1) % 10 for digit in diagonal]
    return new_number


def main():
    n = 10
    decimals = create_list_of_decimals(n)

    print("List of decimals:")
    for decimal in decimals:
        print(f"0.{''.join(map(str, decimal))}")

    new_decimal = cantors_diagonal_argument(decimals)
    print(f"\nNew decimal constructed using Cantor's Diagonal Argument: 0.{''.join(map(str, new_decimal))}")


if __name__ == "__main__":
    main()
```
## 9. Reference
1.1 https://www.maa.org/sites/default/files/pdf/upload_library/22/Ford/Gray819-832.pdf
1.2 https://books.google.hr/books?id=wEj3Spept0AC&pg=PA20&redir_esc=y#v=onepage&q&f=false
1.3 https://jlmartin.ku.edu/courses/math410-S09/cantor.pdf
1.4 Uvod u teoriju skupova – Pavle Papić

slike
 2.1 https://jpmacmanus.me/assets/images/blog/hilbert/hilbert-np1.png- prikaz Hilbertov hotel paradox
2.2  https://jpmacmanus.me/assets/images/blog/hilbert/hilbert-2n.png - prikaz Hilbertov hotel paradox
2.3 https://www.tutorialspoint.com/automata_theory/images/halting_machine.jpg - prikaz Halting machine
2.4 https://www.tutorialspoint.com/automata_theory/images/inverted_halting_machine.jpg- prikaz obrnute Halting 






  









