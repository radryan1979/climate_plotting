# Request builder for CDS API

import cdsapi
import os

class RequestBuilder(object):
    '''
    Tool to help build CDS API requests and submit them.
    
    Attributes
    ----------
    product_type : str
        options include reanalysis
    level_type : str 
        single or pressure
    format : str
        netcdf or grib
    month : list
        1 through 12 by default
    day : list
        1 through 31 by default
    times : list
        hours 00, 06, 12, 18 by default
    pressure_levels : list
        None by default
    year : str
    
        
        
    Methods
    -------
    
    '''
    
    
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
        self.pressure_levels = None
        self.year = None
        self.area = [90, -180, -90, 180]
        self.save_folder = None
        self.file_name = None
        
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

