# Merkkijono, josta tehdään viivakoodia common-variantti
while True:

    text = input('Syötä kirjain: ')
    characterValue = ord(text)
    print('Kirjaimen numeerinen arvo on', characterValue)
    if characterValue <  32:
        print('Kirjaimen', text, 'välin 0 - 31 merkkejä ei voi käyttää.')
    elif characterValue < 127:
        print('Kirjaimen', text, 'arvo on välillä 0 - 126, se voi olla 7 bittinen merkki.')
        code128Value = characterValue - 32
        print('Viivakoodi  varmistussummaa laskettaessa arvo on', code128Value)
    elif characterValue == 127:
        print('Kirjaimen', text, 'arvo on 127, mutta se ei ole sallittu merkki.')
    elif characterValue < 195:
        print('Kirjaimen', text, 'välin 127 - 194 merkkejä ei voi käyttää.')
    elif characterValue > 202:
        print('Kirjaimen', text, 'merkkejä, joiden arvo on yli 202 ei voi käyttää.')
    else:
        print('Kirjaimen', text, 'arvo on suurempi kuin 127, se on vähintään 8 bittinen')
        code128Value = characterValue - 100
        print('Viivakoodin varmistussummaa laskettaessa arvo on', code128Value)
