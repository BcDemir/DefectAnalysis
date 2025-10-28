# 🧠 Power BI Defect Analysis Dashboard

A complete **end-to-end data analytics project** built in **Power BI** using a real-world *manufacturing defects dataset*.  
This dashboard demonstrates my ability to clean, model, analyze, and visualize operational data to uncover insights and drive process improvements.

---

![Dashboard](/image/dashboard_image.png)

## 📊 Project Overview

The goal of this project is to analyze **defects in manufactured products** — identifying trends, costs, and key risk factors across time, location, and severity.

This dashboard can help a manufacturing or quality engineering team to:
- Track the **number of defects** and **total repair costs**
- Monitor **defect severity trends**
- Evaluate **inspection method effectiveness**
- Highlight **critical defects and high-cost areas**
- Support **data-driven decisions** in quality improvement

---

## 🧩 Dataset

**File:** `defects_data.csv`  
**Records:** ~1,000 rows  
**Source:** [Manufacturing dataset - Kaggle] (https://www.kaggle.com/datasets/fahmidachowdhury/manufacturing-defects)  

### Key Columns
| Column | Description |
|--------|--------------|
| `defect_id` | Unique identifier for each defect |
| `product_id` | ID of the affected product |
| `defect_date` | Date defect was reported |
| `defect_type` | Type/category of defect |
| `defect_location` | Area or section where the defect occurred |
| `inspection_method` | Method used to detect defect |
| `severity` | Severity classification (Minor, Major, Critical) |
| `repair_cost` | Cost of repair for the defect (USD) |

---

## ⚙️ Data Cleaning & Preparation (Python)

The raw data was cleaned using **Python (Pandas)** before loading into Power BI.