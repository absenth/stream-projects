package weather

import "github.com/ramsgoli/openweathermap"


owm := openweathermap.OpenWeatherMap{API_KEY: os.Getenv("OPENWEATHERMAP_API")}
