CREATE TABLE IF NOT EXISTS signal (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP,
    wind_speed_mean FLOAT,
    wind_speed_min FLOAT,
    wind_speed_max FLOAT,
    wind_speed_std FLOAT,
    power_mean FLOAT,
    power_min FLOAT,
    power_max FLOAT,
    power_std FLOAT
);
