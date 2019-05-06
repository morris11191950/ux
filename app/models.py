from app import db
from flask import session

#usrDatabases = session['usrDatabases']

class Queries():

    def __init__(self):
        try:
            conn = db.connect()
        except cursor.Error as e:
            print("Error %d: %s" % (e.args[0], e.args[1]))
            sys.exit(1)
        self.conn = conn

#######################################################################
# CATEGORIES ALL
######################################################################
    def categories_all(self):

        json_categories = []
        cursor = self.conn.cursor()
        sql = """SELECT category_id, category_description
            FROM category
            ORDER BY category_description"""
        cursor.execute(sql)
        self.conn.close()
        rows = cursor.fetchall()
        #Convert to JSON format
        for row in rows:
            json_category = {'category_id': row[0], 'category_description': row[1]}
            json_categories.append(json_category)
            json_category = {}
        return json_categories

#######################################################################
# SPECIAL COLLECTIONS ALL
######################################################################
    def specialCollections_all(self):
        json_specialCollections = []
        cursor = self.conn.cursor()
        sql = """SELECT spcol_id, spcol_description
            FROM special_collection
            ORDER BY spcol_description"""
        cursor.execute(sql)
        self.conn.close()
        rows = cursor.fetchall()
        #Convert to JSON format
        for row in rows:
            json_specialCollection = {'spcol_id': row[0], 'spcol_description': row[1]}
            json_specialCollections.append(json_specialCollection)
            json_specialCollection = {}
        return json_specialCollections

#######################################################################
# DISTRICTS ALL
######################################################################
    def districts_all(self):
        json_districts = []
        cursor = self.conn.cursor()
        sql = """SELECT district_id, district_name
        FROM district
        ORDER BY district_name """
        cursor.execute(sql)
        self.conn.close()
        rows = cursor.fetchall()
        #Convert to JSON format
        for row in rows:
            json_district = {'district_id': row[0], 'district_name': row[1]}
            json_districts.append(json_district)
            json_district = {}
        return json_districts

#######################################################################
# DATABASES ALL
######################################################################
    def databases_all(self):
        json_databases = []
        cursor = self.conn.cursor()
        sql = """SELECT DISTINCT database_name
        FROM deposit
        ORDER BY database_name """
        cursor.execute(sql)
        self.conn.close()
        rows = cursor.fetchall()
        #Convert to JSON format
        for row in rows:
            json_database = {'database_name': row[0]}
            json_databases.append(json_database)
            json_database = {}
        return json_databases

#######################################################################
# COUNTIES ALL
######################################################################
    def counties_all(self):
        json_counties = []
        cursor = self.conn.cursor()
        sql = """SELECT c.county_id, c.county, s.state_id, s.state
        FROM county c
        INNER JOIN state s ON s.state_id = c.state_id
        ORDER BY s.state """
        cursor.execute(sql)
        self.conn.close()
        rows = cursor.fetchall()
        #print('County rows ', rows)
        #Convert to JSON format
        for row in rows:
            json_county = {'county_id': row[0], 'county': row[1], 'state_id':row[2], 'state':row[3]}
            json_counties.append(json_county)
            json_county = {}
        return json_counties

#######################################################################
# DEPOSITS ALL
######################################################################
    def deposits_all(self):

        usrDatabases = session['usrDatabases']
        if usrDatabases is None:
            usrDatabases = ['SJM']

        sql_parms = usrDatabases
        format_strings = ','.join(['%s'] * len(usrDatabases))

        json_deposits = []
        cursor = self.conn.cursor()
        #BOGS DOWN IF TOO MANY DEPOSITS, MUST LIMIT SELECTION
        sql = """SELECT deposit_id, deposit_name
        FROM deposit
        WHERE database_name IN ({db_list})
        ORDER BY deposit_name """.format(db_list=format_strings)

        cursor.execute(sql, sql_parms)
        self.conn.close()
        rows = cursor.fetchall()
        #print('Deposit models rows ')
        #Convert to JSON format
        for row in rows:
            json_deposit = {'deposit_id': row[0], 'deposit_name': row[1]}
            json_deposits.append(json_deposit)
            json_deposit = {}
        return json_deposits

#######################################################################
# DEPOSITS BY DISTRICT
######################################################################
    def deposits_by_district(self, district_id):

        usrDatabases = session['usrDatabases']
        if usrDatabases is None:
            usrDatabases = ['SJM']

        district_id_str = str(district_id)
        sql_parms = [district_id_str]
        sql_parms.extend(usrDatabases)
        format_strings = ','.join(['%s'] * len(usrDatabases))
        #print('Model/deposits_by_district (format_strings) ', format_strings)

        json_deposits = []
        cursor = self.conn.cursor()
        sql = """SELECT DISTINCT d.deposit_id, d.deposit_name,
                d.latitude, d.longitude, s.state,
                c1.country, c2.county, dis.district_name,
                p.pounds_u3o8, p.grade, d.database_name
            FROM deposit d
            LEFT JOIN district_to_deposit dd
                ON dd.deposit_id = d.deposit_id
            INNER JOIN district dis ON dis.district_id = dd.district_id
            LEFT JOIN state s ON s.state_id = d.state_id
            LEFT JOIN country c1 ON c1.country_id = d.country_id
            LEFT JOIN county c2 ON c2.county_id = d.county_id
            LEFT JOIN production p ON p.deposit_id = d.deposit_id
            WHERE dd.district_id = %s AND d.database_name IN ({db_list})
            ORDER BY d.deposit_id """ .format(db_list=format_strings)

        cursor.execute(sql, sql_parms)
        self.conn.close()
        rows = cursor.fetchall()
        #Convert to JSON format
        for row in rows:
            json_deposit = {'deposit_id':row[0], 'deposit_name':row[1],
                'latitude':row[2], 'longitude':row[3],
                'state':row[4], 'country':row[5], 'county':row[6],
                'district_name':row[7], 'pounds_u3o8':row[8], 'grade':row[9], 'database_name':row[10]}
            json_deposits.append(json_deposit)
            json_deposit = {}

        return json_deposits

#######################################################################
# DEPOSITS BY DATABASE
######################################################################
    def deposits_by_database(self, databaseName):
        json_deposits = []
        cursor = self.conn.cursor()
        sql = """SELECT DISTINCT d.deposit_id, d.deposit_name,
                d.latitude, d.longitude, s.state,
                c1.country, c2.county, dis.district_name,
                p.pounds_u3o8, p.grade
            FROM deposit d
            LEFT JOIN district_to_deposit dd
                ON dd.deposit_id = d.deposit_id
            LEFT JOIN district dis ON dis.district_id = dd.district_id
            LEFT JOIN state s ON s.state_id = d.state_id
            LEFT JOIN country c1 ON c1.country_id = d.country_id
            LEFT JOIN county c2 ON c2.county_id = d.county_id
            LEFT JOIN production p ON p.deposit_id = d.deposit_id
            WHERE (d.database_name = %s)
            ORDER BY d.deposit_name """
        #print('Models: SQL ', sql)
        cursor.execute(sql, databaseName)
        self.conn.close()
        rows = cursor.fetchall()
        #Convert to JSON format
        for row in rows:
            json_deposit = {'deposit_id':row[0], 'deposit_name':row[1],
                'latitude':row[2], 'longitude':row[3],
                'state':row[4], 'country':row[5], 'county':row[6],
                'district_name':row[7], 'pounds_u3o8':row[8], 'grade':row[9]}
            json_deposits.append(json_deposit)
            json_deposit = {}

        return json_deposits

#######################################################################
# DEPOSITS BY COUNTY
######################################################################
    def deposits_by_county(self, county_id, state_id):
        #print('type county_id ', type(county_id))
        usrDatabases = session['usrDatabases']
        if usrDatabases is None:
            usrDatabases = ['SJM']

        county_id = str(county_id)
        state_id = str(state_id)
        sql_parms = [county_id, state_id]
        sql_parms.extend(usrDatabases)
        format_strings = ','.join(['%s'] * len(usrDatabases))

        json_deposits = []
        cursor = self.conn.cursor()
        sql = """SELECT DISTINCT d.deposit_id, d.deposit_name,
                d.latitude, d.longitude, s.state,
                c1.country, c.county,
                p.pounds_u3o8, p.grade, d.database_name
            FROM deposit d
            LEFT JOIN county c ON c.county_id = d.county_id
            LEFT JOIN state s ON s.state_id = d.state_id
            LEFT JOIN country c1 ON c1.country_id = d.country_id
            LEFT JOIN production p ON p.deposit_id = d.deposit_id
            WHERE c.county_id = %s AND s.state_id = %s AND d.database_name IN ({db_list})
            ORDER BY d.deposit_id """.format(db_list=format_strings)
        #print('SQL ', sql)
        #print('county_id, state_id ', county_id,  ' ', state_id)
        cursor.execute(sql, sql_parms)
        #print('SQL executed')
        self.conn.close()
        rows = cursor.fetchall()
        #Convert to JSON format
        for row in rows:
            json_deposit = {'deposit_id':row[0], 'deposit_name':row[1],
                'latitude':row[2], 'longitude':row[3],
                'state':row[4], 'country':row[5], 'county':row[6],
                'pounds_u3o8':row[7], 'grade':row[8], 'database_name':row[9]}
            json_deposits.append(json_deposit)
            json_deposit = {}

        return json_deposits

#######################################################################
# DEPOSITS BY DEPOSIT
######################################################################
    def deposits_by_deposit(self, deposit_ids):
        #GET INDIVIDUAL IDS AS ARRAY OF STRINGS
        list_of_ids = deposit_ids.split('!')
        list_of_ids.remove('')
        #print('list_of_ids ', list_of_ids, ' ', type(list_of_ids))
        format_strings = ','.join(['%s'] * len(list_of_ids))
        #print('format_strings ', format_strings)
        tuple_of_ids = tuple(list_of_ids)
        json_deposits = []
        cursor = self.conn.cursor()
        sql = """SELECT DISTINCT d.deposit_id, d.deposit_name,
                d.latitude, d.longitude, s.state,
                c1.country, c2.county,
                p.pounds_u3o8, p.grade, d.database_name
            FROM deposit d
            LEFT JOIN state s ON s.state_id = d.state_id
            INNER JOIN country c1 ON c1.country_id = d.country_id
            LEFT JOIN county c2 ON c2.county_id = d.county_id
            LEFT JOIN production p ON p.deposit_id = d.deposit_id
            WHERE (d.deposit_id IN (%s))
            ORDER BY d.deposit_id """ % format_strings
        #print('SQL in models ', sql)
        cursor.execute(sql, tuple_of_ids)
        #cursor.execute(sql, deposit_ids)
        self.conn.close()
        rows = cursor.fetchall()
        #print('rows in models ', rows)
        #Convert to JSON format
        for row in rows:
            json_deposit = {'deposit_id':row[0], 'deposit_name':row[1],
                'latitude':row[2], 'longitude':row[3],
                'state':row[4], 'country':row[5], 'county':row[6],
                'pounds_u3o8':row[7], 'grade':row[8], 'database_name':row[9]}
            json_deposits.append(json_deposit)
            json_deposit = {}

        return json_deposits

######################################################################
# DEPOSITS SEARCH
######################################################################
    def deposits_search(self, usrFrag):
        #print('Models usrFrag: ', usrFrag)
        json_deposits = []
        cursor = self.conn.cursor()
        usrFragSQL1 = '%' + '' + '%'
        usrFragSQL2 = '%' + '' + '%'
        usrFragSQL3 = '%' + '' + '%'
        usrFragSplit = usrFrag.split(',')
        #print('Models usrFragSplit: ', usrFragSplit)
        if len(usrFragSplit) == 1:
            usrFragSQL1 = '%' + usrFragSplit[0] + '%'
        if len(usrFragSplit) == 2:
            usrFragSQL1 = '%' + usrFragSplit[0] + '%'
            usrFragSQL2 = '%' + usrFragSplit[1] + '%'
        if len(usrFragSplit) == 3:
            usrFragSQL1 = '%' + usrFragSplit[0] + '%'
            usrFragSQL2 = '%' + usrFragSplit[1] + '%'
            usrFragSQL3 = '%' + usrFragSplit[2] + '%'
        #print('Models usrFragSQLs: ', usrFragSQL1, usrFragSQL2, usrFragSQL3)
        sql = """SELECT DISTINCT d.deposit_id, d.deposit_name,
                d.latitude, d.longitude, s.state,
                c1.country, c.county, dis.district_name,
                p.pounds_u3o8, p.grade, d.database_name
            FROM deposit d
            LEFT JOIN district_to_deposit dd
                ON dd.deposit_id = d.deposit_id
            LEFT JOIN district dis ON dis.district_id = dd.district_id
            LEFT JOIN county c ON c.county_id = d.county_id
            LEFT JOIN state s ON s.state_id = d.state_id
            LEFT JOIN country c1 ON c1.country_id = d.country_id
            LEFT JOIN production p ON p.deposit_id = d.deposit_id
            WHERE (d.deposit_name like %s and d.deposit_name like %s and d.deposit_name like %s)
            ORDER BY d.deposit_name """
        #print('sql: ', sql)
        cursor.execute(sql, (usrFragSQL1, usrFragSQL2, usrFragSQL3))
        #print('sql2: ', sql)
        self.conn.close()
        rows = cursor.fetchall()
        #Convert to JSON format
        for row in rows:
            json_deposit = {'deposit_id':row[0], 'deposit_name':row[1],
                'latitude':row[2], 'longitude':row[3],
                'state':row[4], 'country':row[5], 'county':row[6],
                'district_name':row[7], 'pounds_u3o8':row[8], 'grade':row[9], 'database_name':row[10]}
            json_deposits.append(json_deposit)
            json_deposit = {}

        return json_deposits

#######################################################################
# REFERENCES ALL
######################################################################
    def references_all(self):
        json_refs = []
        cursor = self.conn.cursor()
        sql = """SELECT reference_id, reference, filename, url
            FROM reference
            ORDER BY reference """
        cursor.execute(sql)
        self.conn.close()
        rows = cursor.fetchall()
        #Convert to JSON format
        for row in rows:
            json_ref = {'reference_id': row[0], 'reference': row[1],
                'filename': row[2], 'url': row[3]}
            json_refs.append(json_ref)
            json_ref = {}
        return json_refs

#######################################################################
# REFERENCES BY DISTRICT
######################################################################
    def references_by_district(self, district_id):
        json_refs = []
        cursor = self.conn.cursor()
        sql = """SELECT r.reference_id, r.reference, r.filename, r.url
            FROM reference r
            INNER JOIN district_to_reference d ON d.reference_id = r.reference_id
            WHERE d.district_id = %s
            ORDER BY r.reference """
        cursor.execute(sql, district_id)
        self.conn.close()
        rows = cursor.fetchall()
        #Convert to JSON format
        for row in rows:
            json_ref = {'reference_id': row[0], 'reference': row[1],
                'filename': row[2], 'url': row[3]}
            json_refs.append(json_ref)
            json_ref = {}
        return json_refs

#######################################################################
# REFERENCES BY CATEGORY
######################################################################
    def references_by_category(self, category_id):
        json_refs = []
        cursor = self.conn.cursor()
        sql = """SELECT r.reference_id, r.reference, r.filename, r.url
            FROM reference r
            INNER JOIN category_to_reference c ON c.reference_id = r.reference_id
            WHERE c.category_id = %s
            ORDER BY r.reference """
        cursor.execute(sql, category_id)
        self.conn.close()
        rows = cursor.fetchall()
        #print('Category rows ', rows)
        #Convert to JSON format
        for row in rows:
            json_ref = {'reference_id': row[0], 'reference': row[1],
                'filename': row[2], 'url': row[3]}
            json_refs.append(json_ref)
            json_ref = {}
        return json_refs

#######################################################################
# REFERENCES BY SPECIALCOLLECTION
######################################################################
    def references_by_specialCollection(self, spcol_id):
        #print('spcol_id is: ', spcol_id)
        json_refs = []
        cursor = self.conn.cursor()
        sql = """SELECT r.reference_id, r.reference, r.filename, r.url
            FROM reference r
            INNER JOIN specialcollection_to_reference sc
                ON sc.reference_id = r.reference_id
            WHERE sc.spcol_id = %s
            ORDER BY r.reference """
        cursor.execute(sql, spcol_id)
        self.conn.close()
        rows = cursor.fetchall()
        #Convert to JSON format
        for row in rows:
            json_ref = {'reference_id': row[0], 'reference': row[1],
                'filename': row[2], 'url': row[3]}
            json_refs.append(json_ref)
            json_ref = {}
        return json_refs

#######################################################################
# REFERENCES SEARCH
######################################################################
    def references_search(self, usrFrag):
        json_refs = []
        cursor = self.conn.cursor()
        usrFragSQL1 = '%' + '' + '%'
        usrFragSQL2 = '%' + '' + '%'
        usrFragSQL3 = '%' + '' + '%'
        usrFragSplit = usrFrag.split(',')
        # print(usrFragSplit)
        if len(usrFragSplit) == 1:
            usrFragSQL1 = '%' + usrFragSplit[0] + '%'
        if len(usrFragSplit) == 2:
            usrFragSQL1 = '%' + usrFragSplit[0] + '%'
            usrFragSQL2 = '%' + usrFragSplit[1] + '%'
        if len(usrFragSplit) == 3:
            usrFragSQL1 = '%' + usrFragSplit[0] + '%'
            usrFragSQL2 = '%' + usrFragSplit[1] + '%'
            usrFragSQL3 = '%' + usrFragSplit[2] + '%'
        sql = """SELECT reference_id, reference, filename, url
                    FROM reference
                    WHERE (reference like %s and reference like %s and reference like %s)
                    ORDER BY reference """
        cursor.execute(sql, (usrFragSQL1, usrFragSQL2, usrFragSQL3))
        self.conn.close()
        rows = cursor.fetchall()
        #Convert to JSON format
        for row in rows:
            json_ref = {'reference_id': row[0], 'reference': row[1],
                'filename': row[2], 'url': row[3]}
            #json_ref = {'reference_id': row[0], 'reference': row[1]}
            json_refs.append(json_ref)
            json_ref = {}
        return json_refs
#######################################################################
# REFERENCE - EDIT PAGE FOR ALL DISTRICTS
######################################################################
    def districts_by_reference(self, refid):
        json_refs = []
        cursor = self.conn.cursor()
        sql = """SELECT r.district_id, d.district_name
            FROM district_to_reference r
            INNER JOIN district d ON d.district_id = r.district_id
            WHERE r.reference_id = %s """
        cursor.execute(sql, refid)
        self.conn.close()
        rows = cursor.fetchall()
        #Convert to JSON format
        for row in rows:
            json_ref = {'district_id': row[0], 'district_name': row[1]}
            json_refs.append(json_ref)
            json_ref = {}
        return json_refs

#######################################################################
# REFERENCE - EDIT PAGE FOR CATEGORIES
######################################################################
    def categories_by_reference(self, refid):
        json_refs = []
        cursor = self.conn.cursor()
        #print('in models ', refid)
        sql = """SELECT r.category_id, c.category_name, c.category_description
            FROM category_to_reference r
            INNER JOIN category c ON c.category_id = r.category_id
            WHERE r.reference_id = %s """
        cursor.execute(sql, refid)
        self.conn.close()
        rows = cursor.fetchall()
        #Convert to JSON format
        for row in rows:
            #print('category row1  ', row[1])
            json_ref = {'category_id': row[0],
                'category_name': row[1], 'category_description': row[2]}
            json_refs.append(json_ref)
            json_ref = {}
        return json_refs

#######################################################################
# REFERENCE - EDIT PAGE FOR SPECIIAL COLLECTIONS
######################################################################
    def specialCollections_by_reference(self, refid):
        json_refs = []
        cursor = self.conn.cursor()
        #print('in models ', refid)
        sql = """SELECT r.spcol_id, s.spcol_name, s.spcol_description
            FROM specialCollection_to_reference r
            INNER JOIN special_collection s ON s.spcol_id = r.spcol_id
            WHERE r.reference_id = %s """
        cursor.execute(sql, refid)
        self.conn.close()
        rows = cursor.fetchall()
        #Convert to JSON format
        for row in rows:
            #print('category row1  ', row[1])
            json_ref = {'special_id': row[0],
                'special_name': row[1], 'special_description': row[2]}
            json_refs.append(json_ref)
            json_ref = {}
        return json_refs

#######################################################################
# REFERENCE - EDIT PAGE FOR ALL REFERENCES
######################################################################
    def references_edit(self, id):
        json_refs = []
        cursor = self.conn.cursor()
        sql = """SELECT *
            FROM reference
            WHERE reference_id = %s"""
        cursor.execute(sql, id)
        self.conn.close()
        rows = cursor.fetchall()
        #Convert to JSON format
        for row in rows:
            json_ref = {'reference_id': row[0], 'reference': row[1],
                'source': row[2], 'verified': row[3], 'filename': row[4],
                'url': row[5], 'section': row[6]}
            json_refs.append(json_ref)
            json_ref = {}
        return json_refs

    #######################################
    # REFERENCE EDIT - UPDATE DATABASE
    #######################################
    def references_edit_submit(self, refid, reference, source, filename, url, yn):

        cursor = self.conn.cursor()
        sql = """UPDATE reference
            SET reference = %s, source = %s, filename = %s, url = %s, verified = %s
            WHERE reference_id = %s"""
        cursor.execute(sql, (reference, source, filename, url, yn, refid))
        self.conn.close()

    def references_edit_new(self, reference, source, filename, url, yn):
        # Get a new reference_id
        cursor = self.conn.cursor()
        sql = """SELECT MAX(reference_id)
           FROM reference"""
        cursor.execute(sql)
        tup = cursor.fetchone()
        refid = str(tup[0] + 1)
        # Insert main dta for new reference
        sql = """INSERT
                INTO reference (reference_id, reference, source, filename, url, verified)
                VALUES(%s, %s, %s, %s, %s, %s)"""
        cursor.execute(sql, (refid, reference, source, filename, url, yn))
        self.conn.commit()
        self.conn.close()
        cursor.close()

        return refid

    def references_edit_delete(self, refid):

        #print("models: refid ", refid)
        cursor = self.conn.cursor()
        # Delete the current reference
        sql = """DELETE
                FROM reference
                WHERE reference_id = %s """
        #print("models: refid ", refid)
        cursor.execute(sql, refid)
        self.conn.commit()
        sql = """DELETE
                FROM district_to_reference
                WHERE reference_id = %s """
        cursor.execute(sql, refid)
        self.conn.commit()
        sql = """DELETE
                FROM category_to_reference
                WHERE reference_id = %s """
        cursor.execute(sql, refid)
        self.conn.commit()
        self.conn.close()
        cursor.close()


    def references_edit_submit_districts(self, refid, district_ids):
        #print('in models, district_ids ', district_ids)
        cursor = self.conn.cursor()
        sql = """DELETE
           FROM district_to_reference
           WHERE reference_id = %s """
        cursor.execute(sql, (refid))
        self.conn.commit()

        for district_id in district_ids:
             sql = """INSERT IGNORE
                INTO district_to_reference (district_id, reference_id)
                VALUES(%s, %s)"""
             cursor.execute(sql, (district_id, refid))
             self.conn.commit()
        cursor.close()

    def references_edit_submit_categories(self, refid, category_ids):
        #print('in models, category_ids ', category_ids)
        cursor = self.conn.cursor()
        sql = """DELETE
           FROM category_to_reference
           WHERE reference_id = %s """
        cursor.execute(sql, (refid))
        self.conn.commit()

        for category_id in category_ids:
             sql = """INSERT IGNORE
                INTO category_to_reference (category_id, reference_id)
                VALUES(%s, %s)"""
             cursor.execute(sql, (category_id, refid))
             self.conn.commit()
        cursor.close()

    def references_edit_submit_specials(self, refid, special_ids):
        #print('in models: refid, special_ids ', refid, special_ids)
        cursor = self.conn.cursor()
        sql = """DELETE
           FROM specialCollection_to_reference
           WHERE reference_id = %s """
        cursor.execute(sql, (refid))
        self.conn.commit()

        for special_id in special_ids:
             sql = """INSERT IGNORE
                INTO specialCollection_to_reference (spcol_id, reference_id)
                VALUES(%s, %s)"""
             cursor.execute(sql, (special_id, refid))
             self.conn.commit()
        cursor.close()

#######################################################################
# REFERENCE DISPLAY PDFS
######################################################################
    def url_pdf(self, id):
        json_refs = []
        cursor = self.conn.cursor()
        sql = """SELECT url, filename,
            CASE
                WHEN filename IS NOT NULL AND filename != 'None' AND filename != ''
                    THEN CONCAT('/static/pdfs/', filename)
                WHEN url IS NOT NULL AND url != 'None' AND url != '' THEN url
            END AS path
            FROM reference
            WHERE reference_id = %s
                AND ((url IS NOT NULL and url != 'None' and url != '')
                    OR (filename IS NOT NULL and filename != 'None' and filename != ''))"""
        cursor.execute(sql, id)
        self.conn.close()
        row = cursor.fetchone()
        #print('in models: row[2] ', row[2])
        #Convert to JSON format
        json_ref = {'url': row[2]}
        return json_ref
