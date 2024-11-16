---

# 🌟 Workshop_03 - Machine Learning Prediction and Streaming Data 🌟

by Manuel Gruezo

---

## 👋 Welcome!  

In this project, you'll train a regression machine learning model to predict the happiness score of countries 🌍. You'll be working with **5 CSV files** containing global happiness data.  

💻 Technologies used:  

- **_Python_** 🐍  
- **_Jupyter Notebook_** 📓  
- **_PostgreSQL_** 🐘  
- **_Apache Kafka_** 🚀  

---

## 🎯 Objectives  

1. **EDA and ETL:** Perform exploratory data analysis and prepare data by cleaning, preprocessing, and selecting relevant features. 🧹  
2. **Regression Model Training:** Develop a regression model, optimize it, and evaluate its performance. 📊  
3. **Real-time Streaming:** Use Apache Kafka to handle real-time data processing from EDA/ETL to predictions. 🔄  
4. **Database Integration:** Store predictions and relevant features in a PostgreSQL database. 📂  

---

## 📂 Folder Structure  

```
Workshop3
├── data                           # 📁 CSV data files
├── notebooks                      # 📝 Jupyter notebooks
│   ├── 001-EDA.ipynb              # Exploratory Data Analysis
│   ├── 002-model_metrics.ipynb    # Model evaluation and metrics
│   └── model.pkl                  # Trained model in pickle format
├── src                            # 🛠️ Project's source code
│   ├── database                   # Database-related modules
│   │   ├── connection.py          # Database connection script
│   │   └── db_settings.json       # Database configuration
│   ├── models                     # Machine learning models
│   └── utils                      # Utility scripts (e.g., feature selection)
├── .env                           # 🌐 Environment variables
├── docker-compose.yml             # 🐋 Docker Compose file
├── consumer.py                    # Consumer microservice script
├── producer.py                    # Producer microservice script
└── requirements.txt               # 📜 Dependencies list
```

---

## 🌐 Data Source  

📥 [World Happiness Report Dataset](https://www.kaggle.com/datasets/unsdsn/world-happiness)  

---

## 🚀 How to Run the Project  

### Pre-requisites:  

- 🐍 **Python:** [Download Python](https://www.python.org/downloads/)  
- 🐘 **PostgreSQL:** [Download PostgreSQL](https://www.postgresql.org/download/)  
- 🐋 **Docker:** [Download Docker](https://www.docker.com/get-started/)  

---

### Steps:

1️⃣ Clone this repository:  
```bash
git clone https://github.com/alej0909/Workshop-3.git
```  

2️⃣ Navigate to the project folder:  
```bash
cd Workshop-3
```  

3️⃣ Create a virtual environment:  
```bash
python -m venv venv
```  

4️⃣ Activate the virtual environment:  
```bash
./venv/Scripts/activate
```  

5️⃣ Configure your database:  
- Create a `db_settings.json` file under `src/database` with:  
```json
{
  "user": "Your PostgreSQL username",
  "password": "Your PostgreSQL password",
  "host": "Your database host address",
  "port": "Your PostgreSQL port",
  "database": "Your database name"
}
```  

6️⃣ Install required libraries:  
```bash
pip install -r requirements.txt
```  

7️⃣ Set up your environment:  
- Create a `.env` file and define the `WORK_PATH` variable.  

8️⃣ Set up your database:  
- Create a PostgreSQL database matching the `database` name in your `db_settings.json`.  

9️⃣ Start with the Jupyter notebook:  
- Open and run `001-EDA.ipynb`.  

---

### 🌟 Running the Streaming Architecture  

🔟 Run Docker:  
```bash
docker compose up
```  

1️⃣1️⃣ Access Kafka container terminal:  
```bash
docker exec -it kafka-test bash
```  

1️⃣2️⃣ Create a Kafka topic:  
```bash
kafka-topics --bootstrap-server kafka-test:9092 --create --topic predict-happiness
```  

1️⃣3️⃣ Run the **producer** and **consumer**:  

- **Producer**:  
```bash
python producer.py
```  

- **Consumer**:  
```bash
python consumer.py
```  

1️⃣4️⃣ Verify your database:  
- Check PostgreSQL for the new table with happiness predictions.  

---

### 🧪 Evaluate the Model  

Run `002-model_metrics.ipynb` to analyze the model's performance and metrics 📈.  

---

🎉 **Congratulations!** You're ready to predict happiness in real-time. 💡