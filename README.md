# Global Climate Risk Profiling (GCRP)

This project analyzes global climate data to identify countries experiencing the most drastic changes in climate patterns—such as temperature, rainfall and many more.

---

## 📊 Data Source & Citation

This project uses climate data provided by the [National Centers for Environmental Information (NCEI), NOAA](https://www.ncei.noaa.gov/).

**Data Source:**  
[NCEI Climate Data Online (CDO) API](https://www.ncei.noaa.gov/access/services/data/v1)

**Cite as:**  
Menne, Matthew J., Imke Durre, Bryant Korzeniewski, Shelley McNeill, Kristy Thomas, Xungang Yin, Steven Anthony, Ron Ray, Russell S. Vose, Byron E.Gleason, and Tamara G. Houston (2012): Global Historical Climatology Network - Daily (GHCN-Daily), Version 3. [indicate subset used]. NOAA National Climatic Data Center. doi:[10.7289/V5D21VHZ](https://doi.org/10.7289/V5D21VHZ) [access date].

**Publications citing this dataset should also cite:**  
Matthew J. Menne, Imke Durre, Russell S. Vose, Byron E. Gleason, and Tamara G. Houston, 2012: An Overview of the Global Historical Climatology Network-Daily Database. J. Atmos. Oceanic Technol., 29, 897-910. [doi:10.1175/JTECH-D-11-00103.1](https://doi.org/10.1175/JTECH-D-11-00103.1)

> **Thank you to the NOAA NCEI team for making this valuable data publicly available!**

---

## 🚀 Getting Started

### 1. **Data Folder Required**
- All notebooks and scripts **assume a `data/` folder exists** in your project root.
- If you’re using Google Colab, upload the `data/` folder before running any notebooks.
- The data is already provided in this repository for convenience.  
  *(If you want to collect new data, see below.)*

### 2. **Running the Notebooks**
- **Run the notebooks in order:**  
  The workflow assumes you execute notebooks serially, from `00_...ipynb` to `10_...ipynb`.
- Each notebook builds on the outputs of the previous one.

### 3. **Collecting New Data**
- Data is collected from:  
  [`https://www.ncei.noaa.gov/access/services/data/v1`](https://www.ncei.noaa.gov/access/services/data/v1)
- **API Key Required:**  
  To collect new data, you must obtain an API key from the [NOAA website](https://www.ncdc.noaa.gov/cdo-web/token).
- Place your API key in a `.env` file as described in the code.
- Run the scripts in `src/data/` to fetch new data.

### 4. **Data & Parameters**
- For detailed information about climate parameters, columns, and their meanings, please refer to the [NOAA documentation](https://www.ncei.noaa.gov/support/access-data-service-api-user-documentation).

---

## 🌍 Key Insights

- **Riskiest countries:**  
  Countries identified as "riskiest" are those that have suffered the most drastic changes in climate patterns—either increases or decreases in temperature, rainfall, and other factors—over the two decades analyzed.
- **Antarctica and similar regions:**  
  Even a slight increase in temperature in regions like Antarctica is significant. We calculated **percentage change** to fairly compare all countries and selected the riskiest accordingly.
- **Disclaimer:**  
  These calculations are **not official** and may be subject to error. Even small modifications in methodology or data can alter the results.

---

## ⚡️ Notes

- Most of the logic and analysis was designed by me.
- Some code generation and automation was assisted by Google Gemini.

---

## 📂 Project Structure

- `data/` — Raw and processed climate data (required for all notebooks).
- `models/` — Saved models (if applicable).
- `reports/` — Generated figures and reports.
- `src/` — Source code for data collection and analysis.
- `notebooks/` — Jupyter/Colab notebooks (run in order).

---

## 📢 Contributing

This project is intended for educational and research purposes.  
Feel free to fork, adapt, or suggest improvements!

---

## 📜 License

[MIT License](LICENSE)
