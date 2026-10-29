# Sakura Lively Widgets

Material You style widget wallpaper for [Lively Wallpaper](https://www.rocksdanister.com/lively/) on Windows.

**Includes:** greeting, local clock, world clocks (Tokyo, Seoul, London, New York), vertical clock and date card, now playing, weather, CPU, RAM and battery.

## Setup

1. Install Lively Wallpaper.
2. Add your own image named `wallpaper.png` in the same folder as `index.html`.
3. Select `index.html`, `LivelyInfo.json` and `wallpaper.png` (the files, not a folder), and zip them.
4. Drag the zip into the Lively window and apply it.

`LivelyInfo.json` must contain these arguments, or CPU, RAM and now playing will stay empty:

```
"Arguments": "--system-nowplaying --system-information"
```

## Customize

- **City and weather:** change `latitude` and `longitude` in the weather `fetch` URL in `index.html`, and the "Bengaluru" labels.
- **World clocks:** edit the `zones` list in `index.html` (and the labels in the HTML).
- **Weather source:** Open-Meteo, no API key needed. It may differ slightly from your taskbar weather.

## Color palette

Edit these in the `:root` block at the top of `index.html`.

| Role | Hex | RGB |
|---|---|---|
| Primary | `#9CD1C7` | 156, 209, 199 |
| On primary | `#104841` | 16, 72, 65 |
| Primary container | `#275B53` | 39, 91, 83 |
| On primary container | `#B8EEE4` | 184, 238, 228 |
| Surface | `#0A0F0E` | 10, 15, 14 |
| On surface | `#DCE8E4` | 220, 232, 228 |
| On surface variant | `#A2ADAA` | 162, 173, 170 |
| Outline | `#6D7875` | 109, 120, 117 |
| Card background | `rgba(19, 27, 26, 0.74)` | 19, 27, 26 at 74% opacity |

## Generate a palette from your own wallpaper

```
py -m pip install -r requirements.txt
py palette.py path\to\wallpaper.png
```

It prints CSS variables with hex and RGB values. Paste them over the `:root` block in `index.html`.

## Troubleshooting

- **CPU and RAM show 0%:** check the `Arguments` line in `LivelyInfo.json`, then re-import the wallpaper and restart Lively.
- **Now playing is empty:** same fix, and make sure something is playing in a supported app or browser.
- **Preview is blank:** `LivelyInfo.json` points to `wallpaper.png`, so add your image or remove the `Thumbnail` and `Preview` lines.

## Optional: matching taskbar

Use the Windhawk mod "Windows 11 Taskbar Styler" with a LiquidGlass theme, and set the Windows accent color to `#9CD1C7`.

## Credits

Wallpaper artwork is not included. Use your own image and credit the artist if you share it.
