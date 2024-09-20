import gradio as gr
from modules import script_callbacks, shared
from modules.options import options_section

mapping = [
    (info.infotext, k) for k, info in shared.opts.data_labels.items() if info.infotext
]

shared.options_templates.update(
    options_section(
        ("uiux_core", "Anapnoe UI-UX", "anapnoe"),
        {
            "uiux_enable_console_log": shared.OptionInfo(False, "Enable console log"),
            "uiux_max_resolution_output": shared.OptionInfo(
                2048, "Max resolution output for txt2img and img2img"
            ),
            "uiux_show_input_range_ticks": shared.OptionInfo(
                True, "Show ticks for input range slider"
            ),
            "uiux_no_slider_layout": shared.OptionInfo(False, "No input range sliders"),
            "uiux_disable_transitions": shared.OptionInfo(False, "Disable transitions"),
            "uiux_default_layout": shared.OptionInfo(
                "Auto", "Layout", gr.Radio, {"choices": ["Auto", "Desktop", "Mobile"]}
            ),
            "uiux_mobile_scale": shared.OptionInfo(
                0.7,
                "Mobile scale",
                gr.Slider,
                {"minimum": 0.5, "maximum": 1, "step": 0.05},
            ),
            "uiux_show_labels_aside": shared.OptionInfo(
                False, "Show labels for aside tabs"
            ),
            "uiux_show_labels_main": shared.OptionInfo(
                False, "Show labels for main tabs"
            ),
            "uiux_show_labels_tabs": shared.OptionInfo(
                False, "Show labels for page tabs"
            ),
            "uiux_ignore_overrides": shared.OptionInfo(
                [],
                "Ignore Overrides",
                gr.CheckboxGroup,
                lambda: {"choices": list(mapping)},
            ),
        },
    )
)

def on_ui_tabs():
    with gr.Blocks(analytics_enabled=False) as anapnoe_sd_uiux_core:
        pass

    return ((anapnoe_sd_uiux_core, "UI-UX Core", "anapnoe_sd_uiux_core"),)

script_callbacks.on_ui_tabs(on_ui_tabs)

