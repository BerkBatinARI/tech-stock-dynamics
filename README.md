# Tech Stock Dynamics
### Relative Performance of Major Technology Stocks Through Time

A reproducible finance visualization project that explores how major technology stocks change in relative performance over time.

Goal: build a clean quant-style workflow: data → cleaned price panel → normalised performance series → ranking dynamics → static plots + animated visualisation.

* * *
## Project structure (high level)

* `src/` — reproducible scripts you run from terminal (`python src/...`)
* `data/` — downloaded datasets (kept out of git except a `.gitkeep`)
* `output/` — generated outputs (ignored by git, except selected tracked figures if needed)

* * *
## What this project will do

* Download daily adjusted close data for selected major tech stocks
* Clean and align the time series into a common trading-date panel
* Normalise all stocks to a common starting value for fair comparison
* Build ranking data showing how leadership changes over time
* Produce:
  * static comparison charts
  * an animated bar-chart-style visualisation of changing stock leadership

* * *
## Planned build steps

* Step 1: initialise repo structure and reproducible setup
* Step 2: download and clean historical stock data
* Step 3: normalise prices and prepare ranking dataset
* Step 4: build a static comparison chart
* Step 5: build the animated visualisation
* Step 6: export outputs and finalise documentation

* * *
## Reproduce locally

### 1) Create venv + install deps

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt