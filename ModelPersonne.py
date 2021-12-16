class Ssn:
    def __init__(self, numeroSecu):
        self.numeroSecu = numeroSecu

    def is_valid(self):
        b = int(self.numeroSecu[:-2]) % 97
        c = 97 - b
        # if c < 10:
        #    c = "0" + str(c)
        # print(c)
        key = int(self.numeroSecu[-2:])
        print(key, c)
        return c == int(self.numeroSecu[-2:])


class Person:
    def __init__(self, nom, prenom, ssn):
        self.prenom = prenom
        self.nom = nom
        self.ssn = ssn

    def getNom(self):
        return self.nom

    def getPrenom(self):
        return self.prenom

    def getSSN(self):
        return self.ssn

    def has_valid_ssn(self):
        ssn = Ssn("269054958815780")
        if ssn.is_valid():
            return True
        else:
            return False

