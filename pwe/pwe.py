MONOISOTOPIC_WEIGHTS = {
    # http://www2.riken.jp/BiomolChar/Aminoacidmolecularmasses.htm
    'G' : 57.02146372,  'A' : 71.03711378,  'S' : 87.03202840,  'P' : 97.05276385,
    'V' : 99.06841391,  'T' : 101.04767847, 'C' : 103.00918478, 'I' : 113.08406398,
    'L' : 113.08406398, 'N' : 114.04292744, 'D' : 115.02694302, 'Q' : 128.05857751,
    'K' : 128.09496301, 'E' : 129.04259309, 'M' : 131.04048491, 'H' : 137.05891186,
    'F' : 147.06841391, 'R' : 156.10111102, 'Y' : 163.06332853, 'W' : 186.07931295
}

def main():
    prot = input()
    weight = sum((MONOISOTOPIC_WEIGHTS[aa] for aa in prot))
    print(weight)

if __name__ == "__main__":
    main()