import datetime
import statistics

class PreySample:
    def __init__(self, full_species_name, delta13c_list, tissue_description, sample_date_utc):
        self.full_species_name = full_species_name
        self.delta13c_list = delta13c_list
        self.tissue_description = tissue_description
        self.sample_date_utc = sample_date_utc
        
    @property
    def get_common_name(self):
        return self.full_species_name.split(' (',) [0])
        
    def get_scientific_name(self):
        return self.full_species_name.split(')') [1])
        
    def get_average_delta13c(self):
        return self.statistics.mean(self.delta13c_list)
        
    def get_tissue_count(self):
        return self.len(self.tissue_description)
        
    def get_sample_date(self):
        return self.datetime.datetime.strptime(sample_date_utc, format: '%Y-%B-%d %H:%M:%S')
