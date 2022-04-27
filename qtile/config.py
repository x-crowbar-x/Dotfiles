import os
# import re
# import socket
import subprocess
from libqtile import layout, bar, widget, hook, qtile
from typing import List  # noqa: F401
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.widget import Spacer

mod = "mod4"
mod1 = "alt"
mod2 = "control"
mod3 = "shift"

terminal = "alacritty"
myBrowser = "firefox"
myFileManager = "thunar"
myOfficeSuite = "libreoffice"
home = os.path.expanduser('~')


@hook.subscribe.startup_once
def autostart():
    subprocess.Popen([home + '/.config/qtile/autostart.sh'])


keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html

    Key([mod], "q", lazy.hide_show_bar(), desc="Toggles between hide/show the bar"),

    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "m", lazy.layout.next(),
        desc="Move window focus to other window"),

    # Launch applications
    Key([mod], "f", lazy.spawn(myBrowser),
        desc="Firefox"),
    Key([mod], "e", lazy.spawn(myFileManager),
        desc="Thunar"),
    Key([mod], "o", lazy.spawn(myOfficeSuite),
        desc="Libreoffice"),
    Key([mod], "a", lazy.spawn("atom"),
        desc="Launch Atom text editor"),
    Key([mod], "x", lazy.spawn(terminal),
        desc="Launch terminal"),
    Key([mod2, "shift"], "f", lazy.spawn("catfish"),
        desc="Search for files with catfish"),

    Key([mod], "c", lazy.spawn("atom .config/qtile/config.py"),
        desc="Open this Qtile confing"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawn("dmenu_run -p 'Run: '"),
        desc="Run Launcher"),
    # Brightness control
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl s +5%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl s 5%- ")),

    # Audio controls

    # Key([], "XF86AudioMute", lazy.spawn("pamixer --toggle-mute")),
    # Key([], "XF86AudioLowerVolume", lazy.spawn("pamixer --decrease 2")),
    # Key([], "XF86AudioRaiseVolume", lazy.spawn("pamixer --increase 2")),
    Key([], "XF86AudioMicMute", lazy.spawn("pamixer --source 46 -t")),
    # Music control buttons
    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause")),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next")),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous")),
    Key([], "XF86AudioStop", lazy.spawn("playerctl stop")),

    # Screenshot
    Key([], "Print", lazy.spawn(home + "/.config/qtile/full_screenshot.sh"),
        desc='Take a screenshot of the whole screen'),
    Key([mod3], "Print", lazy.spawn(home + "/.config/qtile/select_screenshot.sh"),
        desc='Select an area of the screen to take a screenshot'),

    # Window controls
    Key([mod], "h", lazy.layout.shrink(), lazy.layout.decrease_nmaster(),
        desc='Shrink window (MonadTall), decrease number in master pane (Tile)'),
    Key([mod], "l", lazy.layout.grow(), lazy.layout.increase_nmaster(),
        desc='Expand window (MonadTall), increase number in master pane (Tile)'),
    Key([mod], "m", lazy.layout.maximize(),
        desc='toggle window between minimum and maximum sizes'),
    Key([mod], "n", lazy.layout.normalize(),
        desc='normalize window size ratios'),
    Key([mod], "t", lazy.window.toggle_floating(),
        desc='Toggle floating layout'),
]

groups = [Group(i) for i in [
    "", "", "", "", "",
]]

for i, group in enumerate(groups):
    actual_key = str(i + 1)
    keys.extend([
        # Switch to workspace N
        Key([mod], actual_key, lazy.group[group.name].toscreen()),
        # Send window to workspace N
        Key([mod, "shift"], actual_key, lazy.window.togroup(group.name))
    ])

# groups = [Group("1", layout='monadtall'),
#           Group("2", layout='monadtall'),
#           Group("3", layout='monadtall'),
#           Group("4", layout='monadtall'),
#           Group("5", layout='floating')]
#
#
# for i in groups:
#     keys.extend([
#         # mod1 + letter of group = switch to group
#         Key([mod], i.name, lazy.group[i.name].toscreen(),
#             desc="Switch to group {}".format(i.name)),
#
#         # mod1 + shift + letter of group = switch to & move focused window to group
#         Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True),
#             desc="Switch to & move focused window to group {}".format(i.name)),
#         # Or, use below if you prefer not to switch to that group.
#         ## mod1 + shift + letter of group = move focused window to group
#         # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
#         #     desc="move focused window to group {}".format(i.name)),
#     ])

colors = [["#282a36", "#282a36"],  # 0
          ["#44475a", "#44475a"],  # 1
          ["#d8d8d8", "#d8d8d8"],  # 2
          ["#3080b1", "#3080b1"],  # 3
          ["#40abbf", "#89f2ff"],  # 4
          ["#c3e88d", "#a1b56c"],  # 5
          ["#ffe585", "#ffe585"],  # 6
          ["#f5c2e7", "#f5c2e7"],  # 7
          ["#d6acff", "#aa7bed"],  # 8
          ["#ab4642", "#ab4642"],  # 9
          ["#f7ca88", "#f7ca88"],  # 10
          ["#ae05fc", "#aa7bed"],  # 11
          ["#0b4d93", "#0b4d93"],  # 12
          ["#ff6e6e", "#ff6e6e"],  # 13
          ["#82aaff", "#82aaff"],  # 14
          ["#414458", "#575b75"],  # 15
          ["#172b60", "#172b60"],  # 16
          ["#164789", "#164789"],  # 17
          ["#7AEEAA", "#7AEEAA"],  # 18
          ["#f28fad", "#ba8baf"],  # 19
          ["#00000000", "#00000000"],  # 20
          ["#aa7bed", "#aa7bed"]]  # 21

layout_theme = {"border_width": 3,
                "margin": 5,
                "single_margin": 0,
                "single_border_width": 0,
                "border_focus": colors[8],
                "border_normal": colors[15]
                }

layouts = [
    # layout.Matrix(**layout_theme),
    # layout.Bsp(**layout_theme),
    # layout.RatioTile(**layout_theme),
    # layout.Zoomy(**layout_theme)
    # layout.Tile(**layout_theme),
    # layout.VerticalTile(**layout_theme),
    # layout.Columns(**layout_theme),
    # layout.MonadWide(**layout_theme),
    layout.MonadTall(**layout_theme),
    layout.Max(**layout_theme),
    layout.Stack(**layout_theme),
    layout.Floating(**layout_theme),
    # layout.TreeTab(
    #     font = 'JetBrains Mono',
    #     fontsize = 13,
    #     bg_color = colors[16],
    #     active_bg = colors[4],
    #     inactive_bg = colors[17],
    #     inactive_fg = colors[2],
    #     active_fg = colors[13],
    #     padding_left = 0,
    #     padding_x = 2,
    #     padding_y =5,
    #     section_top =10,
    #     section_bottom = 20,
    #     vspace = 3,
    #     panel_width = 220),
]

# prompt = "Run: "

# Default widget settings
widget_defaults = dict(
    font='JetBrains Mono SemiBold',
    fontsize=16,
    padding=3,
    background=colors[20],
)
extension_defaults = widget_defaults.copy()


def long_name_parse(text):
    for string in ["Firefox", "Atom", " LibreOffice", "Telegram", "E-book viewer"]:
        if string in text:
            text = string
    return text



def bat_charge():
    bat_state = subprocess.check_output(home + '/.config/qtile/bat_state.sh').decode("utf-8").replace('\n', '')
    bat_capacity = subprocess.check_output(home + '/.config/qtile/bat_capacity.sh').decode("utf-8").replace('\n', '')
    integer = int(bat_capacity)
    if (bat_state == 'Charging') and (integer <= 5):
        return ' {}% '.format(integer)
    elif (bat_state == 'Charging') and (integer <= 10):
        return ' {}% '.format(integer)
    elif (bat_state == 'Charging') and (integer <= 20):
        return ' {}% '.format(integer)
    elif (bat_state == 'Charging') and (integer <= 30):
        return ' {}% '.format(integer)
    elif (bat_state == 'Charging') and (integer <= 40):
        return ' {}% '.format(integer)
    elif (bat_state == 'Charging') and (integer <= 50):
        return ' {}% '.format(integer)
    elif (bat_state == 'Charging') and (integer <= 60):
        return ' {}% '.format(integer)
    elif (bat_state == 'Charging') and (integer <= 70):
        return ' {}% '.format(integer)
    elif (bat_state == 'Charging') and (integer <= 80):
        return ' {}% '.format(integer)
    elif (bat_state == 'Charging') and (integer <= 90):
        return ' {}% '.format(integer)
    elif (bat_state == 'Charging') and (integer <= 100):
        return ' {}% '.format(integer)
    elif (bat_state == 'Discharging') and (integer <= 5):
        return ' {}%'.format(integer)
    elif (bat_state == 'Discharging') and (integer <= 10):
        return ' {}%'.format(integer)
    elif (bat_state == 'Discharging') and (integer <= 20):
        return ' {}%'.format(integer)
    elif (bat_state == 'Discharging') and (integer <= 30):
        return ' {}%'.format(integer)
    elif (bat_state == 'Discharging') and (integer <= 40):
        return ' {}%'.format(integer)
    elif (bat_state == 'Discharging') and (integer <= 50):
        return ' {}%'.format(integer)
    elif (bat_state == 'Discharging') and (integer <= 60):
        return ' {}%'.format(integer)
    elif (bat_state == 'Discharging') and (integer <= 70):
        return ' {}%'.format(integer)
    elif (bat_state == 'Discharging') and (integer <= 80):
        return ' {}%'.format(integer)
    elif (bat_state == 'Discharging') and (integer <= 90):
        return ' {}%'.format(integer)
    elif (bat_state == 'Discharging') and (integer <= 100):
        return ' {}%'.format(integer)
    elif bat_state == 'Full':
        return ' {}%'.format(integer)
    elif bat_state == 'Unknown':
        return ' {}%'.format(integer)


screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Spacer(
                    length=10,
                ),
                widget.CurrentLayoutIcon(
                    background=colors[11],
                    fontsize=10
                ),
                widget.Spacer(
                    length=5,
                ),
                widget.CurrentLayout(
                    foreground=colors[11],
                    fontshadow=colors[15],
                    fontsize=14),
                widget.Sep(
                    linewidth=1,
                    padding=6,
                    foreground=colors[11],
                ),
                widget.GroupBox(
                    fontsize=25,
                    margin_y=5,
                    margin_x=1,
                    padding_y=5,
                    padding_x=3,
                    borderwidth=3,
                    active=colors[2],
                    inactive=colors[8],
                    rounded=True,
                    highlight_color=colors[11],
                    highlight_method="line",
                    this_current_screen_border=colors[11],
                    this_screen_border=colors[12],
                    fontshadow=colors[15],
                ),
                widget.Spacer(
                    length=6,
                ),
                widget.Sep(
                    linewidth=1,
                    padding=6,
                    foreground=colors[11],
                ),
                widget.WidgetBox(
                    text_closed='', text_open='',
                    foreground=colors[21],
                    fontsize=25,
                    fontshadow=colors[15],
                    padding=5,
                    widgets=[
                        widget.Cmus(
                            play_color=colors[21],
                            noplay_color=colors[1],
                            foreground=colors[21],
                            fontsize=20,
                            fontshadow=colors[15],
                            update_interval=1
                        )]),
                widget.Sep(
                    linewidth=1,
                    padding=6,
                    foreground=colors[11],
                ),
                widget.Spacer(
                    length=5,
                ),
                widget.WindowName(
                    foreground=colors[6],
                    fontshadow=colors[15],
                    max_chars=0,
                    parse_text=long_name_parse,
                ),
                ###########################
                # System tray begins here #
                ###########################

                widget.Systray(
                    # background=colors[8],
                    padding=0,
                    icon_size=24
                ),
                widget.Sep(
                    linewidth=1,
                    padding=6,
                    foreground=colors[11],
                ),
                widget.GenPollText(
                    foreground=colors[4],
                    update_interval=2,
                    func=bat_charge,
                    fontsize=16
                ),
                widget.Sep(
                    linewidth=1,
                    padding=6,
                    foreground=colors[11],
                ),
                widget.GenPollText(
                    foreground=colors[10],
                    update_interval=1,
                    func=lambda: subprocess.check_output(home + "/.config/qtile/get_current_layout.sh").decode("utf-8"),
                    fontsize=17
                ),
                widget.Sep(
                    linewidth=1,
                    padding=6,
                    foreground=colors[11],
                ),
                widget.Clock(
                    foreground=colors[18],
                    #    background=colors[17],
                    format="%H:%M  %d.%m.%Y",
                    padding=3
                ),
                widget.Sep(
                    linewidth=1,
                    padding=6,
                    foreground=colors[11],
                ),
                widget.TextBox(
                    text='溜',
                    #        background=colors[3],
                    foreground=colors[14],
                    padding=2,
                    fontsize=23),
                widget.Memory(
                    foreground=colors[14],
                    #        background=colors[3],
                    measure_mem='M',
                    update_interval=3.0,
                    fontshadow=colors[15],
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(terminal + ' -e htop')},
                ),
                widget.Sep(
                    linewidth=1,
                    padding=6,
                    foreground=colors[11],
                ),
                widget.WidgetBox(
                    text_closed='', text_open='',
                    foreground=colors[2],
                    #        background=colors[17],
                    fontsize=25,
                    fontshadow=colors[15],
                    padding=5,
                    widgets=[
                        widget.Sep(
                            linewidth=1,
                            padding=8,
                            foreground=colors[11],
                        ),
                        widget.TextBox(
                            text=' ',
                            font="Ubuntu Mono",
                            #        background=colors[17],
                            foreground=colors[4],
                            fontshadow=colors[15],
                            fontsize=18
                        ),
                        widget.Net(
                            interface="wlan0",
                            format='{down}↓↑{up}',
                            foreground=colors[4],
                            #        background=colors[17],
                            padding=3,
                            fontshadow=colors[15]
                        ),
                        widget.Sep(
                            linewidth=1,
                            padding=8,
                            foreground=colors[11],
                        ),
                        widget.CPU(
                            foreground=colors[5],
                            #    background=colors[3],
                            format='CPU Load: {load_percent}',
                            fontshadow=colors[15],
                        ),
                        widget.Sep(
                            linewidth=1,
                            padding=8,
                            foreground=colors[11],
                        ),
                        widget.TextBox(
                            text='ﰇ',
                            font="Ubuntu Mono",
                            #    background=colors[17],
                            foreground=colors[10],
                            fontshadow=colors[15],
                            fontsize=24,
                            padding=3,
                            mouse_callbacks={'Button1': lambda: qtile.cmd_spawn('reboot')},
                        ),
                        widget.Spacer(
                            #    background=colors[17],
                            length=10),
                        widget.TextBox(
                            text='⏻',
                            font="Ubuntu Mono",
                            #    background=colors[17],
                            foreground=colors[9],
                            fontshadow=colors[15],
                            fontsize=24,
                            padding=2,
                            mouse_callbacks={'Button1': lambda: qtile.cmd_spawn('shutdown now')},
                        ),
                        widget.Spacer(
                            length=4),
                    ]
                ),
                widget.Sep(
                    linewidth=1,
                    padding=6,
                    foreground=colors[11],
                ),
                widget.Spacer(
                    length=4),
            ],
            size=20,
            opacity=1,
            background=colors[20],
            margin=1
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),
    Match(wm_class='makebranch'),
    Match(wm_class='maketag'),
    Match(wm_class='ssh-askpass'),
    Match(title='branchdialog'),
    Match(title='pinentry'),
    Match(wm_class='splash'),
    Match(title='Confirmation'),
    Match(title='Friends List'),
    Match(title='Migrating Plugins'),
])
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
