#!/usr/bin/env python3
"""
build_site.py - generate the POSEIDON T-Embed showcase pages.

WHY A GENERATOR:
    The main POSEIDON site hand-copies its <nav> into every page, so adding one
    link is a ten-file edit and the pages drift apart. Here the shell (head, nav,
    footer, scripts) lives in exactly one place and each page supplies only its
    own body. Run this after editing PAGES; it rewrites docs/*.html.

USAGE:  python build_site.py
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DOCS = ROOT / "docs"

NAV = [
    ("index.html",  "Overview"),
    ("nfc.html",    "NFC"),
    ("radios.html", "Radios"),
    ("encoder.html","Encoder"),
    ("hardened.html","Hardened"),
    ("hardware.html","Hardware"),
    ("status.html", "Status"),
    ("flash/",      "Flash"),
]

EXTERNAL = [
    ("https://generaldussduss.github.io/poseidon/", "Cardputer"),
    ("https://github.com/GeneralDussDuss/poseidon", "GitHub"),
]

STYLE = """
.te-accent{color:#22d3ee}
.te-panel{border:1px solid rgba(34,211,238,.32);border-radius:18px;background:linear-gradient(135deg,rgba(34,211,238,.08) 0%,rgba(14,165,233,.04) 100%);backdrop-filter:blur(6px);position:relative;overflow:hidden;padding:clamp(1.5rem,3vw,2.2rem)}
.te-panel .glow{position:absolute;top:-40px;right:-40px;width:180px;height:180px;background:radial-gradient(circle,rgba(34,211,238,.22) 0%,transparent 70%);pointer-events:none}
.te-mono{font-family:var(--font-mono);font-size:.82rem;line-height:1.75;background:rgba(6,10,22,.6);border:1px solid rgba(34,211,238,.25);border-radius:12px;padding:1rem 1.2rem;color:#94a3b8;overflow-x:auto}
.te-mono .g{color:#6ee7b7;font-weight:700}.te-mono .w{color:#fbbf24;font-weight:700}.te-mono .c{color:#22d3ee}
.te-compare{width:100%;border-collapse:collapse;font-size:.9rem;margin-top:1.5rem}
.te-compare th,.te-compare td{text-align:left;padding:.7rem .9rem;border-bottom:1px solid rgba(255,255,255,.05);vertical-align:top}
.te-compare thead th{font-family:var(--font-mono);font-size:.68rem;letter-spacing:.16em;text-transform:uppercase;color:#64748b}
.te-compare tbody td:first-child{color:#cbd5e1;font-weight:500;width:26%}
.te-compare .te-col{color:#7dd3fc}.te-compare .cp-col{color:#a3b4cf}
.te-status-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:1rem;margin-top:1.5rem}
.te-status{background:linear-gradient(180deg,var(--bg-raised),var(--bg-card));border:1px solid rgba(34,211,238,.12);border-radius:14px;padding:1.4rem 1.5rem;position:relative;overflow:hidden}
.te-status::before{content:'';position:absolute;top:0;left:0;width:4px;height:100%}
.te-status.ready::before{background:#22c55e;box-shadow:0 0 12px rgba(34,197,94,.4)}
.te-status.bring::before{background:#fbbf24;box-shadow:0 0 12px rgba(251,191,36,.4)}
.te-status .st{font-family:var(--font-mono);font-size:.66rem;letter-spacing:.16em;text-transform:uppercase;margin-bottom:.5rem;display:flex;align-items:center;gap:.4rem}
.te-status.ready .st{color:#22c55e}.te-status.bring .st{color:#fbbf24}
.te-status h4{font-family:var(--font-display);font-size:1rem;color:#e2e8f0;margin-bottom:.5rem;letter-spacing:.03em}
.te-status p{font-size:.9rem;color:#a3b4cf;line-height:1.55}
.spec-row{display:flex;justify-content:space-between;gap:1rem;padding:.5rem 0;border-bottom:1px solid rgba(255,255,255,.04);font-size:.9rem}
.spec-row .k{color:#cbd5e1;font-weight:500}
.spec-row .v{color:#7dd3fc;font-family:var(--font-mono);font-size:.82rem;text-align:right}
#videoSplash{position:fixed;inset:0;z-index:10001;background:#000;display:flex;align-items:center;justify-content:center;opacity:1;transition:opacity .6s ease}
#videoSplash.done{opacity:0;pointer-events:none}
#videoSplash video,#videoSplash img{max-width:100%;max-height:100%;width:auto;height:auto;object-fit:contain;display:block}
#splashSkip{position:fixed;bottom:18px;right:18px;z-index:10002;font-family:var(--font-mono);font-size:.66rem;letter-spacing:.16em;color:#7dd3fc;background:rgba(4,10,20,.6);border:1px solid rgba(34,211,238,.5);border-radius:8px;padding:.4rem .8rem;cursor:pointer;opacity:.7}
#splashSkip:hover{opacity:1;box-shadow:0 0 14px rgba(34,211,238,.35)}
@media(prefers-reduced-motion:reduce){#videoSplash{display:none}}
"""

SPLASH_JS = """
(function(){
  var ov=document.getElementById('videoSplash'); if(!ov) return;
  var vid=document.getElementById('splashVid'), hud=document.getElementById('hud');
  var done=false, maxT=0;
  function finish(){ if(done) return; done=true; clearTimeout(maxT);
    ov.classList.add('done');
    if(hud) setTimeout(function(){ hud.classList.add('visible'); }, 300);
    setTimeout(function(){ if(ov.parentNode) ov.parentNode.removeChild(ov); }, 700);
  }
  if(matchMedia('(prefers-reduced-motion: reduce)').matches){ finish(); return; }
  function showGif(){
    try{ if(vid) vid.style.display='none';
      var img=document.createElement('img'); img.src='assets/hero-splash.gif'; img.alt='';
      ov.insertBefore(img, ov.firstChild);
    }catch(e){}
    clearTimeout(maxT); maxT=setTimeout(finish, 4200);
  }
  maxT=setTimeout(finish, 9000);
  if(vid){ vid.muted=true;
    vid.addEventListener('ended', finish);
    vid.addEventListener('error', showGif);
    var pr=vid.play(); if(pr&&pr.catch) pr.catch(showGif);
  } else { showGif(); }
  ['click','keydown','touchstart'].forEach(function(ev){ ov.addEventListener(ev, finish, {once:true}); });
  var sk=document.getElementById('splashSkip');
  if(sk) sk.addEventListener('click', function(e){ e.stopPropagation(); finish(); });
})();
"""


def nav_html(active):
    items = []
    for href, label in NAV:
        cls = ' class="active"' if href == active else ""
        items.append(f'    <li><a href="{href}"{cls}>{label}</a></li>')
    for href, label in EXTERNAL:
        items.append(f'    <li><a href="{href}" target="_blank" rel="noopener">{label}</a></li>')
    return "\n".join(items)


def page(slug, title, desc, body, *, splash=False, boot_name="T-EMBED", boot_line="one board, every radio"):
    splash_block = ""
    splash_script = ""
    if splash:
        splash_block = """<div id="videoSplash" aria-hidden="true">
  <video id="splashVid" muted playsinline autoplay preload="auto">
    <source src="assets/hero-splash.mp4" type="video/mp4">
  </video>
  <button id="splashSkip" type="button">SKIP &#9656;</button>
</div>

"""
        splash_script = f"<script>{SPLASH_JS}</script>\n"

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:image" content="https://generaldussduss.github.io/poseidon-tembed/assets/og.png">
<meta name="theme-color" content="#06121f">
<link rel="icon" href="assets/icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;700;900&family=Rajdhani:wght@300;400;500;600;700&family=JetBrains+Mono:wght@300;400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/style.css">
<style>{STYLE}</style>
</head>
<body data-matrix>

{splash_block}<div id="bootOverlay">
  <div class="boot-trident">&#128305;</div>
  <div class="boot-logo">{boot_name}</div>
  <div class="boot-lines"><div class="boot-line"><span class="dim">[BOOT]</span> {boot_line} <span class="ok">OK</span></div></div>
</div>

<div id="scrollProgress"></div>
<div id="hud"><div class="hud-row"><span class="hud-dot"></span>T-EMBED CC1101 PLUS &middot; 5 RADIOS ONBOARD</div></div>

<nav id="mainNav">
  <a href="index.html" class="nav-logo"><span class="icon">P</span><span>POSEIDON &middot; T-EMBED</span></a>
  <ul class="nav-links">
{nav_html(slug)}
  </ul>
</nav>

{body}

<footer>
  <div class="foot-glyph">&#10208;</div>
  <div class="suite-label">PART OF THE SUITE</div>
  <div class="suite-links">
    <a href="https://generaldussduss.github.io/poseidon/">POSEIDON (CARDPUTER)</a>
    <a href="https://generaldussduss.github.io/suite/">THE SUITE</a>
    <a href="https://generaldussduss.github.io/faceless/">FACELESS</a>
  </div>
  <div class="copy">&copy; 2026 POSEIDON T-EMBED &mdash; commander of the deep &mdash; MIT</div>
</footer>

<canvas id="particles" style="position:fixed;inset:0;z-index:-1;pointer-events:none"></canvas>
<script src="assets/site.js"></script>
{splash_script}</body>
</html>
"""


def head(kicker, h1, lede):
    return f"""<header class="page-head">
  <div class="kicker">{kicker}</div>
  <h1>{h1}</h1>
  <p class="lede">{lede}</p>
</header>
"""


def console(*pairs):
    inner = "".join(f'    <span>{k}=<span class="nm">{v}</span></span>\n' for k, v in pairs)
    return f"""<div class="console-strip">
  <div class="console-bar">
    <span class="ck">[HW]</span>
{inner}    <span class="blink">&#9656;</span>
  </div>
</div>
"""
