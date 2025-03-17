import time
from datetime import datetime, timedelta, timezone

observer_lon = -107.877739

print("\n" * 2)

while True:
    now_utc = datetime.now(timezone.utc)

    rounded_offset = round(observer_lon / 15.0)
    hour_longitudinal_time = now_utc + timedelta(hours=rounded_offset)

    precise_offset = observer_lon / 15.0
    precise_longitudinal_time = now_utc + timedelta(hours=precise_offset)

    print("\033[F\033[K" * 2, end="")
    print(f"Hour Longitudinal Time: {hour_longitudinal_time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Precise Longitudinal Time: {precise_longitudinal_time.strftime('%Y-%m-%d %H:%M:%S')}")

    time.sleep(1)