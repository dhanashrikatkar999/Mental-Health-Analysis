# 🧠 Mental Health Status Predictor using EEG Data

A simple and effective machine learning-based application that predicts mental health status (Relaxed, Neutral, or Stressed) using EEG (Electroencephalogram) signal parameters.

---

# 🚀 Features

- ✅ Input EEG parameters: TF9, AF7, AF8, TP10, RIGHT AUX
- ✅ Predicts mental state: Relaxed 🟢, Neutral 🟡, Stressed 🔴
- ✅ Easy-to-use web or command-line interface
- ✅ Fast and lightweight predictions

---

# 🧩 How It Works

1. Collect EEG data using a device (or enter simulated values).
2. Input the following EEG signal parameters:
   - TF9 - Temporal Frontal Left
   - AF7 - Anterior Frontal Left
   - AF8 - Anterior Frontal Right
   - TP10 - Temporal Parietal Right
   - RIGHT AUX - Auxiliary Sensor (Right side)
3. The trained ML model processes the input and outputs the mental state:
   - 🟢 Relaxed
   - 🟡 Neutral
   - 🔴 Stressed

---

# 📥 Inputs Example

| TF9  | AF7  | AF8  | TP10 | RIGHT AUX |
|------|------|------|------|-----------|
| 456  | 872  | 659  | 512  | 1100      |

✅ Predicted Output:Stressed

---

# 🛠 Tech Stack

- Frontend: HTML, CSS, JavaScript
- Backend: Python
- Machine Learning: Scikit-learn / TensorFlow / Keras
- Deployment: Localhost, Streamlit, or any cloud service

---

## 📦 Installation & Usage

```bash
# Clone the repository
git clone https://github.com/yourusername/mental-health-eeg-predictor.git
cd mental-health-eeg-predictor

# Run the app
python app.py


