# Kenya Cost of Living Analysis (2025–2026)

A Python-based data analysis project investigating changes in selected consumer prices, grocery basket costs, public transport expenses, and household budget pressure in Kenya.

The project uses price observations attributed to the Kenya National Bureau of Statistics (KNBS) to compare September 2025 and September 2026. It combines data cleaning, price-change calculations, calculation auditing, an illustrative grocery basket, household budget modelling, and transport-cost sensitivity analysis.

## Research Question

**How are changing consumer prices and public transport costs affecting the monthly budget of a low-income household in Kenya?**

The analysis uses an illustrative household scenario. It is not intended to represent every Kenyan household.

## Key Findings

### 1. Fixed-Quantity Grocery Basket

A selected basket of ten grocery items was calculated using fixed quantities so that the two periods could be compared on a consistent basis.

| Measure | September 2025 | September 2026 |
|---|---:|---:|
| Cost of selected fixed-quantity basket | KSh 732.36 | KSh 791.15 |
| Balance from KSh 1,000 | KSh 267.64 | KSh 208.85 |

- **Absolute increase:** KSh 58.79
- **Percentage increase:** 8.03%

The percentage change is calculated as:

`((2026 basket cost - 2025 basket cost) / 2025 basket cost) × 100`

The basket uses selected quantities of maize flour, beans, sukuma wiki, cabbage, tomatoes, milk, eggs, bread, sugar, and cooking oil.

This is an illustrative fixed-quantity basket, not the official KNBS consumer price index basket and not a complete monthly household food budget.

### 2. Public Transport Cost Sensitivity

The transport model assumes a monthly income of KSh 30,000, 22 commuting days, and two one-way journeys per working day.

| Assumed one-way fare | Monthly transport cost | Income remaining under the model |
|---:|---:|---:|
| KSh 50 | KSh 2,200 | KSh 6,965 |
| KSh 100 | KSh 4,400 | KSh 4,765 |
| KSh 150 | KSh 6,600 | KSh 2,565 |
| KSh 200 | KSh 8,800 | KSh 365 |

The remaining-income figures use the same non-transport budget assumptions while varying transport costs.

Under this scenario, increasing the assumed one-way fare from KSh 50 to KSh 200 raises monthly transport spending from KSh 2,200 to KSh 8,800. The modelled amount remaining after expenses falls from KSh 6,965 to KSh 365.

These fares are hypothetical scenarios, not verified average matatu fares. Actual transport costs vary by route, location, travel frequency, and time.

### 3. Illustrative Household Budget

The budget model uses assumed monthly income of KSh 30,000.

| Budget measure | Amount |
|---|---:|
| Monthly income | KSh 30,000 |
| Total modelled expenses | KSh 25,235 |
| Income remaining | KSh 4,765 |
| Share of income allocated to expenses | 84.1% |

The model includes rent, food, transport, cooking fuel, electricity, water, phone and data, child-related needs, toiletries and cleaning supplies, and healthcare or emergencies.

The rent figure uses a national reference price. Several other expense values are illustrative planning assumptions that require validation against actual household expenditure data.

The food budget is separate from the selected fixed-quantity grocery basket. The remaining KSh 4,765 is a modelled balance, not a measured household savings or disposable-income average.

## Data Sources

- Kenya National Bureau of Statistics (KNBS), [CPI Explorer](https://cpiexplorer.knbs.or.ke/)
- KNBS, [Consumer Price Indices and Inflation Rates — September 2026](https://www.knbs.or.ke/reports/consumer-price-indices-and-inflation-rates-september-2026/)

The raw dataset is stored in `data/raw/knbs-prices.csv`. It contains 16 selected price observations with September 2025 and September 2026 values and source attribution.

## Methodology

The project follows a reproducible analysis workflow:

1. Load the raw CSV into a pandas DataFrame.
2. Inspect the dataset structure, columns, units, and source information.
3. Calculate absolute and percentage price changes for each item.
4. Independently reproduce the calculations to audit the results.
5. Calculate a selected fixed-quantity grocery basket for both periods.
6. Model monthly household expenses and remaining income.
7. Test different assumed public transport fares while holding other budget assumptions constant.
8. Use Matplotlib to visualise transport-cost sensitivity.
9. Document assumptions, sources, limitations, and findings.

The calculation audit checks mathematical consistency. It does not independently verify the original source observations.

## Repository Structure

```text
kenya-cost-of-living-2026/
├── data/
│   ├── raw/
│   │   └── knbs-prices.csv
│   └── processed/
│       ├── transport_sensitivity_analysis.csv
│       └── household_budget_audit.csv
├── visuals/
│   └── transport_sensitivity_analysis.png
├── kenya_cost_of_living_analysis.ipynb
└── README.md
```

The notebook is the main entry point for reviewing the calculations and assumptions. Raw data and processed outputs are kept separate to support transparency and reproducibility.

## Tools and Skills Demonstrated

- **Python:** analytical calculations and data processing
- **pandas:** data loading, filtering, transformation, and aggregation
- **Matplotlib:** data visualisation
- **Google Colab:** cloud-based notebook development
- **GitHub:** version control and project documentation
- **Data validation:** independent recalculation and numerical checks
- **Analytical communication:** explaining results, assumptions, and limitations

## Limitations

- The analysis covers 16 selected price observations, not the full set of goods and services used to calculate official CPI.
- The fixed-quantity grocery basket is illustrative and is not an official KNBS consumption basket.
- The basket is not a monthly food expenditure estimate.
- Several household expense categories are provisional assumptions rather than verified expenditure records.
- Transport fares are hypothetical scenarios, not verified market averages.
- A national reference rent may differ substantially from rent in a particular town, estate, or neighbourhood.
- A two-period comparison identifies price movements but does not establish their causes.
- The household scenario is hypothetical and is not statistically representative of Kenyan households.
- Source attribution does not, by itself, independently verify the underlying observations.

## Conclusion

This project demonstrates how selected consumer price observations can be analysed and audited to explore changes in grocery costs and household budget pressure.

The selected fixed-quantity grocery basket increased by **8.03%**, from KSh 732.36 in September 2025 to KSh 791.15 in September 2026. The transport sensitivity model shows that higher assumed commuting fares can substantially reduce the income remaining under the specified household budget.

These findings apply only to the selected items and stated assumptions. They should not be interpreted as a complete measure of inflation or a representative estimate of household expenditure across Kenya.

## Reproducibility

Open the notebook in Google Colab or another compatible Jupyter environment and run its cells in order. The analysis uses Python and publicly attributed price observations, alongside clearly identified illustrative household and transport assumptions.

**Portfolio project:** entry-level data analysis, data validation, visualisation, and analytical communication.
