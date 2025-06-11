# CHIRPS Data Tools

A Python toolkit to download, extract, and convert CHIRPS daily precipitation data. Supports point-based extraction to CSV and daily raster export to GeoTIFF.

---

## Features

- **Download CHIRPS NetCDF** files for specified years
- **Extract precipitation data** for given coordinates (lat/lon) into CSV
- **Convert daily bands** of CHIRPS NetCDF to single-band GeoTIFFs

---

## Installation

Clone this repository:

```bash
git clone https://github.com/cpadubidri/chirps-data-tools.git
cd chirps-data-tools
```

Install required packages:

```bash
pip install -r requirements.txt
```

---

## Usage

### 1. Download CHIRPS NetCDF files

```python
from src.downloader_chirps import download_chirps_netcdf

download_chirps_netcdf(
    start_year=2020,
    end_year=2023,
    base_url="https://data.chc.ucsb.edu/products/CHIRPS-2.0/global_daily/netcdf/p05/",
    output_dir="./data",
    log=your_logger_instance
)
```

### 2. Extract data for points (CSV output)

```python
from src.utils import extract_precip_for_points
import pandas as pd

# Sample points DataFrame
points = pd.DataFrame({
    "id": ["loc1", "loc2"],
    "latitude": [12.97, 13.01],
    "longitude": [77.59, 77.60]
})

df, year = extract_precip_for_points("./data/chirps-v2.0.2023.days_p05.nc", points)
df.to_csv(f"precip_{year}.csv", index=False)
```

---

## Requirements

- Python 3.8+
- `xarray`
- `rioxarray`
- `pandas`
- `requests`
- `tqdm`

Install all dependencies with:

```bash
pip install -r requirements.txt
```

---

## License

MIT License © 2025 [cpadubidri](https://github.com/cpadubidri)
