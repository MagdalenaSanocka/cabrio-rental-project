Projekt Cabrio Rental to aplikacja webowa napisana w języku Python przy użyciu frameworka Django. 
Aplikacja umożliwia rezerwację samochodów z bazy danych z poziomu panelu użytkownika oraz zarządzanie rezerwacjami przez administratora.

Wymagania >>
Do poprawnego działania aplikacji wymagane są:

Python 3.x
Django 3.x

W tym projekcie, w obecnej formie, jest zaprojektowana jedynie baza danych złożona z dwóch modeli. 

Modele w bazie danych
W bazie danych zaimplementowane są dwa modele:


***Car*** <<< Dane pojazdów dodane z poziomu administratora w Django(przeglądarka). <<<
Model Car przechowuje informacje o samochodach dostępnych do wypożyczenia, takie jak:

marka,
model,
rocznik,
typ nadwozia,
moc,
liczba miejsc,
cena za dzień.


***Reservation***
Model Reservation przechowuje informacje o rezerwacjach samochodów, takie jak:

samochód,
użytkownik dokonujący rezerwacji,
data rozpoczęcia rezerwacji,
data zakończenia rezerwacji.
