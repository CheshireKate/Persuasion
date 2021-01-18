import csv
from itertools import combinations
from math import floor, ceil

suits = set(['💎', '👑', '🙏', '🌹', '🗡'])

crests = {
    'black': '#000000',
    'blue': '#332288',
    'green': '#117733',
    'teal': '#88CCEE',
    'yellow': '#DDCC77',
    'pink': '#FF7C92',
    'purple': '#BD1CA3',
    'white': '#FFFFFF'
}

html = '''<html>
<head>
    <style>
        @font-face {{
            font-family: Symbola;
            src: url('dependencies/Symbola.otf');
        }}

        body {{
          border: 0px !important;
          margin: 0px !important;
          padding: 0px !important;
        }}

        .page {{
          page-break-before: always;
          page-break-after: always;
          width: 100%;
          height: 100%;
        }}

        table, tr, td {{
          font-family: Symbola;
          border: 0px;
          margin: 0px;
          padding: 0px;
          border-spacing: 0px;
          border-color: transparent;
          border-collapse: collapse;

          vertical-align: top;
          text-align: left;
        }}

        .card {{
          -webkit-background-size: cover;
          -moz-background-size: cover;
          -o-background-size: cover;
          background-size: cover;

          width: {}%;
          height: {}%;

          /* Custom Styling */
        {}
    </style>
</head>
<body>
{}
</body>
'''

crestCards = ['Ring']

crestSection = '''
        #{0} {{
          background:url("resources/{0}{1}.jpg") no-repeat center center ;
        }}
'''

traitCard = '''<div class="container">
    <table class="innerTrait">
        <tr>
            <td rowspan="5" class="contents">
                <div class="symbols"><span class="desiresText">{desires}</span></div>
                <div class="symbols"><span class="extrasText">{extras}</span></div>
                <div class="title">{title}</div>
            </td>
            <td class="symbolCell"><div class="symbolCalc">{💎}</div></td>
        </tr>
        <tr><td class="symbolCell"><div class="symbolCalc">{👑}</div></td></tr>
        <tr><td class="symbolCell"><div class="symbolCalc">{🙏}</div></td></tr>
        <tr><td class="symbolCell"><div class="symbolCalc">{🌹}</div></td></tr>
        <tr><td class="symbolCell"><div class="symbolCalc">{🗡}</div></td></tr>
    </table>
</div>'''


styles = {
    'traits': '''
          background-color: {};
        }}

        .innerTrait {{
          width: 100%;
          height: 100%;
          vertical-align: top;
          text-align: left;
        }}

        .container {{
          width: {};
          height: {};
          margin: auto;

          background:url("resources/traitFront.jpg") no-repeat center center ;
        }}

        .symbols {{
          height: auto;
          width: 100%;
          vertical-align: top;
          text-align: left;
          font-size: 72;
        }}

        .title {{
          font-family: Gentium Book Basic;
          font-style: italic;
          font-weight: bold;
          vertical-align: top;
          text-align: center;
          font-size: 48;
        }}

        .contents {{
          height: 100%;
          width: 95%;
        }}

        .desiresText {{
        }}

        .extrasText {{
        }}

        .symbolColumn {{
          width: 5%;
          height: 95%;
          margin-top: 5%;
        }}

        .symbolCell {{
          height: 20%;
          width: 100%;
          vertical-align: middle;
          text-align: center;
        }}

        .symbolCalc {{
          margin-left: -100px;
          margin-right: -80px;
          margin-top: 30px;
          font-family: Symbola;
          vertical-align: middle;

          text-align: center;
          font-size: 32;

          transform: rotate(90deg);
        }}
        ''',

    'markers': '''
          background:url("resources/marker.jpg") no-repeat center center ;
          vertical-align: middle;
          text-align: center;
          font-size: 288;
        }
        ''',

    'postbox': '''
          background:url("resources/postbox.jpg") no-repeat center center ;
        }
        ''',

    'crests': '''
        }}

        div {{
          width: 100%;
          height: 100%;

          -webkit-background-size: contain !important;
          -moz-background-size: contain !important;
          -o-background-size: contain !important;
          background-size: contain !important;
        }}

        {}
        '''
}

def writeCards(originalCards, name, style=None, sheetColumns=10, sheetRows=5):
    if style == None:
        style = styles[name]

    sheetCount = sheetColumns * sheetRows
    cell = '<td class="card">{}</td>'
    row = '        <tr>{}</tr>'.format(cell * sheetColumns)
    page = '    <table class="page">{}</table>'.format(row * sheetRows)
    pages = []
    cards = originalCards[:]

    if len(cards) <= sheetColumns:
        split = ceil(len(cards) / 2)
        cards = cards[:split] + [''] * (sheetColumns - split) + cards[split:]

    #  Fill sheet with blanks
    cards.extend([''] * (sheetCount - (len(cards) % sheetCount)))

    for pageNum in range(len(cards) // sheetCount):
        pages.append(page.format(*cards[pageNum * sheetCount:((pageNum + 1) * sheetCount)]))

    with open('{}.html'.format(name), 'w', encoding="utf-8") as f:
        f.write(html.format(floor(100 / sheetColumns), floor(100 / sheetRows), style, ''.join(pages)))

# Generate traits deck
cards = []

symbolMap = []

# Convert CSV to cards
with open('resources/Persuasion - Trait Effects.csv', 'r', encoding="utf-8") as input:
    cardDetails = csv.DictReader(input)
    for i, row in enumerate(cardDetails):
        if i == 60:
            break
        symbolMap.append([])
        params = {
            'desires': '',
            'modifiers': '',
            'extras': '',
            'title': row['Name'],
            '💎': '',
            '👑': '',
            '🙏': '',
            '🌹': '',
            '🗡': ''
        }
        for sign in ["＋", "－"]:
            first = True
            for symbol in row[sign]:
                val = sign + symbol
                params[symbol] = val
                if first:
                    first = False
                    params['desires'] = val
                else:
                    params['extras'] = val
                symbolMap[i].append(val)

        cards.append(traitCard.format(**params))

# Write a lua object mapping cards to their desires characters
with open('symbolMap.lua', 'w', encoding="utf-8") as f:
    f.write('symbolMap = {\n  {"' + '"},\n  {"'.join(['", "'.join(x) for x in symbolMap]) + '"}\n}')

# Generate desires without border
writeCards(cards, 'traits-desires', style=styles['traits'].format('None', '100%', '100%'))

# Generate trait cards with borders for each player
for color, hex in crests.items():
    writeCards(cards, 'traits-{}'.format(color), style=styles['traits'].format(hex, '94%', '96%'))

# Generate suited one offs (Rings)
cards = ['<div id="{}"></div>'.format(color) for color in crests.keys()]

for crestType in crestCards:
    styleSections = []
    for color, hex in crests.items():
        styleSections.append(crestSection.format(color, crestType))

    style = styles['crests'].format(''.join(styleSections))
    writeCards(cards, crestType, style=style)

# Generate symbol markers
for modifier in [('＋', 'plusSide'), ('－', 'minusSide')]:
    cards = []
    for i, suit in enumerate(suits):
        cards.append('{}{}'.format(modifier[0], suit))
        if i == 2:
            cards.extend([''] * 2)

    writeCards(cards, modifier[1], style=styles['markers'], sheetColumns=5, sheetRows=4)
