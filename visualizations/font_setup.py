"""Utilities for enabling Chinese text rendering in generated visualizations.

Matplotlib/Seaborn and Plotly do not bundle CJK fonts by default, so Chinese
characters can appear as squares or blanks. Import and call
``configure_chinese_font`` before creating plots to register a CJK font and set
common rendering defaults (including fixing the minus sign).
"""

from __future__ import annotations

import warnings
from pathlib import Path
from typing import Optional

import plotly.io as pio

try:
    from matplotlib import font_manager, rcParams  # type: ignore
except Exception as exc:  # pragma: no cover - import guard for environments without matplotlib
    raise ImportError(
        "matplotlib is required for Chinese font configuration. Install it with `pip install matplotlib`."
    ) from exc


DEFAULT_FONT_FILENAME = "NotoSansSC-Regular.otf"
DEFAULT_FONT_DIR = Path(__file__).resolve().parent / "fonts"
DEFAULT_FONT_PATH = DEFAULT_FONT_DIR / DEFAULT_FONT_FILENAME


def configure_chinese_font(font_path: Optional[Path] = None) -> Optional[Path]:
    """Register a Chinese font for Matplotlib/Seaborn and Plotly.

    Args:
        font_path: Optional explicit path to a font file. If omitted, the helper
            looks for ``visualizations/fonts/NotoSansSC-Regular.otf``.

    Returns:
        The font path that was registered, or ``None`` when no font was found.
    """

    selected_font = Path(font_path) if font_path else DEFAULT_FONT_PATH

    if not selected_font.exists():
        warnings.warn(
            f"Chinese font not found at {selected_font}. "
            "Place a CJK font (e.g., NotoSansSC-Regular.otf) in the visualizations/fonts directory "
            "to enable Chinese text rendering.",
            stacklevel=2,
        )
        return None

    # Register the font with Matplotlib and rebuild the cache so seaborn picks it up.
    font_manager.fontManager.addfont(str(selected_font))
    font_manager._rebuild()  # type: ignore[attr-defined]

    # Matplotlib needs the font's internal name, not the filename.
    font_name = font_manager.FontProperties(fname=str(selected_font)).get_name()

    rcParams.update(
        {
            "font.sans-serif": [
                font_name,
                "Noto Sans CJK SC",
                "Noto Sans SC",
                "Microsoft YaHei",
                "SimHei",
                "sans-serif",
            ],
            "font.family": "sans-serif",
            # Avoid minus sign rendering as boxes when using custom fonts
            "axes.unicode_minus": False,
        }
    )

    # Apply the same font to Plotly templates so HTML charts render Chinese correctly.
    cn_template = pio.templates["plotly_white"].layout.copy()
    cn_template.font.family = font_name
    pio.templates["cn_default"] = pio.templates["plotly_white"].update(layout=cn_template)
    pio.templates.default = "cn_default"

    return selected_font


if __name__ == "__main__":
    font_used = configure_chinese_font()
    if font_used is None:
        print(
            "⚠️  No Chinese font found. Download a CJK font (e.g., NotoSansSC-Regular.otf) "
            "and place it in visualizations/fonts/, then rerun this script."
        )
    else:
        print(f"✅ Chinese font registered: {font_used}")
