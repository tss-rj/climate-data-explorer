import os
import xarray as xr

def convert_netcdf_to_zarr(netcdf_path: str, zarr_path: str) -> str:
    os.makedirs(os.path.dirname(zarr_path), exist_ok=True)

    ds = xr.open_dataset(netcdf_path)
    ds.to_zarr(zarr_path, mode="w")

    return zarr_path

if __name__ == "__main__":
    netcdf_path = "data/raw/sample_air_2020.nc"
    zarr_path = "data/processed/sample_air_2020.zarr"

    print("Converting to Zarr...")
    convert_netcdf_to_zarr(netcdf_path, zarr_path)
    print("Saved Zarr at:", zarr_path)
