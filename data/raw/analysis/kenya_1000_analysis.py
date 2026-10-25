
import csv
from pathlib import Path

# Locate the raw dataset relative to this script.
ROOT = Path(__file__).resolve().parents[1]
INPUT_FILE = ROOT / "data" / "raw" / "knbs-prices.csv"
OUTPUT_FILE = ROOT / "data" / "processed" / "price-comparison.csv"

OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

results = []

with INPUT_FILE.open("r", newline="", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)

    for row in reader:
        old_price = float(row["sep_2025"])
        new_price = float(row["sep_2026"])

        change = round(new_price - old_price, 2)
        percentage = round((change / old_price) * 100, 2)

        results.append({
            "item": row["item"],
            "unit": row["unit"],
            "sep_2025": f"{old_price:.2f}",
            "sep_2026": f"{new_price:.2f}",
            "change_ksh": f"{change:.2f}",
            "change_percent": f"{percentage:.2f}",
            "source": row["source"],
        })

with OUTPUT_FILE.open("w", newline="", encoding="utf-8") as file:
    columns = [
        "item", "unit", "sep_2025", "sep_2026",
        "change_ksh", "change_percent", "source"
    ]
    writer = csv.DictWriter(file, fieldnames=columns)
    writer.writeheader()
    writer.writerows(results)

print(f"Processed {len(results)} items.")
print(f"Saved results to: {OUTPUT_FILE}")
print("\nLargest price increases:")

for row in sorted(
    results,
    key=lambda item: float(item["change_percent"]),
    reverse=True
)[:5]:
    print(f'{row["item"]}: {row["change_percent"]}%')
