def stars(arr):
    for l in arr:
        if isinstance(l, str):
            print l[0].lower() * len(l)
        else:
            print str("*") * l


stars([4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"])

def draw_stars(arr):
    for l in arr:
        print "*" * l


draw_stars([4, 6, 1, 3, 5, 7, 25])
