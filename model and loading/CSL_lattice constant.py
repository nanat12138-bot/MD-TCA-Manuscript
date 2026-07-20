lat1 = num  # the lattice constant of the γ phase
lat2 = num # the lattice constant of the γ' phase
error = 0.3  # CSL principle
up_limit = 100  # limit
for i in range(1, up_limit):
    lat1_ = lat1*i
    nlat2 = lat1_ // lat2
    eps = abs(nlat2*lat2 - lat1_)
    if eps < error:
        print(f"{i} {int(nlat2)} {lat1_:.3f} {eps:.5f}")



