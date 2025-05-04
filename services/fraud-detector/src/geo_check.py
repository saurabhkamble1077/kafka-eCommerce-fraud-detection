from math import radians, sin, cos, sqrt, atan2

EARTH_RADIUS_KM = 6371
MAX_TRAVEL_KM_PER_HOUR = 900  

def haversine(lat1, lon1, lat2, lon2) -> float:
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = sin(dlat/2)**2 + cos(lat1)*cos(lat2)*sin(dlon/2)**2
    return 2 * EARTH_RADIUS_KM * atan2(sqrt(a), sqrt(1-a))

def is_geo_anomaly(prev_lat, prev_lon, prev_ts, curr_lat, curr_lon, curr_ts) -> bool:
    dist = haversine(prev_lat, prev_lon, curr_lat, curr_lon)
    hours = (curr_ts - prev_ts) / 3600
    if hours <= 0:
        return True
    speed = dist / hours
    return speed > MAX_TRAVEL_KM_PER_HOUR