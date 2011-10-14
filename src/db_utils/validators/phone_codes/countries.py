#!/usr/bin/python
# -*- coding: utf-8 -*-


""" In this file is provided a list of countries with their phone codes.


FIXME: Countries should be in English and internationalized with
``gettext``.

"""


from db_utils.validators.phone_codes.lt import (
        REGIONS_PHONE_CODES_LT, REGIONS_PHONE_CODES_LT_BY_CODE)


COUNTRIES_PHONE_CODES = [
    {
        'country': u'Afganistanas',
        'code': u'93',
    },
    {
        'country': u'Airija',
        'code': u'353',
    },
    {
        'country': u'Albanija',
        'code': u'355',
    },
    {
        'country': u'Alžyras',
        'code': u'213',
    },
    {
        'country': u'Amerikos Samoa',
        'code': u'684',
    },
    {
        'country': u'Andora',
        'code': u'376',
    },
    {
        'country': u'Angola',
        'code': u'244',
    },
    {
        'country': u'Anguilla',
        'code': u'1264',
    },
    {
        'country': u'Antigva ir Barbuda',
        'code': u'1268',
    },
    {
        'country': u'Argentina',
        'code': u'54',
    },
    {
        'country': u'Armėnija',
        'code': u'374',
    },
    {
        'country': u'Aruba',
        'code': u'297',
    },
    {
        'country': u'Australija',
        'code': u'61',
    },
    {
        'country': u'Austrija',
        'code': u'43',
    },
    {
        'country': u'Azerbaidžanas',
        'code': u'994',
    },
    {
        'country': u'Bahamos',
        'code': u'1242',
    },
    {
        'country': u'Bahreinas',
        'code': u'973',
    },
    {
        'country': u'Baltarusija',
        'code': u'375',
    },
    {
        'country': u'Bangladešas',
        'code': u'880',
    },
    {
        'country': u'Barbadosas',
        'code': u'1246',
    },
    {
        'country': u'Belgija',
        'code': u'32',
    },
    {
        'country': u'Belizas',
        'code': u'501',
    },
    {
        'country': u'Beninas',
        'code': u'229',
    },
    {
        'country': u'Bermuda',
        'code': u'1441',
    },
    {
        'country': u'Bisau Gvinėja',
        'code': u'245',
    },
    {
        'country': u'Bolivija',
        'code': u'591',
    },
    {
        'country': u'Bosnija ir Hercegovina',
        'code': u'387',
    },
    {
        'country': u'Bostvana',
        'code': u'267',
    },
    {
        'country': u'Brazilija',
        'code': u'55',
    },
    {
        'country': u'Brunėjus',
        'code': u'673',
    },
    {
        'country': u'Bulgarija',
        'code': u'359',
    },
    {
        'country': u'Burkina Fasas',
        'code': u'226',
    },
    {
        'country': u'Burundis',
        'code': u'257',
    },
    {
        'country': u'Butanas',
        'code': u'975',
    },
    {
        'country': u'Čadas',
        'code': u'235',
    },
    {
        'country': u'Čekija',
        'code': u'420',
    },
    {
        'country': u'Centrinės Afrikos respublika',
        'code': u'236',
    },
    {
        'country': u'Čilė',
        'code': u'56',
    },
    {
        'country': u'Dangun Žengimo sala',
        'code': u'247',
    },
    {
        'country': u'Danija',
        'code': u'45',
    },
    {
        'country': u'Didžioji Britanija',
        'code': u'44',
    },
    {
        'country': u'Diego Garcia',
        'code': u'246',
    },
    {
        'country': u'Dominika',
        'code': u'1767',
    },
    {
        'country': u'Dominikos Respublika',
        'code': u'1809',
    },
    {
        'country': u'Dramblio Kaulo krantas',
        'code': u'225',
    },
    {
        'country': u'Džibutis',
        'code': u'253',
    },
    {
        'country': u'Egiptas',
        'code': u'20',
    },
    {
        'country': u'Ekvadoras',
        'code': u'593',
    },
    {
        'country': u'Emsat',
        'code': u'88213',
    },
    {
        'country': u'Eritrėja',
        'code': u'291',
    },
    {
        'country': u'Estija',
        'code': u'372',
    },
    {
        'country': u'Etiopija',
        'code': u'251',
    },
    {
        'country': u'Farerų salos',
        'code': u'298',
    },
    {
        'country': u'Fidžis',
        'code': u'679',
    },
    {
        'country': u'Filipinai',
        'code': u'63',
    },
    {
        'country': u'Folklando salos',
        'code': u'500',
    },
    {
        'country': u'Gabonas',
        'code': u'241',
    },
    {
        'country': u'Gajana',
        'code': u'592',
    },
    {
        'country': u'Gambija',
        'code': u'220',
    },
    {
        'country': u'Gana',
        'code': u'233',
    },
    {
        'country': u'Gibraltaras',
        'code': u'350',
    },
    {
        'country': u'Graikija',
        'code': u'30',
    },
    {
        'country': u'Grenada',
        'code': u'1473',
    },
    {
        'country': u'Grenlandija',
        'code': u'299',
    },
    {
        'country': u'Gruzija',
        'code': u'995',
    },
    {
        'country': u'Guamas',
        'code': u'1671',
    },
    {
        'country': u'Gvadelupa',
        'code': u'590',
    },
    {
        'country': u'Gvatemala',
        'code': u'502',
    },
    {
        'country': u'Gvinėja',
        'code': u'224',
    },
    {
        'country': u'Haitis',
        'code': u'509',
    },
    {
        'country': u'Hondūras',
        'code': u'504',
    },
    {
        'country': u'Honkongas',
        'code': u'852',
    },
    {
        'country': u'Indija',
        'code': u'91',
    },
    {
        'country': u'Indonezija',
        'code': u'62',
    },
    {
        'country': u'Inmarsat A',
        'code': u'8711',
    },
    {
        'country': u'Inmarsat A',
        'code': u'8721',
    },
    {
        'country': u'Inmarsat A',
        'code': u'8731',
    },
    {
        'country': u'Inmarsat A',
        'code': u'8741',
    },
    {
        'country': u'Inmarsat B',
        'code': u'8703',
    },
    {
        'country': u'Inmarsat B',
        'code': u'8713',
    },
    {
        'country': u'Inmarsat B',
        'code': u'8723',
    },
    {
        'country': u'Inmarsat B',
        'code': u'8743',
    },
    {
        'country': u'Inmarsat C',
        'code': u'8704',
    },
    {
        'country': u'Inmarsat M',
        'code': u'8706',
    },
    {
        'country': u'Inmarsat M',
        'code': u'8716',
    },
    {
        'country': u'Inmarsat M',
        'code': u'8726',
    },
    {
        'country': u'Inmarsat M',
        'code': u'8736',
    },
    {
        'country': u'Inmarsat M',
        'code': u'8746',
    },
    {
        'country': u'Inmarsat MiniM',
        'code': u'87076',
    },
    {
        'country': u'Inmarsat MiniM',
        'code': u'87176',
    },
    {
        'country': u'Inmarsat MiniM',
        'code': u'87276',
    },
    {
        'country': u'Inmarsat MiniM',
        'code': u'87376',
    },
    {
        'country': u'Inmarsat MiniM',
        'code': u'87476',
    },
    {
        'country': u'Irakas',
        'code': u'964',
    },
    {
        'country': u'Iranas',
        'code': u'98',
    },
    {
        'country': u'Iridium',
        'code': u'8816',
    },
    {
        'country': u'Iridium',
        'code': u'8817',
    },
    {
        'country': u'Islandija',
        'code': u'354',
    },
    {
        'country': u'Ispanija',
        'code': u'34',
    },
    {
        'country': u'Italija',
        'code': u'39',
    },
    {
        'country': u'Izraelis',
        'code': u'972',
    },
    {
        'country': u'Jamaika',
        'code': u'1876',
    },
    {
        'country': u'Japonija',
        'code': u'81',
    },
    {
        'country': u'JAV',
        'code': u'1',
    },
    {
        'country': u'Jemenas',
        'code': u'967',
    },
    {
        'country': u'Jordanija',
        'code': u'962',
    },
    {
        'country': u'Jungtiniai Arabų Emyratai',
        'code': u'971',
    },
    {
        'country': u'Kabo Verdė',
        'code': u'238',
    },
    {
        'country': u'Kaimanų salos',
        'code': u'1345',
    },
    {
        'country': u'Kambodža',
        'code': u'855',
    },
    {
        'country': u'Kamerūnas',
        'code': u'237',
    },
    {
        'country': u'Kanada',
        'code': u'1',
    },
    {
        'country': u'Kataras',
        'code': u'974',
    },
    {
        'country': u'Kazachstanas',
        'code': u'7',
    },
    {
        'country': u'Kenija',
        'code': u'254',
    },
    {
        'country': u'Kinija',
        'code': u'86',
    },
    {
        'country': u'Kipras',
        'code': u'357',
    },
    {
        'country': u'Kirgizija',
        'code': u'996',
    },
    {
        'country': u'Kiribatis',
        'code': u'686',
    },
    {
        'country': u'Kolumbija',
        'code': u'57',
    },
    {
        'country': u'Komorai',
        'code': u'269',
    },
    {
        'country': u'Kongas',
        'code': u'242',
    },
    {
        'country': u'Kongo Demokratinė respublika',
        'code': u'243',
    },
    {
        'country': u'Kosta Rika',
        'code': u'506',
    },
    {
        'country': u'Kroatija',
        'code': u'385',
    },
    {
        'country': u'Kuba',
        'code': u'53',
    },
    {
        'country': u'Kuko salos',
        'code': u'682',
    },
    {
        'country': u'Kuveitas',
        'code': u'965',
    },
    {
        'country': u'Laosas',
        'code': u'856',
    },
    {
        'country': u'Latvija',
        'code': u'371',
    },
    {
        'country': u'Lenkija',
        'code': u'48',
    },
    {
        'country': u'Lesotas',
        'code': u'266',
    },
    {
        'country': u'Libanas',
        'code': u'961',
    },
    {
        'country': u'Liberija',
        'code': u'231',
    },
    {
        'country': u'Libija',
        'code': u'218',
    },
    {
        'country': u'Lichtenšteinas',
        'code': u'423',
    },
    {
        'country': u'Lietuva',
        'code': u'370',
        'regions': REGIONS_PHONE_CODES_LT,
        'regions_by_code': REGIONS_PHONE_CODES_LT_BY_CODE,
        'number_length_min': 11,
        'number_length_max': 11,
    },
    {
        'country': u'Liuksemburgas',
        'code': u'352',
    },
    {
        'country': u'Macao',
        'code': u'853',
    },
    {
        'country': u'Madagaskaras',
        'code': u'261',
    },
    {
        'country': u'Makedonija',
        'code': u'389',
    },
    {
        'country': u'Malaizija',
        'code': u'60',
    },
    {
        'country': u'Malavis',
        'code': u'265',
    },
    {
        'country': u'Maldyvai',
        'code': u'960',
    },
    {
        'country': u'Malis',
        'code': u'223',
    },
    {
        'country': u'Malta',
        'code': u'356',
    },
    {
        'country': u'Marokas',
        'code': u'212',
    },
    {
        'country': u'Maršalo salos',
        'code': u'692',
    },
    {
        'country': u'Martinika',
        'code': u'596',
    },
    {
        'country': u'Mauricijus',
        'code': u'230',
    },
    {
        'country': u'Mauritanija',
        'code': u'222',
    },
    {
        'country': u'Mayotte',
        'code': u'269',
    },
    {
        'country': u'Meksika',
        'code': u'52',
    },
    {
        'country': u'Mergelių salos (Britų)',
        'code': u'1284',
    },
    {
        'country': u'Mergelių salos (JAV)',
        'code': u'1340',
    },
    {
        'country': u'Mianmaras',
        'code': u'95',
    },
    {
        'country': u'Mikronezija',
        'code': u'691',
    },
    {
        'country': u'Moldova',
        'code': u'373',
    },
    {
        'country': u'Monakas',
        'code': u'377',
    },
    {
        'country': u'Mongolija',
        'code': u'976',
    },
    {
        'country': u'Montseratas',
        'code': u'1664',
    },
    {
        'country': u'Mozambikas',
        'code': u'258',
    },
    {
        'country': u'Namibija',
        'code': u'264',
    },
    {
        'country': u'Naujoji Kaledonija',
        'code': u'687',
    },
    {
        'country': u'Naujoji Zelandija',
        'code': u'64',
    },
    {
        'country': u'Nauru',
        'code': u'674',
    },
    {
        'country': u'Nepalas',
        'code': u'977',
    },
    {
        'country': u'Nigerija',
        'code': u'234',
    },
    {
        'country': u'Nigeris',
        'code': u'227',
    },
    {
        'country': u'Nikaragva',
        'code': u'505',
    },
    {
        'country': u'Niue sala',
        'code': u'683',
    },
    {
        'country': u'Norfolko sala',
        'code': u'672',
    },
    {
        'country': u'Norvegija',
        'code': u'47',
    },
    {
        'country': u'Olandija',
        'code': u'31',
    },
    {
        'country': u'Olandų Antilai',
        'code': u'599',
    },
    {
        'country': u'Omanas',
        'code': u'968',
    },
    {
        'country': u'Pakistanas',
        'code': u'92',
    },
    {
        'country': u'Palau',
        'code': u'680',
    },
    {
        'country': u'Panama',
        'code': u'507',
    },
    {
        'country': u'Papua ir Naujoji Gvinėja',
        'code': u'675',
    },
    {
        'country': u'Paragvajus',
        'code': u'595',
    },
    {
        'country': u'Peru',
        'code': u'51',
    },
    {
        'country': u'Pietų Afrikos Respublika',
        'code': u'27',
    },
    {
        'country': u'Pietų Korėja',
        'code': u'82',
    },
    {
        'country': u'Portugalija',
        'code': u'351',
    },
    {
        'country': u'Prancūzija',
        'code': u'33',
    },
    {
        'country': u'Prancūzijos Gviana',
        'code': u'594',
    },
    {
        'country': u'Prancūzijos Polinezija',
        'code': u'689',
    },
    {
        'country': u'Puerto Rikas',
        'code': u'1787',
    },
    {
        'country': u'Pusiaujo Gvinėja',
        'code': u'240',
    },
    {
        'country': u'Reunionas',
        'code': u'262',
    },
    {
        'country': u'Ruanda',
        'code': u'250',
    },
    {
        'country': u'Rytų Timoras',
        'code': u'670',
    },
    {
        'country': u'Vokietija',
        'code': u'49',
    }
    ]
