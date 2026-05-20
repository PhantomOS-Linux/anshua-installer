import sys
import gi

from welcome_page import WelcomePage


from config_manager import ConfigManager

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")

from gi.repository import Gtk, Adw

class AnshuaInstaller(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.config = ConfigManager("config").get_config()

        self.set_title("Anshua Installer")
        self.set_default_size(1200, 800)


        self.main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.main_box.set_hexpand(True)
        self.main_box.set_vexpand(True)
        self.set_child(self.main_box)

        self.widgets = Gtk.Stack()
        self.main_box.append(self.widgets)

        # Widgets
        self.welcome_page = WelcomePage()
        self.widgets.add_named(self.welcome_page, "welcome")

        self.widgets.set_visible_child_name("welcome")


class AnshuaInstallerApp(Adw.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connect('activate', self.on_activate)

    def on_activate(self, app):
        self.win = AnshuaInstaller(application=app)
        self.win.present()

app = AnshuaInstallerApp(application_id="com.phantomos.anshuainstaller")
app.run(sys.argv)