import requests


def sunrise_lookup(lat, lng, utc_offset):
    base_url = "https://api.sunrise-sunset.org/json?"
    complete_url = f"{base_url}lat={lat}&lng={lng}&formatted=0"

    # Example QUERY string
    # https://api.sunrise-sunset.org/json?lat=36.7201600&lng=-4.4203400
    # https://api.sunrise-sunset.org/json?lat=-97.7436995&lng=30.2711286

    response = requests.get(complete_url).json()
    sunrise = (response['results']['sunrise'])
    sunset = (response['results']['sunset'])
    day_length = (response['results']['day_length'])
    out = (
        f"sunrise: {sunrise} utc | sunset: {sunset} utc | length of day: {day_length} | powered by https://sunrise-sunset.org")
    return out


if __name__ == "__main__":
    out = sunrise_lookup("-0.1276474", "51.5073219", "-0600")
    print(out)
