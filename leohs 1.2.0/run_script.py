import ee
from leohs import run_leohs

ee.Authenticate()   #need to authenticate GEE
project_ID="ee-gamr05055"
ee.Initialize(project=project_ID)     #need to initialize GEE, project ID does not need to be specified on all systems


'''run_leohs(
    Aoi_shp_path=r'E:\GIS\Landsat_Why\0Layers\Group_1_10km.shp',
    Save_folder_path=r'E:\GIS\Landsat_Why\Harmonization-onepair_all_1mill',
    XGB_models = True,
    SR_or_TOA="SR",
    months=[8],
    years=[2020],
    SR_ATMOS_OPACITY_filtering = True,
    sample_points_n=1000000,
    Water=True,
    Snow=True,
    shp=True,
    maxCloudCover = 5,
    project_ID=project_ID)

run_leohs(
    Aoi_shp_path=r'E:\GIS\Landsat_Why0Layers\Group_1_10km.shp',
    Save_folder_path=r'E:\GIS\Landsat_Why\Harmonization-moredates_all_1mill',
    XGB_models = True,
    SR_or_TOA="SR",
    months=[7,8],
    years=[2018,2019,2020,2021,2022],
    SR_ATMOS_OPACITY_filtering = True,
    sample_points_n=10000,
    Water=True,
    Snow=True,
    shp=True,
    maxCloudCover = 50,
    project_ID=project_ID)'''


run_leohs(
    Aoi_shp_path=r'E:\GIS\Landsat Normalization\Test_AOIS\CONUS.shp',
    Save_folder_path=r'E:\GIS\harmfix_test',
    XGB_models = True,
    Regression_types = ['OLS','RMA'],
    SR_or_TOA="TOA",
    months=[4, 5],
    years=[2013, 2014, 2015, 2016],
    SR_ATMOS_OPACITY_filtering = True,
    sample_points_n=10000,
    Water=True,
    Snow=True,
    shp=True,
    maxCloudCover = 50,
    project_ID=project_ID)

# Update wrs reading to avoid issues with matching shapefile column names