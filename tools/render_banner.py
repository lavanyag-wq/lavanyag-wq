"""Render the profile hero banner to a committed, animated SVG.

All motion is SMIL (animate, animateTransform): GitHub serves committed
SVGs through an img tag, where SMIL and CSS run but scripts do not, so the
animation needs no JavaScript and degrades to the static frame anywhere
animations are off. The gradient lives inside the SVG because GitHub's
sanitizer strips style attributes from README markup. Deterministic output:
same code, same bytes.
"""

from __future__ import annotations

import math
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "assets" / "banner.svg"
W, H = 960, 220


def main() -> None:
    cols = [90, 230, 370, 510]
    layers = [4, 5, 5, 3]
    pos = {}
    for c, (x, n) in enumerate(zip(cols, layers, strict=True)):
        for i in range(n):
            y = H / 2 + (i - (n - 1) / 2) * 34
            pos[(c, i)] = (x, y)
    edges = []
    k = 0
    for c in range(len(cols) - 1):
        for i in range(layers[c]):
            for j in range(layers[c + 1]):
                x1, y1 = pos[(c, i)]
                x2, y2 = pos[(c + 1, j)]
                base = 0.14 + 0.08 * math.sin(i + j)
                begin = (k * 0.37) % 4.0
                edges.append(
                    f'<line x1="{x1}" y1="{y1:.0f}" x2="{x2}" y2="{y2:.0f}" '
                    f'stroke="#7da7c7" stroke-width="1.1" opacity="{base:.2f}" '
                    f'stroke-dasharray="6 90">'
                    f'<animate attributeName="stroke-dashoffset" from="96" to="0" '
                    f'dur="4s" begin="{begin:.2f}s" repeatCount="indefinite"/>'
                    f'<animate attributeName="opacity" '
                    f'values="{base:.2f};{base + 0.25:.2f};{base:.2f}" dur="4s" '
                    f'begin="{begin:.2f}s" repeatCount="indefinite"/></line>')
                k += 1
    nodes = []
    for (c, i), (x, y) in pos.items():
        r = 7 if c in (0, len(cols) - 1) else 5
        begin = ((c * 5 + i) * 0.45) % 3.6
        nodes.append(
            f'<circle cx="{x}" cy="{y:.0f}" r="{r}" fill="url(#node)">'
            f'<animate attributeName="r" values="{r};{r + 1.8:.1f};{r}" dur="3.6s" '
            f'begin="{begin:.2f}s" repeatCount="indefinite"/></circle>')
    particles = []
    for i in range(6):
        px = 560 + i * 64
        dur = 7 + (i % 3) * 2
        particles.append(
            f'<circle cx="{px}" cy="210" r="2" fill="#7cf5c8" opacity="0.0">'
            f'<animate attributeName="cy" values="214;6" dur="{dur}s" '
            f'begin="{i * 1.3:.1f}s" repeatCount="indefinite"/>'
            f'<animate attributeName="opacity" values="0;0.5;0" dur="{dur}s" '
            f'begin="{i * 1.3:.1f}s" repeatCount="indefinite"/></circle>')
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
<defs>
<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
<stop offset="0" stop-color="#0d1b2a">
<animate attributeName="stop-color" values="#0d1b2a;#12263c;#0d1b2a" dur="12s" repeatCount="indefinite"/>
</stop>
<stop offset="1" stop-color="#1b3a4b">
<animate attributeName="stop-color" values="#1b3a4b;#14453f;#1b3a4b" dur="12s" repeatCount="indefinite"/>
</stop>
</linearGradient>
<linearGradient id="head" x1="-1" y1="0" x2="0" y2="0" gradientUnits="objectBoundingBox" spreadMethod="reflect">
<stop offset="0" stop-color="#9be7ff"/><stop offset="0.5" stop-color="#7cf5c8"/>
<stop offset="1" stop-color="#ffd166"/>
<animate attributeName="x1" values="-1;1;-1" dur="6s" repeatCount="indefinite"/>
<animate attributeName="x2" values="0;2;0" dur="6s" repeatCount="indefinite"/>
</linearGradient>
<radialGradient id="node"><stop offset="0" stop-color="#bfe9ff"/>
<stop offset="1" stop-color="#5c93b8"/></radialGradient>
</defs>
<rect width="{W}" height="{H}" fill="url(#bg)"/>
{''.join(edges)}
{''.join(nodes)}
{''.join(particles)}
<text x="600" y="92" font-family="Helvetica, Arial, sans-serif" font-size="40"
 font-weight="bold" fill="url(#head)">Lavanya Gurrapu</text>
<text x="600" y="126" font-family="Helvetica, Arial, sans-serif" font-size="17"
 fill="#d7e8f2">Data Scientist: ML, Predictive Analytics and MLOps
<animate attributeName="opacity" values="0;1" dur="1.2s" fill="freeze"/></text>
<text x="600" y="162" font-family="Helvetica, Arial, sans-serif" font-size="14"
 fill="#9fc2d4">Turning large-scale behavioral data into models,
<animate attributeName="opacity" values="0;0;1" dur="1.8s" fill="freeze"/></text>
<text x="600" y="184" font-family="Helvetica, Arial, sans-serif" font-size="14"
 fill="#9fc2d4">experiments and decisions that hold up in production.
<animate attributeName="opacity" values="0;0;1" dur="2.2s" fill="freeze"/></text>
</svg>'''
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(svg)
    print(f"wrote {OUT} ({len(svg)} bytes)")


if __name__ == "__main__":
    main()
