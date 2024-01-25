import unittest
from ca.uqam.info.mgl7760.tp1.domain.auteur import Auteur

class TestAuteurs(unittest):

    def test_creation_auteur(self):
        auteur_1 = Auteur(1,"Jean Tremblay")
        auteur_2 = Auteur(2,"Diane Bergeron")
        auteur_3 = Auteur(3,"Francois Bergeron")

        self.assertTrue(auteur_1.nom == "Jean Tremblay")


if __name__ == '__main__':

    unittest.main()

