#!/usr/bin/env python3
"""把網誌成品 HTML 轉成 markdown 鏡像（HTML 為真實來源 → md 供 git 版本史/閱讀）。

用法：
  python3 blog-html-to-md.py --html "<成品.html>" --out "<鏡像.md>" [--url "<Blogger 網址>"]

只擷取 <article ...> 內的內容；<style>、<colgroup>、<col> 略過。
支援 h2/h3、p、ul/ol+li、table（thead/tbody）、行內 <a>/<strong>。
標題取自 <title>。每次執行為完整重生成（不保留手動編輯）——
所以網址等中繼資訊用 --url 帶入，保持可重現。
"""
import argparse
import re
import sys
from html.parser import HTMLParser

INLINE_BLOCKS = {"h2", "h3", "p", "li", "td", "th"}


def collapse(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


class BlogParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.title = ""
        self.blocks = []
        self.in_title = False
        self.in_style = False
        self.in_article = False
        self.capturing = False
        self.buf = ""
        self.cur_tag = None
        # links
        self.in_a = False
        self.a_href = ""
        self.a_buf = ""
        # lists
        self.list_items = None
        # tables
        self.in_table = False
        self.rows = None
        self.cur_row = None

    # --- helpers ---
    def _start_capture(self, tag):
        self.capturing = True
        self.cur_tag = tag
        self.buf = ""

    def _finish_capture(self):
        text = collapse(self.buf)
        self.capturing = False
        self.cur_tag = None
        self.buf = ""
        return text

    # --- tag handlers ---
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "title":
            self.in_title = True
            return
        if tag == "style":
            self.in_style = True
            return
        if tag == "article":
            self.in_article = True
            return
        if not self.in_article:
            return
        if tag in ("colgroup", "col"):
            return
        if tag == "a" and self.capturing:
            self.in_a = True
            self.a_href = a.get("href", "")
            self.a_buf = ""
            return
        if tag in ("strong", "b") and self.capturing:
            self.buf += "**"
            return
        if tag == "br" and self.capturing:
            self.buf += " "
            return
        if tag in ("ul", "ol"):
            self.list_items = []
            return
        if tag == "table":
            self.in_table = True
            self.rows = []
            return
        if tag == "tr" and self.in_table:
            self.cur_row = []
            return
        if tag in ("td", "th") and self.in_table:
            self._start_capture(tag)
            return
        if tag in INLINE_BLOCKS:
            self._start_capture(tag)

    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False
            return
        if tag == "style":
            self.in_style = False
            return
        if tag == "article":
            self.in_article = False
            return
        if not self.in_article:
            return
        if tag == "a" and self.in_a:
            self.buf += f"[{collapse(self.a_buf)}]({self.a_href})"
            self.in_a = False
            self.a_href = ""
            self.a_buf = ""
            return
        if tag in ("strong", "b") and self.capturing:
            self.buf += "**"
            return
        if tag in ("td", "th") and self.in_table:
            self.cur_row.append(self._finish_capture())
            return
        if tag == "tr" and self.in_table:
            if self.cur_row:
                self.rows.append(self.cur_row)
            self.cur_row = None
            return
        if tag == "table":
            self._emit_table()
            self.in_table = False
            self.rows = None
            return
        if tag in ("ul", "ol"):
            if self.list_items:
                self.blocks.append("\n".join("- " + it for it in self.list_items))
            self.list_items = None
            return
        if tag == "li":
            self.list_items.append(self._finish_capture())
            return
        if tag == "h2":
            self.blocks.append("## " + self._finish_capture())
            return
        if tag == "h3":
            self.blocks.append("### " + self._finish_capture())
            return
        if tag == "p":
            text = self._finish_capture()
            if text:
                self.blocks.append(text)

    def handle_data(self, data):
        if self.in_style:
            return
        if self.in_title:
            self.title += data
            return
        if self.in_a:
            self.a_buf += data
            return
        if self.capturing:
            self.buf += data

    def _emit_table(self):
        if not self.rows:
            return
        header = self.rows[0]
        body = self.rows[1:]
        n = len(header)
        lines = ["| " + " | ".join(header) + " |",
                 "|" + "|".join(["---"] * n) + "|"]
        for r in body:
            r = (r + [""] * n)[:n]
            lines.append("| " + " | ".join(r) + " |")
        self.blocks.append("\n".join(lines))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--html", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--url", default="")
    args = ap.parse_args()

    with open(args.html, encoding="utf-8") as f:
        p = BlogParser()
        p.feed(f.read())

    title = collapse(p.title) or "(無標題)"
    note = ["> 網誌成品 **HTML 為真實來源**（OneDrive），本檔由 `blog-html-to-md.py` 自動轉出，供 git 版本史與閱讀。",
            "> 每次發佈/定稿後重跑此腳本即可；請勿手動改本檔。"]
    if args.url:
        note.append(f"> 已發佈：<{args.url}>")

    parts = [f"# {title}", "\n".join(note), "---"] + p.blocks
    out = "\n\n".join(parts).rstrip() + "\n"
    with open(args.out, "w", encoding="utf-8") as f:
        f.write(out)
    print(f"✓ 轉出 {args.out}（{len(p.blocks)} 區塊；標題：{title}）", file=sys.stderr)


if __name__ == "__main__":
    main()
