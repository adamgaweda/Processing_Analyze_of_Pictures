# Przetwarzanie Obrazów

Repozytorium zawiera materiały, zadania i ćwiczenia laboratoryjne z przedmiotu **Przetwarzanie Obrazów** (Digital Image Processing) realizowane w środowisku Python z wykorzystaniem Jupyter Notebooks.

---

## 📁 Struktura projektu

* **`lab01/` – Podstawowe metody przetwarzania obrazu**
  * Wczytywanie, konwersja oraz wizualizacja obrazów (`scikit-image`, `PIL`, `matplotlib`).
  * Analiza i rozdzielanie kanałów barwnych (RGB, RGBA) oraz detekcja kanału alfa.
  * Wyznaczanie i analiza histogramów jasności/kolorów.
  * Samodzielna analiza cech obrazów cyfrowych.

* **`lab02/` – Morfologia matematyczna**
  * Generowanie i binaryzacja obrazów testowych.
  * Podstawowe operacje morfologiczne: erozja, dylatacja, otwarcie, zamknięcie.
  * Analiza i modyfikacja kształtów oraz struktury obiektów binarnych przy użyciu elementów strukturujących.

* **`lab03/` – Szkieletyzacja i pocienianie (Thinning)**
  * Metody szkieletyzacji obiektów binarnych (`skeletonize`, `thin`).
  * Usuwanie artefaktów i przycinanie krótkich gałązek (pruning).
  * Zastosowanie w analizie biometrycznej – przetwarzanie bazy odcisków palców (*Tsinghua Distorted Fingerprint Database*).

---

## 🛠️ Wymagania i stos technologiczny

* **Python** (zalecana wersja >= 3.10)
* Główne biblioteki:
  * `numpy` – operacje numeryczne i macierzowe
  * `matplotlib` – wizualizacja obrazów i wykresów
  * `scikit-image` – zaawansowane algorytmy przetwarzania obrazów
  * `pillow` (`PIL`) – odczyt i operacje na plikach graficznych
  * `scipy` – operacje naukowe i analiza danych
  * `ipykernel` / `jupyter` – środowisko uruchomieniowe notatników

---

## 🚀 Uruchomienie projektu

1. **Klonowanie repozytorium:**
   ```bash
   git clone <URL_REPOZYTORIUM>
   cd Obrazki1
   ```

2. **Utworzenie i aktywacja wirtualnego środowiska:**
   * **Windows (PowerShell):**
     ```powershell
     python -m venv .venv
     .\.venv\Scripts\Activate.ps1
     ```
   * **Linux / macOS:**
     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     ```

3. **Instalacja zależności:**
   ```bash
   pip install numpy matplotlib scikit-image pillow scipy ipykernel
   ```

4. **Uruchomienie notatników:**
   ```bash
   jupyter notebook
   ```
   Możesz także otworzyć folder projektu w środowisku **VS Code** lub **PyCharm** z zainstalowanym rozszerzeniem do obsługi Jupyter Notebooks.

