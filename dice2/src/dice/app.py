"""
Dice
"""

import random
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, CENTER


class Dice(toga.App):
    def startup(self):
        self.main_box = toga.Box(
            style=Pack(
                padding=10,
                alignment=CENTER,
                direction=COLUMN,
            )
        )

        self.dice = {
            "6": {
                "1": toga.Image("resources/d6_1.png"),
                "2": toga.Image("resources/d6_2.png"),
                "3": toga.Image("resources/d6_3.png"),
                "4": toga.Image("resources/d6_4.png"),
                "5": toga.Image("resources/d6_5.png"),
                "6": toga.Image("resources/d6_6.png"),
            }
        }

        self.roll_button = toga.Button(
            "Roll!",
            on_press=self.roll_dice,
            style=Pack(padding=10, width=150, height=50),
        )
        self.clear_button = toga.Button(
            "Clear!",
            on_press=self.clear,
            style=Pack(padding=10, width=150, height=50),
        )

        self.main_box.add(self.roll_button)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = self.main_box
        self.main_window.show()

    def roll_dice(self, widget):
        self.main_box.remove(self.roll_button)
        dice_number = random.randint(1, 6)
        dice_image = self.dice["6"][str(dice_number)]
        self.dice_view = toga.ImageView(dice_image, style=Pack(width=72))
        self.main_box.add(self.dice_view)
        self.main_box.add(self.clear_button)

    def clear(self, widget):
        self.main_box.remove(self.dice_view)
        self.main_box.remove(self.clear_button)
        self.main_box.add(self.roll_button)


def main():
    return Dice()
