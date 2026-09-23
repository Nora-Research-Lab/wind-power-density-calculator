import gradio as gr
import matplotlib
matplotlib.use('Agg')
from wind_power_density_calculator import compute_wpd, classify_wpd, generate_plot

def calculate_wpd(v_avg, k, rho):
    try:
        if v_avg is None:
            return None, "Please enter a wind speed.", "", None
        v_avg = float(v_avg)
        k = float(k)
        rho = float(rho)
        wpd = compute_wpd(v_avg, k, rho)
        class_str, suitable = classify_wpd(wpd)
        fig = generate_plot(wpd)
        return round(wpd, 2), class_str, suitable, fig
    except ValueError as e:
        return None, f"Input error: {e}", "", None
    except Exception as e:
        return None, f"Unexpected error: {e}", "", None

with gr.Blocks(title="Wind Power Density Calculator") as demo:
    gr.Markdown("# Wind Power Density Calculator")
    with gr.Row():
        v_avg_input = gr.Number(label="Average Wind Speed (m/s)", value=6.0, minimum=0.1, maximum=30, step=0.1)
        k_input = gr.Number(label="Weibull Shape Parameter k", value=2.0, minimum=1.0, maximum=3.5, step=0.01)
        rho_input = gr.Number(label="Air Density (kg/m³)", value=1.225, minimum=0.8, maximum=1.5, step=0.001)
    calc_btn = gr.Button("Calculate")
    wpd_output = gr.Number(label="Wind Power Density (W/m²)", interactive=False, precision=2)
    class_output = gr.Textbox(label="Classification", lines=1)
    suitability_output = gr.Textbox(label="Suitability", lines=1)
    plot_output = gr.Plot(label="WPD vs Class Boundaries")

    calc_btn.click(
        fn=calculate_wpd,
        inputs=[v_avg_input, k_input, rho_input],
        outputs=[wpd_output, class_output, suitability_output, plot_output]
    )

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
