import datetime
import statistics

class PreySample:
    def __init__(self, full_species_name, delta13c_list, tissue_description, sample_date_utc):
        self.full_species_name = full_species_name
        self.delta13c_list = delta13c_list
        self.tissue_description = tissue_description
        self.sample_date_utc = sample_date_utc

    def get_common_name(self):
        return self.full_species_name.split(" (")[0]
    def get_scientific_name(self):
        return self.full_species_name.split(")")[1]
    def get_average_delta13c(self):
        return statistics.mean(self.delta13c_list)
    def get_tissue_count(self):
        return self.len(self.tissue_description)
    def get_sample_date(self):
        return self.datetime.datetime.strptime(self.sample_date_utc, "%Y-%m-%d %H:%M:%S")

sample1 = PreySample(
    full_species_name = "Harbor Seal (Phoca vitulina",
    delta13c_list = [-12.4, -11.3, -10.6, -13.5, -15.8],
    tissue_description = "Bone collagen, Bone collagen, Muscle, Skin",
    sample_date_utc ='2020-11-16T04:25:032'
)
print(sample1.get_common_name())
print(sample1.get_scientific_name())
print(sample1.get_average_delta13c())
print(sample1.get_average_delta13c())
print(sample1.get_sample_date())

