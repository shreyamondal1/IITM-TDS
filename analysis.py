# 23f1001792@ds.study.iitm.ac.in  <-- required email as comment

import marimo

app = marimo.App()

# ----------------------------------------------------------
# Cell 1: Import libs + create some sample data
# Documenting data flow: This data is used by Cell 2 and Cell 3.
# ----------------------------------------------------------
@app.cell
def cell_1():
    import numpy as np
    import pandas as pd

    # Simple synthetic dataset
    x = np.linspace(0, 10, 100)
    y = 2 * x + 5  # linear relationship

    df = pd.DataFrame({"x": x, "y": y})
    df
    return df


# ----------------------------------------------------------
# Cell 2: Interactive widget (slider)
# Data flow: slider value → feeds into dynamic markdown + chart
# ----------------------------------------------------------
@app.cell
def cell_2():
    import marimo as mo

    slope_slider = mo.ui.slider(start=1, stop=5, step=0.1, value=2.0, label="Adjust slope")
    slope_slider
    return slope_slider


# ----------------------------------------------------------
# Cell 3: Dynamic markdown depending on slider
# Data flow: slope_slider.value → dynamic text + computed values
# ----------------------------------------------------------
@app.cell
def cell_3(slope_slider):
    import marimo as mo

    md = mo.md(f"""
    ## Dynamic Analysis

    The current slope selected is **{slope_slider.value}**.

    We use this value to recompute the predicted relationship:

    **y = {slope_slider.value} × x + 5**
    """)

    md
    return md


# ----------------------------------------------------------
# Cell 4: Plot using modified slope
# Data flow: uses df from Cell 1 + slider from Cell 2
# ----------------------------------------------------------
@app.cell
def cell_4(df, slope_slider):
    import matplotlib.pyplot as plt

    plt.figure(figsize=(6,4))
    plt.plot(df["x"], df["y"], label="Original line")
    plt.plot(df["x"], slope_slider.value * df["x"] + 5,
             label=f"New slope = {slope_slider.value}")
    plt.legend()
    plt.title("Interactive Relationship Plot")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.show()


# ----------------------------------------------------------
# Launch app
# ----------------------------------------------------------
if __name__ == "__main__":
    app.run()
