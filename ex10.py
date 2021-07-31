class TestPhrase:
    def test_set_phrase(self):
        phrase = input("Set a phrase: ")
        assert len(phrase) < 15, "Слишком длинная фраза"
