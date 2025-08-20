# analysis.py
# Author: 23f2000814@ds.study.iitm.ac.in
# Interactive Data Analysis with Marimo

import marimo

__generated_with = "0.8.0"
app = marimo.App()


@app.cell
def __():
    # Author: 23f2000814@ds.study.iitm.ac.in
    # Interactive Data Analysis with Marimo
    # This notebook demonstrates reactive programming with variable dependencies
    
    import marimo as mo
    import numpy as np
    import pandas as pd
    import plotly.express as px
    import plotly.graph_objects as go
    from datetime import datetime, timedelta
    
    mo.md("""
    # Interactive Data Analysis with Marimo
    
    **Author:**  
    23f2000814@ds.study.iitm.ac.in  
    
    **Date:** August 20, 2025
    
    This notebook demonstrates Marimo's reactive programming capabilities with:
    - Variable dependencies between cells
    - Interactive widgets
    - Dynamic markdown output
    - Real-time data visualization
    """)
    return datetime, go, mo, np, pd, px, timedelta


@app.cell
def __(np, pd, timedelta, datetime):
    # Generate sample dataset: daily data for 100 days
    np.random.seed(42)
    days = 100
    dates = [datetime.today() - timedelta(days=i) for i in range(days)]
    data = pd.DataFrame({
        "date": dates[::-1],
        "x": np.linspace(0, 10, days),
        "y": np.sin(np.linspace(0, 10, days)) + np.random.normal(0, 0.1, days)
    })
    data.head()
    return data, dates, days


@app.cell
def __(mo):
    # Create an interactive slider widget for selecting window size
    window_slider = mo.ui.slider(start=1, stop=20, value=5, label="Rolling Mean Window Size")
    window_slider
    return window_slider,


@app.cell
def __(data, window_slider, pd):
    # Compute rolling mean (dependent on window_slider value)
    data_with_mean = data.copy()
    data_with_mean["y_mean"] = data_with_mean["y"].rolling(window=window_slider.value).mean()
    data_with_mean.head()
    return data_with_mean,


@app.cell
def __(px, data_with_mean, window_slider):
    # Plot interactive visualization with rolling mean
    fig = px.line(data_with_mean, x="date", y=["y", "y_mean"],
                  labels={"value": "Signal", "date": "Date"},
                  title=f"Signal with Rolling Mean (window={window_slider.value})")
    fig
    return fig,


@app.cell
def __(mo, window_slider):
    # Dynamic Markdown output that reacts to slider state
    mo.md(f"""
    ## ℹ️ Analysis Report
    
    Current rolling window size: **{window_slider.value}**
    
    {"🟢" * window_slider.value}
    """)
    return


@app.cell
def __(mo):
    # Explanation of notebook dependencies
    mo.md("""
    ---
    ## 📋 Notebook Structure & Dependencies
    
    - Cell 2 generates the dataset.
    - Cell 3 defines the slider widget.
    - Cell 4 computes rolling mean (depends on slider value).
    - Cell 5 visualizes raw data + rolling mean.
    - Cell 6 outputs dynamic markdown reacting to slider state.
    
    **Author:**  
    23f2000814@ds.study.iitm.ac.in  
    
    **Created with**: Marimo v0.8.0  
    **Date**: August 20, 2025
    """)
    return


if __name__ == "__main__":
    app.run()