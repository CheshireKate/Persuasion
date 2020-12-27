from itertools import combinations
from math import floor

sheetRows = 5
sheetColumns = 10
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
          font-size: 36;
          border: none;
          margin: none;
          padding: none;
          vertical-align: top;
          text-align: left;
        }}}}

        td {{{{
          background:url("resources/background.jpg") no-repeat center center ;
          -webkit-background-size: cover;
          -moz-background-size: cover;
          -o-background-size: cover;
          background-size: cover;
          width: {}%;
        }}}}
    </style>
</head>
<body>
{{}}
</body>
'''.format(floor(100 / sheetColumns))

cell = '<td>{}</td>'
row = '        <tr>{}</tr>'.format(cell * sheetColumns)
page = '''    <table>
{}
    </table>
'''.format(row * sheetRows)

templatePlus = '{plus}{{}}{{}}<br>{minus}{{}}'.format(plus=plus, minus=minus)
templateMinus = '{plus}{{}}<br>{minus}{{}}{{}}'.format(plus=plus, minus=minus)

sheetCount = sheetColumns * sheetRows

cards = []

# Generate combinations
for pairs in combinations(suits, 2):
    for spare in suits.difference(set(pairs)):
        cards.append(templatePlus.format(pairs[0], pairs[1], spare))
        cards.append(templateMinus.format(spare, pairs[0], pairs[1]))

#  Fill sheet with blanks
cards.extend(['&nbsp<br>&nbsp'] * (sheetCount - (len(cards) % sheetCount)))

pages = []

for pageNum in range(len(cards) // sheetCount):
    pages.append(page.format(*cards[pageNum * sheetCount:((pageNum + 1) * sheetCount)]))

with open('cards.html', 'w') as f:
    f.write(html.format(''.join(pages)))
