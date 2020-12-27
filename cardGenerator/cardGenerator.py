from itertools import combinations

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

        table {{
          page-break-before: always;
          page-break-after: always;

          width: 100%;
          height: 100%;

          font-family: Symbola;
          font-size: 32;

          border: none;
          margin: none;
          padding: none;

          vertical-align: top;
          text-align: left;

          background:url("resources/background.jpg") no-repeat center center ;
          -webkit-background-size: cover;
          -moz-background-size: cover;
          -o-background-size: cover;
          background-size: cover;
        }}
    </style>
</head>
<body>
{}
</body>
'''

templatePlus = '''    <div>
        {plus}{{}}{{}}<br>{minus}{{}}
    </div>'''.format(plus=plus, minus=minus)

templateMinus = '''    <div>
        {plus}{{}}<br>{minus}{{}}{{}}
    </div>
'''.format(plus=plus, minus=minus)

cards = []

for pairs in combinations(suits, 2):
    for spare in suits.difference(set(pairs)):
        cards.append(templatePlus.format(pairs[0], pairs[1], spare))
        cards.append(templateMinus.format(spare, pairs[0], pairs[1]))

print(html.format(''.join(cards)))
with open('cards.html', 'w') as f:
    f.write(html.format(''.join(cards)))



'''
suits = {
    'wealth': '&#x1F48E',
    'title': '&#x1F451',
    'power': '&#x1F5E1',
    'romance': '&#x1F339',
    'faith': '&#x1F64F'
}

import pdfkit


options = {
    'page-size': 'A4',
    'margin-top': '0.0in',
    'margin-right': '0.0in',
    'margin-bottom': '0.0in',
    'margin-left': '0.0in',
}

pdfkit.from_file('index.html', 'traits.pdf', css="C:/Users/QuazAndWally/Documents/GitHub/Persuation/cardGenerator/fashion.css", options=options)
'''
