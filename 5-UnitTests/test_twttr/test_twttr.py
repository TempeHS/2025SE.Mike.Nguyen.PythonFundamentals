from twttr import shorten


def main():
    test_twttr()


def test_twttr():
    assert shorten("watermelon") == "wtrmln"
    assert shorten("cake") == "ck"
    assert shorten("twitter") == "twttr"


if __name__ == "__main__":
    main()
