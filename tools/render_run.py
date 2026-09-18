"""Render a live-run JSON file as a terminal-style PNG for the README."""

from __future__ import annotations

import json
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


def _font(size: int) -> ImageFont.ImageFont:
    for name in ("consola.ttf", "Consolas.ttf", "DejaVuSansMono.ttf", "cour.ttf"):
        try:
            return ImageFont.truetype(name, size)
        except OSError:
            continue
    return ImageFont.load_default()


def render(json_path: Path, png_path: Path) -> None:
    data = json.loads(json_path.read_text(encoding="utf-8"))
    pretty = json.dumps(data, indent=2)
    lines = pretty.splitlines()
    if len(lines) > 48:
        lines = lines[:48] + ["  …"]
    header = [
        "jev-master  ·  POST https://api.typesafe.ai/v1/systemone  ·  model=jev-latest",
        "live run  ·  typed answers  ·  composed in code  ·  not an LLM chat",
        "",
    ]
    body = header + lines
    font = _font(16)
    line_h = 22
    width = 1100
    height = 40 + line_h * len(body) + 40
    image = Image.new("RGB", (width, height), (11, 15, 20))
    draw = ImageDraw.Draw(image)
    draw.rectangle((0, 0, width, 8), fill=(45, 212, 191))
    y = 28
    for i, line in enumerate(body):
        if i < 2:
            color = (94, 234, 212)
        elif '"decision"' in line or '"action"' in line or '"department"' in line:
            color = (250, 204, 21)
        elif '"choice"' in line or '"score"' in line or '"noul"' in line:
            color = (167, 139, 250)
        else:
            color = (226, 232, 240)
        draw.text((28, y), line[:110], font=font, fill=color)
        y += line_h
    png_path.parent.mkdir(parents=True, exist_ok=True)
    image.save(png_path, "PNG")


if __name__ == "__main__":
    src = Path(sys.argv[1])
    dest = Path(sys.argv[2])
    render(src, dest)
    print(dest)
