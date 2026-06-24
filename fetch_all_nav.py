import requests
import pandas as pd

schemes = {
    119551: "SBI_Bluechip",
    120503: "ICICI_Bluechip",
    118632: "Nippon_Large_Cap",
    119092: "Axis_Bluechip",
    120841: "Kotak_Bluechip"
}

for code, name in schemes.items():

    print(f"Fetching {name}...")

    url = f"https://api.mfapi.in/mf/{code}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        df = pd.DataFrame(data["data"])

        df.to_csv(
            f"data/raw/{name}.csv",
            index=False
        )

        print(f"{name} saved.")

    else:
        print(f"Failed for {name}")