def add_time(time: int, duration: int):
    if (type(time) == int):
        end_time = (time+duration)%24
    else:
        print("Enter time as int, FOOL!")
        end_time = None
    return end_time

if __name__ == "__main.py__":
    print(add_time(23,4))
    print(add_time(23.5,4))  # auch möglich, da int in def add_time(time: int, duration: int): kein Datentypcheck sondern nur für Dokuzwecke 


