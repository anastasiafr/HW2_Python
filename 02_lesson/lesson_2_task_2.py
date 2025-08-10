def is_year_leap(year):
    return year % 4 == 0


year_to_check = 2023  # можно заменить на любой другой год:2000,1400 и т.д

result = is_year_leap(year_to_check)

print(f"год {year_to_check}: {result}")
