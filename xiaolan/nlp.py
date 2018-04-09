import sys
import os
import json
import 
        if intent == 1:
            if domain == 'train':
                arrival_city = r.json()['arrival_city']
                start_city = r.json()['start_city']
                start_station = r.json()['start_station']
                train_type = r.json()['train_type']
                return train_type, start_station, start_city, arrival_city
            elif domain == 'weather':
                date = r.json()['date']
                region = r.json()['region']
                return date
                return region
            elif domain == 'flight':
                start_date = r.json['start_date']
                start_city = r.json()['start_city']
                arrival_city = r.json()['arrival_city']
                airline = r.json()['airline']
                return airline, arrival_city, start_city, start_date
            elif domain == 'map':
                start = r.json()['start']
                arrival = r.json()['arrival']
                drive_sort = r.json()['drive_sort']
                route_type = r.json()[' route_type ']
                return route_type
                return drive_sort
                return arrival
                return start
            elif domain == 'telephone':
                name = r.json()['name']
                operator = r.json()['operator']
                location = r.json()['location']
                return name
                return operator
                return location
            elif domain == 'app':
                appname = r.json()['appname']
                return appname
            elif domain == 'website':
                sitename = r.json()['sitename']
                browser = r.json()['browser']
                return browser
                return sitename
            elif domain == 'music':
                name = r.json()['name']
                return name
            elif domain == 'joke':
                sence = r.json()['sence']
                audience = r.json()['audience']
                return sence
                return audience
            elif domian == 'instruction':
                inent = r.json()['intent']
                return inent
            else:
                tuling = 'tuling'
                return tuling
