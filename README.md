
## Key Findings

### 1. Selected grocery basket

A selected basket of 10 grocery items increased in cost from KSh 732.36 in September 2025 to KSh 791.15 in September 2026.

- **Additional cost:** KSh 58.79
- **Percentage increase:** 8.03%
- **What KSh 1,000 leaves behind:** KSh 267.64 in 2025 versus KSh 208.85 in 2026.

This is an illustrative basket of selected items, not the official KNBS household consumption basket.

### 2. Transport sensitivity analysis

The project models a household earning KSh 30,000 per month, consisting of one adult and one child, with public transport commuting for 22 working days.

| Assumed one-way fare | Monthly transport cost | Income remaining |
|---:|---:|---:|
| KSh 50 | KSh 2,200 | KSh 6,965 |
| KSh 100 | KSh 4,400 | KSh 4,765 |
| KSh 150 | KSh 6,600 | KSh 2,565 |
| KSh 200 | KSh 8,800 | KSh 365 |

![Transport sensitivity analysis](visuals/transport_sensitivity_analysis.png)

The model holds other budget items constant to isolate the effect of transport costs. Fares are illustrative scenarios, not verified average matatu fares.

### 3. Household budget implications

Under the current illustrative budget, total monthly expenses are KSh 25,235, leaving KSh 4,765 from an assumed monthly income of KSh 30,000.

However, most budget categories are provisional assumptions or scenarios rather than verified household expenditure data. The result should therefore be interpreted as a planning scenario, not a statistically representative estimate of the average Kenyan household.

## Data Sources

- [Kenya National Bureau of Statistics (KNBS) CPI Explorer](https://cpiexplorer.knbs.or.ke/)
- [KNBS: Consumer Price Indices and Inflation Rates, September 2026](https://www.knbs.or.ke/reports/consumer-price-indices-and-inflation-rates-september-2026/)

## Methods

This project uses Python and pandas to calculate absolute and percentage price changes, construct an illustrative grocery basket, model monthly household expenses, and conduct transport-cost sensitivity analysis. Matplotlib is used to visualise the scenario results.

## Limitations

- The selected grocery basket is not an official CPI basket.
- The household budget includes assumptions that require further validation.
- Transport fares represent hypothetical scenarios, not observed market averages.
- A national reference rent may differ considerably from actual rent in a specific town or neighbourhood.
- Price changes alone do not establish the causes of inflation or measure every household's cost of living.

## Tools

- Python
- pandas
- Matplotlib
- Google Colab
- GitHub
