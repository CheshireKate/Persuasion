from math import ceil
traitDescription = 'To resleeve, right click, select State, then pick the relevant sleeve'
cardCount = 42

base = {
    'deckID': 1,
    'tts_color': "None",
    'name': 'Trait',
    'cardList': ', '.join([str(i) for i in range(100, 100 + cardCount)]),
    'height': str(ceil(cardCount/10.0)),
    'description': traitDescription,
    'face': 'http://cloud-3.steamusercontent.com/ugc/1762567303610929161/E80610595A4E9B7F16C9921AE6E2F41C75AAA9D1/',
    'back': 'http://cloud-3.steamusercontent.com/ugc/1760314147747003169/3FA671000FC54F9E5820713587059A40F17D4ADD/'
}

decks = [
    {
        'deckID': 2,
        'tts_color': "Brown",
        'name': 'Black Dog Trait',
        'description': traitDescription,
        'face': 'http://cloud-3.steamusercontent.com/ugc/1762567303610930323/B143F0FA1222A74CD27075EBA6937A50F2EC556D/',
        'back': 'http://cloud-3.steamusercontent.com/ugc/1656728318303124139/3386D885EC1630D77C835EA6C49FA6B6C64C8952/'
    },
    {
        'deckID': 3,
        'tts_color': "Blue",
        'name': 'Blue Lion Trait',
        'description': traitDescription,
        'face': 'http://cloud-3.steamusercontent.com/ugc/1762567303610930760/3783878756FB8B06C8D872E0C520CF0BAADC0D07/',
        'back': 'http://cloud-3.steamusercontent.com/ugc/1656728318303214207/F6C545671C5D9E26A8587061ADE177DD0240D2B0/'
    },
    {
        'deckID': 4,
        'tts_color': "Green",
        'name': 'Green Tree Trait',
        'description': traitDescription,
        'face': 'http://cloud-3.steamusercontent.com/ugc/1762567303610931285/51BFCF32FBCADD846FB7549AE8CB998DD695BB2F/',
        'back': 'http://cloud-3.steamusercontent.com/ugc/1656728318303219676/E43B426C0EC6E5C4828774496FA767B4D9FD2810/'
    },
    {
        'deckID': 5,
        'tts_color': "Teal",
        'name': 'Cyan Shield Trait',
        'description': traitDescription,
        'face': 'http://cloud-3.steamusercontent.com/ugc/1762567303610933078/45A200EC81CBB1EC55864D2CE6D8F1D8792E04EC/',
        'back': 'http://cloud-3.steamusercontent.com/ugc/1656728318303223441/26EBC8436FCDFF59041E702E58506D1E068985AE/'
    },
    {
        'deckID': 6,
        'tts_color': "Yellow",
        'name': 'Yellow Sun Trait',
        'description': traitDescription,
        'face': 'http://cloud-3.steamusercontent.com/ugc/1762567303611410144/6BA0AB8737EA89EDB71DC09FB45D8466F22C5656/',
        'back': 'http://cloud-3.steamusercontent.com/ugc/1656728318303226151/8173A6620818B8C3A202227FF9B6198F64A1AA13/'
    },
    {
        'deckID': 7,
        'tts_color': "Pink",
        'name': 'Pink Horn Trait',
        'description': traitDescription,
        'face': 'http://cloud-3.steamusercontent.com/ugc/1762567303610931906/F5FEE517C77DAC9BBBFB77BC9D47F4634C2641CF/',
        'back': 'http://cloud-3.steamusercontent.com/ugc/1656728318303220938/68722CE40FB18FE8CFAC5D06AB8E00D53BCA4A33/'
    },
    {
        'deckID': 8,
        'tts_color': "Purple",
        'name': 'Purple Clover Trait',
        'description': traitDescription,
        'face': 'http://cloud-3.steamusercontent.com/ugc/1762567303610932450/1D3492B2618F73DAEF4AF420BAEA36B009479F20/',
        'back': 'http://cloud-3.steamusercontent.com/ugc/1656728318303222134/F7EA4278B2C0EC7640592E7804317356071B0788/'
    },
    {
        'deckID': 9,
        'tts_color': "White",
        'name': 'White Horse Trait',
        'description': traitDescription,
        'face': 'http://cloud-3.steamusercontent.com/ugc/1762567303611409757/2CC5DF282DD011CD807FB37FB435090EC67C8243/',
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
          "GMNotes": "{tts_color}",
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
              "GMNotes": "{tts_color}",
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
for cardID in range(cardCount):
    states = []
    for deck in decks:
        deck['cardID'] = deck['deckID'] * 100 + cardID
        deck['height'] = base['height']
        states.append(state.format(**deck))

    base['cardID'] = base['deckID'] * 100 + cardID
    base['states'] = ','.join(states);

    cards.append(card.format(**base))

with open('allCards.json', 'w') as f:
    f.write(ttsObject.format(','.join(cards)))
