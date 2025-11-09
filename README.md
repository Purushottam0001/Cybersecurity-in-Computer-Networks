# 🚀 Cybersecurity in Computer Networks – IDS Demo  

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)  
![License](https://img.shields.io/badge/License-MIT-green.svg)  
![ML](https://img.shields.io/badge/Machine%20Learning-RandomForest-orange)  
![Status](https://img.shields.io/badge/Status-Active-success)  

---

### 🔐 Overview  
This project demonstrates a **Machine Learning–based Intrusion Detection System (IDS)** developed as part of the **“Cybersecurity in Computer Networks”** coursework at KIIT University.  

The system generates synthetic network traffic, trains a RandomForest model to classify normal and attack patterns, and provides a minimal Flask API for real-time predictions.  

---

### 🧩 Features  
✅ Synthetic network dataset generator  
✅ ML-based anomaly classification (RandomForest)  
✅ Flask-based REST API for live detection  
✅ Modular and extensible code structure  
✅ Ready for deployment and demonstration  

---

### ⚙️ Tech Stack  
- **Language:** Python  
- **Libraries:** NumPy, Pandas, Scikit-learn, Flask, Joblib  
- **Model:** RandomForest Classifier  
- **Interface:** REST API  

---

### 📂 Project Structure  
```
Cybersecurity-in-Computer-Networks/
│
├── generate_data.py        # Create synthetic network traffic
├── train_model.py          # Train and save RandomForest model
├── evaluate.py             # Evaluate accuracy and classification report
├── app.py                  # Flask app for real-time detection
├── requirements.txt        # Dependencies
├── USAGE.txt               # Example curl commands
└── README.md               # Documentation
```

---

### 🧠 How It Works  
1. **Data Generation:** Simulates normal and attack traffic with random patterns.  
2. **Training:** Uses RandomForest to classify packets.  
3. **Evaluation:** Prints model accuracy and precision/recall report.  
4. **API Simulation:** Flask endpoint `/predict` accepts JSON and predicts if the packet is “normal” or “attack.”  

---

### 💻 Run Locally  
```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Generate data
python generate_data.py --output demo_data.csv --n 2000

# 3. Train model
python train_model.py --input demo_data.csv --model model.joblib

# 4. Evaluate
python evaluate.py --model model.joblib

# 5. Start Flask app
python app.py
```

---

### 🧪 Example API Request  
```bash
curl -X POST http://127.0.0.1:5000/predict -H "Content-Type: application/json" -d '{
  "duration": 0.4,
  "src_bytes": 300,
  "dst_bytes": 200,
  "wrong_fragment": 0,
  "urgent": 0,
  "hot": 1,
  "num_failed_logins": 0,
  "count": 12,
  "srv_count": 9,
  "serror_rate": 0.01,
  "srv_serror_rate": 0.02,
  "dst_host_srv_count": 5,
  "dst_host_diff_srv_rate": 0.1
}'
```

Response:
```json
{
  "prediction": 0,
  "probabilities": [0.92, 0.08]
}
```

---

### 📈 Future Improvements  
- Integrate deep learning for higher accuracy.  
- Use real-world datasets (like NSL-KDD).  
- Add dashboard for visual monitoring.  

---

### 👨‍💻 Author  
**Purushottam Kumar (23053230)**  
B.Tech CSE, CSE 26 – KIIT University  
📅 November 2025  

---

### 📚 References  
- IEEE Xplore: *AI-Based Network Intrusion Detection Systems*  
- ScienceDirect: *Advances in Cybersecurity for Next-Generation Networks*  
- SpringerLink: *Deep Learning Approaches to Network Security*