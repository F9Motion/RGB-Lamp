# RGB Lamp

A cylindrical frosted-glass mood lamp with 4 addressable RGB LEDs, a small OLED screen and two buttons. It has 14 color modes, adjustable brightness and a smooth fade on/off. The whole thing sits on a custom round PCB and is powered over USB-C.
<img width="1920" height="1080" alt="FINAL" src="https://github.com/user-attachments/assets/a9f7becf-06a9-4e47-866b-a3bb0af1a1fb" />

## Why I made this
I find RGB Lamp like this in marketplace and take idea :D

## Features

- 14 modes: Rainbow, Aqua, Heart, White, Warm Yellow, Orange, Red, Neon, Purple, Blue, Green, Lime, Indigo, Soft Peach
- Brightness from 10% to 100% in steps of 10%
- Smooth fade in and fade out when turning on and off
- Breathing animation mode
- OLED screen with a boot animation that turns off after 15 seconds of inactivity
- Settings (mode and brightness) are saved and restored after power loss
- Custom round PCB designed in KiCad
- USB-C powered

## Pictures

### Full 3D model
<img width="1920" height="1080" alt="FINAL" src="https://github.com/user-attachments/assets/172d4bb6-7ee1-414d-93d1-5cda9480ea07" />


### PCB
<img width="1065" height="663" alt="Снимок экрана 2026-10-10 174252" src="https://github.com/user-attachments/assets/08adc8c2-da7d-47c6-a527-db3ddb53547e" />

## How it works

The ESP32 runs MicroPython firmware that drives 4 addressable LEDs through a single data pin. Two tactile buttons control modes and brightness, and an SSD1306-compatible OLED on the I2C bus shows the status. The glass diffuser spreads the light from the LEDs into one even glow.

| Function        | GPIO |
|-----------------|------|
| LED data        | 2    |
| Button 1        | 4    |
| Button 2        | 5    |
| OLED SDA        | 8    |
| OLED SCL        | 9    |

## Controls

| Action                          | Result                          |
|---------------------------------|---------------------------------|
| Button 1: hold for 2 seconds    | Turn the lamp on / off (fade)   |
| Button 1: short press           | Next mode                       |
| Button 1: double press          | Brightness +10%                 |
| Button 2: short press           | Previous mode                   |
| Button 2: quick repeated press  | Brightness −10%                 |

## How to assemble

1. **Order the PCB.** Use the Gerber files from the `/pcb` folder (KiCad project: `RGB_LAMP.kicad_pro`).
2. **Print the parts.** Print `bottom.step`, `top.step` and `pushes.step` from the `/cad` folder. Suggested settings: PLA, 0.2 mm layer height, [15%] infill. The `glass.step` part is the diffuser: print it in white/translucent filament or use a frosted tube [choose one].
3. **Solder the PCB.** Solder the SMD parts first (resistors, LEDs, small ICs, USB-C), then the through-hole parts (ESP32 module, buttons, connector).
4. **Connect the OLED.** Solder the OLED display to the 4-pin header on the edge of the PCB (VCC, GND, SDA, SCL).
5. **Flash the firmware** (see the next section) and test the lamp before closing it.
6. **Install the PCB** into the bottom part. The two buttons should line up with the holes in the base, and the OLED with the rectangular window.
7. **Insert the button caps** (`pushes`) into the holes.
8. **Close the lamp.** Place the glass diffuser on the base and fit the top cap.

## How to flash

1. Install [Thonny](https://thonny.org/).
2. Flash MicroPython to the ESP32 (Thonny: *Tools → Options → Interpreter → Install or update MicroPython*).
3. Open `firmware/firmware.py` in Thonny.
4. Save it to the board as `main.py` (*File → Save as → MicroPython device*).
5. Restart the board. The OLED shows a loading bar and the lamp is ready.

## Bill of Materials (BOM)
| Object name | Cost | Link |
|----------------|-------|---------------------------------------------------------------------------------------------------------------------------------------|
| Baterry | $9.16 | https://aliexpress.ru/item/1005008218024646.html?spm=a2g2w.cart.cart_split.2.17184aa6sdf0tM&sku_id=12000044269020504 |
| Capisitor 1 | $1.72 | https://aliexpress.ru/item/1005008523091680.html?spm=a2g2w.cart.cart_split.4.17184aa6sdf0tM&sku_id=12000045550598782 |
| Capisator 2 | $2.13 | https://aliexpress.ru/item/1005008523091680.html?spm=a2g2w.cart.cart_split.5.17184aa6sdf0tM&sku_id=12000045550598821 |
| Rezistors 1 | $2.13 | https://aliexpress.ru/item/1005008523091680.html?spm=a2g2w.cart.cart_split.5.17184aa6sdf0tM&sku_id=12000045550598821 |
| Rezistors 2 | $1.32 | https://aliexpress.ru/item/1005010124491295.html?spm=a2g2w.cart.cart_split.8.17184aa6sdf0tM&sku_id=12000051226894950 |
| Rezistors 3 | $1.32 | https://aliexpress.ru/item/1005010124491295.html?spm=a2g2w.cart.cart_split.9.17184aa6sdf0tM&sku_id=12000051226894989 |
| Type- C | $1.98 | https://aliexpress.ru/item/1005009725016771.html?spm=a2g2w.cart.cart_split.11.17184aa6sdf0tM&sku_id=12000049959236831 |
| Inductor | $1.79 | https://aliexpress.ru/item/1005010057784411.html?spm=a2g2w.cart.cart_split.13.17184aa6sdf0tM&sku_id=12000050979456491 |
| MT3608 | $1.40 | https://aliexpress.ru/item/1005008595377934.html?spm=a2g2w.cart.cart_split.15.17184aa6sdf0tM&sku_id=12000045882365662 |
| Diode | $1.22 | https://aliexpress.ru/item/4000331408791.html?spm=a2g2w.cart.cart_split.17.17184aa6sdf0tM&sku_id=10000001361365766 |
| Display | $1.78 | https://aliexpress.ru/item/1005011610851521.html?spm=a2g2w.cart.cart_split.19.17184aa6sdf0tM&sku_id=12000056053164321 |
| Pushes | $0.68 | https://aliexpress.ru/item/1005006046180384.html?spm=a2g2w.cart.cart_split.21.17184aa6sdf0tM&sku_id=12000035472972531 |
| RGB Diodes | $1.82 | https://aliexpress.ru/item/1005002055349908.html?spm=a2g2w.cart.cart_split.23.17184aa6sdf0tM&sku_id=12000034806960293 |
| MCP73831T-2ACI | $1.09 | https://aliexpress.ru/item/1005003129269009.html?spm=a2g2w.cart.cart_split.25.17184aa6sdf0tM&sku_id=12000024251863101 |
| ESP32 | $4.28 | https://aliexpress.ru/item/1005005046672312.html?spm=a2g2w.cart.cart_split.27.17184aa6sdf0tM&sku_id=12000034261565598 |
| Print PCB | $13 | |
| top.step | $0.37 |
| bottom.step | $0.53 |
| glass.step | $0.7 |
| pushes.step | $0.01 |

## Credits
- CAD: Blender, PCB: KiCad
- Everything else (design, PCB, firmware): Rasul
