def search_by_title(cart, title):
    results = []

    for dvd in cart.items:
        if title.lower() in dvd.title.lower():
            results.append(dvd)

    return results