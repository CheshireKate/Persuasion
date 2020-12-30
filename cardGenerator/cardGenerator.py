from itertools import combinations
from math import floor

sheetRows = 5
sheetColumns = 10
sheetCount = sheetColumns * sheetRows

plus = '&#xFF0B'
minus = '&#xFF0D'
suits = set(['&#x1F48E', '&#x1F451', '&#x1F5E1', '&#x1F339', '&#x1F64F'])

html = '''<html>
<head>
    <style>
        @font-face {{{{
            font-family: Symbola;
            src: url('resources/Symbola.otf');
        }}}}

        body {{{{
          border: 0px !important;
          margin: 0px !important;
          padding: 0px !important;
        }}}}

        table {{{{
          page-break-before: always;
          page-break-after: always;
          width: 100%;
          height: 100%;
        }}}}

        table, tr, td {{{{
          font-family: Symbola;
          border: none;
          margin: none;
          padding: none;
        }}}}

        td {{{{
          border: 1px;
          -webkit-background-size: cover;
          -moz-background-size: cover;
          -o-background-size: cover;
          background-size: cover;

          width: {}%;
          height: {}%;

          /* Custom Styling */
        {{}}
    </style>
</head>
<body>
{{}}
</body>
'''.format(floor(100 / sheetColumns), floor(100 / sheetRows))

style = {
    'traits': '''
          background:url("resources/background.jpg") no-repeat center center ;
          vertical-align: top;
          text-align: left;
          font-size: 36;
        }
        ''',

    'desires': '''
          background:url("resources/background.jpg") no-repeat center center ;
          vertical-align: center;
          text-align: center;
          font-size: 72;
        }

        p {
          font-size: 24;
        }
        ''',

    'backs': '''
        }

        div {
          width: 100%;
          height: 100%;

          -webkit-background-size: contain !important;
          -moz-background-size: contain !important;
          -o-background-size: contain !important;
          background-size: contain !important;
        }

        #default {
          background:url("resources/cardBack.jpg") no-repeat center center ;
        }

        #anna {
          background:url("resources/Anna.png") no-repeat center center ;
        }

        #john {
          background:url("resources/John.png") no-repeat center center ;
        }

        #penelope {
          background:url("resources/Penelope.png") no-repeat center center ;
        }

        #rose {
          background:url("resources/Rose.png") no-repeat center center ;
        }

        #sarah {
          background:url("resources/Sarah.png") no-repeat center center ;
        }

        #thomas {
          background:url("resources/Thomas.png") no-repeat center center ;
        }

        #victor {
          background:url("resources/Victor.png") no-repeat center center ;
        }

        #william {
          background:url("resources/William.png") no-repeat center center ;
        }
        '''
}

def writeCards(cards, deck):
    pages = []

    #  Fill sheet with blanks
    cards.extend([''] * (sheetCount - (len(cards) % sheetCount)))

    for pageNum in range(len(cards) // sheetCount):
        pages.append(page.format(*cards[pageNum * sheetCount:((pageNum + 1) * sheetCount)]))

    with open('{}.html'.format(deck), 'w') as f:
        f.write(html.format(style[deck], ''.join(pages)))

cell = '<td>{}</td>'
row = '        <tr>{}</tr>'.format(cell * sheetColumns)
page = '''    <table>
{}
    </table>
'''.format(row * sheetRows)

# Generate traits deck
cards = []

traitPlus = '{plus}{{}}{{}}<br>{minus}{{}}'.format(plus=plus, minus=minus)
traitMinus = '{plus}{{}}<br>{minus}{{}}{{}}'.format(plus=plus, minus=minus)

# Generate combinations
for pairs in combinations(suits, 2):
    for spare in suits.difference(set(pairs)):
        cards.append(traitPlus.format(pairs[0], pairs[1], spare))
        cards.append(traitMinus.format(spare, pairs[0], pairs[1]))

writeCards(cards, 'traits')

# Generate desires deck
cards = []

desirePlus = '<p>Looking for...<br></p>{plus}{{}}'.format(plus=plus, minus=minus)
desireMinus = '<p>Looking for<br></p>{minus}{{}}'.format(plus=plus, minus=minus)

for suit in suits:
    cards.append(desirePlus.format(suit))
    cards.append(desireMinus.format(suit))

writeCards(cards, 'desires')

# Generate deck backs
cards = [
    '<div id="default"></div>',
    '<div id="anna"></div>',
    '<div id="john"></div>',
    '<div id="penelope"></div>',
    '<div id="rose"></div>',
    '<div id="sarah"></div>',
    '<div id="thomas"></div>',
    '<div id="victor"></div>',
    '<div id="william"></div>',
]

writeCards(cards, 'backs')
