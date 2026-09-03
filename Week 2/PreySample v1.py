class PreySample:
    def __init__(self, full_species_name, delta13c_list, tissue_description, sample_date_utc):
        self.full_species_name=full_species_name
        self.delta13c_list=delta13c_list
        self.tissue_description=tissue_description
        self.sample_date_utc=sample_date_utc
        
    def get_common_name(self):
        data_string = ‘common name (scientific name)’
        data_list = data_string.split('('))
        
    def get_scientific_name(self):
        data_string = 'get_scientific_name'
      
    def get_average_delta13c(self):
        import statistics
        get_average_delta13c = statistics.mean(delta13c_list)
        print(get_average_delta13c)
        
    def get_tissue_count(self):
        get_tissue_count = len(tissue_description)
        print(get_tissue_count)
   
    def get_sample_date(self):
        import datetime
        