"""Render the profile hero banner to a committed SVG, deterministically.

The gradient lives inside the SVG because GitHub's sanitizer strips style
attributes and inline SVG from a README, so a gradient headline can only
arrive as a committed image. Explicit width and height so the img renders
with its aspect ratio everywhere.
"""

from __future__ import annotations

import math
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "assets" / "banner.svg"
W, H = 960, 220


def main() -> None:
    nodes = []
    edges = []
    cols = [90, 230, 370, 510]
    layers = [4, 5, 5, 3]
    pos = {}
    for c, (x, n) in enumerate(zip(cols, layers, strict=True)):
        for i in range(n):
            y = H / 2 + (i - (n - 1) / 2) * 34
            pos[(c, i)] = (x, y)
    for c in range(len(cols) - 1):
        for i in range(layers[c]):
            for j in range(layers[c + 1]):
                x1, y1 = pos[(c, i)]
                x2, y2 = pos[(c + 1, j)]
                opacity = 0.18 + 0.1 * math.sin(i + j)
                edges.append(f'<line x1="{x1}" y1="{y1:.0f}" x2="{x2}" y2="{y2:.0f}" '
                             f'stroke="#7da7c7" stroke-width="1" opacity="{opacity:.2f}"/>')
    for (c, i), (x, y) in pos.items():
        r = 7 if c in (0, len(cols) - 1) else 5
        nodes.append(f'<circle cx="{x}" cy="{y:.0f}" r="{r}" fill="url(#node)"/>')
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
<defs>
<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
<stop offset="0" stop-color="#0d1b2a"/><stop offset="1" stop-color="#1b3a4b"/>
</linearGradient>
<linearGradient id="head" x1="0" y1="0" x2="1" y2="0">
<stop offset="0" stop-color="#9be7ff"/><stop offset="0.5" stop-color="#7cf5c8"/>
<stop offset="1" stop-color="#ffd166"/>
</linearGradient>
<radialGradient id="node"><stop offset="0" stop-color="#bfe9ff"/>
<stop offset="1" stop-color="#5c93b8"/></radialGradient>
</defs>
<rect width="{W}" height="{H}" fill="url(#bg)"/>
{''.join(edges)}
{''.join(nodes)}
<text x="600" y="92" font-family="Helvetica, Arial, sans-serif" font-size="40"
 font-weight="bold" fill="url(#head)">Lavanya Gurrapu</text>
<text x="600" y="126" font-family="Helvetica, Arial, sans-serif" font-size="17"
 fill="#d7e8f2">Data Scientist: ML, Predictive Analytics and MLOps</text>
<text x="600" y="162" font-family="Helvetica, Arial, sans-serif" font-size="14"
 fill="#9fc2d4">Turning large-scale behavioral data into models,</text>
<text x="600" y="184" font-family="Helvetica, Arial, sans-serif" font-size="14"
 fill="#9fc2d4">experiments and decisions that hold up in production.</text>
</svg>'''
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(svg)
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
