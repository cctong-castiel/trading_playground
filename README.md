# Trading View Library
## Introduction
This repository contains a lightweight, modular framework for building and visualising financial‑time‑series data.  
It is designed to be **plug‑and‑play**: download data from Yahoo Finance, run a variety of technical indicators, and render the results with `lightweight_charts`.

Lightweight_charts is a python package which using TradingView open source codes to allow developers to build a fancy trading UI with customized functionalities.

## Purpose
* **Rapid prototyping** – quickly experiment with new indicators or data‑sources.  
* **Educational** – a clear, well‑structured codebase that demonstrates how to build trading tools with Python.  
* **Re‑usability** – each indicator lives in its own module and can be dropped into any project that needs it.

## Quick Start
> **Prerequisites** – Python 3.10+ and the packages listed in `requirements.txt`.  
> ```bash
> pip install -r lib/requirements.txt
> ```

### Run the main script
The top‑level `main.py` demonstrates the data‑download and indicator pipeline.

```bash
python src/main.py
```

### Test the plotting routine
The `plotting.py` module shows the OHLC chart, RSI and Stochastic Oscillator in separate windows.

```bash
python src/trading_funcs/charting/plotting.py
```

## Reference
1. lightweight-chart pypi: https://pypi.org/project/lightweight-charts-2/
2. lightweight-chart repository: https://github.com/louisnw01/lightweight-charts-python/tree/052d778beda66f569175cbe6774aba5d3e3b1dea
3. Replicating TradingView Chart in Python: https://www.insightbig.com/post/replicating-tradingview-chart-in-python

## Acknowledgement
1. TradingView free-charting-libraries: https://www.tradingview.com/free-charting-libraries/