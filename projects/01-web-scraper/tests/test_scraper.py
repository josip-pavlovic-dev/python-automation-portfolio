"""
Pytest scaffold for Web Scraper Tool
"""

import pytest

# Import from local module when tests run inside project folder
from scraper import Scraper  # type: ignore

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
        pass

    def error(self, *args, **kwargs):
        pass


@pytest.fixture
def scraper():
    return Scraper(urls=[], headers={}, output_path="/tmp/out.csv", timeout=5, delay=0, logger=DummyLogger())


def test_parse_quotes(scraper):
    data = scraper.parse_quotes(HTML_FIXTURE)
    assert isinstance(data, list)
    assert len(data) == 2
    assert data[0]["author"] == "Author 1"
    assert "tags" in data[0]
