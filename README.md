# Customer satisfection prediction

This project builds a machine learning model to predict wheth customer setisfied or not. It involves data preprocessing, save piple line data, and save clean data for model training, model training, evaluation, create a pipeline and Streamlit deployment.

---

## 📁 Project Structure

```
├── data/                  
├── notebooks/   
|    ├── clean.ipynb          
│    └── model_train.ipynb       
├── Model Deploy/
│   ├── app.py              
│   └── model.pkl           
├── requirements.txt          
├── README.md                
```

---

## 🎯 Objective

To predict if a Customer setisfie or not.

---

## 📦 Features Used

- Customer 
- Age	 
- Days_Since_Purchase	
- Customer Gender	  
- Product Purchased	 
- Ticket Subject	
- Satisfaction_Level    
---

## 🛠️ Technologies Used

- Python (Pandas, NumPy, seaborn, matplotlib, Scikit-learn, Imbalanced-learn)
- Streamlit (for deployment)
- Joblib (for model saving/loading)

---

## 📊 Model & Evaluation

- **Model Used:** e.g., RandomForestClassifier / LogisticRegression  
- **Evaluation Metrics:**
  - Accuracy
  - Precision, Recall, F1-score
  - Confusion Matrix

- **Issue Solved:** Fix over fitting and remove null values in target columns.

---

## 🚀 How to Run the App

1. Clone the repository:
   ```bash
   git clone https://github.com/Priyanshu-techp/Customer-setifection-prediction.git
   cd bank-marketing-prediction
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. activate the enviroment
   ```bash
   venv/scripts/activate

4. Run the Streamlit app:
   ```bash
   streamlit run "Model_Deploying/app.py"
   ```
---

## 📈 Results

- **Best r2-score:** ~0.89  
- **Overall Accuracy:** ~0.89  
- **Handel Missing values in taget column**

---

## ⚠️ Notes

- Ensure consistent `scikit-learn` versions during model saving and loading.
- Threshold tuning may be required for better minority class detection.

---

## 👤 Author

**Priyanshu Pandey**  
Diploma in Automation & Robotics  
Aspiring Data Scientist  
[LinkedIn Profile](https://www.linkedin.com/in/priyanshu-pandey-672767320)


