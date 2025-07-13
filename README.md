# 💳 Financial Identity Splitter

A smart, automated dashboard that analyzes personal bank statements to reveal monthly spending habits and generate personalized financial personas.

## 📸 Dashboard Previews

Here are some snapshots from the interactive dashboard:

### 🔍 Overview Table & Filters
![Overview](assets/monthly%20financial%20personas%201.png)

### 📊 Top Spending Trends
![Trends](assets/monthly%20financial%20personas%202.png)

### 🥧 Persona Breakdown
![Persona Pie Chart](assets/monthly%20financial%20personas%203.png)


Built with Python 🐍, FastAPI ⚡, Pandas 📊, and Chart.js 📈.

---

## 📦 Project Overview

**Financial Identity Splitter** takes raw bank statements (PDF) and transforms them into a fully interactive analytics app — showing where your money goes, what type of spender you are each month, and how you can improve.

### 🔍 Key Features

| Feature                       | Description |
|------------------------------|-------------|
| 🧾 PDF → CSV Extractor       | Extracts transactions from messy PDF bank statements using table recognition |
| 📂 Auto Categorization       | Assigns categories to each transaction (e.g. Food, Transfers, Bills) |
| 📊 Monthly Summary           | Summarizes debit/credit activity per category |
| 🧠 Financial Personas        | Generates monthly \"persona tags\" like `The Provider`, `The Middleman`, etc. |
| 📈 Data Visualizations       | Bar, Line, and Pie charts with spending trends and category breakdown |
| 🎛️ Interactive Filters      | Filter transactions by month, category, or persona |
| ⬇️ Export Tool              | Download filtered transactions as CSV |
| ⚡ Powered by FastAPI        | Lightweight backend with HTML templates and API routes |

---

## 📁 Project Structure
<pre lang="markdown">
financial_identity_splitter/
├── app/
│ ├── main.py # FastAPI backend
│ └── templates/
│ └── dashboard.html # Interactive dashboard UI
├── data/ # Input/output files
│ ├── bank_statement.pdf
│ ├── transactions.csv
│ ├── transactions_categorized.csv
│ ├── monthly_summary.csv
│ └── monthly_personas.csv
├── scripts/
│ ├── extract_transactions.py
│ ├── categorize_transactions.py
│ ├── summarize_transactions.py
│ └── generate_personas.py
└── README.md
</pre>

---

## 🚀 How to Run

### 1. Clone this repo
```bash
git clone https://github.com/yourusername/financial-identity-splitter.git
cd financial-identity-splitter
```

### 2. Install dependencies
```
pip install -r requirements.txt
```

### 3. Add your bank statement (PDF)
```
data/your_statement.pdf
```

### 4. Run the processing pipeline
```
python scripts/extract_transactions.py
python scripts/categorize_transactions.py
python scripts/summarize_transactions.py
python scripts/generate_personas.py
```

### 5. Launch the dashboard
```
uvicorn app.main:app --reload
```
Visit: http://127.0.0.1:8000

### 📊 Example Personas

| Month    | Top Category    | Persona       |
| -------- | --------------- | ------------- |
| Nov 2024 | Transfers & P2P | The Middleman |
| Jan 2025 | Family Support  | The Provider  |
| Mar 2025 | Self-Care       | The Pamperer  |

### 🌍 Deployment (Optional)
You can deploy to:

- Render

- Railway

- Hugging Face Spaces (via Gradio or FastAPI + Static template)

### 💡 Future Ideas
- 🧠 ML-powered persona clustering

- 🔐 Add login for privacy

- 📆 Weekly breakdowns

- 📱 Mobile-friendly UI

- 💬 Personalized financial advice 

### 👨‍💻 Author

Henry C. Dibie — @kinghenrymorgan

Project powered by real financial data, built from scratch to showcase automation, analytics, and storytelling with data.