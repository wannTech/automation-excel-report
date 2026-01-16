import pandas as pd

df = pd.read_excel(r"C:\automation_excel_report\input\sales_raw.xlsx")

# normalisasi header (BEST PRACTICE CORPORATE)
df.columns = df.columns.astype(str).str.strip().str.lower()

df = df.dropna()
df["total"] = df["quantity"] * df["price"]

report = df.groupby("product", as_index=False)["total"].sum()

report.to_excel(r"C:\automation_excel_report\output\sales_report.xlsx", index=False)

print("Laporan berhasil dibuat.")
