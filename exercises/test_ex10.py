class TestPhrase:
    def test_phrase_length(self):
        phrase = input("Set a phrase: ")
        assert len(phrase) < 15, "The phrase is longer than 15 symbols"
