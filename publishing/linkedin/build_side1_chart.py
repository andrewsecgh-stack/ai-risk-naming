import cairosvg

W, H = 1080, 1260
PAD = 68
USABLE = W - 2*PAD
FONT = "DejaVu Sans, Arial, sans-serif"

INK="#1A1A17"; SEC="#5F5E5A"; MUT="#9A9992"; FAINT="#C9C7C0"
BLUE="#185FA5"; RED="#A32D2D"; AMB="#8A5410"
LINE="#E2E0D8"; WHITE="#FFFFFF"

warn=[]
def esc(s): return s.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")
def txt(x,y,s,size,color,weight=400,anchor="start",style=""):
    if anchor=="start" and len(s)*0.60*size > USABLE:
        warn.append(f"OVERFLOW: {s!r} @ {size}")
    return (f'<text x="{x}" y="{y}" font-family="{FONT}" font-size="{size}" font-weight="{weight}" '
            f'fill="{color}" text-anchor="{anchor}"{style}>{esc(s)}</text>')

p=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
   f'<rect width="{W}" height="{H}" fill="{WHITE}"/>']

y = 96
p.append(txt(PAD, y, "Side 1 — the people behind the risks", 40, INK, 500)); y += 44
p.append(txt(PAD, y, "Naming the human scenarios behind the OWASP LLM Top 10.", 23, SEC)); y += 30
p.append(txt(PAD, y, "This chart is deliberately unfinished.", 23, BLUE, 500)); y += 46
p.append(f'<rect x="{PAD}" y="{y}" width="{USABLE}" height="2" fill="{LINE}"/>'); y += 46

def section(label, color):
    global y
    p.append(txt(PAD, y, label, 21, color, 500)); y += 44

def row(name, line, tag, name_color, line_color, tag_color, gap=False):
    global y
    if gap:
        p.append(f'<rect x="{PAD}" y="{y-20}" width="{USABLE}" height="46" rx="6" fill="none" '
                 f'stroke="{FAINT}" stroke-width="1.5" stroke-dasharray="6 5"/>')
        p.append(txt(PAD+18, y+8, name, 22, MUT, 400))
        p.append(txt(W-PAD-18, y+8, tag, 19, MUT, 400, "end"))
        y += 62
    else:
        p.append(txt(PAD, y, name, 27, name_color, 500))
        p.append(txt(W-PAD, y, tag, 19, tag_color, 500, "end"))
        y += 27
        p.append(txt(PAD, y, line, 21, line_color))
        y += 48

section("WORKED — full entries written", INK)
row("The Disgruntled Employee", "Angry insider burns tokens before access is cut.", "malicious · LLM10", INK, SEC, RED)
row("The Plant", "Never loyal — placed to take from day one.", "malicious · LLM02/06", INK, SEC, RED)
row("The Ghost Login", "Access and agents nobody answers for anymore.", "malicious / none · LLM10/02/06", INK, SEC, RED)

y += 12
section("SKETCHED — a name and a line, not yet worked", SEC)
row("The Oversharer", "Pastes company secrets into a public AI tool.", "negligent · LLM02", SEC, MUT, AMB)
row("The Overengineer", "Burns 20x the tokens through needless complexity.", "ignorant · LLM10", SEC, MUT, AMB)
row("The Runaway Agent", "A well-meant agent loops unbounded, and bills you.", "negligent · LLM10", SEC, MUT, AMB)
row("The Poisoned PDF", "Hidden instructions ride in on a shared document.", "malicious · LLM01", SEC, MUT, AMB)

y += 12
section("GAPS — no persona yet. Your turn.", MUT)
row("?", "", "LLM03 · supply chain", 0,0,0, gap=True)
row("?", "", "LLM07 · system prompt leakage", 0,0,0, gap=True)
row("?", "", "LLM08 · vector & embedding weaknesses", 0,0,0, gap=True)
row("?", "", "LLM09 · misinformation", 0,0,0, gap=True)

p.append(txt(PAD, H-52, "The Disgruntled Employee: the AI risk OWASP doesn't name", 21, MUT, 500))
p.append("</svg>")

svg = "".join(p)
cairosvg.svg2png(bytestring=svg.encode(), write_to="side1_chart.png", output_width=W, output_height=H)
print("built side1_chart.png · height used:", y)
print("WARNINGS:", warn if warn else "none")
