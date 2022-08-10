# -*- coding: utf-8 -*-
import sys
from os import path, makedirs, remove
try:
    from urllib.request import urlretrieve
except:
    from urllib import urlretrieve

def write_theme(theme_name, theme_data):
    for theme_id in range(0, len(DIRS)):
        out_file = path.join(
            'themes',
            DIRS[theme_id],
            'theme-sh-' + theme_name + '.pyradio-theme'
        )
        print('    {}'.format(out_file))

        lines = TEMPLATES[theme_id].split('\n')
        for k in 'foreground', 'background':
            for i in range(0, len(lines)):
                lines[i] = lines[i].replace('{' + k + '}', theme_data[k])

        for k in range(15, -1, -1):
            if k == 8 and \
                    theme_data[str(8)] == theme_data['background']:
                ''' fix border color when it's equal to background '''
                color_data = theme_data[str(5 + (theme_id % 2))]
            else:
                color_data = theme_data[str(k)]
            token = '{color' + str(k) + '}'
            for i in range(0, len(lines)):
                lines[i] = lines[i].replace(token, color_data)

        try:
            with open(out_file, 'w') as out_file:
                for n in lines:
                    out_file.write(n + '\n')
        except:
            print('        Theme creation failed...')

DIRS = (
    'default',
    'default-alt',
    'variation',
    'variation-alt',
)

TEMPLATES = ('''# Main foreground and background
Stations            {foreground} {background}

# Playing station text color
# (background color will come from Stations)
Active Station      {color1}

# Status bar foreground and background
Status Bar          {background} {color4}

# Normal cursor foreground and background
Normal Cursor       {background} {color1}

# Cursor foreground and background
# when cursor on playing station
Active Cursor       {background} {color4}

# Cursor foreground and background
# This is the Line Editor cursor
Edit Cursor         {background} {foreground}

# Text color for extra function indication
# and jump numbers within the status bar
# (background color will come from Stations)
Extra Func          {color1}

# Text color for URL
# (background color will come from Stations)
PyRadio URL         {color2}

# Message window borser foreground
# (background color will come from Stations)
Messages Border     {color8}

# Theme Transparency
# Values are:
#   0: No transparency (default)
#   1: Theme is transparent
#   2: Obey config setting
transparency        0
''', '''# Main foreground and background
Stations            {foreground} {background}

# Playing station text color
# (background color will come from Stations)
Active Station      {color4}

# Status bar foreground and background
Status Bar          {background} {color1}

# Normal cursor foreground and background
Normal Cursor       {background} {color4}

# Cursor foreground and background
# when cursor on playing station
Active Cursor       {background} {color1}

# Cursor foreground and background
# This is the Line Editor cursor
Edit Cursor         {background} {foreground}

# Text color for extra function indication
# and jump numbers within the status bar
# (background color will come from Stations)
Extra Func          {color4}

# Text color for URL
# (background color will come from Stations)
PyRadio URL         {color2}

# Message window borser foreground
# (background color will come from Stations)
Messages Border     {color8}

# Theme Transparency
# Values are:
#   0: No transparency (default)
#   1: Theme is transparent
#   2: Obey config setting
transparency       0
''', '''# Main foreground and background
Stations            {foreground} {background}

# Playing station text color
# (background color will come from Stations)
Active Station      {color1}

# Status bar foreground and background
Status Bar          {background} {color2}

# Normal cursor foreground and background
Normal Cursor       {background} {color1}

# Cursor foreground and background
# when cursor on playing station
Active Cursor       {background} {color2}

# Cursor foreground and background
# This is the Line Editor cursor
Edit Cursor         {background} {foreground}

# Text color for extra function indication
# and jump numbers within the status bar
# (background color will come from Stations)
Extra Func          {color1}

# Text color for URL
# (background color will come from Stations)
PyRadio URL         {foreground}

# Message window borser foreground
# (background color will come from Stations)
Messages Border     {color8}

# Theme Transparency
# Values are:
#   0: No transparency (default)
#   1: Theme is transparent
#   2: Obey config setting
transparency        0
''', '''# Main foreground and background
Stations            {foreground} {background}

# Playing station text color
# (background color will come from Stations)
Active Station      {color2}

# Status bar foreground and background
Status Bar          {background} {color1}

# Normal cursor foreground and background
Normal Cursor       {background} {color2}

# Cursor foreground and background
# when cursor on playing station
Active Cursor       {background} {color1}

# Cursor foreground and background
# This is the Line Editor cursor
Edit Cursor         {background} {foreground}

# Text color for extra function indication
# and jump numbers within the status bar
# (background color will come from Stations)
Extra Func          {color2}

# Text color for URL
# (background color will come from Stations)
PyRadio URL         {foreground}

# Message window borser foreground
# (background color will come from Stations)
Messages Border     {color8}

# Theme Transparency
# Values are:
#   0: No transparency (default)
#   1: Theme is transparent
#   2: Obey config setting
transparency        0
'''
)

''' download theme.sh '''
try:
    r = urlretrieve('https://raw.githubusercontent.com/lemnos/theme.sh/master/bin/theme.sh')
except:
    print('Cannot contact github...')
    sys.exit(1)

''' create output dirs '''
if not path.exists('themes'):
    makedirs('themes')
for theme_id in range(0, len(DIRS)):
    if not path.exists(path.join('themes', DIRS[theme_id])):
        makedirs(path.join('themes', DIRS[theme_id]))

lines = []
themes_data = {}
count = 0

''' read themes '''
with open(r[0], 'r') as file:
    for line in file:
        lines.append(line.replace('\n', ''))
        if line.startswith('cursor:'):
            count += 1
            ''' we have a theme '''
            for n in lines[-19:]:
                sp = n.split(': ')
                themes_data[sp[0]] = sp[1]

            print('Writing themes for theme {0}: {1}'.format(count, lines[-20]))
            ''' create themes '''
            write_theme(lines[-20], themes_data)
            lines = []


    remove(r[0])

