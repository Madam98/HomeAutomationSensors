# Opis projektu na przedmiot "Systemy wbudowane"

Poniżej znajduje się pełny wstępny opis założeń, wykonania oraz przygotowania się do projektu.



#### Opis koncepcji projektu

Głównym założeniem projektu jest zbudowanie urządzenia dla użytkownika, które będzie spełniać najważniejsze funkcje potrzebne do monitorowania swojego mieszkania. Urządzenie *(wymyśleć nazwę projektu dla picu np. Spyjek albo ZabezpieczoCzujnikoDominator)* monitorować będzie kilka czynników zmieniających się w środowisku:

- monitorowanie temperatury i wilgotności w mieszkaniu (potrzebny czujnik temperatury i wilgotności - zdecydować czy decydujemy się na czujnik analogowy czy też cyfrowy. Wybór na dziś https://botland.com.pl/czujniki-multifunkcyjne/9301-czujnik-temperatury-i-wilgotnosci-dht11-60c.html, koszt 10zł)
- monitorowanie dymu i czadu w pomieszczeniu (potrzebny czujnik czadu - https://botland.com.pl/czujniki-gazow/3027-czujnik-dymu-i-latwopalnych-gazow-mq-2-polprzewodnikowy-modul-niebieski-5904422303693.html)
- monitorowanie czy nowa osoba nie weszła do pomieszczenia (potrzebna kamera, z tego względu, że fajnie, by było aby nasze urządzenie działało w ciemnych pomieszczeniach, 24h na dobę najlepiej będzie wybrać kamerę tą: Kamera HD Night Vision E OV5647 5Mpx - dla Raspberry Pi + moduły IR - Waveshare 10300 https://botland.com.pl/kamery-do-raspberry-pi/4522-kamera-hd-night-vision-e-ov5647-5mpx-dla-raspberry-pi-moduly-ir-waveshare-10300-5904422332860.html . Pojawia się jednak jeden problem, urządzenie nie działa na fale podczerwieni; zamiast tego za pomocą dwóch lamp podświetla otoczenie przez co wytwarza po prostu światło. Do omówienia czy akceptujemy światło w pomieszczeniu (kolejny algorytm rozpoznawania czy jest ciemno w pomieszczeniu aby naświetlać))
- przetwornik A/C 3008 SPI-DIP https://botland.com.pl/przetworniki/2358-przetwornik-a-c-mcp3008-10-bitowy-8-kanalowy-spi-dip-5904422302696.html
- pakiecik rezystorów też się przyda
- lutownica (znajomy)

Możliwe, że w czasie implementacji projektu pojawi się jeszcze jeden czujnik.

Jeśli chodzi o platformę projektu najlepiej będzie to zrealizować na platformie Kotlin + OpenVPN na raspberry pi (Pivpn skrocona wersja konfiguruje wszystko za nas). Dzięki temu będziemy musieli zaimplementować łączenie się tylko w sieci lokalnej z aplikacją; VPN rozwiąże problem zdalnego łączenia  się poza siecią, ponieważ wciąż aplikacja będzie widzieć oba połączenia jako połączenia lokalne. Na dzień dzisiejszy najważniejszymi kwestiami potrzebnych do działania aplikacji będzie:

1. rozpoznawanie obrazu na rapsberry pi w pythonie (przyklad poradnika: https://www.youtube.com/watch?v=o-x1PE0LVKM)
2. implementacja i wymiana danych w sqlite3
3. przemyśleć sposób reprezentacji danych z bazy danych na grafach w aplikacji

Jeśli chodzi o resztę rzeczy, które już są a mogą być potrzebne do projektu:

- Raspberry pi 3 B (w wersji podstawowej, możliwe ogarnięcie Raspberry pi 4gb w przypadku braku mocy)
- płytka stykowa
- karta pamięci (16gb lub 32gb z przygotowanym czystym systemem Buster)
- multimetr



Dodatkowo jeśli uda nam się wcześniej przygotować projekt znajomy za 4pak harnasi może zaprojektować i wydrukować nam obudowę do projektu na drukarce 3D ;-)

Dodatkowo z tego względu, że mając już koncept projektu sama reszta może nam pójść szybko chciałbym ułożyć terminarz jeśli chodzi o robienie projektu. Najlepiej aby sam system raspberka działał przed świętami i był gotowy.

Proponuję więc następne 3 albo 4 weekendy (piątek sobota albo niedziela obojetnie) spotkać się u mnie jak już będziemy mieli czujniki i wszystko co nam potrzebne. Czyli:

- **26.11-27.11**

- **3.12-4.12**
- **10.12-11.12**

- **17.12-18.12**

Zobaczymy ile spotkań uda się zrobić. Tutaj załączam szybki poglądowy startowy schemat wyglądu projektu:

<figure>
    <center><img src="C:\Users\adamie2\Desktop\Studia\Semestr 5\Systemy wbudowane\Projekt-github\Rasberek\scheme.png" alt="Trulli" style="transform:rotate(-90deg); width:55%"></center>
    <figcaption align = "center"><b>Schemat podłączenia czujników do Raspberry pi (nie uwzględniłem kamery którą będziemy podłączać bezpośrednio do wejścia - następny rysunek ma podpisane połączenia)</b></figcaption>
</figure>

<figure>
    <center><img src="C:\Users\adamie2\Desktop\Studia\Semestr 5\Systemy wbudowane\Projekt-github\Rasberek\scheme2.jpg" alt="Trulli" style="width:50%"></center>
<figcaption align = "center"><b</b></figcaption>
</figure>

Dobra, a teraz dla zasady szybki formalny opis projektu:







## Opis projektu

#### 1. Analiza wymagań

Jako odbiorca danego urządzenia, chcemy móc kontrolować i monitorować rzeczy które dzieją się w naszym mieszkaniu i bla bla bla później się dokończy