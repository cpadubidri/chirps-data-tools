import os
import pandas as pd

from src.downloader_chirps import download_chirps_netcdf

from src.config import CHIRPS_BASE_URL, OUTPUT_DIR, START_YEAR, END_YEAR
from src.utils import logger
from src.process_chirps import save_chirps_day_as_tif, extract_precip_for_points #, get_precip


if __name__ == "__main__":
    # log = logger(log_dir="./log", log_filename="download2.log")
    # download_chirps_netcdf(
    #     start_year=START_YEAR,
    #     end_year=END_YEAR,
    #     base_url=CHIRPS_BASE_URL,
    #     output_dir=OUTPUT_DIR,
    #     log=log
    # )
    # save_chirps_day_as_tif("./data/chirps_v2_p/05/chirps-v2.0.1988.days_p05.nc",1,"test.tif")

    # ts = get_precip("./data/chirps_v2_p05/chirps-v2.0.1988.days_p05.nc",35.146207, 33.39219)
    # print(type(ts))
    # import pandas as pd

    # ts.to_csv("example.csv",index=None)

    chirps_folder = './data/chirps_v2_p05'
    output_folder = './data/chirps_v2_p05_nicosia'
    csv_file = './data/nic-pts.csv'

    points_df = pd.read_csv(csv_file)

    for fname in sorted(os.listdir(chirps_folder)):
        if fname.endswith(".nc") and "chirps-v2.0." in fname:
            nc_path = os.path.join(chirps_folder, fname)
            print(f"Processing: {fname}")

            result_df, year = extract_precip_for_points(nc_path, points_df)
            out_path = os.path.join(output_folder, f"nicosia_chirps-v2.0_{year}.csv")
            result_df.to_csv(out_path, index=False)
            print(f"Saved: {out_path}")
        
        # break