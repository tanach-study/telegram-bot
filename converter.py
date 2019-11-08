# parasha

parasha_to_sefer = {
    'bereshit': 'bereshit',
    'noah': 'bereshit',
    'lech lecha': 'bereshit',
    'vayera': 'bereshit',
    'haye sarah': 'bereshit',
    'toledot': 'bereshit',
    'vayetze': 'bereshit',
    'vayishlah': 'bereshit'
}

sefer_to_parasha = {
    'bereshit': [
        'bereshit',
        'noah',
        'lech lecha',
        'vayera',
        'haye sarah',
        'toledot',
        'vayetze',
        'vayishlah',
    ]
}

masechet_to_seder = {
    'berachot': 'zeraim',
    'peah': 'zeraim',
    'demai': 'zeraim',
    'kilayim': 'zeraim',
    'sheviit': 'zeraim',
    'terumot': 'zeraim',
    'maasrot': 'zeraim',
    'maaser sheni': 'zeraim',
    'halla': 'zeraim',
    'orla': 'zeraim',
    'bikurim': 'zeraim',
    'shabbat': 'moed',
    'eruvin': 'moed',
    'pesahim': 'moed',
    'shekalim': 'moed',
    'yoma': 'moed',
    'sukka': 'moed',
    'beitza': 'moed',
    'rosh hashana': 'moed',
    'taanit': 'moed',
    'megilla': 'moed',
    'moed katan': 'moed',
    'hagiga': 'moed',
    'yevamot': 'nashim',
    'ketubot': 'nashim',
    'nedarim': 'nashim',
    'nazir': 'nashim',
    'sota': 'nashim',
    'gittin': 'nashim',
    'kidushin': 'nashim',
    'bava kamma': 'nezikin',
    'bava metzia': 'nezikin',
    'bava batra': 'nezikin',
    'sanhedrin': 'nezikin',
    'makkot': 'nezikin',
    'shevuot': 'nezikin',
    'eduyot': 'nezikin',
    'avoda zara': 'nezikin',
    'avot': 'nezikin',
    'horayot': 'nezikin',
    'zevahim': 'kadashim',
    'menahot': 'kadashim',
    'hullin': 'kadashim',
    'bechorot': 'kadashim',
    'arachin': 'kadashim',
    'temura': 'kadashim',
    'keritot': 'kadashim',
    'meila': 'kadashim',
    'tamid': 'kadashim',
    'middot': 'kadashim',
    'kinnim': 'kadashim',
    'kelim': 'taharot',
    'ohalot': 'taharot',
    'negaim': 'taharot',
    'para': 'taharot',
    'taharot': 'taharot',
    'mikvaot': 'taharot',
    'nidda': 'taharot',
    'machshirin': 'taharot',
    'zavim': 'taharot',
    'tevul yom': 'taharot',
    'yadayim': 'taharot',
    'oktzin': 'taharot',
}

seder_to_masechet = {
    'zeraim': [
        'berachot',
        'peah',
        'demai',
        'kilayim',
        'sheviit',
        'terumot',
        'maasrot',
        'maaser sheni',
        'halla',
        'orla',
        'bikurim',
    ],
    'moed': [
        'shabbat',
        'eruvin',
        'pesahim',
        'shekalim',
        'yoma',
        'sukka',
        'beitza',
        'rosh hashana',
        'taanit',
        'megilla',
        'moed katan',
        'hagiga',
    ],
    'nashim': [
        'yevamot',
        'ketubot',
        'nedarim',
        'nazir',
        'sota',
        'gittin',
        'kidushin',
    ],
    'nezikin': [
        'bava kamma',
        'bava metzia',
        'bava batra',
        'sanhedrin',
        'makkot',
        'shevuot',
        'eduyot',
        'avoda zara',
        'avot',
        'horayot',
    ],
    'kadashim': [
        'zevahim',
        'menahot',
        'hullin',
        'bechorot',
        'arachin',
        'temura',
        'keritot',
        'meila',
        'tamid',
        'middot',
        'kinnim',
    ],
    'taharot': [
        'kelim',
        'ohalot',
        'negaim',
        'para',
        'taharot',
        'mikvaot',
        'nidda',
        'machshirin',
        'zavim',
        'tevul yom',
        'yadayim',
        'oktzin',
    ]
}


def get_sefer_from_parasha(parasha, pretty = False):
    global parasha_to_sefer
    p = parasha.lower()
    sefer = parasha_to_sefer[p]
    if pretty:
        return sefer.title()
    return sefer


def get_parashot_from_sefer(sefer, pretty = False):
    global sefer_to_parasha
    s = sefer.lower()
    parashot = sefer_to_parasha[s]
    if pretty:
        return [p.title() for p in parashot]
    return parashot


def get_seder_from_masechet(masechet, pretty = False):
    global masechet_to_seder
    m = masechet.lower()
    seder = masechet_to_seder[m]
    if pretty:
        return seder.title()
    return seder


def get_masechtot_from_seder(seder, pretty = False):
    global seder_to_masechet
    s = seder.lower()
    masechet = seder_to_masechet[s]
    if pretty:
        return masechet.title()
    return masechet

