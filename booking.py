def get_booking_uri(booking_list, journey_type='multi-city', f_class='Economy', adt=1, chd=0, inf=0, pos='VN', lc='vi-VI'):
    uri = "https://fly.vietnamairlines.com/dx/VNDX/#/flight-selection?"
    params = {}
    params["journeyType"] = journey_type
    params["direction"] = 0
    params["pointOfSale"] = pos
    params["locale"] = lc
    params["class"] = f_class
    params["ADT"] = adt
    params["CHD"] = chd
    params["INF"] = inf
    for idx, trip in enumerate(booking_list):
        origin, destination, date = trip.split(",")
        if idx > 0:
            params['origin{}'.format(idx)] = origin
            params['destination{}'.format(idx)] = destination
            params['date{}'.format(idx)] = date
        else:
            params['origin'] = origin
            params['destination'] = destination
            params['date'] = date
    uri += "&".join(["{}={}".format(k, v) for k,v in params.items()])
    return uri
