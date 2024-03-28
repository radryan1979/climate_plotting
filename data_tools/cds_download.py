# Request builder for CDS API

import cdsapi
import os

class RequestBuilder(object):
    
    
    
    def __init__(self):
        self.product_type = 'reanalysis'
        self.level_type = 'single'
        self.format = 'netcdf'
        self.month = [
            '01', '02', '03',
            '04', '05', '06',
            '07', '08', '09',
            '10', '11', '12',
        ]
        self.day = [
            '01', '02', '03',
            '04', '05', '06',
            '07', '08', '09',
            '10', '11', '12',
            '13', '14', '15',
            '16', '17', '18',
            '19', '20', '21',
            '22', '23', '24',
            '25', '26', '27',
            '28', '29', '30',
            '31',
        ]
        self.times = [
            '00:00', '06:00', '12:00',
            '18:00',
        ]
        self.pressure_levels = []
        self.year = ''
        self.area = []
        self.save_folder = ''
        self.file_name = ''
        
    def buildRequest(self):
        '''
        Creates a cds   api request dictionary to submit to the client
        '''
        
        
    def submitRequest(self):
        '''
        Submits the request dictionary to CDI's API using
        the cdsapi library
        '''
        
    
    
        







c = cdsapi.Client()

