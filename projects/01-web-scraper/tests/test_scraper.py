"""Pytest suite for Web Scraper Tool."""

import pytest
from scraper import Scraper

HTML_FIXTURE = """
<html>
  <body>
    <div class="quote">
      <span class="text">Quote 1</span>
      <small class="author">Author 1</small>
      <a class="tag">life</a>
      <a class="tag">wisdom</a>
    </div>
    <div class="quote">
      <span class="text">Quote 2</span>
      <small class="author">Author 2</small>
    </div>
  </body>
</html>
"""


class DummyLogger:
    def info(self, *args, **kwargs):
        return None

    def error(self, *args, **kwargs):
        return None


@pytest.fixture
def scraper():
    return Scraper(
        urls=[],
        headers={},
        output_path="/tmp/out.csv",
        timeout=5,
        delay=0,
        logger=DummyLogger(),
    )


def test_parse_quotes(scraper):
    data = scraper.parse_quotes(HTML_FIXTURE)
    assert isinstance(data, list)
    assert len(data) == 2
    assert data[0]["author"] == "Author 1"
    assert "tags" in data[0]
    assert data[0]["tags"] == ["life", "wisdom"]


def test_run_uses_fetch_and_parse(monkeypatch):
    calls = {"fetch": 0}

    s = Scraper(urls=["https://example.com"], headers={}, delay=0, logger=DummyLogger())

    def fake_fetch(url: str) -> str:
        calls["fetch"] += 1
        return HTML_FIXTURE

    monkeypatch.setattr(s, "fetch", fake_fetch)

    rows = s.run()

    assert calls["fetch"] == 1
    assert len(rows) == 2
    assert rows[0]["text"] == "Quote 1"
