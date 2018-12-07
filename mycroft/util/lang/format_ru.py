def nice_time_ru(dt, speech=True, use_24hour=True, use_ampm=False):
    string = dt.strftime("%H:%M")
    if not speech:
        return string
    return string
    
