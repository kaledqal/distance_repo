import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','QuickProject.settings')

import django
django.setup()

from hello_world.models import Iata
records = None
with open('airport_lat_long.txt','r') as recs:
    records = recs.read().split('\n')
    records.pop()#the last record is a blank tring so i remove that
    print("{l} Records where retrieved from the file ".format(l=len(records)))


def add_record():
    for i in range(1,len(records)):
        data = records[i].split(',')
        code = data[0]
        lat = float(data[1])
        lngtd = float(data[2])
        iata = Iata.objects.get_or_create(iata_code=code,lat=lat,lng=lngtd)[0]
        iata.save()




if __name__ == '__main__':
    print('Importing records from file into Database...')
    add_record()
    print('Importing complete')
