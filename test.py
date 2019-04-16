import json

d1 = [
    {
        'title': 'IMAX',
        'subtitle': 'IMAX - EXPERIENȚA CINEMATOGRAFICĂ DINCOLO DE LIMITELE IMAGINAȚIEI',
        'content': 'IMAX este cea mai avansată tehnologie disponibilă publicului – prin care tesimți înmijlocul acțiunii. Ecranul imens te transpune într-o altă galaxie, iarsunetul carezguduie pământul o te facă să îți bată inima mai repede, incat vei trăi oexperiențăcinematografică de neuitat.',
    },
    {
        'title': '4DX',
        'subtitle': 'SIMTE PUTEREA CINEMATOGRAFULUI',
        'content': 'Sala 4DX® este un loc unde filmul devine realitate. 4DX® este o tehnologie revoluționară, prima de acest fel din lume, pentru proiectarea celor mai mari producții de filme de la Hollywood in format 4D. Scaunele mobile și soluțiile ambientale de ultimă oră vor oferi spectatorilor o experiență cinematografică extremă care este plină de efecte speciale și care permite publicului sǎ devinǎ parte din film.'
    },
    {
        'title': 'VIP',
        'subtitle': 'VIP - DIN DRAGOSTE PENTRU CINEMA',
        'content': 'Iubim filmele și, mai presus de orice, iubim să le vedem pe marele ecran.Departe deviețile atât de aglomerate și zgomotoase, în care suntem mereu grăbiți șiobosiți,în sala de cinema ne deconectăm și pătrundem într-o lume specială, a căreimagieeste reînnoită cu fiecare inovație tehnologică sau nou format de vizionare.Iarodată cu noul concept VIP de la Cinema City ParkLake - cină și film-, eștitransformat chiar tu, spectatorul, în personajul principal.'
    }
]

with open('home.json', 'w+') as fh:
    json.dump(d1, fh)
