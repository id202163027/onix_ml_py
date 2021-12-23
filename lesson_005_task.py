import urllib.request, csv, sqlite3

def main():

    url = 'https://worldweather.wmo.int/en/json/full_city_list.txt'
    db_name = 'database.db'

    # read data from source
    with urllib.request.urlopen(url) as response:
        response = response.read().decode('UTF-8').splitlines()
    
        # exclude 2 last lines with updatedate
        file = response[:-2]
    
        # data is semicolon-delimited
        csv.register_dialect('semicolon-delimited', delimiter=';')
        csv_reader = csv.DictReader(file, dialect='semicolon-delimited')
    
        # dict with cities data from source for db
        data = [row for row in csv_reader]
    
    # create db
    con = sqlite3.connect(db_name)
    cur = con.cursor()

    # create table with unique index (country,city)
    sql_init = """\
    CREATE TABLE IF NOT EXISTS city (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        country TEXT,
        city TEXT,
        city_id INTEGER);
    CREATE UNIQUE INDEX unique_city_id ON city (country,city);
    """
    # push data to db
    sql_push = """\
    INSERT INTO city (country, city, city_id) VALUES(:Country, :City, :CityId)
    """
    try:
        cur.executescript(sql_init)
        cur.executemany(sql_push, data)
    except sqlite3.DatabaseError as err:
        print ('Error:', err)
    else:
        print('Success!')
        con.commit()
    
    cur.close()
    con.close()

main()

def update(country, city, city_id=None):
    """This function make update city_id in database.db. 
    Args:
        country (str): country of the city.
        city (str): city.
        city_id (int): city id by WWIS. Defaults to None.
    Returns:
        list: all fields for pair (country,city). Return current state if city_id is missing.
    """
    
    db_name = 'database.db'
    con = sqlite3.connect(db_name)
    cur = con.cursor()
    try:
        if city_id is not None:
            # insert or ignore in case pair (country,city) present in table
            cur.execute('INSERT OR IGNORE INTO city (country, city, city_id) VALUES (?, ?, ?)', \
                        (country, city, city_id))
            # update city_id
            cur.execute('UPDATE city SET city_id = ?  WHERE country = ? AND city = ?', \
                        (city_id, country, city))
        # current state for city
        r = cur.execute('SELECT * FROM city WHERE  country = ? AND city = ?', \
                        (country, city)).fetchall()
    except sqlite3.DatabaseError as err:
        print ('Error:', err)
    else:
        con.commit()
        return r
    cur.close()
    con.close()