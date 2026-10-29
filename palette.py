import re
import sys
from PIL import Image
from materialyoucolor.quantize import QuantizeCelebi
from materialyoucolor.score.score import Score
from materialyoucolor.hct import Hct
from materialyoucolor.dynamiccolor.material_dynamic_colors import MaterialDynamicColors
from materialyoucolor.scheme.scheme_tonal_spot import SchemeTonalSpot

if len(sys.argv) < 2:
    sys.exit("Usage: python palette.py path\\to\\wallpaper.png")

image = Image.open(sys.argv[1]).convert("RGB")
image.thumbnail((256, 256))

result = QuantizeCelebi(list(image.getdata()), 128)
argb = Score.score(result)[0]

scheme = SchemeTonalSpot(Hct.from_int(argb), True, 0.0)  # True = dark mode

wanted = [
    "primary", "onPrimary", "primaryContainer", "onPrimaryContainer",
    "surface", "surfaceContainerLow", "surfaceContainer", "surfaceContainerHigh",
    "onSurface", "onSurfaceVariant", "outline", "background",
]
for name in wanted:
    c = getattr(MaterialDynamicColors, name)
    r, g, b, _ = c.get_hct(scheme).to_rgba()
    css = "--" + re.sub(r"([A-Z])", lambda m: "-" + m.group(1).lower(), name)
    print(f"{css}: #{r:02x}{g:02x}{b:02x};  /* rgb({r}, {g}, {b}) */")
