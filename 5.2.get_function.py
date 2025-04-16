def get(dictionary, key, default=None):
    if key in dictionary:
        return dictionary[key]
    return default


if __name__ == '__main__':
    ghibli_release_dates = {
        'Castle in the Sky': '1986-08-02',
        'My Neighbor Totoro': '1988-04-16',
        'Spirited Away': '2001-07-20',
        'Ponyo': '2008-07-19',
    }

    print(get(ghibli_release_dates, 'Ponyo'))                     # 2008-07-19
    print(get(ghibli_release_dates, 'Men in Black'))              # None
    print(get(ghibli_release_dates, 'Men in Black', '???'))       # ???
