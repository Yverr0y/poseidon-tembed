<!-- markdownlint-disable MD033 MD041 -->

<div align="center">

```
██████╗  ██████╗ ███████╗███████╗██╗██████╗  ██████╗ ███╗   ██╗
██╔══██╗██╔═══██╗██╔════╝██╔════╝██║██╔══██╗██╔═══██╗████╗  ██║
██████╔╝██║   ██║███████╗█████╗  ██║██║  ██║██║   ██║██╔██╗ ██║
██╔═══╝ ██║   ██║╚════██║██╔══╝  ██║██║  ██║██║   ██║██║╚██╗██║
██║     ╚██████╔╝███████║███████╗██║██████╔╝╚██████╔╝██║ ╚████║
╚═╝      ╚═════╝ ╚══════╝╚══════╝╚═╝╚═════╝  ╚═════╝ ╚═╝  ╚═══╝

         ≋≋≋   commander of the deep   ≋≋≋
      ────────  now on the T-Embed  ────────
```

**Dial-driven pentesting firmware for the LilyGO T-Embed CC1101 Plus**

![target](https://img.shields.io/badge/target-T--Embed%20CC1101%20Plus-red?style=flat-square)
![platform](https://img.shields.io/badge/framework-Arduino%2FPlatformIO-blue?style=flat-square)
![license](https://img.shields.io/badge/license-MIT-green?style=flat-square)
![features](https://img.shields.io/badge/features-128-magenta?style=flat-square)
![version](https://img.shields.io/badge/version-0.6.8-cyan?style=flat-square)
![radios](https://img.shields.io/badge/radios-5%20onboard-8b5cf6?style=flat-square)
![nfc](https://img.shields.io/badge/NFC%2FEMV-untested-f59e0b?style=flat-square)

**128 features. Five radios. One knob.**
POSEIDON already owned the Cardputer. Now it runs on the **LilyGO T-Embed CC1101 Plus** — a 320x170 panel, a clicky rotary encoder wrapped in an 8 LED ring, and a radio stack soldered to the board instead of bolted onto a hat. Sub-GHz, 2.4 GHz, WiFi, BLE, IR **and a real PN532 NFC reader**, all at once, no swapping, no add-ons.

[**Flash it in your browser →**](https://generaldussduss.github.io/poseidon-tembed/flash/) · [Web site](https://generaldussduss.github.io/poseidon-tembed/) · [Firmware source](https://github.com/GeneralDussDuss/poseidon) · [Cardputer edition](https://generaldussduss.github.io/poseidon/)

**◐ Read this first.** Most of this is running on real hardware right now. **NFC, EMV and over the air sub-GHz are not.** That code is written and flashed but has never been validated against a live tag, a real card, or a real fob. [Full honest status ↓](#-what-actually-works)

</div>

---

## ⌁ The one thing the Cardputer cannot do

The Cardputer needs a hat for sub-GHz, and a *different* hat for 2.4 GHz, and it has no NFC at all. You pick one and live with it.

The T-Embed has **all of them soldered on**, plus the one chip POSEIDON never had anywhere: a **PN532 NFC reader**. That is a genuinely new class of target — contactless cards, transit passes, access badges, tags — reachable from the same menu as everything else.

No hats. No swapping. No compromise.

---

## 🌊 New to all this? Start here

POSEIDON is a **pocket hacking gadget**. It runs on a small handheld with a screen and a dial, and turns it into a Swiss army knife for the invisible signals all around you. **No PC, no coding.** Flash it once and start turning the knob.

**What can it actually do?**

- 📶 **WiFi** — see every network around you, test your own, map them as you walk
- 📱 **Bluetooth** — find lost trackers (AirTags / Tiles), spot hidden ones following you
- 🚗 **Remotes and signals** — record and replay garage doors, fobs, doorbells *(on stuff you own)*
- 💳 **NFC** — read tags and contactless cards held against the back of the board
- 📺 **Infrared** — a universal TV remote, plus the classic "turn every TV off" button
- 🐾 **Argus** — an on screen pet that hunts WiFi handshakes on its own and reacts with moods
- 💡 **A light ring** that animates to whatever the radios are doing

**Get it on your device (about 2 minutes):**

1. Open the [**web flasher**](https://generaldussduss.github.io/poseidon-tembed/flash/) in Chrome or Edge
2. Plug the T-Embed in over USB-C, click **Connect**, pick the port
3. Click **Install**. Wait. It boots straight to the menu.

> ⚠️ **Be cool.** This is for exploring *your own* stuff and learning how wireless actually works. Do not touch networks or devices you do not own — that is both uncool and illegal.

<div align="center">

### ⌁ Want the deep technical breakdown? The nerd zone starts here. ⌁

</div>

---

## What is this?

POSEIDON is pentesting firmware for the **LilyGO T-Embed CC1101 Plus** (ESP32-S3, 16 MB flash, PSRAM, 320x170 ST7789, rotary encoder). It is the same codebase as the [Cardputer edition](https://github.com/GeneralDussDuss/poseidon), compiled for a board with a completely different input model and a much better radio loadout.

**The Cardputer version is keyboard first. This one is not** — there is no keyboard to be first with. Every screen was reworked around a dial:

- **Turn** to move, **press** to select, **double press** to go back, **hold** for a context menu
- **Text entry by character wheel** — spin to a letter, press to commit
- **Full panel layouts** — 320x170 is 68% more pixels than the Cardputer, and every list screen was re laid out to actually use them
- **An 8 LED ring** around the encoder that animates per activity
- **Anti aliased icons** drawn from five 96px sprite sheets, real fonts, no pixel mush

Everything that needed an external module on the Cardputer is **compiled out** of this build. No Feather menu, no C5 satellite menu, no MIMIR. If it is in the menu, this board's own hardware does it.

---

## Quick Start — Flash it

### Browser flasher (easiest, nothing to install)

Chrome, Edge or Opera. Plug the T-Embed in over USB-C and open:

> **<https://generaldussduss.github.io/poseidon-tembed/flash/>**

Click **Connect**, pick the serial port, hit **Install**. The page writes the factory image at offset `0x0` for you.

> ### ⚠️ Flash at 115200, not 921600
>
> This board drops the USB link partway through a fast write, leaving a half written image and a device that **looks dead**. At 115200 it writes 4.7 MB in about 25 seconds with zero retries. The flasher already pins this for you.
>
> **A "dead" board after a failed flash is almost certainly fine.** GPIO15 is a soft power latch that the firmware has to hold high — with no valid app, the board simply powers itself off. Re flash at 115200 and it comes back.

### Command line

```bash
pip install esptool
esptool --chip esp32s3 --port COM3 --baud 115200 write_flash 0x0 poseidon-tembed-factory.bin
```

The factory image already contains bootloader, partition table and app at their correct offsets, so `0x0` is all you need.

### Build from source

Firmware source lives in the **main POSEIDON repo**, built with the `tembed` environment:

```bash
git clone https://github.com/GeneralDussDuss/poseidon.git
cd poseidon
pio run -e tembed -t upload
```

*(This repo holds the showcase site, the browser flasher and the prebuilt image.)*

---

## Feature Overview (128)

Every one of these is compiled into the T-Embed build. Nothing here needs an add on.

| Category | Count | What is in it |
|---|---|---|
| **WiFi** | 21 | Scan, deauth, beacon spam, evil portal, PMKID hunt, handshake capture, wardrive, karma |
| **Bluetooth LE** | 18 | Scan, tracker detect, SourApple / Android / Samsung spam, HID, sniffer, spoof |
| **Network / LAN** | 20 | Port scan, ping, DNS, ARP, connect, plus the SaltyJack LAN attack suite |
| **Infrared** | 15 | TV-B-Gone, Samsung remote, capture, replay, learn, and 10 pranks |
| **Sub-GHz (CC1101)** | 9 | Scan, capture, replay, broadcast, jam, `.sub` file support, band select antenna |
| **2.4 GHz (nRF24)** | 6 | Scan, jam, MouseJack, channel sweep |
| **BadUSB** | 8 | Live keyboard, DuckyScript runner, 165+ payloads |
| **System** | 11 | Files, clock, WiFi credentials, theme, brightness, settings |
| **Tools** | 8 | Flashlight, stopwatch, dice, and friends |
| **Argus** | 4 | Autonomous handshake hunting gotchi with a mood sprite |
| **NFC** ◐ | 2 | PN532 tag reader plus a contactless **EMV card reader** |
| **Other** | 6 | Mesh beacon, PC bridge, SD mass storage, KERBEROS FIDO2 |

---

## 💳 The NFC stack ◐

The headline feature of this board, and **the one that still needs proving**.

The T-Embed carries a **PN532 on I2C** — the same chip in most hobbyist NFC readers. POSEIDON drives it with a hand written transport, then layers a real **EMV parser** on top:

```
PPSE  →  AID select  →  GPO  →  AFL record walk  →  BER-TLV decode
```

That is meant to surface PAN (tag `5A`), expiry (`5F24`), cardholder name (`5F20`) and Track 2 equivalent data (`57`) off a contactless card held against the back of the board — the same trick a Flipper does.

**It has never read a real card.** The driver is complete, the record walk is bounds checked, and it is flashed on the device, but until a live card confirms it, treat it as unproven. If it fails, open the NFC screen with serial attached at 115200 — it prints an I2C bus scan telling you whether the PN532 is answering at all, which separates a wiring fault from a code fault.

---

## ◐ What actually works

Straight answer, no marketing.

| Subsystem | State |
|---|---|
| Boot, animated splash, menus, icons, fonts | ✅ Running on hardware |
| Rotary encoder navigation and character wheel text entry | ✅ Running on hardware |
| Display, full panel list layouts, LED ring | ✅ Running on hardware |
| SD card mount and file browser | ✅ Running on hardware |
| WiFi suite (21) | ✅ Running on hardware |
| BLE suite (18) | ✅ Running on hardware |
| CC1101 driver and antenna band select | ✅ Initialises, tunes, selects band |
| **Sub-GHz capture / replay on air** | ◐ **Unproven** — decoders repaired, no live fob has confirmed it |
| **NFC tag read** | ◐ **Unproven** — has never seen a live tag |
| **EMV card read** | ◐ **Unproven** — has never seen a real card |

Those last three are the honest edge of this build. Everything above them has been watched working on the board.

---

## Hardware

| Component | Spec |
|---|---|
| MCU | ESP32-S3 @ 240 MHz, 16 MB flash, PSRAM |
| Display | 1.9" ST7789 320x170 IPS, landscape |
| Input | Rotary encoder plus select and back buttons |
| Sub-GHz | CC1101, 300-928 MHz, switched antenna network |
| 2.4 GHz | nRF24L01+ *(populated on the **Plus** SKU only)* |
| NFC | PN532 over I2C |
| WiFi / BLE | ESP32-S3 native, WiFi 4 + BLE 5.0 |
| IR | Transmit **and** receive |
| LEDs | 8x WS2812B ring around the encoder |
| Audio | NS4168 I2S speaker, PDM microphone |
| Power | BQ25896 charger, BQ27220 fuel gauge, LiPo |
| Storage | microSD, shared SPI bus |

**Plain CC1101 vs CC1101 Plus:** identical pinout. The Plus has the nRF24 module populated. On a plain unit everything works except the six 2.4 GHz features.

### Hardware notes worth knowing

- **GPIO15 is a power latch.** Firmware must hold it high or the board powers off. This is why a bad flash looks like a brick.
- **One shared SPI bus** carries display, SD, CC1101 and nRF24. Bus contention is the first suspect for odd display or SD behaviour.
- **The panel has no reset pin** (`-1`). The schematic ties it to GPIO40, but GPIO40 is the I2S word clock, and LilyGO's own sources never drive it as a reset.
- **nRF24 CS/CE sit on GPIO 43/44**, shared with UART0, so serial logging and nRF traffic can interfere.
- **The select button is GPIO0**, the BOOT strap pin. Holding it during reset enters the bootloader instead of registering a press.

---

## Legal

This is for **authorized security testing, research, and education only**. You are responsible for complying with all applicable laws. Do not use against networks or devices without explicit authorization.

MIT License. Take it, fork it, improve it.

---

<div align="center">

```
   ≋≋≋≋≋     ≋≋≋≋≋     ≋≋≋≋≋     ≋≋≋≋≋     ≋≋≋≋≋     ≋≋≋≋≋
 ≋≋     ≋≋ ≋≋     ≋≋ ≋≋     ≋≋ ≋≋     ≋≋ ≋≋     ≋≋ ≋≋     ≋≋
≋         ≋         ≋         ≋         ≋         ≋         ≋
```

*commander of the deep*

</div>
