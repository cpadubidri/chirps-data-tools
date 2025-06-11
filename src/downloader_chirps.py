import os
import requests
from tqdm import tqdm

def download_chirps_netcdf(start_year, end_year, base_url, output_dir, log):
    os.makedirs(output_dir, exist_ok=True)
    log.info(f"Starting download from {start_year} to {end_year}")

    for year in (range(start_year, end_year + 1)):
        log.info(f"Download year {year}")
        filename = f"chirps-v2.0.{year}.days_p05.nc"
        file_url = base_url + filename

        local_path = os.path.join(output_dir, filename)

        if os.path.exists(local_path):
            log.info(f"Already downloaded: {filename}")
            continue

        try:
            with requests.get(file_url, stream=True, timeout=60) as response:
                if response.status_code == 200:
                    total_size = int(response.headers.get('content-length', 0))
                    with open(local_path, 'wb') as f, tqdm(
                        desc=f"Downloading {filename}",
                        total=total_size,
                        unit='B',
                        unit_scale=True,
                        unit_divisor=1024
                    ) as bar:
                        for chunk in response.iter_content(chunk_size=1024):
                            if chunk:
                                f.write(chunk)
                                bar.update(len(chunk))
                    log.info(f"Saved: {local_path}")
                else:
                    log.error(f"Failed to download: {filename} (HTTP {response.status_code})")
                    log.error(f"Check URL: {file_url}")
        except Exception as e:
            log.error(f"Error downloading {filename}: {e}")