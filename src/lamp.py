"""
| Dimmer swith level | Bulb with 30 wattage | Bulb with 50 wattage | Bulb with 70 wattage |
| ------------------ | -------------------- | -------------------- | -------------------- |
| 5		             | 0 brightness 	    | 0 brightness 	       | 0 brightness 	      |
| 10	       	     | 15 brightness 	    | 25 brightness 	   | 35 brightness 	      |
| 15		         | 30 brightness 	    | 50 brightness 	   | 70 brightness 	      |
"""


class Dimmer:
    def __init__(self, level=5):
        self.level = level
        self.wattage = 0
        self._update_wattage(level)
        self.bulbs = []

    def add_bulbs(self, bulbs):
        for bulb in bulbs:
            self.bulbs.append(bulb)
            self._update_bulb_brightness(bulb)

    def switch_level(self, level):
        self.level = level
        self._update_wattage(level)
        self._update_bulbs_brightness()

    def _update_wattage(self, level):
        if level == 5:
            self.wattage = 0
        elif level == 10:
            self.wattage = 0.5
        elif level == 15:
            self.wattage = 1
        else:
            raise Exception

    def _update_bulbs_brightness(self):
        for bulb in self.bulbs:
            self._update_bulb_brightness(bulb)

    def _update_bulb_brightness(self, bulb):
        bulb.update_brightness(self.wattage)


class Bulb:
    def __init__(self, wattage):
        self.wattage = wattage
        self.brightness = 0

    def update_brightness(self, dimmer_wattage):
        self.brightness = self.wattage * dimmer_wattage


if __name__ == "__main__":
    # Dimmers
    d = Dimmer()
    assert d.level == 5
    assert d.wattage == 0

    # Bulbs
    b1 = Bulb(wattage=30)
    assert b1.wattage == 30
    assert b1.brightness == 0
    b2 = Bulb(wattage=50)
    assert b2.wattage == 50
    assert b2.brightness == 0
    b3 = Bulb(wattage=70)
    assert b3.wattage == 70
    assert b2.brightness == 0

    # Bulbs on Dimmer with level 5
    bulbs = [b1, b2, b3]
    d.add_bulbs(bulbs)
    assert d.bulbs == bulbs
    for bulb in bulbs:
        assert bulb.brightness == 0

    # Bulbs on Dimmer with level 10
    d.switch_level(10)
    assert d.level == 10
    assert d.wattage == 0.5
    assert b1.brightness == 15
    assert b2.brightness == 25
    assert b3.brightness == 35

    # Bulbs on Dimmer with level 15
    d.switch_level(15)
    assert d.level == 15
    assert d.wattage == 1
    assert b1.brightness == 30
    assert b2.brightness == 50
    assert b3.brightness == 70

    # Add bulb on dimmer with level 15
    b4 = Bulb(30)
    d.add_bulbs([b4])
    assert b4.brightness == 30

    # Add bulb on dimmer with level 10
    b5 = Bulb(50)
    d.switch_level(10)
    d.add_bulbs([b5])
    assert b5.brightness == 25
