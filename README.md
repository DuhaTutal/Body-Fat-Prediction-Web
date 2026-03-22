# Vücut Yağ Oranı Tahmini

Kaggle Body Fat veri seti kullanılarak geliştirilmiş, vücut yağ oranını tahmin eden web uygulaması.

## Proje Hakkında

Bu proje, vücut ölçüleri (boyun, göğüs, karın, kalça vb.) ve bazı kişisel bilgiler (yaş, kilo) girilerek vücut yağ oranının tahmin edilmesini sağlar. Tahmin modeli Kaggle'daki Body Fat veri seti ile eğitilmiştir.

## Geliştirme Notu

- **Model eğitimi, veri ön işleme, FastAPI backend ve proje mimarisi** tamamen benim tarafımdan geliştirilmiştir.
- **Web arayüzü** (HTML, CSS, JavaScript) Cursor AI desteği ile oluşturulmuştur.

## Teknolojiler

- **Backend:** FastAPI, Uvicorn
- **ML:** scikit-learn, pandas
- **Frontend:** HTML, CSS, JavaScript (vanilla)

## Kurulum

1. Depoyu klonlayın:
   ```bash
   git clone https://github.com/username/body_fat.git
   cd body_fat
   ```

2. Sanal ortam oluşturup aktifleştirin:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   ```

3. Bağımlılıkları yükleyin:
   ```bash
   pip install -r requirements.txt
   ```

4. Uygulamayı çalıştırın:
   ```bash
   uvicorn app:app --reload
   ```

5. Tarayıcıda `http://127.0.0.1:8000` adresine gidin.

## Gereksinimler

- `body_fat_model.pkl` dosyasının proje kök dizininde bulunması gerekir (eğitilmiş model ve scaler içerir).

## API

- **POST `/predict`** — Vücut yağ oranı tahmini
  - Girdi: JSON (Age, Weight, Neck, Chest, Abdomen, Hip, Thigh, Knee, Ankle, Biceps, Forearm, Wrist)
  - Çıktı: `{"predicted_body_fat": float}`
