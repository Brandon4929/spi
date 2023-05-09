from luma.core.interface.serial import spi
from luma.oled.device import ssd1322
from luma.core.render import canvas

serial = spi(port=0, device=0)
device = ssd1322(serial, rotate=0)

with canvas(device) as draw:
    draw.text((10, 10), "Testing 123", fill="white")

