CREATE TABLE IF NOT EXISTS signal (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP,   -- ou data se você preferir separar data e horário
    wind_speed_mean FLOAT,
    wind_speed_min FLOAT,
    wind_speed_max FLOAT,
    wind_speed_std FLOAT,
    power_mean FLOAT,
    power_min FLOAT,
    power_max FLOAT,
    power_std FLOAT,
    ambient_temperature_mean FLOAT,
    ambient_temperature_min FLOAT,
    ambient_temperature_max FLOAT,
    ambient_temperature_std FLOAT
);
