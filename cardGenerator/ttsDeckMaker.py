from math import floor, ceil

traitDescription = 'To resleeve, right click, select State, then pick the relevant sleeve'
cardCount = 30
suits = [(10, 'gem'), (20, 'crown'), (30, 'rose')]

base = {
    'deckID': 1,
    'name': 'Trait',
    'cardList': ', '.join([str(i) for i in range(100, 100 + cardCount)]),
    'height': str(ceil(cardCount/10.0)),
    'description': traitDescription,
    'face': 'http://cloud-3.steamusercontent.com/ugc/1762567360939882924/85820BFE02674A5483CE246645E6D37B1E6789E4/',
    'back': 'http://cloud-3.steamusercontent.com/ugc/1760314147747003169/3FA671000FC54F9E5820713587059A40F17D4ADD/'
}

decks = [
    {
        'deckID': 2,
        'name': 'Black Dog Trait',
        'description': traitDescription,
        'face': 'http://cloud-3.steamusercontent.com/ugc/1762567360939883297/54B51409190595E3897C558E423981BC8135C7F9/',
        'back': 'http://cloud-3.steamusercontent.com/ugc/1656728318303124139/3386D885EC1630D77C835EA6C49FA6B6C64C8952/'
    },
    {
        'deckID': 3,
        'name': 'Blue Lion Trait',
        'description': traitDescription,
        'face': 'http://cloud-3.steamusercontent.com/ugc/1762567360939883654/4EF128AD0671E44C4F36A16E5E658A2DCF815E55/',
        'back': 'http://cloud-3.steamusercontent.com/ugc/1656728318303214207/F6C545671C5D9E26A8587061ADE177DD0240D2B0/'
    },
    {
        'deckID': 4,
        'name': 'Green Tree Trait',
        'description': traitDescription,
        'face': 'http://cloud-3.steamusercontent.com/ugc/1762567360939884042/C9821E40A15544478312B3417E66B5DBCF86DBA3/',
        'back': 'http://cloud-3.steamusercontent.com/ugc/1656728318303219676/E43B426C0EC6E5C4828774496FA767B4D9FD2810/'
    },
    {
        'deckID': 5,
        'name': 'Cyan Shield Trait',
        'description': traitDescription,
        'face': 'http://cloud-3.steamusercontent.com/ugc/1762567360939885784/272EAEA88C11C6757BC524D4732617BE604AC1FC/',
        'back': 'http://cloud-3.steamusercontent.com/ugc/1656728318303223441/26EBC8436FCDFF59041E702E58506D1E068985AE/'
    },
    {
        'deckID': 6,
        'name': 'Yellow Sun Trait',
        'description': traitDescription,
        'face': 'http://cloud-3.steamusercontent.com/ugc/1762567360939892948/515376D95F8503FE59C2E4070A30AA4F3B7DC9EC/',
        'back': 'http://cloud-3.steamusercontent.com/ugc/1656728318303226151/8173A6620818B8C3A202227FF9B6198F64A1AA13/'
    },
    {
        'deckID': 7,
        'name': 'Pink Song Trait',
        'description': traitDescription,
        'face': 'http://cloud-3.steamusercontent.com/ugc/1762567360939884664/5A68C36D886E50E76858E9597593EFC4269A2B2E/',
        'back': 'http://cloud-3.steamusercontent.com/ugc/1656728318303220938/68722CE40FB18FE8CFAC5D06AB8E00D53BCA4A33/'
    },
    {
        'deckID': 8,
        'name': 'Purple Clover Trait',
        'description': traitDescription,
        'face': 'http://cloud-3.steamusercontent.com/ugc/1762567360939885160/6748BC3DF58CC75C943448C35F452AFF64F5BD65/',
        'back': 'http://cloud-3.steamusercontent.com/ugc/1656728318303222134/F7EA4278B2C0EC7640592E7804317356071B0788/'
    },
    {
        'deckID': 9,
        'name': 'White Horse Trait',
        'description': traitDescription,
        'face': 'http://cloud-3.steamusercontent.com/ugc/1762567360939892623/A0B379AA2FA0DE3E99D42A6385A7568FF7F2B692/',
        'back': 'http://cloud-3.steamusercontent.com/ugc/1656728318303224897/771F94BB2FA229907293E17D9AC8310D6617C6B0/'
    }
]

ttsObject = '''{{{{
  "SaveName": "",
  "GameMode": "",
  "Date": "",
  "Gravity": 0.5,
  "PlayArea": 0.5,
  "GameType": "",
  "GameComplexity": "",
  "Tags": [],
  "Table": "",
  "Sky": "",
  "Note": "",
  "Rules": "",
  "TabStates": {{{{}}}},
  "ObjectStates": [
    {{{{
      "Name": "Deck",
      "Transform": {{{{
        "posX": -7.72676373,
        "posY": 0.999352634,
        "posZ": 11.263113,
        "rotX": 2.76832234E-05,
        "rotY": 180.001541,
        "rotZ": 180.210648,
        "scaleX": 1.0,
        "scaleY": 1.0,
        "scaleZ": 1.0
      }}}},
      "Nickname": "Traits",
      "Description": "",
      "GMNotes": "",
      "ColorDiffuse": {{{{
        "r": 0.713235259,
        "g": 0.713235259,
        "b": 0.713235259
      }}}},
      "Locked": false,
      "Grid": true,
      "Snap": true,
      "IgnoreFoW": false,
      "MeasureMovement": false,
      "DragSelectable": true,
      "Autoraise": true,
      "Sticky": true,
      "Tooltip": true,
      "GridProjection": false,
      "HideWhenFaceDown": true,
      "Hands": false,
      "SidewaysCard": false,
      "DeckIDs": [ {cardList} ],
      "CustomDeck": {{{{
        "1": {{{{
          "FaceURL": "{face}",
          "BackURL": "{back}",
          "NumWidth": 10,
          "NumHeight": {height},
          "BackIsHidden": true,
          "UniqueBack": false,
          "Type": 0
        }}}}
      }}}},
      "LuaScript": "",
      "LuaScriptState": "",
      "XmlUI": "",
      "ContainedObjects": [
        {{}}
      ],
      "GUID": "100000"
    }}}}
  ],
  "LuaScript": "",
  "LuaScriptState": "",
  "XmlUI": "",
  "VersionNumber": ""
}}}}'''.format(**base)

card = '''{{
          "Name": "Card",
          "Transform": {{
            "posX": -7.69503927,
            "posY": 1.0400672,
            "posZ": 11.0366421,
            "rotX": 359.9547,
            "rotY": 179.977524,
            "rotZ": 179.976715,
            "scaleX": 1.0,
            "scaleY": 1.0,
            "scaleZ": 1.0
          }},
          "Nickname": "{name}",
          "Description": "{description}",
          "GMNotes": "{suit}",
          "ColorDiffuse": {{
            "r": 0.713235259,
            "g": 0.713235259,
            "b": 0.713235259
          }},
          "Locked": false,
          "Grid": true,
          "Snap": true,
          "IgnoreFoW": false,
          "MeasureMovement": false,
          "DragSelectable": true,
          "Autoraise": true,
          "Sticky": true,
          "Tooltip": true,
          "GridProjection": false,
          "HideWhenFaceDown": true,
          "Hands": true,
          "CardID": "{cardID:d}",
          "SidewaysCard": false,
          "CustomDeck": {{
            "1": {{
              "FaceURL": "{face}",
              "BackURL": "{back}",
              "NumWidth": 10,
              "NumHeight": {height},
              "BackIsHidden": true,
              "UniqueBack": false,
              "Type": 0
            }}
          }},
          "LuaScript": "",
          "LuaScriptState": "",
          "XmlUI": "",
          "GUID": "10{cardID:04d}",
          "States": {{
          {states}
          }}
        }}'''

# States start
state = '''"{deckID:d}": {{
              "Name": "Card",
              "Transform": {{
                "posX": -5.430677,
                "posY": 0.982206643,
                "posZ": 11.5248652,
                "rotX": 359.9847,
                "rotY": 180.000015,
                "rotZ": -0.00292019383,
                "scaleX": 1.0,
                "scaleY": 1.0,
                "scaleZ": 1.0
              }},
              "Nickname": "{name}",
              "Description": "{description}",
              "GMNotes": "{suit}",
              "ColorDiffuse": {{
                "r": 0.713235259,
                "g": 0.713235259,
                "b": 0.713235259
              }},
              "Locked": false,
              "Grid": true,
              "Snap": true,
              "IgnoreFoW": false,
              "MeasureMovement": false,
              "DragSelectable": true,
              "Autoraise": true,
              "Sticky": true,
              "Tooltip": true,
              "GridProjection": false,
              "HideWhenFaceDown": true,
              "Hands": true,
              "CardID": "{cardID:d}",
              "SidewaysCard": false,
              "CustomDeck": {{
                "{deckID:d}": {{
                  "FaceURL": "{face}",
                  "BackURL": "{back}",
                  "NumWidth": 10,
                  "NumHeight": {height},
                  "BackIsHidden": true,
                  "UniqueBack": false,
                  "Type": 0
                }}
              }},
              "LuaScript": "",
              "LuaScriptState": "",
              "XmlUI": "",
              "GUID": "10{cardID:04d}"
            }}'''

# Generate combinations
cards = []
suitIndex = 0
suit = suits[0][1]
for cardID in range(cardCount):
    if cardID >= suits[suitIndex][0]:
        suitIndex += 1
        suit = suits[suitIndex][1]

    states = []
    for deck in decks:
        deck['cardID'] = deck['deckID'] * 100 + cardID
        deck['suit'] = suit
        deck['height'] = base['height']
        states.append(state.format(**deck))

    base['cardID'] = base['deckID'] * 100 + cardID
    base['suit'] = suit
    base['states'] = ','.join(states);

    cards.append(card.format(**base))

with open('allCards.json', 'w') as f:
    f.write(ttsObject.format(','.join(cards)))
