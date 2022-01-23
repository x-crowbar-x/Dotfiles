
import os
import re
import socket
import subprocess
from libqtile import layout, bar, widget, qtile

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

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html

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
    Key([mod], "x", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),
    # Brightness control
    Key([mod], "space", lazy.widget["keyboardlayout"].next_keyboard(),
        desc="Next keyboard layout."),
        Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl s +10%")),
        Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl s 10%- ")),

    # Audio controls

    #Key([], "XF86AudioMute", lazy.spawn("pamixer --toggle-mute")),
    #Key([], "XF86AudioLowerVolume", lazy.spawn("pamixer --decrease 5")),
    #Key([], "XF86AudioRaiseVolume", lazy.spawn("pamixer --increase 5")),
    Key([], "XF86AudioMicMute", lazy.spawn("pamixer --source 46 -t")),
    # Music control buttons
    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause")),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next")),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous")),
    Key([], "XF86AudioStop", lazy.spawn("playerctl stop")),

    # Screenshot
    Key([], "Print", lazy.spawn('scrot ' + home + '/Pictures/'),
    desc='Take a screenshot of the whole screen'),
    Key([mod3], "Print", lazy.spawn('scrot -s ' + home + '/Pictures/'),
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

]

groups = [Group(i) for i in [
    "", "", "",  "", "",
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



colors = [["#282a36", "#282a36"], # 0
          ["#44475a", "#44475a"], # 1
          ["#f8f8f2", "#a8a8a6"], # 2
          ["#6272a4", "#798cc4"], # 3
          ["#80d2e5", "#6387f2"], # 4
          ["#50fa7b", "#29ad4a"], # 5
          ["#ffb86c", "#bc874f"], # 6
          ["#ff79c6", "#a55181"], # 7
          ["#bd93f9", "#aa7bed"], # 8
          ["#ff5555", "#a03636"], # 9
          ["#f1fa8c", "#bac44c"], # 10
          ["#ae05fc", "#aa7bed"], # 11
          ["#0973e5", "#0b4d93"], # 12
          ["#096166", "#108389"], # 13
          ["#361ccc", "#2a14a8"], # 14
          ["#414458", "#575b75"], # 15
          ["#2b2e3b", "#363949"], # 16
          ["#16557a", "#25536d"]] # 17

layout_theme = {"border_width": 3,
                "margin": 6,
                "border_focus": colors[4],
                "border_normal": colors[17]
                }

layouts = [
    #layout.Matrix(**layout_theme),
    #layout.Bsp(**layout_theme),
    #layout.RatioTile(**layout_theme),
    #layout.Zoomy(**layout_theme)
    #layout.Tile(**layout_theme),
    #layout.VerticalTile(**layout_theme),
    layout.MonadTall(**layout_theme),
    layout.MonadWide(**layout_theme),
    layout.Max(**layout_theme),
    layout.Columns(**layout_theme),
    layout.Stack(**layout_theme),
    layout.TreeTab(
        font = "mononoki",
        fontsize = 14,
        bg_color = colors[16],
        active_bg = colors[9],
        inactive_bg = colors[3],
        inactive_fg = colors[10],
        padding_left = 0,
        padding_x = 0,
        padding_y =5,
        section_top =10,
        section_bottom = 20,
        vspace = 3,
        panel_width = 210),
    layout.Floating(**layout_theme),
]



prompt = "[{0}@{1}]$ ".format(os.environ["USER"], socket.gethostname())

# Default widget settings
widget_defaults = dict(
    font = 'Ubuntu Mono Bold',
    fontsize = 16,
    padding = 2,
    background = colors[16],
)
extension_defaults = widget_defaults.copy()

PacmanImage = "~/.config/qtile/icons/pacman.png"
PacmanGhostImg1 = "~/.config/qtile/icons/pacman-ghost1.png"
PacmanGhostImg2 = "~/.config/qtile/icons/pacman-ghost2.png"

# I have only one screen,
# so didn't bother to create different functions
screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Spacer(
                        length = 10,
                        ),
                widget.CurrentLayoutIcon(
                background = colors[4],
                fontsize = 13
                ),
                widget.Spacer(
                        length = 5,
                        ),
                widget.CurrentLayout(
                        foreground = colors[4],
                        fontshadow = colors[17],
                        fontsize = 14),
                widget.Sep(
                        linewidth = 2,
                        padding = 3,
                        foreground = colors[4],
                        ),
                widget.GroupBox(
                       fontsize = 24,
                       margin_y = 5,
                       margin_x = 1,
                       padding_y = 5,
                       padding_x = 3,
                       borderwidth = 3,
                       active = colors[2],
                       inactive = colors[4],
                       rounded = True,
                       highlight_color = colors[3],
                       highlight_method = "line",
                       this_current_screen_border = colors[17],
                       this_screen_border = colors[4],
                       fontshadow = colors[17],
                        ),
                widget.Sep(
                        linewidth = 2,
                        padding = 3,
                        foreground = colors[4],
                        ),
                widget.Spacer(
                        length = 6,
                        ),
                widget.Prompt(
                        fontsize = 15,
                        foreground = colors[4],
                        bell_style = None,
                        prompt = prompt,
                        fontshadow = colors[16],
                        ),
                widget.WindowName(
                        fontsize = 14,
                        foreground = colors[2],
                        fontshadow = colors[16]
                        ),
    # System tray begins here
                widget.TextBox(
                       text = '',
                       font = "Ubuntu Mono",
                       background = colors[17],
                       foreground = colors[16],
                       padding = 0,
                       fontsize = 33,
                       fontshadow = colors[15]
                       ),
                widget.Image(
                        background = colors[17],
                        filename = PacmanImage,
                        scale = "False",
                        mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn('steam')}
                        ),
                widget.Systray(
                        background = colors[17],
                        padding = 0,
                        icon_size = 26
                        ),
                widget.Image(
                        background = colors[17],
                        filename = PacmanGhostImg1,
                        mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn('github-desktop')}
                        ),
                widget.TextBox(
                       text = '',
                       font = "Ubuntu Mono",
                       background = colors[3],
                       foreground = colors[17],
                       padding = 0,
                       fontsize = 33,
                       fontshadow = colors[15]
                       ),
                widget.KeyboardLayout(
                        foreground = colors[2],
                        background = colors[3],
                        padding = 6,
                        configured_keyboards = ['us','ru'],
                        fontshadow = colors[15],
                        ),
                widget.Image(
                        background = colors[3],
                        filename = PacmanGhostImg2,
                        mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn('idea')}
                        ),
                widget.TextBox(
                       text = '',
                       font = "Ubuntu Mono",
                       background = colors[17],
                       foreground = colors[3],
                       padding = 0,
                       fontsize = 33,
                       fontshadow = colors[15]
                       ),
                widget.Clock(
                        foreground = colors[2],
                        background = colors[17],
                        format = "%H:%M  %d.%m.%Y",
                        fontshadow = colors[15],
                        padding = 3
                        ),
                widget.Image(
                        background = colors[17],
                        filename = PacmanGhostImg1,
                        padding = 3,
                        mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn('gimp')}
                        ),
                widget.TextBox(
                       text = '',
                       font = "Ubuntu Mono",
                       background = colors[3],
                       foreground = colors[17],
                       padding = 0,
                       fontsize = 33,
                       fontshadow = colors[15]
                       ),
                widget.TextBox(
                        text = '',
                        font = "Ubuntu Mono",
                        background = colors[3],
                        foreground = colors[2],
                        padding = 0,
                        fontshadow = colors[15],
                        fontsize = 27
                        ),
                widget.Memory(
                        foreground = colors[2],
                        background = colors[3],
                        measure_mem = 'M',
                        update_interval = 3.0,
                        fontshadow = colors[15],
                        mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e htop')},
                        ),
                widget.Image(
                        background = colors[3],
                        filename = PacmanGhostImg2,
                        ),
                widget.TextBox(
                       text = '',
                       font = "Ubuntu Mono",
                       background = colors[17],
                       foreground = colors[3],
                       padding = 0,
                       fontsize = 33,
                       fontshadow = colors[15]
                       ),
                widget.WidgetBox(
                       text_closed = '理', text_open = 'ﲅ',
                       foreground = colors[2],
                       background = colors[17],
                       fontsize = 25,
                       fontshadow = colors[15],
                       padding = 6,
                       widgets=[
                widget.TextBox(
                       text = '  ',
                       font = "Ubuntu Mono",
                       background = colors[17],
                       foreground = colors[2],
                       fontshadow = colors[15],
                       fontsize = 17
                       ),
                widget.Net(
                        interface = "wlan0",
                        format = '{down}↓↑{up}',
                        foreground = colors[2],
                        background = colors[17],
                        padding = 0,
                        fontshadow = colors[15],
                        ),
                widget.Image(
                        background = colors[17],
                        filename = PacmanGhostImg1,
                        ),
                widget.TextBox(
                       text = '',
                       font = "Ubuntu Mono",
                       background = colors[3],
                       foreground = colors[17],
                       padding = 0,
                       fontsize = 33,
                       fontshadow = colors[15]
                       ),
                widget.CPU(
                        foreground = colors[2],
                        background = colors[3],
                        format = 'CPU {load_percent}%',
                        fontshadow = colors[15],
                        ),
                widget.Image(
                        background = colors[3],
                        filename = PacmanGhostImg2,
                        ),
                widget.TextBox(
                       text = '',
                       font = "Ubuntu Mono",
                       background = colors[17],
                       foreground = colors[3],
                       padding = 0,
                       fontsize = 33,
                       fontshadow = colors[15]
                       ),
                ]
            ),
        ],
            size = 22,
            opacity = 1,
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
])
auto_fullscreen = True
focus_on_window_activation = "focus"
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
