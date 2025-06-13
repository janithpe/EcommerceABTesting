# Ecommerce A/B Testing
Analyzing an A/B Test for an E-commerce Checkout Redesign

## Project Purpose and Goals
The goal of this A/B test is to evaluate whether introducing a redesigned e-commerce checkout page increases the **conversion rate** compared to the current version. I intend to make a **data-driven decision** on whether to roll out the new design to all users based on statistical evidence from the experiment.

**Primary Objective:**
> Test the hypothesis that the redesigned checkout page leads to a significantly higher conversion rate.


## Dataset Source and Description
### Datasets Used:
1. `ab_test.csv`
    - User-level A/B test data including group assignment, landing page version, and conversion status.
    - Size: ~294,478 records before cleaning.

2. `countries_ab.csv`
    - Mapping of users to their country (US, CA, UK).
    - Joined with `ab_test.csv` on `user_id`.

### Key Columns:
| Column        | Description                                 |
|---------------|---------------------------------------------|
| `user_id`     | Unique identifier for each user             |
| `group`       | A/B test group assignment (control/treatment) |
| `landing_page`| Page seen by the user (`old_page`, `new_page`) |
| `converted`   | Whether the user completed a conversion     |
| `country`     | User's country (from `countries_ab.csv`)    |


## Tools and Libraries Used
| Tool / Library     | Purpose                            |
|--------------------|------------------------------------|
| `pandas`           | Data wrangling and transformation  |
| `matplotlib.pyplot`| Visualization (bar plots)          |
| `seaborn`          | Enhanced visual styling            |
| `scipy.stats`      | Z-test for proportions             |
| `numpy`            | Array and mathematical operations  |


## How to Run the Code
1. Place `ab_test.csv` and `countries_ab.csv` in a `Data/` directory.
2. Run the Python script `AB_Testing.py`.
3. Required installations (if not already installed):
```bash
pip install -r Requirements.txt
```
4. Main steps in the code:
   - Load and clean the datasets
   - Validate experimental groups and page assignments
   - Merge in country data
   - Compute conversion rates
   - Perform overall and country-level Z-tests
   - Visualize results
   - Summarize findings and recommendations


## Summary of Results
### Data Cleaning
- Removed 1 duplicated user (`user_id`)
- Removed 3,893 mismatches where group ≠ landing page
- Final clean dataset size: **290,585 records**

---

### Overall A/B Test Results
| Group     | Conversion Rate |
|-----------|------------------|
| Control   | 12.04% (0.12039) |
| Treatment | 11.89% (0.11892) |

**Z-Test Result:**
- Z-Score: 1.31
- P-Value: 0.189
> **Conclusion:** No statistically significant improvement from the new page.

---

### Country-Level Insights
| Country | Control CR | Treatment CR | Z-Score | P-Value |
|---------|------------|--------------|---------|---------|
| US      | 12.06%     | 11.85%       | 1.51    | 0.132   |
| CA      | 11.88%     | 11.19%       | 1.30    | 0.195   |
| UK      | 12.00%     | 12.12%       | -0.47   | 0.635   |

> Across all countries, the differences in conversion were small and **not statistically significant**.

---

### Visualizations Created
- Bar chart of landing page distribution by group (data validation)
- Conversion rate by country and group
- Difference in conversion rate per country (treatment - control)


## Recommendation
- Based on both **overall and segmented results**, the **new checkout page does not show statistically significant improvement**.
- I recommend **not proceeding with a full rollout** of the redesign at this time.


## Next Steps
- Gather **qualitative feedback** (e.g., user surveys or session recordings) to explore why the new page underperforms.
- Analyze **conversion by user segments** (device type, browser, traffic source).
- Run **multivariate or multistep funnel tests** to evaluate isolated changes in the redesign.