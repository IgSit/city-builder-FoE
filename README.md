# city-builder-FoE

## Cele
* mapa z budynkami i drogami
* budynki obronne
* budynki towarowe (wydobywcze)
* jest budynek główny (ratusz)
* żeby budynek działał, musi być podłączony drogą do ratusza
* warsztaty mają różne tryby pracy (5/15 minut itd) - zegar systemowy
* mechanika ataków na osadę - gra losowo atakuje osadę gracza
* technologie (lepsze budynki z czasem, itd)
* targ z surowcami (komputerowi kupcy pojawiający się na jakiś czas)
* misje
* schowek do przebudowy osady

## Harmonogram
**III zajęcia**: mapa ze wstawianiem rzeczy (same prostokąty do przeciągnięcia na mapę) + 
 ewentualnie implementacja budynków

**IV zajęcia**: na pewno budynki (wszystkie) + tryby pracy budynków

**V zajęcia**: mechanika ataków + targ

**VI zajęcia**: misje + technologie

**VII zajęcia**: oddanie końcowe

## Klasy:
* mapa (2d matrix)
  * pilnuje, czy budynek może zostać postawiony na polach
* budynek (abstract)
  * wymiary
  * koszt
  * życie (gdy budynek jest zniszczony, to nie może pracować, ma koszt naprawy proporcjonalny do zniszczeń)
  * może być przeniesiony lub usunięty
  * wymagana ilość ludzi do postawienia
* budynek mieszkalny
  * ilość ludzi
  * budynek zasobowy
  * koszt produkcji
  * tryby pracy
* budynek obronny (wieżyczki/mury)
  * zasięg
  * obrażenia
* targ
  * oferty (ograniczone czasowo (i ewentualnie liczbą surowców))
* misja
  * warunki
  * nagroda
* drzewko technologii
  * trzyma technologie
* technologia
  * koszt
  * wymagana wcześniejsza technologia
* wróg
  * życie
  * obrażenia
  * metoda znajdowania budynków (najbliższy/priorytet na obronne)
*schowek
  * trzyma budynki
  * pozwala na zatwierdzenie zmiany budynków, gdy jest pusty
