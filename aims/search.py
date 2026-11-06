def search_by_category(cart, category):
    results = []

    for dvd in cart.items:
        if category.lower() in dvd.category.lower():
            results.append(dvd)

    return results


def search_by_title(cart, title):
    results = []

    for dvd in cart.items:
        if title.lower() in dvd.title.lower():
            results.append(dvd)

    return results