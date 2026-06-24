import requests
import pandas as pd

scheme_code = 125497

url = f"https://api.mfapi.in/mf/{scheme_code}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    print("Scheme Name:")
    print(data["meta"]["scheme_name"])

    nav_df = pd.DataFrame(data["data"])

    nav_df.to_csv(
        "data/raw/hdfc_top100_live_nav.csv",
        index=False
    )

    print("Live NAV saved successfully.")

else:
    print("API request failed.")