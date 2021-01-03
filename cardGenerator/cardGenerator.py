from itertools import combinations
from math import floor, ceil

plus = '&#xFF0B'
minus = '&#xFF0D'
suits = set(['&#x1F48E', '&#x1F451', '&#x1F5E1', '&#x1F339', '&#x1F64F'])

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

        table {{
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
        }}

        td {{
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

crestCards = ['Ring', 'Mail']

crestSection = '''
        #{0} {{
          background:url("resources/{0}{1}.jpg") no-repeat center center ;
        }}
'''

styles = {
    'traits': '''
          width: calc(10% - 10px);
          height: calc(10% - 10px);
          padding: 10px;
          background-color: {};
        }}

        div {{
          width: 100%;
          height: 100%;

          background:url("resources/traitFront.jpg") no-repeat center center ;
          vertical-align: top;
          text-align: left;
          font-size: 72;
        }}
        ''',

    'markers': '''
          background:url("resources/marker.jpg") no-repeat center center ;
          vertical-align: middle;
          text-align: center;
          font-size: 288;
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
    cell = '<td>{}</td>'
    row = '        <tr>{}</tr>'.format(cell * sheetColumns)
    page = '    <table>{}</table>'.format(row * sheetRows)
    pages = []
    cards = originalCards[:]

    if len(cards) <= sheetColumns:
        split = ceil(len(cards) / 2)
        cards = cards[:split] + [''] * (sheetColumns - split) + cards[split:]

    #  Fill sheet with blanks
    cards.extend([''] * (sheetCount - (len(cards) % sheetCount)))

    for pageNum in range(len(cards) // sheetCount):
        pages.append(page.format(*cards[pageNum * sheetCount:((pageNum + 1) * sheetCount)]))

    with open('{}.html'.format(name), 'w') as f:
        f.write(html.format(floor(100 / sheetColumns), floor(100 / sheetRows), style, ''.join(pages)))


# Generate traits deck
cards = []

traitPlus = '<div>{plus}{{}}{{}}<br>{minus}{{}}</div>'.format(plus=plus, minus=minus)
traitMinus = '<div>{plus}{{}}<br>{minus}{{}}{{}}</div>'.format(plus=plus, minus=minus)

# Generate combinations
for pairs in combinations(suits, 2):
    for spare in suits.difference(set(pairs)):
        cards.append(traitPlus.format(pairs[0], pairs[1], spare))
        cards.append(traitMinus.format(spare, pairs[0], pairs[1]))

# Generate trait cards with borders for each player
for color, hex in crests.items():
    style = styles['traits'].format(hex)

    writeCards(cards, 'traits-{}'.format(color), style=style)

cards = ['<div id="{}"></div>'.format(color) for color in crests.keys()]

for crestType in crestCards:
    styleSections = []
    for color, hex in crests.items():
        styleSections.append(crestSection.format(color, crestType))

    style = styles['crests'].format(''.join(styleSections))

    writeCards(cards, crestType, style=style)

for modifier in [(plus, 'plusSide'), (minus, 'minusSide')]:
    cards = []
    for i, suit in enumerate(suits):
        cards.append('{}{}'.format(modifier[0], suit))
        if i == 2:
            cards.extend([''] * 2)

    writeCards(cards, modifier[1], style=styles['markers'], sheetColumns=5, sheetRows=4)
