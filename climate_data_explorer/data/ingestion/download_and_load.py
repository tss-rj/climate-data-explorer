import os
import xarray as xr
import requests

def download_sample_data(url: str, save_path: str) -> str:
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    response = requests.get(url)
    response.raise_for_status()
    with open(save_path, "wb") as f:
        f.write(response.content)
    return save_path

def load_sample_netcdf(path: str) -> xr.Dataset:
    return xr.open_dataset(path)

if __name__ == "__main__":
    # Sample dataset (small)
    url = "https://psl.noaa.gov/thredds/fileServer/Datasets/ncep.reanalysis.dailyavgs/surface/air.sig995.2020.nc"
    save_path = "data/raw/sample_air_2020.nc"

    print("Downloading sample dataset...")
    download_sample_data(url, save_path)
    print("Loading dataset...")
    ds = load_sample_netcdf(save_path)
    print(ds)
