import csv
from itertools import combinations
from math import floor, ceil

conversions = {
    '✍': '<span class="symbol" style="font-size:40">✍</span>',
    '🗝': '<span class="symbol">🔑</span>',
    '👒': '<span class="symbol" style="font-size:40">👒</span>',
    '🐦': '<span class="symbol" style="font-size:40">🐦</span>',
    '🔓': '<span class="symbol">🔓</span>',
    '🔒': '<span class="symbol">🔒</span>',
    '💎': '<span class="symbol addShadow 💎">💎</span>',
    '👑': '<span class="symbol addShadow 👑">👑</span>',
    '🌹': '<span class="symbol addShadow 🌹">🌹</span>',
    '🎭': '<span class="symbol" style="font-weight: normal">🎭</span>',
    '♡': '<span class="symbol">♡</span>',
    '🗫': '<span class="symbol">🗫</span>',
    'revealing': '<b><i>revealing</i></b>',
    'reveals': '<b><i>reveals</i></b>',
    'reveal': '<b><i>reveal</i></b>',
    'matrimony': '<b><i>Matrimony</i></b>',
    'Matrimony': '<b><i>Matrimony</i></b>',
    'engaged': '<b><i>engaged</i></b>',
    'engage': '<b><i>engage</i></b>',
    'diary': '<i>diary</i>',
    'diaries': '<i>diaries</i>',
    'Desired Wins': '<b><i>Desired Wins</i></b>',
    'Desired Win': '<b><i>Desired Win</i></b>',
    'If I send this to you': '<b><i>If I send this to you</i></b>',
    'If I discard this': '<b><i>If I discard this</i></b>',
    'While you hold this': '<b><i>While you hold this</i></b>',
    'swap': '<b><i>swap</i></b>',
    '(': '<i>(',
    ')': ')</i>'
}

noBold = set( ['your', 'yours', 'friend', 'a', 'an', 'and'] )

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

traitCard = '''<div class="container {modifiers}">
    <div class="bigSymbol {symbol}">{symbol}</div>
    <div class="modifiers">{modifiers}</div>
    <div class="reference">{reference}</div>
    <div class="contents">
        <div class="art">{art}</div>
        <div class="power">{power}</div>
        <div class="signed">{signed}</div>
    </div>
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
          position: relative;
          width: {};
          height: {};
          margin: {};

          background:url("resources/traitFront.jpg") no-repeat center center ;
        }}

        .🔒 {{
          background:url("resources/diaryFront.jpg") no-repeat center center ;
        }}

        .bigSymbol {{
          position: absolute;
          left: 3%;
          top: 0%;
          font-family: Symbola;
          font-style: normal;
          font-weight: normal;
          text-align: left;
          font-size: 72;
          text-shadow:
            -2px -2px 0 #000,
            2px -2px 0 #000,
            -2px 2px 0 #000,
            2px 2px 0 #000;
        }}

        .modifiers {{
          position: absolute;
          left: 7%;
          top: 12%;
          font-family: Symbola;
          font-style: normal;
          font-weight: bolder;
          text-align: left;
          font-size: 48;
        }}

        .reference {{
          position: absolute;
          left: 1%;
          bottom: 1%;
          font-family: Symbola;
          font-style: normal;
          font-weight: normal;
          text-align: left;
          font-size: 36;
        }}

        .symbol {{
          font-family: Symbola;
          font-style: normal;
          font-weight: normal;
        }}

        .symbol scan {{
          font-family: Symbola;
          font-style: normal;
          font-weight: normal;
        }}

        .addShadow {{
          text-shadow:
            -1px -1px 0 #000,
            1px -1px 0 #000,
            -1px 1px 0 #000,
            1px 1px 0 #000;
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

        .title {{
          font-family: Gentium Book Basic;
          font-style: italic;
          font-weight: bold;
          vertical-align: top;
          text-align: center;
          font-size: 42;
        }}

        .art {{
          display: flex;
          justify-content: flex-start;
          align-items: flex-end;
          height: 46%;
          margin: 0% 5% 8% 5%;
          width: 90%;
          /* font-family: Gentium Book Basic; */
          font-family: Segoe Script;
          vertical-align: bottom;
          text-align: left;
          font-size: 42;
          font-weight: bold;
          font-style: italic;
        }}

        .powerName {{
          width: 100%;
          font-family: Gentium Book Basic;
          vertical-align: middle;
          text-align: center;
          font-size: 32;
          font-weight: bold;
          font-style: italic;
          line-height: 1.2;
        }}

        .powerSub {{
          font-weight: normal;
          font-style: italic;
          font-size: 28;
        }}

        .power {{
          height: 36%;
          margin: 0% 5% 0% 5%;
          width: 90%;
          font-family: Gentium Book Basic;
          vertical-align: middle;
          text-align: center;
          font-size: 28;
          line-height: 1.2;
        }}

        .signed {{
          height: 10%;
          width: 90%;
          margin: 0% 5% 0% 5%;
          font-family: Segoe Script;
          font-style: italic;
          vertical-align: bottom;
          text-align: right;
          font-size: 28;
        }}

        ''',

    'markers': '''
          vertical-align: middle;
          text-align: center;

          font-family: Symbola;
          font-style: normal;
          font-weight: normal;
          font-size: 1000;
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

def formatLine(text):
    formatting = '<div class="powerName">{}</div>{}'
    leftSub = '<scan class="powerSub">('
    rightSub = ')</scan>'
    if ':' in text:
        boldPart, theRest = text.split(':', 1)
        boldPart = boldPart.replace('(', leftSub)
        boldPart = boldPart.replace(')', rightSub)
        return formatting.format(boldPart, theRest)

def formatText(text):
    lines = []
    if '\n' in text:
        for chunk in text.split('\n'):
            lines.append(formatLine(chunk))
        text = '<br/><br/>'.join(lines)
    elif ':' in text:
        text = formatLine(text)

    for formatFrom, formatTo in conversions.items():
        text = text.replace(formatFrom, formatTo)

    return text

def formatSignature(text):
    if len(text) == 0:
        return ''

    words = []
    if ' ' in text:
        for word in text.split(' '):
            if word.lower() in noBold:
                words.append(word)
            else:
                words.append('<b>{}</b>'.format(word))
    else:
        words.append('<b>{}</b>'.format(text))

    return '- {}'.format(' '.join(words))


# Generate traits deck
cards = []

# Convert CSV to cards
with open('resources/Persuasion - Traits.csv', 'r', encoding="utf-8") as input:
    cardDetails = csv.DictReader(input)
    for row in cardDetails:
        # Skip lines that aren't ready or have a power written
        if row['Ready?'] == '🚏':
            break
        elif row['Ready?'] != '✅':
            continue

        if row['Mods'] == '🔒':
            greeting = '<div class="greeting">Dear diary,</div>'
        else:
            greeting = '<div class="greeting">Dear</div>'

        params = {
            'title': row['Name'],
            'symbol': row['Suit'],
            'modifiers': row['Mods'],
            'reference': row['Ref'],
            'art': greeting,
            'power': formatText(row['Effect']),
            'signed': formatSignature(row['Signed'])
        }
        cards.append(traitCard.format(**params))

# Generate traits without border
writeCards(cards, 'traits-unsleeved', style=styles['traits'].format('None', '100%', '100%', 'auto'))

# Generate trait cards with borders for each player
for color, hex in crests.items():
    writeCards(cards, 'traits-{}'.format(color), style=styles['traits'].format(hex, '94%', '96%', 'auto'))

cards = ['<div id="{}"></div>'.format(color) for color in crests.keys()]
# Generate suited one offs (Rings)

for crestType in crestCards:
    styleSections = []
    for color, hex in crests.items():
        styleSections.append(crestSection.format(color, crestType))

    style = styles['crests'].format(''.join(styleSections))
    writeCards(cards, crestType, style=style)

cards = [ '✍', '🗝', '👒', '🐦', '🔓', '🪞', '💌', '✉', '📤', '📥', '📦', '📨', '📩', '📭', '📮', '🎭', '🗯️', '💬', '🗫', '🔒' ]

writeCards(cards, 'symbols', style=styles['markers'], sheetColumns=4, sheetRows=3)
