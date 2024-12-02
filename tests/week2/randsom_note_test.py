from grind75.week1.randsom_note import Solution


def test_single_letter_note_not_in_magazine():
    ransom_note = "a"
    magazine = "b"
    solution = Solution()

    res = solution.canConstruct(ransom_note, magazine)

    assert res is False


def test_two_letter_note_not_in_magazine():
    ransom_note = "aa"
    magazine = "ab"
    solution = Solution()

    res = solution.canConstruct(ransom_note, magazine)

    assert res is False


def test_note_is_constructable():
    ransom_note = "aa"
    magazine = "aab"
    solution = Solution()

    res = solution.canConstruct(ransom_note, magazine)

    assert res is True
