#!/usr/bin/env python3
# สคริปต์สร้าง asset SVG (ธีม Glass Purple: light + dark) สำหรับ README
# วิธีใช้: แก้ CONFIG ด้านล่าง แล้วรัน  python3 build-assets.py
# ผลลัพธ์: โฟลเดอร์ assets/ (วางคู่กับ README.md ได้เลย)
import os
from xml.sax.saxutils import escape as esc

# ───────────── CONFIG: แก้ตรงนี้เท่านั้น ─────────────
CONFIG = {
    "hi": "Hi, I'm",
    "line1": "Build. Create.",
    "line2": "Iterate.",
    "tagline": ["นักพัฒนาและครีเอทีฟ ที่หลงใหลในการสร้างสิ่งใหม่", "ด้วยเทคโนโลยีและความคิดสร้างสรรค์"],
    "btn1": "Explore My Work",
    "btn2": "Learn More",
    "pill": "Design. Develop. Deploy.",
    "sections": [  # (ไฟล์, eyebrow, หัวข้อ)
        ("quickstart", "Get Started", "Quickstart"),
        ("work", "My Projects", "Featured Work"),
        ("services", "Services", "What I Can Do"),
        ("about", "About Me", "Developer. Creator. Lifelong Learner."),
        ("contact", "Get in Touch", "Let's Work Together"),
    ],
}
# ────────────────────────────────────────────────────

FONT = "Inter,'Segoe UI','Noto Sans Thai',Helvetica,Arial,sans-serif"
T = {
 "light": dict(bg1="#FBFAFF", bg2="#E4DDFF", ink="#14122B", sub="#4A4670", acc1="#5B3DF5", acc2="#9B84FF",
               btn="#14122B", btntxt="#FFFFFF", o1="#8B6CFF", o2="#C4B5FF", oop=".40", win1="#1E1850", win2="#0C0A26",
               ghost="#14122B", line="#C9BFFF"),
 "dark":  dict(bg1="#0B0820", bg2="#1B1258", ink="#FFFFFF", sub="#B9B4E0", acc1="#8B6CFF", acc2="#C9BCFF",
               btn="#7C5CFF", btntxt="#FFFFFF", o1="#6D4AFF", o2="#3B2BB5", oop=".60", win1="#2A2080", win2="#100B38",
               ghost="#FFFFFF", line="#3A2F8F"),
}

def w(name, s):
    with open(os.path.join("assets", name), "w", encoding="utf-8") as f:
        f.write(s)

def hero(t):
    c = CONFIG
    code = [(0,0,120,"#8B6CFF"),(0,1,200,"#5EA8FF"),(1,2,160,"#C9BCFF"),(1,3,230,"#7C5CFF"),
            (2,4,140,"#5EA8FF"),(2,5,190,"#8B6CFF"),(1,6,110,"#C9BCFF"),(0,7,170,"#7C5CFF"),(0,8,90,"#5EA8FF")]
    lines = "".join(f'<rect x="{34+i*18}" y="{58+r*20}" width="{ww}" height="8" rx="4" fill="{col}" opacity=".85"/>' for i,r,ww,col in code)
    tag = "".join(f'<text x="60" y="{318+i*30}" font-size="21" fill="{t["sub"]}">{esc(x)}</text>' for i,x in enumerate(c["tagline"]))
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 460" width="1200" height="460" font-family="{FONT}">
<defs>
<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{t['bg1']}"/><stop offset="1" stop-color="{t['bg2']}"/></linearGradient>
<linearGradient id="acc" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{t['acc1']}"/><stop offset="1" stop-color="{t['acc2']}"/></linearGradient>
<linearGradient id="win" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{t['win1']}"/><stop offset="1" stop-color="{t['win2']}"/></linearGradient>
<linearGradient id="glass" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#fff" stop-opacity=".45"/><stop offset="1" stop-color="#fff" stop-opacity=".05"/></linearGradient>
<linearGradient id="cA" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#9B84FF"/><stop offset="1" stop-color="#4B2FE0"/></linearGradient>
<filter id="blur" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="55"/></filter>
<filter id="sh" x="-20%" y="-20%" width="140%" height="150%"><feDropShadow dx="0" dy="22" stdDeviation="22" flood-color="#5B3DF5" flood-opacity=".45"/></filter>
<clipPath id="r"><rect width="1200" height="460" rx="28"/></clipPath>
</defs>
<g clip-path="url(#r)">
<rect width="1200" height="460" fill="url(#bg)"/>
<circle cx="980" cy="90" r="170" fill="{t['o1']}" opacity="{t['oop']}" filter="url(#blur)"/>
<circle cx="150" cy="470" r="200" fill="{t['o2']}" opacity="{t['oop']}" filter="url(#blur)"/>
<circle cx="640" cy="440" r="140" fill="{t['o1']}" opacity=".25" filter="url(#blur)"/>
<g transform="translate(655 120) rotate(-8)"><rect width="420" height="250" rx="22" fill="url(#glass)" stroke="#fff" stroke-opacity=".5"/></g>
<g transform="translate(690 78) rotate(-5)" filter="url(#sh)">
<rect width="430" height="260" rx="20" fill="url(#win)" stroke="{t['acc2']}" stroke-opacity=".7" stroke-width="1.5"/>
<circle cx="26" cy="26" r="6" fill="#FF5F57"/><circle cx="46" cy="26" r="6" fill="#FEBC2E"/><circle cx="66" cy="26" r="6" fill="#28C840"/>
{lines}
</g>
<g transform="translate(1100 82)">
<polygon points="0,-46 44,-22 0,2 -44,-22" fill="#C9BCFF"/>
<polygon points="-44,-22 0,2 0,54 -44,30" fill="url(#cA)"/>
<polygon points="44,-22 0,2 0,54 44,30" fill="#5B3DF5"/>
</g>
<g transform="translate(960 232)"><rect width="216" height="38" rx="19" fill="url(#glass)" stroke="#fff" stroke-opacity=".5"/>
<circle cx="20" cy="19" r="5" fill="{t['acc1']}"/><text x="34" y="25" font-size="14" fill="{t['ink']}">{esc(c['pill'])}</text></g>
<text x="60" y="118" font-size="28" font-weight="500" fill="{t['ink']}">{esc(c['hi'])}</text>
<text x="56" y="196" font-size="76" font-weight="800" fill="{t['ink']}" letter-spacing="-2">{esc(c['line1'])}</text>
<text x="56" y="272" font-size="76" font-weight="800" fill="url(#acc)" letter-spacing="-2">{esc(c['line2'])}</text>
{tag}
<rect x="60" y="388" width="200" height="48" rx="24" fill="{t['btn']}"/>
<text x="160" y="418" font-size="16" font-weight="600" fill="{t['btntxt']}" text-anchor="middle">{esc(c['btn1'])}  →</text>
<rect x="276" y="388.75" width="150" height="46.5" rx="23.25" fill="none" stroke="{t['ghost']}" stroke-opacity=".3"/>
<text x="351" y="418" font-size="16" font-weight="500" fill="{t['ink']}" text-anchor="middle">{esc(c['btn2'])}</text>
</g></svg>'''

def section(t, eyebrow, title):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 96" width="1200" height="96" font-family="{FONT}">
<defs><linearGradient id="a" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{t['acc1']}"/><stop offset="1" stop-color="{t['acc2']}" stop-opacity="0"/></linearGradient></defs>
<text x="4" y="28" font-size="18" font-weight="600" fill="{t['acc1']}">{esc(eyebrow)}</text>
<rect x="{18+len(eyebrow)*10}" y="22" width="90" height="2" fill="url(#a)"/>
<text x="2" y="76" font-size="44" font-weight="800" fill="{t['ink']}" letter-spacing="-1">{esc(title)}</text></svg>'''

def divider(t):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 24" width="1200" height="24">
<defs><linearGradient id="l" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{t['acc1']}" stop-opacity="0"/><stop offset=".5" stop-color="{t['acc1']}"/><stop offset="1" stop-color="{t['acc1']}" stop-opacity="0"/></linearGradient>
<filter id="g"><feGaussianBlur stdDeviation="4"/></filter></defs>
<rect x="0" y="11" width="1200" height="2" fill="url(#l)"/>
<circle cx="600" cy="12" r="9" fill="{t['acc1']}" opacity=".6" filter="url(#g)"/><circle cx="600" cy="12" r="4" fill="{t['acc2']}"/></svg>'''

def logo(t):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 56" width="120" height="56">
<defs><linearGradient id="a" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{t['acc1']}"/><stop offset="1" stop-color="{t['acc2']}"/></linearGradient></defs>
<polygon points="20,50 38,6 52,6 34,50" fill="{t['ink']}"/><polygon points="52,50 70,6 84,6 66,50" fill="url(#a)"/></svg>'''

def footer(t):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 140" width="1200" height="140" preserveAspectRatio="none">
<defs><linearGradient id="a" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{t['acc1']}" stop-opacity=".0"/><stop offset=".5" stop-color="{t['acc1']}" stop-opacity=".35"/><stop offset="1" stop-color="{t['acc2']}" stop-opacity=".0"/></linearGradient></defs>
<path d="M0 90 C200 20 400 130 600 70 S1000 20 1200 80 V140 H0Z" fill="url(#a)"/>
<path d="M0 115 C250 60 450 140 700 95 S1050 60 1200 105 V140 H0Z" fill="url(#a)" opacity=".7"/></svg>'''

def project(n):
    base = '<defs><linearGradient id="a" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#0E0B2E"/><stop offset="1" stop-color="#2A1B8F"/></linearGradient><linearGradient id="b" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#5B3DF5"/><stop offset="1" stop-color="#7FB0FF"/></linearGradient></defs><rect width="480" height="260" rx="18" fill="url(#a)"/>'
    art = {
     1: '<path d="M0 190 C120 60 220 230 330 120 S440 80 480 110" fill="none" stroke="url(#b)" stroke-width="10" opacity=".9"/><path d="M0 220 C140 120 240 250 350 160 S450 120 480 150" fill="none" stroke="#9B84FF" stroke-width="6" opacity=".6"/>',
     2: '<g fill="#C9BCFF" opacity=".75"><polygon points="140,60 190,110 140,160 90,110"/><polygon points="240,100 290,150 240,200 190,150" opacity=".7"/><polygon points="340,50 390,100 340,150 290,100" opacity=".5"/></g>',
     3: '<polygon points="0,260 120,140 190,200 300,70 400,190 480,150 480,260" fill="#1A1560"/><polygon points="300,70 340,125 300,110 270,130" fill="#E6E0FF"/><circle cx="390" cy="60" r="22" fill="#9B84FF" opacity=".8"/>',
    }[n]
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 480 260" width="480" height="260">{base}{art}</svg>'

os.makedirs("assets", exist_ok=True)
for name, t in T.items():
    w(f"hero-{name}.svg", hero(t))
    w(f"divider-{name}.svg", divider(t))
    w(f"logo-{name}.svg", logo(t))
    w(f"footer-{name}.svg", footer(t))
    for key, eb, ti in CONFIG["sections"]:
        w(f"section-{key}-{name}.svg", section(t, eb, ti))
for n in (1, 2, 3):
    w(f"project-{n}.svg", project(n))
print("เสร็จ:", len(os.listdir("assets")), "ไฟล์ใน assets/")
