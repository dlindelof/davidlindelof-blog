#!/usr/bin/env python3
"""Generate the printable companion to the German noun-gender post."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path

from reportlab.lib.colors import HexColor, white
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas


INK = HexColor("#172033")
MUTED = HexColor("#64748B")
LINE = HexColor("#94A3B8")
CREAM = HexColor("#F8F4EA")
PAPER = HexColor("#FFFEFB")
ARTICLE_COLOURS = {
    "der": HexColor("#2563EB"),
    "die": HexColor("#DB2777"),
    "das": HexColor("#D97706"),
}
FONT_REGULAR = "HandoutSans"
FONT_BOLD = "HandoutSans-Bold"
FONT_ITALIC = "HandoutSans-Italic"


def register_fonts() -> None:
    candidates = (
        {
            FONT_REGULAR: Path("/System/Library/Fonts/Supplemental/Arial.ttf"),
            FONT_BOLD: Path("/System/Library/Fonts/Supplemental/Arial Bold.ttf"),
            FONT_ITALIC: Path("/System/Library/Fonts/Supplemental/Arial Italic.ttf"),
        },
        {
            FONT_REGULAR: Path("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"),
            FONT_BOLD: Path("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"),
            FONT_ITALIC: Path("/usr/share/fonts/truetype/dejavu/DejaVuSans-Oblique.ttf"),
        },
    )
    font_files = next(
        (font_set for font_set in candidates if all(path.exists() for path in font_set.values())),
        None,
    )
    if font_files is None:
        raise FileNotFoundError("Could not find Arial or DejaVu Sans fonts")
    for name, path in font_files.items():
        pdfmetrics.registerFont(TTFont(name, path))


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def draw_arrow(
    pdf: canvas.Canvas,
    x1: float,
    y1: float,
    x2: float,
    y2: float,
) -> None:
    pdf.setStrokeColor(LINE)
    pdf.setFillColor(LINE)
    pdf.setLineWidth(1.3)
    pdf.line(x1, y1, x2, y2)

    head = 5
    path = pdf.beginPath()
    if abs(x2 - x1) >= abs(y2 - y1):
        path.moveTo(x2, y2)
        path.lineTo(x2 - head, y2 + head * 0.65)
        path.lineTo(x2 - head, y2 - head * 0.65)
    else:
        path.moveTo(x2, y2)
        path.lineTo(x2 - head * 0.65, y2 + head)
        path.lineTo(x2 + head * 0.65, y2 + head)
    path.close()
    pdf.drawPath(path, stroke=0, fill=1)


def draw_article_pill(
    pdf: canvas.Canvas,
    x: float,
    y: float,
    article: str,
    width: float = 72,
    height: float = 34,
) -> None:
    pdf.setFillColor(ARTICLE_COLOURS[article])
    pdf.roundRect(
        x - width / 2,
        y - height / 2,
        width,
        height,
        height / 2,
        stroke=0,
        fill=1,
    )
    pdf.setFillColor(white)
    pdf.setFont(FONT_BOLD, 13)
    pdf.drawCentredString(x, y - 4.5, article)


def draw_footer(pdf: canvas.Canvas, page_number: int) -> None:
    width, _ = A4
    pdf.setStrokeColor(HexColor("#E2E8F0"))
    pdf.setLineWidth(0.6)
    pdf.line(42, 35, width - 42, 35)
    pdf.setFillColor(MUTED)
    pdf.setFont(FONT_REGULAR, 7.7)
    pdf.drawString(42, 22, "blog.davidlindelof.com")
    pdf.drawRightString(width - 42, 22, f"Page {page_number} of 2")


def draw_tree_page(
    pdf: canvas.Canvas,
    tree: list[dict[str, str]],
    core_size: int,
) -> None:
    width, height = A4
    pdf.setFillColor(PAPER)
    pdf.rect(0, 0, width, height, stroke=0, fill=1)

    pdf.setFillColor(INK)
    pdf.setFont(FONT_BOLD, 21)
    pdf.drawString(42, height - 58, "German noun gender")
    pdf.setFont(FONT_REGULAR, 11)
    pdf.setFillColor(MUTED)
    pdf.drawString(42, height - 80, "A compact decision tree and its memorized exception core")

    callout_y = height - 126
    pdf.setFillColor(HexColor("#EEF2F7"))
    pdf.roundRect(42, callout_y - 29, width - 84, 47, 8, stroke=0, fill=1)
    pdf.setFillColor(INK)
    pdf.setFont(FONT_REGULAR, 9.3)
    pdf.drawString(
        55,
        callout_y - 2,
        f"If the noun is not in the {core_size}-word exception core on page 2, start here.",
    )
    pdf.setFont(FONT_BOLD, 9.3)
    pdf.drawString(55, callout_y - 17, "Follow No downward. A Yes gives the article.")

    top_y = height - 190
    bottom_y = 158
    spacing = (top_y - bottom_y) / len(tree)
    question_x = 48
    question_width = 248
    question_height = 38
    question_centre_x = question_x + question_width / 2
    leaf_x = width - 91

    centres = [top_y - index * spacing for index in range(len(tree))]
    default_y = centres[-1] - spacing

    for index, (row, centre_y) in enumerate(zip(tree, centres)):
        pdf.setFillColor(CREAM)
        pdf.setStrokeColor(HexColor("#CBD5E1"))
        pdf.setLineWidth(0.8)
        pdf.roundRect(
            question_x,
            centre_y - question_height / 2,
            question_width,
            question_height,
            8,
            stroke=1,
            fill=1,
        )
        pdf.setFillColor(INK)
        question_font_size = 11.2
        while (
            stringWidth(row["question"], FONT_BOLD, question_font_size)
            > question_width - 24
            and question_font_size > 8.2
        ):
            question_font_size -= 0.2
        pdf.setFont(FONT_BOLD, question_font_size)
        pdf.drawCentredString(
            question_centre_x,
            centre_y - 4,
            row["question"],
        )

        draw_arrow(
            pdf,
            question_x + question_width,
            centre_y,
            leaf_x - 42,
            centre_y,
        )
        pdf.setFillColor(MUTED)
        pdf.setFont(FONT_REGULAR, 8.3)
        pdf.drawCentredString(
            (question_x + question_width + leaf_x - 42) / 2,
            centre_y + 8,
            "Yes",
        )
        draw_article_pill(pdf, leaf_x, centre_y, row["yes_article"])

        next_y = centres[index + 1] if index + 1 < len(centres) else default_y
        draw_arrow(
            pdf,
            question_centre_x,
            centre_y - question_height / 2,
            question_centre_x,
            next_y + question_height / 2,
        )
        pdf.setFillColor(MUTED)
        pdf.setFont(FONT_REGULAR, 8.3)
        pdf.drawString(
            question_centre_x + 7,
            (centre_y + next_y) / 2 - 3,
            "No",
        )

    default_article = next(
        row["no_article"]
        for row in tree
        if row.get("no_article") in ARTICLE_COLOURS
    )
    draw_article_pill(pdf, question_centre_x, default_y, default_article)
    pdf.setFillColor(MUTED)
    pdf.setFont(FONT_REGULAR, 8.3)
    pdf.drawRightString(question_centre_x - 43, default_y - 3, "otherwise")

    displayed_articles = {
        row["yes_article"] for row in tree
    } | {default_article}
    if "das" not in displayed_articles:
        pdf.setFillColor(MUTED)
        pdf.setFont(FONT_ITALIC, 7.8)
        pdf.drawString(
            42,
            49,
            "This accuracy-optimized tree has no das leaf; neuter exceptions are memorized on page 2.",
        )
    draw_footer(pdf, 1)
    pdf.showPage()


def draw_core_page(pdf: canvas.Canvas, core: list[dict[str, str]]) -> None:
    width, height = A4
    pdf.setFillColor(PAPER)
    pdf.rect(0, 0, width, height, stroke=0, fill=1)

    pdf.setFillColor(INK)
    pdf.setFont(FONT_BOLD, 21)
    pdf.drawString(42, height - 58, f"The {len(core)}-word exception core")
    pdf.setFillColor(MUTED)
    pdf.setFont(FONT_REGULAR, 9.6)
    pdf.drawString(
        42,
        height - 79,
        "The highest-frequency mistakes from the preliminary tree, listed alphabetically.",
    )
    pdf.setFont(FONT_ITALIC, 8.6)
    pdf.drawString(42, height - 95, "Learn the article together with the noun.")

    margin = 42
    top = height - 128
    bottom = 55
    column_count = 2 if len(core) <= 60 else 4
    rows_per_column = (len(core) + column_count - 1) // column_count
    column_width = (width - 2 * margin) / column_count
    row_height = min(24, (top - bottom) / rows_per_column)

    for index, row in enumerate(core):
        column = index // rows_per_column
        row_index = index % rows_per_column
        x = margin + column * column_width
        y = top - row_index * row_height

        if row_index % 2 == 0:
            pdf.setFillColor(HexColor("#F8FAFC"))
            pdf.roundRect(
                x - 4,
                y - row_height + 6,
                column_width - 7,
                row_height - 2,
                3,
                stroke=0,
                fill=1,
            )

        article = row["article"]
        noun = row["noun"]
        pdf.setFillColor(ARTICLE_COLOURS[article])
        article_font_size = 10.2 if column_count == 2 else 8.8
        pdf.setFont(FONT_BOLD, article_font_size)
        pdf.drawString(x, y - 8, article)

        noun_x = x + 21
        noun_font_size = 11.0 if column_count == 2 else 9.6
        available_width = column_width - 32
        while (
            stringWidth(noun, FONT_REGULAR, noun_font_size) > available_width
            and noun_font_size > 7.4
        ):
            noun_font_size -= 0.2
        pdf.setFillColor(INK)
        pdf.setFont(FONT_REGULAR, noun_font_size)
        pdf.drawString(noun_x, y - 8, noun)

    draw_footer(pdf, 2)
    pdf.showPage()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--core-csv", required=True, type=Path)
    parser.add_argument("--tree-csv", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    core = read_csv(args.core_csv)
    tree = read_csv(args.tree_csv)
    if not core or not tree:
        raise ValueError("Both input CSV files must contain data")
    if not all(row.get("article") in ARTICLE_COLOURS for row in core):
        raise ValueError("Unexpected article in core vocabulary")
    if not all(row.get("yes_article") in ARTICLE_COLOURS for row in tree):
        raise ValueError("Unexpected article in decision tree")

    register_fonts()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    pdf = canvas.Canvas(str(args.output), pagesize=A4, pageCompression=1)
    pdf.setTitle("German noun gender: core vocabulary and decision tree")
    pdf.setAuthor("David Lindelof")
    pdf.setSubject("Printable companion to the German noun-gender classifier post")
    draw_tree_page(pdf, tree, len(core))
    draw_core_page(pdf, core)
    pdf.save()


if __name__ == "__main__":
    main()
