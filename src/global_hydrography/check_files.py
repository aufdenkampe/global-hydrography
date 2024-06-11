import os
from pathlib import Path
import geopandas as gpd

def check_files():
    output_file_path = 'J:\\MMW\\TDX_Hydro\\output.txt'
    with open(output_file_path, 'w') as output_file:
        for file in os.listdir('J:\\MMW\\TDX_Hydro'):
            file_path = os.path.join('J:\\MMW\\TDX_Hydro', file)
            try:
                df = gpd.read_file(file_path)
                output_file.write(f"-----------------------------------------------\n")
                output_file.write(f"File: {file}\n")
                df.info(buf=output_file)
                output_file.write(f"Size: {df.size}\n")
                output_file.write(f"-----------------------------------------------\n\n\n")
                print(f"{file} done!")
            except Exception as e:
                print(f"ERROR for {file}: ", e)


if __name__ == "__main__":
    check_files()