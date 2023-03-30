import pandas as pd
import geopandas as gpd
site_locations = pd.read_csv('data/LOCAR_Site_Information.csv',
                                skipfooter=11, engine='python',
                                usecols=['Site Code', 'Longitude', 'Latitude'],
                                index_cols='Site Code')

site_geometry = gpd.points_from_xy(site_locations['Longitude'],
                                    site_locations['Latitude'], crs='EPSG:4326']

site_gdf = gpd.GeoDataFrame(site_locations, geometry = site_geometry)

>>> site_gdf

>>> site_gdf.crs

FP_catchment = gpd.GeoDataFrame.from_file('data/river_catchment/frome_piddle_catchment.shp')

import matplotlib.pyplot as plt
>>> FP_catchment.plot()
>>> plt.show()

from geopandas.tools import sjoin
FP_sites = sjoin(site_gdf, FP_catchment)
>>> FP_sites

def is_site_within_cathcment(site_dataframe, catchment_dataframe):
    answer_dataframe = sjoin(site_dataframe, catchment_dataframe)
    if answer_dataframe.size:
        return True
    else:
        return False

>>> is_site_within_cathcment(site_gdf.loc[['FP23']],FP_catchment)
#True
>>> is_site_within_cathcment(site_gdf.loc[['TE03']],FP_catchment)
#False

from shapely.geometry import Point
position = gpd.GeoDataFrame(geometry=[Point((longitude,latitude))],crs='EPSG:4326')
>>> position
p = Site(name = name, longitude = longitude, latitude = latitude)
>>> p.location
>>> p.location.geometry_equals(position)
# 0 True
# dtype: bool

gpd.GeoDataFrame.geom

