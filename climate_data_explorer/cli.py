import argparse
from climate_data_explorer.data.ingestion.download_and_load import download_sample_data, load_sample_netcdf
from climate_data_explorer.data.compression.zarr_converter import convert_netcdf_to_zarr

def main():
    parser = argparse.ArgumentParser(description="Climate Data Explorer CLI")
    parser.add_argument("--download", action="store_true", help="Download sample dataset")
    parser.add_argument("--convert", action="store_true", help="Convert downloaded NetCDF to Zarr")
    args = parser.parse_args()

    if args.download:
        url = "https://psl.noaa.gov/thredds/fileServer/Datasets/ncep.reanalysis.dailyavgs/surface/air.sig995.2020.nc"
        save_path = "data/raw/sample_air_2020.nc"
        download_sample_data(url, save_path)
        print("Downloaded to:", save_path)

    if args.convert:
        netcdf_path = "data/raw/sample_air_2020.nc"
        zarr_path = "data/processed/sample_air_2020.zarr"
        convert_netcdf_to_zarr(netcdf_path, zarr_path)
        print("Converted to Zarr:", zarr_path)

if __name__ == "__main__":
    main()
