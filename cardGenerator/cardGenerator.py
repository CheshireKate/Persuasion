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
symbolTemplate = '    {} = {}'
symbolNames = {
    '💎': 'wealth',
    '👑': 'title',
    '🙏': 'faith',
    '🌹': 'passion',
    '🗡': 'daring'
}
desireCount = {
    '＋💎': 0,
    '－💎': 0,
    '＋👑': 0,
    '－👑': 0,
    '＋🙏': 0,
    '－🙏': 0,
    '＋🌹': 0,
    '－🌹': 0,
    '＋🗡': 0,
    '－🗡': 0
}

baseValue = 10101
valueMap = {
    '💎': 1,
    '👑': 100,
    '🙏': 10000,
    '🌹':  0,
    '🗡':  0
}

bitMap = []

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
        cardValue = baseValue
        for sign in ["＋", "－"]:
            first = True
            for symbol in row[sign]:
                val = sign + symbol
                params[symbol] = val
                if first:
                    first = False
                    params['desires'] += val
                    desireCount[val] += 1
                else:
                    params['extras'] += val
                if sign == "＋":
                    symbolMap[i].append(symbolTemplate.format(symbolNames[symbol], '1'))
                    cardValue += valueMap[symbol]
                else:
                    symbolMap[i].append(symbolTemplate.format(symbolNames[symbol], '-1'))
                    cardValue -= valueMap[symbol]
        bitMap.append(cardValue)

        cards.append(traitCard.format(**params))

# Our test baseline desire card
bitMap.remove(202)

handSizes = [10, 9, 8, 7, 6, 5]

# Write a lua object mapping cards to their desires characters
with open('probability.txt', 'w', encoding="utf-8") as f:
    for handSize in handSizes:
        possibleHands = 0
        singleMatch = 0
        doubleMatch = 0
        tripleMatch = 0
        anyTwo = 0
        anyOne = 0
        almostSingle = 0
        almostDouble = 0
        almostTriple = 0
        almostAnyTwo = 0
        almostAnyOne = 0

        for hand in combinations(bitMap, handSize):
            possibleHands += 1
            matches = [0, 0, 0]
            almostMatches = [0, 0, 0]
            total = sum(hand)
            if (total - (total % 10000)) < (handSize * 10000):
                matches[0] = 1
            if (total - (total % 10000)) <= (handSize * 10000):
                almostMatches[0] = 1
            total = total % 10000
            if (total - (total % 100)) > (handSize * 100):
                matches[1] = 1
            if (total - (total % 100)) >= (handSize * 100):
                almostMatches[1] = 1
            total = total % 100
            if total > handSize:
                matches[2] = 1
            if total >= handSize:
                almostMatches[2] = 1
            if matches[0] > 0:
                singleMatch += 1
            if almostMatches[0] > 0:
                almostSingle += 1
            if matches[0] + matches[1] > 1:
                doubleMatch += 1
            if almostMatches[0] + almostMatches[1] > 1:
                almostDouble += 1
            total = sum(matches)
            almostTotal = sum(almostMatches)
            if total > 2:
                tripleMatch += 1
            if total > 1:
                anyTwo += 1
            if total > 0:
                anyOne += 1

            if almostTotal > 2:
                almostTriple += 1
            if almostTotal > 1:
                almostAnyTwo += 1
            if almostTotal > 0:
                almostAnyOne += 1

            if possibleHands % 100000000 == 0:
                print("Hand size: {}".format(handSize))
                print("   Calculated {} so far...".format(possibleHands))
                print("   Triple: {:05.2f}% = {}/{}".format(((tripleMatch / possibleHands) * 100.0), tripleMatch, possibleHands))
                print("   Double: {:05.2f}% = {}/{}".format(((doubleMatch / possibleHands) * 100.0), doubleMatch, possibleHands))
                print("   Single: {:05.2f}% = {}/{}".format(((singleMatch / possibleHands) * 100.0), singleMatch, possibleHands))
                print("   AnyTwo: {:05.2f}% = {}/{}".format(((anyTwo / possibleHands) * 100.0), anyTwo, possibleHands))
                print("   AnyOne: {:05.2f}% = {}/{}".format(((anyOne / possibleHands) * 100.0), anyOne, possibleHands))
                print("  The following are almost matches, off by one")
                print("   Triple: {:05.2f}% = {}/{}".format(((almostTriple / possibleHands) * 100.0), almostTriple, possibleHands))
                print("   Double: {:05.2f}% = {}/{}".format(((almostDouble / possibleHands) * 100.0), almostDouble, possibleHands))
                print("   Single: {:05.2f}% = {}/{}".format(((almostSingle / possibleHands) * 100.0), almostSingle, possibleHands))
                print("   AnyTwo: {:05.2f}% = {}/{}".format(((almostAnyTwo / possibleHands) * 100.0), almostAnyTwo, possibleHands))
                print("   AnyOne: {:05.2f}% = {}/{}".format(((almostAnyOne / possibleHands) * 100.0), almostAnyOne, possibleHands))
                print("")

        f.write("Hand size: {}".format(handSize))
        f.write("   Calculated {} total".format(possibleHands))
        f.write("   Triple: {:05.2f}% = {}/{}".format(((tripleMatch / possibleHands) * 100.0), tripleMatch, possibleHands))
        f.write("   Double: {:05.2f}% = {}/{}".format(((doubleMatch / possibleHands) * 100.0), doubleMatch, possibleHands))
        f.write("   Single: {:05.2f}% = {}/{}".format(((singleMatch / possibleHands) * 100.0), singleMatch, possibleHands))
        f.write("   AnyTwo: {:05.2f}% = {}/{}".format(((anyTwo / possibleHands) * 100.0), anyTwo, possibleHands))
        f.write("   AnyOne: {:05.2f}% = {}/{}".format(((anyOne / possibleHands) * 100.0), anyOne, possibleHands))
        f.write("  The following are almost matches, off by one")
        f.write("   Triple: {:05.2f}% = {}/{}".format(((almostTriple / possibleHands) * 100.0), almostTriple, possibleHands))
        f.write("   Double: {:05.2f}% = {}/{}".format(((almostDouble / possibleHands) * 100.0), almostDouble, possibleHands))
        f.write("   Single: {:05.2f}% = {}/{}".format(((almostSingle / possibleHands) * 100.0), almostSingle, possibleHands))
        f.write("   AnyTwo: {:05.2f}% = {}/{}".format(((almostAnyTwo / possibleHands) * 100.0), almostAnyTwo, possibleHands))
        f.write("   AnyOne: {:05.2f}% = {}/{}".format(((almostAnyOne / possibleHands) * 100.0), almostAnyOne, possibleHands))
        f.write("")

# Write a lua object mapping cards to their desires characters
with open('symbolMap.lua', 'w', encoding="utf-8") as f:
    f.write('symbolMap = { { ' + ' }, { '.join([', '.join(x) for x in symbolMap]) + ' } }')

# Generate desires without border
writeCards(cards, 'traits-desires', style=styles['traits'].format('None', '100%', '100%'))

# Generate trait cards with borders for each player
for color, hex in crests.items():
    writeCards(cards, 'traits-{}'.format(color), style=styles['traits'].format(hex, '94%', '96%'))

total = len(cards)

cards = []
# Generate table for distribution
with open('desireTotal.csv', 'w', encoding="utf-8") as f:
    for symbol, count in sorted(desireCount.items(), key=lambda x: x[1], reverse=True):
        f.write(symbol + ',' + str(count) + '\n')

row = 0
for symbol, count in desireCount.items():
    cards.append(symbol + ' <span>' + str(count) + '/' + str(total) + '</span>')
    row += 1
    if row % 2 == 0:
        cards.extend(['']*4)
writeCards(cards, 'distribution', style=styles['distribution'], sheetColumns=6, sheetRows=10)

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
