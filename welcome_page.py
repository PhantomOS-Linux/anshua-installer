import sys
import gi
from config_manager import ConfigManager

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")

from gi.repository import Gtk, Adw

class WelcomePage(Gtk.Box):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_orientation(Gtk.Orientation.VERTICAL)
        self.set_vexpand(True)
        self.set_hexpand(True)
        self.set_valign(Gtk.Align.FILL)
        self.set_halign(Gtk.Align.FILL)
        self.set_spacing(20)
        self.set_margin_top(20)
        self.set_margin_bottom(15)
        self.set_margin_start(15)
        self.set_margin_end(15)

        self.configMgr = ConfigManager("config")
        self.config = self.configMgr.get_config()

        self.center_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.center_box.set_vexpand(True)
        self.center_box.set_valign(Gtk.Align.CENTER)
        self.center_box.set_halign(Gtk.Align.CENTER)

        self.system_name = getattr(self.config, "system_name", "Anshua OS")

        self.title = Gtk.Label(label=f"Welcome to the {self.system_name} Installer")
        self.title.set_halign(Gtk.Align.CENTER)
        self.description = Gtk.Label(label=f"This installer will guide you through the installation process of {self.system_name}. Click 'Next' to continue.")
        self.description.set_halign(Gtk.Align.CENTER)
        self.description.add_css_class("dim-label")

        self.logo = Gtk.Picture.new_for_filename("logo.png")
        self.logo.set_can_shrink(True)
        self.logo.set_halign(Gtk.Align.CENTER)
        self.logo.set_valign(Gtk.Align.CENTER)
        self.logo.set_size_request(256, 256)


        self.center_box.append(self.title)
        self.center_box.append(self.logo)
        self.center_box.append(self.description)

        self.append(self.center_box)

        self.bottom_bar = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.bottom_bar.set_hexpand(True)
        self.bottom_bar.set_halign(Gtk.Align.END)

        self.next_button = Gtk.Button(label="Next")
        self.next_button.add_css_class("suggested-action")
        self.bottom_bar.set_valign(Gtk.Align.END)
        self.bottom_bar.append(self.next_button)

        self.append(self.bottom_bar)