# https://cs50.harvard.edu/python/2022/psets/1/meal/
# # Main solution
# def main():
#     meal = input("What time is it? ")
#     if 7 <= convert(meal) <= 8:
#         print("breakfast time")
#     elif 12 <= convert(meal) <= 13:
#         print("lunch time")
#     elif 18 <= convert(meal) <= 19:
#         print("dinner time")
  
# def convert(time):
#     hour, min = time.split(":")
#     return int(hour) + int(min) / 60

# if __name__ == "__main__":
#     main()

# Challenge solution
def main():
    meal = input("What time is it? ")

    if 7 <= convert(meal) <= 8:
        print("breakfast time")
    elif 12 <= convert(meal) <= 13:
        print("lunch time")
    elif 18 <= convert(meal) <= 19:
        print("dinner time")
  
def convert(time):
    if "a.m." in time or "p.m." in time:
        hr_min, am_pm = time.split(" ")
        hour, min = hr_min.split(":")
        if am_pm == "p.m." and int(hour) != 12:
            hour = int(hour) + 12
    else:
        hour, min = time.split(":")
    return float(hour) + float(min) / 60

if __name__ == "__main__":
    main()