import os
import pandas as pd
import xarray as xr
import rioxarray

def extract_precip_for_points(nc_file_path, points_df):
    ds = xr.open_dataset(nc_file_path)
    precip = ds['precip']

    precip.rio.set_spatial_dims(x_dim="longitude", y_dim="latitude", inplace=True)
    precip.rio.write_crs("EPSG:4326", inplace=True)

    year = os.path.basename(nc_file_path).split('.')[2]

    output_df = points_df.copy()

    all_series = []
    for idx, row in points_df.iterrows():
        lat = row['latitude']
        lon = row['longitude']

        ts = precip.sel(latitude=lat, longitude=lon, method="nearest")
        ts_series = ts.to_series()

        ts_df = ts_series.reset_index()
        ts_df.columns = ['date', 'precip']
        ts_df['id'] = row['id']

        all_series.append(ts_df)

    combined = pd.concat(all_series)

    pivot_df = combined.pivot(index='id', columns='date', values='precip').reset_index()

    output_df = points_df.merge(pivot_df, on='id')


    return output_df, year


import xarray as xr
import rioxarray

def save_chirps_day_as_tif(nc_file_path, band_index, output_tif_path):
    ds = xr.open_dataset(nc_file_path)

    precip = ds['precip']
    precip.rio.set_spatial_dims(x_dim="longitude", y_dim="latitude", inplace=True)
    precip.rio.write_crs("EPSG:4326", inplace=True)

    precip_day = precip.isel(time=band_index)

    precip_day.rio.to_raster(output_tif_path)

    print(f"Saved: {output_tif_path}")
