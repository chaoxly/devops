# Projekt: Prosta aplikacja webowa z Flask

### Opis projektu

Projekt przedstawia prostą aplikację webową stworzoną w Pythonie z wykorzystaniem frameworka Flask. Aplikacja wyświetla stronę zawierającą przykładowe dane. Proces tworzenia, wdrażania i testowania aplikacji został zautomatyzowany za pomocą narzędzia GitHub Actions.

### Funkcjonalności aplikacji

- Wyświetlanie danych pod określonym adresem URL (/michal).

### Wymagania wstępne

Przed rozpoczęciem instalacji i uruchomienia projektu należy upewnić się, że następujące narzędzia są zainstalowane na Twoim systemie:

- Docker

- Git

### Instrukcja instalacji i uruchomienia

1. Sklonowanie repozytorium

Sklonuj projekt na swoją maszynę lokalną:

`git clone https://github.com/chaoxly/devops
cd devops`

2. Budowanie obrazu Dockera

Zbuduj obraz Dockera dla aplikacji:

`docker build -t projekt .`

3. Uruchomienie aplikacji w kontenerze Docker

Uruchom aplikację w kontenerze:

`docker run -d -p 5000:5000 projekt`

4. Testowanie aplikacji

Możesz przetestować aplikację, odwiedzając http://localhost:5000/michal w przeglądarce internetowej.

*Opcjonalnie możemy zainstalować lynx

Widok aplikacji w przeglądarce:
![{675893DA-3D01-4BD2-B15C-FE2B41276613}](https://github.com/user-attachments/assets/f9481b8c-7e93-451f-9d75-f35f88de5ba0)

Projekt został wykonany przez Michal Kwak.
