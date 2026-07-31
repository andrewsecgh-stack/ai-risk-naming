import cairosvg, os, glob, img2pdf

W = H = 1080
PAD = 96
USABLE = W - 2*PAD
FACTOR = 0.60  # conservative char-width estimate for DejaVu Sans
FONT = "DejaVu Sans, Arial, sans-serif"

INK="#1A1A17"; SEC="#5F5E5A"; MUT="#9A9992"
BLUE="#185FA5"; BLUE_BG="#E9F1FA"
RED="#A32D2D"; RED_BG="#FBEDEC"
AMB="#8A5410"; GRAYBG="#F3F1EA"; WHITE="#FFFFFF"

warn=[]
def check(s,size):
    if len(s)*FACTOR*size > USABLE:
        warn.append(f"OVERFLOW ({int(len(s)*FACTOR*size)}px): {s!r} @ {size}")

def esc(s): return s.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")

def txt(x,y,s,size,color,weight=400,anchor="start"):
    if anchor=="start": check(s,size)
    return (f'<text x="{x}" y="{y}" font-family="{FONT}" font-size="{size}" '
            f'font-weight="{weight}" fill="{color}" text-anchor="{anchor}">{esc(s)}</text>')

def lines(x,y,arr,size,color,weight=400,lh=1.42):
    step=size*lh; out=[]
    for i,s in enumerate(arr): out.append(txt(x,y+i*step,s,size,color,weight))
    return "\n".join(out)

def slide(bg,body,idx,border=None):
    b=f'<rect x="18" y="18" width="{W-36}" height="{H-36}" rx="28" fill="none" stroke="{border}" stroke-width="3"/>' if border else ""
    tag=txt(PAD,H-70,"The Disgruntled Employee: the AI risk OWASP doesn't name",23,MUT,500)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">'
            f'<rect width="{W}" height="{H}" fill="{bg}"/>{b}{body}{tag}</svg>')

S=[]

# 1 cover
b = txt(PAD,150,"The human side of the LLM Top 10",30,MUT,500)
b += f'<rect x="{PAD}" y="182" width="150" height="6" rx="3" fill="{BLUE}"/>'
b += lines(PAD,470,["OWASP tells you","what breaks."],92,INK,500,1.32)
b += txt(PAD,470+92*1.32*2+18,"Not who breaks it.",92,BLUE,500)
S.append(slide(WHITE,b,1))

# 2 the gap
b = txt(PAD,150,"The gap",30,SEC,500)
b += lines(PAD,400,["The framework names the risk —","the mechanism inside the system.","",
                    "It doesn't name the scenario:","who trips the wire, or why."],46,INK,400,1.45)
b += txt(PAD,830,"We're missing the plain-language names.",36,SEC,500)
S.append(slide(WHITE,b,2))

# 3 disgruntled
b = txt(PAD,150,"LLM10  ·  Unbounded consumption",30,RED,500)
b += txt(PAD,330,"The Disgruntled Employee",56,RED,500)
b += lines(PAD,500,["A valid login. A motive.","They loop the priciest calls —",
                    "or strip the rate limits they","were trusted to manage."],42,INK,400,1.5)
b += txt(PAD,880,"Denial of wallet — with a face.",42,RED,500)
S.append(slide(RED_BG,b,3,border="#F0BBB9"))

# 4 strip the motive
b = txt(PAD,150,"Strip the motive",30,SEC,500)
b += lines(PAD,430,["Take the motive away and","the damage stays. The same",
                    "bill lands when someone","simply isn't thinking clearly."],46,INK,400,1.45)
b += txt(PAD,880,"No anger, no plan, same outcome.",42,BLUE,500)
S.append(slide(WHITE,b,4))

# 5 intent axis
b = txt(PAD,150,"The missing axis: intent",30,SEC,500)
y=350
for name,desc,col in [("Malicious","meant to hurt you",RED),
                      ("Negligent","knew better, cut the corner",AMB),
                      ("Ignorant","had no idea",BLUE)]:
    b += f'<circle cx="{PAD+16}" cy="{y-18}" r="16" fill="{col}"/>'
    b += txt(PAD+64,y,name,54,col,500)
    b += txt(PAD+64,y+56,desc,36,SEC,400)
    y+=185
b += lines(PAD,880,["Same risk. Different people,","different controls, conversations."],34,SEC,500,1.35)
S.append(slide(GRAYBG,b,5))

# 6 beyond top 10
b = txt(PAD,150,"Beyond the Top 10",30,SEC,500)
b += lines(PAD,430,["Some failures don't map at all","— shadow AI, or over-reliance",
                    "on an agent that's confidently","wrong."],46,INK,400,1.45)
b += txt(PAD,850,"Governance gaps, not system flaws.",42,SEC,500)
S.append(slide(WHITE,b,6))

# 7 CTA
b = txt(PAD,150,"Your turn",30,BLUE,500)
b += lines(PAD,450,["What's a scenario","the framework doesn't","have a name for?"],68,BLUE,500,1.32)
b += txt(PAD,900,"Drop it in the comments.",44,BLUE,500)
S.append(slide(BLUE_BG,b,7,border="#AECBE8"))

os.makedirs("slides",exist_ok=True)
for i,svg in enumerate(S,1):
    cairosvg.svg2png(bytestring=svg.encode(),write_to=f"slides/slide_{i}.png",output_width=1080,output_height=1080)

f=sorted(glob.glob("slides/slide_*.png"),key=lambda x:int(x.split('_')[1].split('.')[0]))
open("carousel_intent_axis.pdf","wb").write(img2pdf.convert(f))
print("built",len(S),"slides + pdf")
print("WARNINGS:", warn if warn else "none")
