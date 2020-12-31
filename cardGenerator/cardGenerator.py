from itertools import combinations
from math import floor

plus = '&#xFF0B'
minus = '&#xFF0D'
suits = set(['&#x1F48E', '&#x1F451', '&#x1F5E1', '&#x1F339', '&#x1F64F'])

html = '''<html>
<head>
    <style>
        @font-face {{
            font-family: Symbola;
            src: url('resources/Symbola.otf');
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
          border: none;
          margin: none;
          padding: none;
        }}

        td {{
          border: 1px;
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

style = {
    'traits': '''
          background:url("resources/background.jpg") no-repeat center center ;
          vertical-align: top;
          text-align: left;
          font-size: 72;
        }

        div {
          width: 100%;
          height: 100%;

          background:url("resources/invitation.jpg") no-repeat center center ;

          -webkit-background-size: contain !important;
          -moz-background-size: contain !important;
          -o-background-size: contain !important;
          background-size: contain !important;
        }
        ''',

    'plusSide': '''
          background:url("resources/background.jpg") no-repeat center center ;
          vertical-align: middle;
          text-align: center;
          font-size: 288;
        }
        ''',

    'characters': '''
        }

        div {
          width: 100%;
          height: 100%;

          -webkit-background-size: contain !important;
          -moz-background-size: contain !important;
          -o-background-size: contain !important;
          background-size: contain !important;
        }

        #anna {
          background:url("resources/Anna.jpg") no-repeat center center ;
        }

        #john {
          background:url("resources/John.jpg") no-repeat center center ;
        }

        #penelope {
          background:url("resources/Penelope.jpg") no-repeat center center ;
        }

        #rose {
          background:url("resources/Rose.jpg") no-repeat center center ;
        }

        #sarah {
          background:url("resources/Sarah.jpg") no-repeat center center ;
        }

        #thomas {
          background:url("resources/Thomas.jpg") no-repeat center center ;
        }

        #victor {
          background:url("resources/Victor.jpg") no-repeat center center ;
        }

        #william {
          background:url("resources/William.jpg") no-repeat center center ;
        }
        ''',

    'independence': '''
          background:url("resources/independent.jpg") no-repeat center center ;
        }
        ''',

    'invitations': '''
        }

        div {
          width: 100%;
          height: 100%;

          -webkit-background-size: contain !important;
          -moz-background-size: contain !important;
          -o-background-size: contain !important;
          background-size: contain !important;
        }

        #anna {
          background:url("resources/AnnaInvite.jpg") no-repeat center center ;
        }

        #john {
          background:url("resources/JohnInvite.jpg") no-repeat center center ;
        }

        #penelope {
          background:url("resources/PenelopeInvite.jpg") no-repeat center center ;
        }

        #rose {
          background:url("resources/RoseInvite.jpg") no-repeat center center ;
        }

        #sarah {
          background:url("resources/SarahInvite.jpg") no-repeat center center ;
        }

        #thomas {
          background:url("resources/ThomasInvite.jpg") no-repeat center center ;
        }

        #victor {
          background:url("resources/VictorInvite.jpg") no-repeat center center ;
        }

        #william {
          background:url("resources/WilliamInvite.jpg") no-repeat center center ;
        }
        ''',

    'proposals': '''
        }

        div {
          width: 100%;
          height: 100%;

          -webkit-background-size: contain !important;
          -moz-background-size: contain !important;
          -o-background-size: contain !important;
          background-size: contain !important;
        }

        #anna {
          background:url("resources/AnnaPropose.jpg") no-repeat center center ;
        }

        #john {
          background:url("resources/JohnPropose.jpg") no-repeat center center ;
        }

        #penelope {
          background:url("resources/PenelopePropose.jpg") no-repeat center center ;
        }

        #rose {
          background:url("resources/RosePropose.jpg") no-repeat center center ;
        }

        #sarah {
          background:url("resources/SarahPropose.jpg") no-repeat center center ;
        }

        #thomas {
          background:url("resources/ThomasPropose.jpg") no-repeat center center ;
        }

        #victor {
          background:url("resources/VictorPropose.jpg") no-repeat center center ;
        }

        #william {
          background:url("resources/WilliamPropose.jpg") no-repeat center center ;
        }
        '''
}

style['minusSide'] = style['plusSide']

def writeCards(originalCards, deck, sheetColumns=10, sheetRows=5):
    sheetCount = sheetColumns * sheetRows
    cell = '<td>{}</td>'
    row = '        <tr>{}</tr>'.format(cell * sheetColumns)
    page = '    <table>{}</table>'.format(row * sheetRows)
    pages = []
    cards = originalCards[:]

    #  Fill sheet with blanks
    cards.extend([''] * (sheetCount - (len(cards) % sheetCount)))

    for pageNum in range(len(cards) // sheetCount):
        pages.append(page.format(*cards[pageNum * sheetCount:((pageNum + 1) * sheetCount)]))

    with open('{}.html'.format(deck), 'w') as f:
        f.write(html.format(floor(100 / sheetColumns), floor(100 / sheetRows), style[deck], ''.join(pages)))


# Generate traits deck
cards = []

traitPlus = '{plus}{{}}{{}}<br>{minus}{{}}'.format(plus=plus, minus=minus)
traitMinus = '{plus}{{}}<br>{minus}{{}}{{}}'.format(plus=plus, minus=minus)

plusCombos = []
minusCombos = []

# Generate combinations
for pairs in combinations(suits, 2):
    for spare in suits.difference(set(pairs)):
        cards.append(traitPlus.format(pairs[0], pairs[1], spare))
        cards.append(traitMinus.format(spare, pairs[0], pairs[1]))

        # For generating a csv page of the emojis
        plusCombos.append('{}{}'.format(pairs[0], pairs[1]))
        plusCombos.append('{}'.format(spare))
        minusCombos.append('{}'.format(spare))
        minusCombos.append('{}{}'.format(pairs[0], pairs[1]))

# For generating a csv page of the emojis
with open('traits-csv.html', 'w') as f:
    for i in range(len(plusCombos)):
        f.write('{},{}<br>'.format(plusCombos[i], minusCombos[i]))

# Add one last card for card back (Will need to be separated out in GIMP)
cards.append('<div></div>')

writeCards(cards, 'traits')

# Generate characters deck
cards = [
    '<div id="anna"></div>',
    '<div id="john"></div>',
    '<div id="penelope"></div>',
    '<div id="rose"></div>',
    '',
    '',
    '',
    '',
    '',
    '',
    '<div id="sarah"></div>',
    '<div id="thomas"></div>',
    '<div id="victor"></div>',
    '<div id="william"></div>'
]

writeCards(cards, 'invitations')

writeCards(cards, 'proposals')

writeCards(cards, 'characters')

cards = [''] * (14);

writeCards(cards, 'independence')

for modifier in [(plus, 'plusSide'), (minus, 'minusSide')]:
    cards = []
    for i, suit in enumerate(suits):
        print(i)
        print(suit)
        cards.append('{}{}'.format(modifier[0], suit))
        if i == 2:
            print(cards)
            cards.extend([''] * 2)

    writeCards(cards, modifier[1], 5, 4)
