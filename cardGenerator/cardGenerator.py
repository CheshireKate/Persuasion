import csv
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

crestCards = ['Ring']

crestSection = '''
        #{0} {{
          background:url("resources/{0}{1}.jpg") no-repeat center center ;
        }}
'''

styles = {
    'traits': '''
          background-color: {};
        }}

        .container {{
          width: {};
          height: {};
          margin: auto;

          background:url("resources/traitFront.jpg") no-repeat center center ;
        }}

        .symbols {{
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

    with open('{}.html'.format(name), 'w', encoding="utf-8") as f:
        f.write(html.format(floor(100 / sheetColumns), floor(100 / sheetRows), style, ''.join(pages)))

# Generate traits deck
cards = []

traitCard = '''<div class="container">
    <div class="symbols">{plus}{{}}<br>{minus}{{}}</div>
    <div class="title">{{}}</div>
</div>'''.format(plus=plus, minus=minus)

# Convert CSV to cards
with open('resources/Persuasion - Trait Effects.csv', 'r', encoding="utf-8") as input:
    cardDetails = csv.DictReader(input)
    for row in cardDetails:
        cards.append(traitCard.format(row['＋'], row['－'], row['Name']))

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
for modifier in [(plus, 'plusSide'), (minus, 'minusSide')]:
    cards = []
    for i, suit in enumerate(suits):
        cards.append('{}{}'.format(modifier[0], suit))
        if i == 2:
            cards.extend([''] * 2)

    writeCards(cards, modifier[1], style=styles['markers'], sheetColumns=5, sheetRows=4)
