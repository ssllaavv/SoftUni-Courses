from math import floor

prod_per_day_per_worker = int(input())
workers_count = int(input())
competitor_prod_per_month = int(input())

prod_per_month = (20 * prod_per_day_per_worker * workers_count) + \
                (10 * floor(.75 * prod_per_day_per_worker * workers_count))
diff = prod_per_month - competitor_prod_per_month
diff_in_percents = 100 * diff / competitor_prod_per_month

print(f"You have produced {prod_per_month:.0f} biscuits for the past month.")
if diff > 0:
    print(f"You produce {diff_in_percents:.2f} percent more biscuits.")
elif diff < 0:
    print(f"You produce {abs(diff_in_percents):.2f} percent less biscuits.")