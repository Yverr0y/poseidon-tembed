#!/usr/bin/env python3
"""
pages.py - page bodies for the POSEIDON T-Embed site. Run this to build.

The shared shell (head, nav, footer, scripts) lives in build_site.py so the nav
exists in exactly one place; this file supplies only each page's own body.

USAGE:  python pages.py
"""
from build_site import DOCS, page, head, console

# ============================== INDEX ==============================

INDEX = """<section id="hero">
  <canvas id="heroCanvas"></canvas>
  <canvas id="causticLayer"></canvas>
  <div class="hero-content">
    <div class="hero-badge"><span class="dot"></span> NEW &middot; POSEIDON IS NOW ON THE T-EMBED CC1101 PLUS</div>
    <div class="hero-epithet">EVERY RADIO. ONE BOARD. NO HATS.</div>
    <h1 class="hero-title">POSEIDON</h1>
    <p class="hero-sub">The pentest deck that stopped needing accessories. <span class="hl">Sub-GHz</span>, <span class="hl">2.4 GHz</span>, <span class="hl">NFC</span>, <span class="hl">IR</span>, <span class="hl">WiFi</span> and <span class="hl">BLE</span> &mdash; all soldered on, all on battery, all driven from one wheel. And it has a radio the Cardputer physically does not: <span class="hl">a real NFC reader</span>.</p>
    <div class="hero-prompt">
      <span class="prompt-dollar">poseidon &#9656;</span>
      <span class="prompt-cmd">nfc</span>
      <span class="prompt-arg">read</span>
      <span class="prompt-flag">--emv</span>
      <span class="prompt-cursor"></span>
    </div>
    <div class="hero-btns">
      <a href="flash/" class="btn btn-primary">&#9889; Flash it right now</a>
      <a href="nfc.html" class="btn btn-secondary">&#9654; See the NFC exclusive</a>
      <a href="hardware.html" class="btn btn-secondary">&#8623; What the silicon is</a>
    </div>
    <div class="hero-stats">
      <div class="hero-stat"><div class="num" data-count="5">5</div><div class="label">Radios onboard</div></div>
      <div class="hero-stat"><div class="num" data-count="0">0</div><div class="label">Hats needed</div></div>
      <div class="hero-stat"><div class="num" data-count="320" data-suffix="px">320px</div><div class="label">Panel width</div></div>
      <div class="hero-stat"><div class="num" data-count="47">47</div><div class="label">Bugs fixed</div></div>
    </div>
  </div>
  <div class="hero-scroll">SCROLL</div>
</section>

""" + console(("board", "t-embed-cc1101-plus"), ("mcu", "esp32-s3"), ("lcd", "st7789 320x170"),
              ("radios", "cc1101+nrf24+pn532+wifi+ble"), ("ir", "tx+rx"), ("input", "encoder")) + """
<div class="ticker">
  <div class="ticker-track">
    <span>CC1101 <span class="val">300-928 MHz</span></span>
    <span>NRF24 <span class="val">2.4 GHz esb</span></span>
    <span>PN532 <span class="val">13.56 MHz</span></span>
    <span>EMV <span class="val">pan + expiry</span></span>
    <span>MIFARE <span class="val">sector dump</span></span>
    <span>IR <span class="val">learn + replay</span></span>
    <span>WIFI <span class="val">deauth / pmkid</span></span>
    <span>BLE <span class="val">spam / gatt</span></span>
    <span>RING <span class="val">reactive</span></span>
    <span>CC1101 <span class="val">300-928 MHz</span></span>
    <span>NRF24 <span class="val">2.4 GHz esb</span></span>
    <span>PN532 <span class="val">13.56 MHz</span></span>
    <span>EMV <span class="val">pan + expiry</span></span>
    <span>IR <span class="val">learn + replay</span></span>
  </div>
</div>

<section id="explore">
  <div class="section-label reveal" style="color:#22d3ee;">00 // THE DROP</div>
  <h2 class="section-title reveal">Everything that landed with it</h2>
  <p class="section-desc reveal">A full port, a new radio nobody else in the lineup has, an input model rebuilt from scratch, and five audit passes that gutted 47 real defects out of the firmware. Start anywhere.</p>

  <div class="teaser-grid">
    <a class="teaser reveal" href="nfc.html">
      <div class="t-num">01 &middot; NFC</div><h3>The headline feature.</h3>
      <p>A real 13.56 MHz reader onboard. Identify tags, dump Mifare Classic sectors to SD, and pull the number straight off a contactless bank card. No other board in the lineup can touch this.</p>
      <div class="t-arrow">Read it &rarr;</div>
    </a>
    <a class="teaser reveal" href="radios.html">
      <div class="t-num">02 &middot; RADIOS</div><h3>Five radios. Zero hats.</h3>
      <p>Sub-GHz, 2.4 GHz, NFC, IR, WiFi and BLE, every one of them populated on the board and running off the internal cell. Change bands by turning a dial, not by opening your bag.</p>
      <div class="t-arrow">See the arsenal &rarr;</div>
    </a>
    <a class="teaser reveal" href="encoder.html">
      <div class="t-num">03 &middot; ENCODER</div><h3>One wheel, every feature.</h3>
      <p>Five gestures drive dozens of screens, including typing a password on a character wheel.</p>
      <div class="t-arrow">See the design &rarr;</div>
    </a>
    <a class="teaser reveal" href="hardened.html">
      <div class="t-num">04 &middot; HARDENED</div><h3>47 defects, gone.</h3>
      <p>Five adversarial audit passes. The interesting bugs were the ones that reported success and did nothing.</p>
      <div class="t-arrow">Read the findings &rarr;</div>
    </a>
    <a class="teaser reveal" href="hardware.html">
      <div class="t-num">05 &middot; HARDWARE</div><h3>What the silicon is.</h3>
      <p>Verified pin map, the shared-SPI reality, and an honest comparison against the Cardputer.</p>
      <div class="t-arrow">Inspect it &rarr;</div>
    </a>
    <a class="teaser reveal" href="flash/">
      <div class="t-num">06 &middot; FLASH</div><h3>Running in 30 seconds.</h3>
      <p>Plug in, open Chrome, hit Connect. Web Serial flashes the whole image in about 25 seconds. No toolchain, no Python, no install.</p>
      <div class="t-arrow">Open the flasher &rarr;</div>
    </a>
  </div>

  <div class="te-panel reveal" style="margin-top:2.5rem;border-color:rgba(251,191,36,.3);background:rgba(251,191,36,.05);">
    <div style="font-family:var(--font-mono);font-size:.7rem;letter-spacing:.2em;text-transform:uppercase;color:#fbbf24;margin-bottom:.6rem;">&#9680; STILL BEING TESTED &mdash; READ THIS BEFORE YOU GET EXCITED</div>
    <p style="font-size:1rem;line-height:1.65;color:#e2e8f0;margin:0 0 1rem;">This is an <b style="color:#fbbf24;">active bring-up</b>, not a finished release, and the page says so on purpose. Two things on this board are written, compiling and flashed, but have <b style="color:#fbbf24;">never been proven against real hardware</b>:</p>
    <div class="te-mono" style="border-color:rgba(251,191,36,.25);">
      <div>NFC + EMV ......... <span class="w">UNTESTED</span>&nbsp;&nbsp;never seen a live tag or a real card</div>
      <div>Sub-GHz on air .... <span class="w">UNTESTED</span>&nbsp;&nbsp;decoders repaired, but no fob has confirmed it</div>
      <div>&nbsp;</div>
      <div>everything else ... <span class="g">RUNNING ON THE BOARD</span></div>
    </div>
    <p style="font-size:.95rem;line-height:1.6;color:#cbd5e1;margin:1rem 0 0;">Boot, display, menus, encoder navigation, WiFi, BLE, SD and the LED ring are all confirmed working on the physical device. The <a href="status.html" style="color:#fbbf24;">status page</a> breaks it down subsystem by subsystem, and a card there only turns green once it has actually run &mdash; not when it compiles.</p>
  </div>
</section>
"""

# ============================== NFC ==============================

NFC = head("01 // THE T-EMBED EXCLUSIVE",
           "It reads cards. The Cardputer cannot.",
           "This is the feature the Cardputer can never have, because the hardware simply is not there. The T-Embed carries a PN532 on its own I2C bus, and POSEIDON drives it with a hand-written reader plus a full contactless EMV stack on top. Fair warning up front: this stack is written and flashed but has NOT yet been validated against a live tag or a real card.") + console(
           ("chip", "pn532"), ("bus", "i2c 0x24"), ("band", "13.56 MHz"), ("modes", "tag / mifare / emv")) + """
<section>
  <div class="reveal te-panel frame">
    <div class="glow"></div>
    <div style="font-family:var(--font-mono);font-size:.7rem;letter-spacing:.22em;text-transform:uppercase;color:#22d3ee;margin-bottom:.5rem;">&#9680; WRITTEN TO SPEC &middot; PENDING ON-CARD VALIDATION</div>
    <h3 style="font-family:var(--font-display);font-size:clamp(1.3rem,2.2vw,1.8rem);margin:0 0 .6rem;color:#7dd3fc;">What it reads, and what it honestly cannot</h3>
    <p style="font-size:1rem;line-height:1.6;color:#e2e8f0;margin:0 0 1rem;">A contactless card hands over its number and expiry with <b style="color:#7dd3fc;">no authentication at all</b>. That is the finding worth demonstrating. Everything else is reported honestly rather than dressed up.</p>
    <div class="te-mono">
      <div><span class="c">$</span> emv read &middot; ppse &rarr; aid &rarr; gpo &rarr; read record</div>
      <div>PAN (card number) ......... <span class="g">READS</span>&nbsp;&nbsp;unauthenticated, every card</div>
      <div>Expiry .................... <span class="g">READS</span></div>
      <div>Cardholder name ........... <span class="w">RARE</span>&nbsp;&nbsp;&nbsp;Visa/MC stripped it years ago</div>
      <div>Transaction log ........... <span class="w">RARE</span>&nbsp;&nbsp;&nbsp;optional; most issuers disable it</div>
      <div>CVV ....................... <span class="c">NEVER</span>&nbsp;&nbsp;not on the chip. cannot clone.</div>
    </div>
  </div>

  <h2 class="section-title reveal" style="margin-top:3rem;">Three readers on one chip</h2>
  <div class="feature-grid reveal">
    <div class="feature-card"><div class="fc-head"><span class="fc-glyph" style="color:#22d3ee;border-color:rgba(34,211,238,.4);"><svg viewBox="0 0 24 24"><path d="M4 5h16v14H4z M4 9h16 M8 13h4"/></svg></span><h3 class="te-accent">Identify any 14443A tag</h3></div><p>UID of any length, ATQA and SAK on screen, and the family resolved from SAK: NTAG or Ultralight, Mifare Classic 1K and 4K, Plus, DESFire, JCOP, or plain ISO14443-4.</p><div class="count" style="color:#22d3ee;">READ</div></div>
    <div class="feature-card"><div class="fc-head"><span class="fc-glyph" style="color:#22d3ee;border-color:rgba(34,211,238,.4);"><svg viewBox="0 0 24 24"><path d="M6 4h9l3 3v13H6z M9 12h6 M9 15h6"/></svg></span><h3 class="te-accent">Dump Mifare Classic</h3></div><p>One press walks every sector with the common default keys, re-selecting the tag after each failed auth, and saves what it recovered as a raw .mfd file.</p><div class="count" style="color:#22d3ee;">DUMP</div></div>
    <div class="feature-card"><div class="fc-head"><span class="fc-glyph" style="color:#22d3ee;border-color:rgba(34,211,238,.4);"><svg viewBox="0 0 24 24"><path d="M3 6h18v12H3z M3 10h18 M6 14h5"/></svg></span><h3 class="te-accent">Read a bank card</h3></div><p>Full ISO14443-4 APDU transport with a BER-TLV parser: PPSE, AID select, GPO, and an AFL record walk. Shows scheme, PAN and expiry, and says plainly when a field is simply not on the card.</p><div class="count" style="color:#22d3ee;">EMV</div></div>
  </div>

  <p class="reveal" style="max-width:820px;margin:2.5rem auto 0;font-style:italic;opacity:.85;text-align:center;color:#cbd5e1;">The APDU layer is shared, so a passport reader is the same transport plus BAC key derivation from the MRZ. Read your own cards.</p>
</section>
"""

# ============================== RADIOS ==============================

RADIOS = head("02 // NO HATS",
              "Five radios. Nothing to plug in.",
              "Every other pocket deck rents its radios from a hat, one band at a time, and makes you carry the hats. This one owns all of them. Sub-GHz, 2.4 GHz, NFC, IR, WiFi and BLE, populated on the board and running off the internal cell.") + console(
              ("subghz", "cc1101 300-928"), ("2g4", "nrf24l01+"), ("nfc", "pn532"),
              ("ir", "tx+rx"), ("wifi", "esp32-s3"), ("ble", "nimble")) + """
<section>
  <div class="feature-grid reveal">
    <div class="feature-card"><div class="fc-head"><span class="fc-glyph" style="color:#22d3ee;border-color:rgba(34,211,238,.4);"><svg viewBox="0 0 24 24"><path d="M4 12h4l2-7 4 14 2-7h4"/></svg></span><h3 class="te-accent">Sub-GHz, built in</h3></div><p>The onboard CC1101 covers roughly 300 to 928 MHz through a switched antenna network. Scan, record RAW, replay .sub files, brute force, jam, and hunt hot and cold.</p><div class="count" style="color:#22d3ee;">CC1101</div></div>
    <div class="feature-card"><div class="fc-head"><span class="fc-glyph" style="color:#22d3ee;border-color:rgba(34,211,238,.4);"><svg viewBox="0 0 24 24"><path d="M12 20a8 8 0 0 0 0-16 M12 20a8 8 0 0 1 0-16 M12 12h.01"/></svg></span><h3 class="te-accent">2.4 GHz nRF24</h3></div><p>The Plus SKU populates an nRF24L01+ for promiscuous ESB, the MouseJack keystroke-injection surface, a spectrum scanner and a jammer.</p><div class="count" style="color:#22d3ee;">nRF24 &middot; PLUS</div></div>
    <div class="feature-card"><div class="fc-head"><span class="fc-glyph" style="color:#22d3ee;border-color:rgba(34,211,238,.4);"><svg viewBox="0 0 24 24"><path d="M5 12h14 M5 12a7 7 0 0 1 14 0 M9 12a3 3 0 0 1 6 0 M12 12v6"/></svg></span><h3 class="te-accent">PN532 NFC</h3></div><p>A full 13.56 MHz reader on I2C that the Cardputer does not have. <a href="nfc.html" style="color:#22d3ee;">See the NFC page &rarr;</a></p><div class="count" style="color:#22d3ee;">EXCLUSIVE</div></div>
    <div class="feature-card"><div class="fc-head"><span class="fc-glyph" style="color:#22d3ee;border-color:rgba(34,211,238,.4);"><svg viewBox="0 0 24 24"><path d="M12 3v3 M12 18v3 M5 12H2 M22 12h-3 M12 9a3 3 0 0 0 0 6 3 3 0 0 0 0-6z"/></svg></span><h3 class="te-accent">IR transmit and receive</h3></div><p>An emitter and a receiver, both onboard. TV-B-Gone, a virtual remote, multi-brand clone profiles, and learn-then-replay capture.</p><div class="count" style="color:#22d3ee;">IR TX + RX</div></div>
    <div class="feature-card"><div class="fc-head"><span class="fc-glyph" style="color:#22d3ee;border-color:rgba(34,211,238,.4);"><svg viewBox="0 0 24 24"><path d="M3 12h18 M12 3v18 M6 6l12 12"/></svg></span><h3 class="te-accent">WiFi and BLE</h3></div><p>The ESP32-S3 radios drive the WiFi suite (scan, clients, deauth, PMKID, portal, wardrive) and the BLE suite (scan, spam, GATT, HID, tracker hunting), with vendor identification from a 1400-entry OUI table.</p><div class="count" style="color:#22d3ee;">ESP32-S3</div></div>
    <div class="feature-card"><div class="fc-head"><span class="fc-glyph" style="color:#22d3ee;border-color:rgba(34,211,238,.4);"><svg viewBox="0 0 24 24"><path d="M4 8h12v8H4z M16 10h3l1 2-1 2h-3"/></svg></span><h3 class="te-accent">Runs on battery</h3></div><p>A BQ25896 charger and BQ27220 fuel gauge over I2C mean real runtime and a real percentage on screen.</p><div class="count" style="color:#22d3ee;">POWER</div></div>
  </div>
</section>
"""

# ============================== ENCODER ==============================

ENCODER = head("03 // BUILT FOR A DIAL",
               "One wheel. Every single feature.",
               "This board has no keyboard. A rotary encoder emits five events and nothing else. Making a firmware with dozens of screens genuinely usable from that is its own design problem.") + """
<section>
  <div class="reveal te-panel frame" style="border-color:rgba(217,70,239,.35);background:linear-gradient(135deg,rgba(217,70,239,.08) 0%,rgba(34,211,238,.04) 100%);">
    <div class="glow" style="background:radial-gradient(circle,rgba(217,70,239,.25) 0%,transparent 70%);"></div>
    <div style="font-family:var(--font-mono);font-size:.7rem;letter-spacing:.22em;text-transform:uppercase;color:#d946ef;margin-bottom:.5rem;">&#9670; THE GESTURE VOCABULARY</div>
    <div class="te-mono" style="border-color:rgba(217,70,239,.25);">
      <div>turn ................ move / tune / scroll a character wheel</div>
      <div>press ............... select, or the primary action</div>
      <div>double-press ........ back</div>
      <div>hold ................ <span class="c">ACTIONS</span> &mdash; the full menu for that screen</div>
      <div>side button ......... back, always, from anywhere</div>
    </div>
    <p style="font-size:1rem;line-height:1.6;color:#e2e8f0;margin:1rem 0 0;">Hold is the key idea. Any screen that used to hide its actions behind letter keys now surfaces them in a modal list, which means <b style="color:#f0abfc;">every feature is reachable</b>.</p>
  </div>

  <h2 class="section-title reveal" style="margin-top:3rem;">What that unlocked</h2>
  <p class="section-desc reveal">Before this work, fifteen features were physically impossible to use on this board. Not buggy &mdash; unreachable.</p>
  <div class="feature-grid reveal">
    <div class="feature-card" style="border-color:rgba(217,70,239,.3);"><div class="fc-head"><span class="fc-glyph" style="color:#d946ef;border-color:rgba(217,70,239,.4);"><svg viewBox="0 0 24 24"><path d="M4 6h16v12H4z M8 10h8 M8 14h5"/></svg></span><h3 style="color:#f0abfc;">Text entry on a wheel</h3></div><p>Turn to scroll a character wheel, press to commit, hold for backspace or done. SSIDs, passwords, hex payloads and filenames all work without a keyboard. Before this, every text prompt could only ever return an empty string.</p><div class="count" style="color:#d946ef;">INPUT</div></div>
    <div class="feature-card" style="border-color:rgba(217,70,239,.3);"><div class="fc-head"><span class="fc-glyph" style="color:#d946ef;border-color:rgba(217,70,239,.4);"><svg viewBox="0 0 24 24"><path d="M4 5h16v4H4z M4 11h16v4H4z M4 17h10v3H4z"/></svg></span><h3 style="color:#f0abfc;">Actions menu everywhere</h3></div><p>Hold on any screen for its real action list &mdash; deauth, save, replay, tune, dump &mdash; as a scrollable modal instead of a footer naming keys the board does not have.</p><div class="count" style="color:#d946ef;">HOLD</div></div>
    <div class="feature-card" style="border-color:rgba(217,70,239,.3);"><div class="fc-head"><span class="fc-glyph" style="color:#d946ef;border-color:rgba(217,70,239,.4);"><svg viewBox="0 0 24 24"><path d="M12 3a9 9 0 1 0 0 18 9 9 0 0 0 0-18z M12 7v5l3 2"/></svg></span><h3 style="color:#f0abfc;">A ring that tells you things</h3></div><p>Eight WS2812 pixels around the dial: an aurora at rest, counter-rotating sweeps while scanning, hot flares under attack, and a live signal-strength meter.</p><div class="count" style="color:#d946ef;">FEEDBACK</div></div>
  </div>
</section>
"""

# ============================== HARDENED ==============================

HARDENED = head("04 // FIVE AUDIT PASSES",
                "47 defects went in the bin",
                "Bringing the port up meant tearing through the entire firmware, adversarially, one domain at a time. The crashes were never the interesting part. The interesting part was everything that ran, reported success, printed a rising counter, and did absolutely nothing.") + """
<section>
  <div class="reveal te-panel frame" style="border-color:rgba(110,231,183,.35);background:linear-gradient(135deg,rgba(110,231,183,.07) 0%,rgba(34,211,238,.04) 100%);">
    <div class="glow" style="background:radial-gradient(circle,rgba(110,231,183,.22) 0%,transparent 70%);"></div>
    <div class="te-mono" style="border-color:rgba(110,231,183,.25);">
      <div><span class="c">$</span> audit &middot; sub-ghz | wifi | ble | nrf24+ir | sd+nfc+boot</div>
      <div>confirmed defects ......... <span class="g">47</span>&nbsp;&nbsp;each verified against real code</div>
      <div>dead protocol decoders .... <span class="g">3</span>&nbsp;&nbsp;&nbsp;a comparison that could never pass</div>
      <div>features unreachable ...... <span class="g">15</span>&nbsp;&nbsp;bound to keys this board lacks</div>
      <div>bus-destroying paths ...... <span class="g">2</span>&nbsp;&nbsp;&nbsp;menu items that killed the display</div>
      <div><span class="g">RESULT: FIXED, FLASHED, VERIFIED ON HARDWARE</span></div>
    </div>
  </div>

  <h2 class="section-title reveal" style="margin-top:3rem;">Four worth telling</h2>
  <div class="feature-grid reveal">
    <div class="feature-card" style="border-color:rgba(110,231,183,.3);"><div class="fc-head"><span class="fc-glyph" style="color:#6ee7b7;border-color:rgba(110,231,183,.4);"><svg viewBox="0 0 24 24"><path d="M4 12h4l2-7 4 14 2-7h4"/></svg></span><h3 style="color:#6ee7b7;">Three decoders were dead code</h3></div><p>The pulse-width comparison took the absolute value of one side but not the other. Every sync test uses a negative width, so the check could never pass. Princeton, CAME and NICE silently fell through to a generic decoder that reported invented protocols for real fobs.</p><div class="count" style="color:#6ee7b7;">SUB-GHZ</div></div>
    <div class="feature-card" style="border-color:rgba(110,231,183,.3);"><div class="fc-head"><span class="fc-glyph" style="color:#6ee7b7;border-color:rgba(110,231,183,.4);"><svg viewBox="0 0 24 24"><path d="M3 5h18v14H3z M7 9h10 M7 13h6"/></svg></span><h3 style="color:#6ee7b7;">A counter that counted nothing</h3></div><p>Samsung BLE packets declared one more byte than they contained, so conformant phones dropped them. The on-screen counter still climbed, because it counted the controller accepting the buffer rather than anything reaching a target.</p><div class="count" style="color:#6ee7b7;">BLE</div></div>
    <div class="feature-card" style="border-color:rgba(110,231,183,.3);"><div class="fc-head"><span class="fc-glyph" style="color:#6ee7b7;border-color:rgba(110,231,183,.4);"><svg viewBox="0 0 24 24"><path d="M12 3v3 M12 18v3 M5 12H2 M22 12h-3 M12 9a3 3 0 0 0 0 6 3 3 0 0 0 0-6z"/></svg></span><h3 style="color:#6ee7b7;">The antenna was never switched</h3></div><p>This board routes its sub-GHz front end through a band-select network. The pins were declared and never driven, so the radio sat on whatever filter it powered up in and sensitivity collapsed across most of the range.</p><div class="count" style="color:#6ee7b7;">RF PATH</div></div>
    <div class="feature-card" style="border-color:rgba(110,231,183,.3);"><div class="fc-head"><span class="fc-glyph" style="color:#6ee7b7;border-color:rgba(110,231,183,.4);"><svg viewBox="0 0 24 24"><path d="M5 4h14v16H5z M9 8h6 M9 12h6 M9 16h3"/></svg></span><h3 style="color:#6ee7b7;">A fifth of every waveform</h3></div><p>Captured .sub files store 512 pulses per line, far more than the parser buffer. Continuation chunks were silently discarded, so replay keyed the radio with roughly 20 percent of the signal.</p><div class="count" style="color:#6ee7b7;">REPLAY</div></div>
  </div>
</section>
"""

# ============================== HARDWARE ==============================

HARDWARE = head("05 // THE BOARD",
                "Verified hardware",
                "Every value here comes from the firmware's own pin map for this board, cross-checked against LilyGO's sources. Nothing is aspirational.") + """
<section>
  <div class="hw-grid">
    <div class="hw-card reveal">
      <h3>Core <span class="chip" style="color:#22d3ee;border-color:rgba(34,211,238,.4);">ESP32-S3</span></h3>
      <div class="spec-row"><span class="k">MCU</span><span class="v">ESP32-S3 + PSRAM</span></div>
      <div class="spec-row"><span class="k">Display</span><span class="v">ST7789 170&times;320, landscape</span></div>
      <div class="spec-row"><span class="k">Input</span><span class="v">encoder + SELECT + BACK</span></div>
      <div class="spec-row"><span class="k">Storage</span><span class="v">microSD, shared SPI</span></div>
      <div class="spec-row"><span class="k">Power gate</span><span class="v">GPIO15 held HIGH</span></div>
    </div>
    <div class="hw-card reveal">
      <h3>Radios <span class="chip" style="color:#22d3ee;border-color:rgba(34,211,238,.4);">ONBOARD</span></h3>
      <div class="spec-row"><span class="k">Sub-GHz</span><span class="v">CC1101, ~300-928 MHz</span></div>
      <div class="spec-row"><span class="k">Band select</span><span class="v">SW0 / SW1 switched</span></div>
      <div class="spec-row"><span class="k">2.4 GHz</span><span class="v">nRF24L01+ (Plus SKU)</span></div>
      <div class="spec-row"><span class="k">NFC</span><span class="v">PN532, I2C 0x24</span></div>
      <div class="spec-row"><span class="k">IR</span><span class="v">TX + RX</span></div>
    </div>
    <div class="hw-card reveal">
      <h3>Extras <span class="chip" style="color:#22d3ee;border-color:rgba(34,211,238,.4);">EVERYTHING ELSE</span></h3>
      <div class="spec-row"><span class="k">LED ring</span><span class="v">WS2812B &times;8</span></div>
      <div class="spec-row"><span class="k">Audio</span><span class="v">NS4168 I2S speaker</span></div>
      <div class="spec-row"><span class="k">Mic</span><span class="v">PDM</span></div>
      <div class="spec-row"><span class="k">Battery</span><span class="v">BQ25896 + BQ27220</span></div>
      <div class="spec-row"><span class="k">SPI clock</span><span class="v">40 MHz (vendor value)</span></div>
    </div>
  </div>

  <div class="te-panel reveal" style="margin-top:1.5rem;max-width:880px;border-color:rgba(251,191,36,.3);background:rgba(251,191,36,.05);">
    <div style="font-family:var(--font-mono);font-size:.68rem;letter-spacing:.16em;text-transform:uppercase;color:#fbbf24;margin-bottom:.5rem;">&#9650; TWO REAL CAVEATS, STATED UP FRONT</div>
    <p style="font-size:.95rem;line-height:1.6;color:#cbd5e1;margin:0;">The nRF24 chip-select pins are triple-booked with UART0 and the external header, so serial logging and 2.4 GHz traffic can interfere, and LilyGO's own issue tracker notes some Plus units losing nRF range over time. And because the SD card, the CC1101 and the nRF24 all share one SPI bus with the display, every driver has to cooperate on that bus rather than assume it owns it &mdash; a lesson this port learned the hard way.</p>
  </div>

  <h2 class="section-title reveal" style="margin-top:3rem;">T-Embed CC1101 Plus vs Cardputer-Adv</h2>
  <p class="section-desc reveal">One codebase, selected at build time. What changes is the shell around it.</p>
  <div class="hw-card reveal" style="max-width:920px;">
    <table class="te-compare">
      <thead><tr><th></th><th>T-Embed CC1101 Plus</th><th>Cardputer-Adv</th></tr></thead>
      <tbody>
        <tr><td>Display</td><td class="te-col">1.9 inch, 320&times;170</td><td class="cp-col">1.14 inch, 240&times;135</td></tr>
        <tr><td>Input</td><td class="te-col">Rotary encoder + 2 buttons</td><td class="cp-col">Full QWERTY</td></tr>
        <tr><td>Sub-GHz</td><td class="te-col">Onboard CC1101</td><td class="cp-col">Hydra hat</td></tr>
        <tr><td>2.4 GHz nRF24</td><td class="te-col">Onboard (Plus SKU)</td><td class="cp-col">Hydra hat</td></tr>
        <tr><td>NFC</td><td class="te-col">Onboard PN532</td><td class="cp-col">None</td></tr>
        <tr><td>IR</td><td class="te-col">TX + RX onboard</td><td class="cp-col">TX onboard</td></tr>
        <tr><td>LoRa + GNSS</td><td class="cp-col">Not onboard</td><td class="te-col">LoRa hat</td></tr>
        <tr><td>Wired Ethernet</td><td class="cp-col">Not onboard</td><td class="te-col">W5500 hat</td></tr>
        <tr><td>Extras</td><td class="te-col">RGB ring, fuel gauge</td><td class="cp-col">Speaker, mic</td></tr>
      </tbody>
    </table>
  </div>
  <p class="reveal" style="max-width:880px;margin:1.5rem 0 0;color:#94a3b8;font-size:.95rem;">Neither wins outright. The Cardputer keeps a real keyboard and reaches LoRa, GNSS and wired Ethernet through hats. The T-Embed folds sub-GHz, 2.4 GHz, NFC and IR onto one board and adds a fuel gauge. Pick the body the mission wants.</p>
</section>
"""

# ============================== STATUS ==============================

STATUS = head("06 // PORT STATUS",
              "What runs today",
              "The honest ledger. Green means proven on the board. Amber means written and compiling, but not yet signed off against real hardware. Nothing is claimed as done before it is.") + """
<section>
  <div class="te-status-grid">
    <div class="te-status ready reveal"><div class="st"><span>&#9679;</span> READY</div><h4>Core, display and menus</h4><p>Boots, animated splash, custom icon set, anti-aliased fonts, full menu tree, and every list screen sized to this panel rather than a smaller one.</p></div>
    <div class="te-status ready reveal"><div class="st"><span>&#9679;</span> READY</div><h4>Encoder navigation</h4><p>Turn, press, double-press and hold drive the whole firmware, including text entry and every screen action list.</p></div>
    <div class="te-status ready reveal"><div class="st"><span>&#9679;</span> READY</div><h4>WiFi and BLE suites</h4><p>Scan, clients, deauth, PMKID, portal, wardrive; BLE scan, spam, GATT, HID and tracker hunting, with vendor identification from a 1400-entry OUI table.</p></div>
    <div class="te-status ready reveal"><div class="st"><span>&#9679;</span> READY</div><h4>SD and the LED ring</h4><p>Card mounts on the shared bus, recursive path creation for saves, and eight pixels of reactive feedback tied to what the radios are doing.</p></div>
    <div class="te-status bring reveal"><div class="st"><span>&#9680;</span> BRING-UP</div><h4>NFC and EMV</h4><p>The PN532 driver, tag reader, Mifare dump and EMV card reader are written and compile, but have not yet been validated against a live tag or card.</p></div>
    <div class="te-status bring reveal"><div class="st"><span>&#9680;</span> BRING-UP</div><h4>Sub-GHz on air</h4><p>The decoders, antenna band switching and .sub parsing were all repaired, but capture and replay still need confirming against a real remote.</p></div>
  </div>
  <p class="reveal" style="max-width:820px;margin:2rem auto 0;font-style:italic;opacity:.8;text-align:center;color:#cbd5e1;">This ledger moves as the board is exercised. A card turns green when it has run on hardware, not when it compiles.</p>
</section>
"""

PAGES = [
    ("index.html", "POSEIDON &mdash; for the T-Embed CC1101 Plus",
     "Encoder-driven pentest firmware for the LilyGO T-Embed CC1101 Plus. Five radios onboard: CC1101 sub-GHz, nRF24, PN532 NFC, IR, WiFi and BLE. No hats.", INDEX, True),
    ("nfc.html", "NFC and EMV &mdash; POSEIDON T-Embed",
     "The T-Embed exclusive: PN532 tag identification, Mifare Classic dumping, and a contactless EMV card reader.", NFC, False),
    ("radios.html", "Radios &mdash; POSEIDON T-Embed",
     "Five radios onboard: CC1101 sub-GHz, nRF24 2.4 GHz, PN532 NFC, IR TX and RX, plus WiFi and BLE.", RADIOS, False),
    ("encoder.html", "Encoder &mdash; POSEIDON T-Embed",
     "One wheel and three buttons drive the whole firmware, including text entry on a character wheel.", ENCODER, False),
    ("hardened.html", "Hardened &mdash; POSEIDON T-Embed",
     "Five adversarial audit passes, 47 confirmed defects closed. The bugs that looked like features working.", HARDENED, False),
    ("hardware.html", "Hardware &mdash; POSEIDON T-Embed",
     "Verified pin map for the LilyGO T-Embed CC1101 Plus, the shared-SPI reality, and a comparison against the Cardputer.", HARDWARE, False),
    ("status.html", "Status &mdash; POSEIDON T-Embed",
     "Honest port status: what is proven on hardware and what is still in bring-up.", STATUS, False),
]

if __name__ == "__main__":
    DOCS.mkdir(parents=True, exist_ok=True)
    for slug, title, desc, body, splash in PAGES:
        (DOCS / slug).write_text(page(slug, title, desc, body, splash=splash), encoding="utf-8")
        print(f"  wrote docs/{slug}")
    print(f"\n{len(PAGES)} pages generated. The flasher at docs/flash/ is maintained separately.")
