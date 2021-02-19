import csv
from itertools import combinations
from math import floor, ceil

traitTotal = 57
desireTotal = 9

suits = set(['💎', '👑', '🌹'])

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

        .page {{
          page-break-before: always;
          page-break-after: always;
          width: 100%;
          height: 100%;
          vertical-align: middle;
          text-align: center;
        }}

        .cardRow {{
          vertical-align: middle;
          text-align: center;
        }}

        .card {{
          -webkit-background-size: cover;
          -moz-background-size: cover;
          -o-background-size: cover;
          background-size: cover;

          width: {}%;
          height: {}%;

          vertical-align: middle;
          text-align: center;

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
    <div class="symbol {symbol}">{symbol}</div>
    <div class="contents">
        <div class="title">{title}</div>
        <div class="power">{power}</div>
    </div>
</div>'''

desireCard = '''<div class="container">
    <div class="title">{title}</div>
    <div class="prim condition"><span class="fancy">Prim victory</span><br/>if I marry a suitor with <span class="symbol {need}">{need}{need}{need}</span></div>
    <div class="proper condition"><span class="fancy">Proper victory</span><br/>if I personally have <br/><span class="symbol {need}">{need}{need}{need}{need}</span></div>
    <div class="bonus condition">{victory}</div>
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

          background:url("resources/{}Front.jpg") no-repeat center center ;
        }}

        .symbol {{
          height: auto;
          width: 100%;
          margin-left: 3%;
          vertical-align: top;
          font-family: Symbola;
          text-align: left;
          font-size: 72;
          text-shadow:
            -2px -2px 0 #000,
            2px -2px 0 #000,
            -2px 2px 0 #000,
            2px 2px 0 #000;
        }}

        .title {{
          font-family: Gentium Book Basic;
          font-style: italic;
          font-weight: bold;
          vertical-align: top;
          text-align: center;
          font-size: 42;
        }}

        .contents {{
          height: 100%;
          width: 100%;
        }}

        .💎 {{
          color: #717BF3;
        }}

        .👑 {{
          color: #FFB544;
        }}

        .🌹 {{
          color: #FF0000;
        }}

        .power {{
          margin: 10%;
          width: 80%;
          font-family: Gentium Book Basic;
          vertical-align: middle;
          text-align: center;
          font-size: 36;
          {}
        }}
        ''',

    'desires': '''
        }

        .container {
          width: 100%;
          height: 100%;
          margin: auto;

          background:url("resources/desireFront.jpg") no-repeat center center ;
        }

        .title {
          height: 23%;
          font-family: Gentium Book Basic;
          font-style: italic;
          font-weight: bold;
          vertical-align: top;
          text-align: center;
          font-size: 64;
          margin-top: -7%;
          margin-bottom: -7%;
        }

        .fancy {
          font-weight: bolder;
          font-size: 52;
        }

        .condition {
          height: 38%;
          font-family: Gentium Book Basic;
          font-style: italic;
          font-weight: bold;
          vertical-align: top;
          text-align: center;
          font-size: 42;
        }

        .prim {
          margin-top: 6%;
        }

        .proper {
          margin-top: 1%;
        }

        .cornerSymbol {
          height: auto;
          width: 100%;
          margin-left: 3%;
          vertical-align: top;
          font-family: Symbola;
          text-align: left;
          font-size: 72;
          text-shadow:
            -2px -2px 0 #000,
            2px -2px 0 #000,
            -2px 2px 0 #000,
            2px 2px 0 #000;
        }

        .symbol {
          font-family: Symbola;
          font-style: normal;
          font-weight: normal;
          vertical-align: top;
          text-align: center;
          font-size: 46;
          text-shadow:
            -1px -1px 0 #000,
            1px -1px 0 #000,
            -1px 1px 0 #000,
            1px 1px 0 #000;
        }

        .💎 {
          color: #717BF3;
        }

        .👑 {
          color: #FFB544;
        }

        .🌹{
          color: #FF0000;
        }
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
        ''',

    'distribution': '''
          font-size: 72;
        }

        span {
          font-weight: bold;
        }
    '''
}

def writeCards(originalCards, name, style=None, sheetColumns=10, sheetRows=5):
    if style == None:
        style = styles[name]

    sheetCount = sheetColumns * sheetRows
    cell = '<td class="card">{}</td>'
    row = '        <tr class="cardRow">{}</tr>'.format(cell * sheetColumns)
    page = '    <table class="page">{}</table>'.format(row * sheetRows)
    pages = []
    cards = originalCards[:]

    if len(cards) <= sheetColumns * 2:
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

subTotal = 0
# Convert CSV to cards
with open('resources/Persuasion - Traits.csv', 'r', encoding="utf-8") as input:
    cardDetails = csv.DictReader(input)
    for subTotal, row in enumerate(cardDetails):
        # Skip lines that aren't ready or have a power written
        if subTotal == traitTotal:
            break
        if row['Ready?'] == '❌' or len(row['Effect']) < 3:
            continue
        params = {
            'modifiers': '', # row['Mods']
            'title': row['Name'],
            'symbol': row['Suit'],
            'power': row['Effect']
        }
        cards.append(traitCard.format(**params))

# Generate traits without border
writeCards(cards, 'traits-unsleeved', style=styles['traits'].format('None', '100%', '100%', 'desire', ''))

# Generate trait cards with borders for each player
for color, hex in crests.items():
    writeCards(cards, 'traits-{}'.format(color), style=styles['traits'].format(hex, '94%', '96%', 'trait', 'display: none;'))

desireCount = {
    '💎': 4,
    '👑': 3,
    '🌹': 2
}
cards = []

row = 0
for symbol, count in desireCount.items():
    cards.append(symbol + ' <span>' + str(count) + '/' + str(desireTotal) + '</span>')
cards.extend(['']*16)
writeCards(cards, 'distribution', style=styles['distribution'], sheetColumns=6, sheetRows=10)

cards = []

# Convert CSV to cards
with open('resources/Persuasion - Desires.csv', 'r', encoding="utf-8") as input:
    cardDetails = csv.DictReader(input)
    for i, row in enumerate(cardDetails):
        if row['Ready?'] == '❌' or len(row['Victory']) < 3:
            continue
        if i == desireTotal:
            break
        params = {
            'title': row['Name'] + " Desires",
            'need': row['❤'],
            'victory': row['Victory']
        }
        cards.append(desireCard.format(**params))

# Generate traits without border
writeCards(cards, 'desires')

cards = ['<div id="{}"></div>'.format(color) for color in crests.keys()]
# Generate suited one offs (Rings)

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
