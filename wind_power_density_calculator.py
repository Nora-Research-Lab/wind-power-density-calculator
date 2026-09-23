import math
from math import gamma

def compute_weibull_scale(v_avg, k):
    if v_avg <= 0:
        raise ValueError("Average wind speed must be positive.")
    if k <= 0:
        raise ValueError("Weibull shape parameter k must be positive.")
    return v_avg / gamma(1 + 1/k)

def compute_mean_cubed_wind_speed(c, k):
    return c**3 * gamma(1 + 3/k)

def compute_wpd(v_avg, k=2.0, rho=1.225):
    if not (0 < v_avg <= 30):
        raise ValueError("Average wind speed must be between 0 and 30 m/s (exclusive of 0).")
    if not (1.0 <= k <= 3.5):
        raise ValueError("Weibull shape parameter k must be between 1.0 and 3.5.")
    if not (0.8 <= rho <= 1.5):
        raise ValueError("Air density must be between 0.8 and 1.5 kg/m³.")
    c = compute_weibull_scale(v_avg, k)
    e_v3 = compute_mean_cubed_wind_speed(c, k)
    return 0.5 * rho * e_v3

def classify_wpd(wpd):
    if wpd < 200:
        cls = 1
        label = "Poor"
    elif wpd < 300:
        cls = 2
        label = "Marginal"
    elif wpd < 400:
        cls = 3
        label = "Moderate"
    elif wpd < 500:
        cls = 4
        label = "Good"
    elif wpd < 600:
        cls = 5
        label = "Excellent"
    elif wpd < 800:
        cls = 6
        label = "Outstanding"
    else:
        cls = 7
        label = "Superb"
    class_str = f"Class {cls}: {label}"
    suitable = "Suitable for utility-scale turbines" if cls >= 3 else "Marginal / small turbines only"
    return class_str, suitable

def generate_plot(wpd):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    import numpy as np

    fig, ax = plt.subplots(figsize=(8, 3))
    ax.barh(['WPD'], [wpd], color='steelblue', height=0.5, label='Wind Power Density')
    boundaries = [200, 300, 400, 500, 600, 800]
    for b in boundaries:
        ax.axvline(x=b, color='gray', linestyle='--', linewidth=0.8)
    max_val = max(wpd, 800) * 1.2
    ax.set_xlim(0, max_val)
    ax.set_xlabel('W/m²')
    ax.set_title('Wind Power Density vs NREL Class Boundaries')
    for b, lbl in zip(boundaries, ['Class 1/2','Class 2/3','Class 3/4','Class 4/5','Class 5/6','Class 6/7']):
        ax.annotate(lbl, xy=(b, 0.5), xytext=(b, 0.8), fontsize=8, ha='center',
                    arrowprops=dict(arrowstyle='->', color='gray', lw=0.5))
    plt.tight_layout()
    return fig
