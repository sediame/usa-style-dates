import os, re, shutil
from pathlib import Path

home = str(Path.home())
for filename in os.listdir(home + '/delicious/cats'):
    match = re.search(r'\d{2}-\d{2}-\d{4}', filename)

    date_extract = match.group()

    amer_date = date_extract.split('-')
    t = amer_date[0]
    amer_date[0] = amer_date[1]
    amer_date[1] = t

    euro_date = "-".join(amer_date)

    name_date = filename.split(date_extract)
    euro_filename = name_date[0] + euro_date + name_date[1]
    amer_filename = os.path.join(home + '/delicious/cats', filename)
    euro_filename = os.path.join(home + '/delicious/cats', euro_filename)
    print(amer_filename)
    print(euro_filename)
    shutil.move(amer_filename, euro_filename)

