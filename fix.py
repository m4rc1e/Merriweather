"""Hot fix script to fix https://github.com/google/fonts/issues/588"""

import os
from fontTools.ttLib import TTFont


VERSION = 1.585

fonts_path = [os.path.join('src', f) for f in os.listdir('src')
              if f.endswith('.ttf')]

trans = {
    'Merriweather-Light.ttf': {
    "uni042C": 0,
    "I": 1304,
    },

    'Merriweather-Regular.ttf': {
    "uni042C": 0,
    "I": 1330,
    },

    'Merriweather-Bold.ttf': {
    "uni042C": 0,
    "I": 1379,
    },

    'Merriweather-Black.ttf': {
    "uni042C": 0,
    "I": 1418,
    },


    'Merriweather-LightItalic.ttf': {
    "uni042C": 0,
    "I": 1212,
    },

    'Merriweather-Italic.ttf': {
    "uni042C": 0,
    "I": 1210,
    },

    'Merriweather-BoldItalic.ttf': {
    "uni042C": 0,
    "I": 1284,
    },

    'Merriweather-BlackItalic.ttf': {
    "uni042C": 0,
    "I": 1347,
    },
}

for filename in trans:
    src_path = os.path.join('src', filename)
    font = TTFont(src_path)

    # fix uni042B
    for comp in font['glyf']['uni042B'].components:
        if comp.glyphName in trans[filename]:
            comp.x = trans[filename][comp.glyphName]
            target_path = os.path.join('fonts', filename)

    # bump version number
    font['head'].fontRevision = VERSION

    
    current_version = str(font['name'].getName(3, 3, 1, 1033)).decode('utf_16_be')
    new_version = current_version.replace('1.584', str(VERSION))
    font['name'].setName(
        new_version.encode('utf_16_be'),
        3, 3, 1, 1033)
    font.save(target_path)
    print "%s saved" % target_path
