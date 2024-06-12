import os
import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk, GLib, Gdk


APPID = 'com.github.taniyoshima.pyt_gtk4_revealer'


@Gtk.Template(filename=os.path.dirname(__file__) + '/ui_file.ui')
class Gtk4TestTest(Gtk.ApplicationWindow):

    __gtype_name__ = "window"

    revealer = Gtk.Template.Child()

    def __init__(self, app):
        Gtk.ApplicationWindow.__init__(self, application=app)

        provider = Gtk.CssProvider()
        try:
            provider.load_from_path('ui_file.css')
        except GLib.Error as e:
            print(f"CSSファイルの読み込み失敗 : {e} ")
            return None
        Gtk.StyleContext.add_provider_for_display(
            Gdk.Display.get_default(), provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

    @Gtk.Template.Callback()
    def on_button_clicked(self, button):
        self.revealer.set_reveal_child(True)

    @Gtk.Template.Callback()
    def on_revealer_button_clicked(self, button):
        self.revealer.set_reveal_child(False)


class Gtk4TestApp(Gtk.Application):

    def __init__(self):
        Gtk.Application.__init__(self, application_id=APPID)

    def do_activate(self):
        window = Gtk4TestTest(self)
        window.present()


def main():
    app = Gtk4TestApp()
    app.run()


if __name__ == '__main__':
    main()
