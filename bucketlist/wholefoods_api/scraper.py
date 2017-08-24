# Importing the dependencies
# This is needed to create a lxml object that uses the css selector
import json

# The requests library
import requests
from lxml.etree import fromstring


class WholeFoodsScraper:
    API_url = 'http://www.wholefoodsmarket.com/views/ajax'
    scraped_stores = []

    def get_stores_info(self, page):
        # This is the only data required by the api
        # To send back the stores info
        data = {
            'view_name': 'store_locations_by_state',
            'view_display_id': 'state',
            'page': page
        }
        # Making the post request
        response = requests.post(self.API_url, data=data)

        # The data that we are looking is in the second
        # Element of the response and has the key 'data',
        # so that is what's returned
        return response.json()[1]['data']


        # get_store_info function

    def parse_stores(self, data, save=False):
        # Creating an lxml Element instance
        element = fromstring(data)

        for store in element.cssselect('.views-row'):
            store_info = {}
            # The lxml etree css selector always returns a list, so we get
            # just the first item
            try:
                store_image = store.cssselect('.views-field-field-storefront-image a img')[0].get('src')
            except IndexError:
                store_image = 'nope'
                continue

            try:
                store_name = store.cssselect('.views-field-title a')[0].text
                store_name = store_name.replace("'", "''")
            except IndexError:
                store_name = 'No name entered'
                continue

            try:
                street_address = store.cssselect('.street-block div')[0].text
            except IndexError:
                street_adress = 'No street address entered'
                continue

            try:
                address_locality = store.cssselect('.locality')[0].text
            except IndexError:
                address_locality = 'No locality'
                continue

            try:
                address_state = store.cssselect('.state')[0].text
            except IndexError:
                address_state = 'NO State'
                continue

            try:
                address_postal_code = store.cssselect('.postal-code')[0].text
                address_postal_code = filter(lambda x: x.isdigit(), address_postal_code)
            except IndexError:
                address_postal_code = 'NO ZIP CODE!'
                continue

            try:
                phone_number = store.cssselect('.views-field-field-phone-number div')[0].text
                # format the phone - strip all non numbers
                phone_number = filter(lambda x: x.isdigit(), phone_number)
            except IndexError:
                phone_number = 'NO PHONE NUMBER LISTED!'
                continue

            try:
                opening_hours = store.cssselect('.views-field-field-store-hours div')[0].text
            except IndexError:
                # Stores that doesn't have opening hours are closed and should not be saved.
                # This is found while debugging, so don't worry if you get errors when you
                # run a scraper
                opening_hours = 'STORE CLOSED'
                continue

            # now we add all the info to a dict
            try:
                storeid = store.cssselect('.views-field-nothing a')[0].get('href').split('/')[-1]
            except IndexError:
                storeid = 'none'
                continue
            store_info = {
                'storeid': storeid.encode('ascii', 'ignore'),
                'name': store_name.encode('ascii', 'ignore'),
                'phone': phone_number.encode('ascii', 'ignore'),
                'hours': str(opening_hours.encode('ascii', 'ignore')),
                'locality': address_locality.encode('ascii', 'ignore'),
                'state': address_state.encode('ascii', 'ignore'),
                'zipcode': address_postal_code.encode('ascii', 'ignore'),
                'store_image': store_image.encode('ascii', 'ignore')
            }

            from django.db import connection
            def my_custom_sql(store_info):
                print 'adding to db?'

                with connection.cursor() as cursor:
                    try:
                        query = "INSERT  INTO `wholefoods_api_wholefoodsstore`(`storeid`, `hours`, `phone`, `name`,  `locality`, `state`, `zipcode`, `store_image`) " \
                                "VALUES( '{0}', '{1}', '{2}', '{3}', '{4}' , '{5}' , '{6}' , '{7}')".format(
                            store_info['storeid'],
                            store_info['hours'],
                            store_info['phone'],
                            store_info['name'],
                            store_info['locality'],
                            store_info['state'],
                            store_info['zipcode'],
                            store_info['store_image'])
                        cursor.execute(query)
                    except:
                        print ('error ', store_info['name'], store_info['storeid'])

            if save:
                my_custom_sql(store_info)

            # We add the store to the scraped stores list
            self.scraped_stores.append(store_info)

    def run(self, start, end, save=False):
        start = int(start)
        end = int(end)
        for page in range(start, end):
            # Retrieving the data
            data = self.get_stores_info(page)
            # Parsing it
            self.parse_stores(data, save)
            print('scraped the page' + str(page))
        if save:
            self.save_data()

    def save_data(self):
        with open('wholefoods_api/wholefoods_stores.json', 'w') as json_file:
            json.dump(self.scraped_stores, json_file, indent=4)

    def open_data(self):
        return (self.scraped_stores)
