"""Landing pages stay bilingual and point at each other."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_english_and_korean_readmes_cross_link() -> None:
    en = (ROOT / "README.md").read_text(encoding="utf-8")
    ko = (ROOT / "README.ko.md").read_text(encoding="utf-8")
    assert "README.ko.md" in en
    assert "README.md" in ko
    assert "한국어" in en
    assert "English" in ko
    for text in (en, ko):
        assert "python -m jev_master ticket" in text
        assert "TYPESAFE_API_KEY" in text
        assert "catalog --kind vision" in text
        assert "--kind official" in text
        assert "djev.dev" in text
        assert "8765" in text
        assert "382" in text
        assert "docs/ECOSYSTEM.md#vision-images-and-local-eyes" in text
        assert "| `agent`" in text
        assert "| `vision`" in text
    assert "Browse by category" in en
    assert "분류별로 보기" in ko
    assert "wait a while" in en
