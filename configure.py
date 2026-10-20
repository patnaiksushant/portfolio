"""Set canonical metadata, sitemap and 404 home link for your public URL."""
from pathlib import Path
from urllib.parse import urlparse
from xml.sax.saxutils import escape
import argparse, json, re
parser = argparse.ArgumentParser()
parser.add_argument("url", help="Full HTTPS URL, including repository path when applicable")
args = parser.parse_args()
url = args.url.rstrip("/") + "/"
parsed = urlparse(url)
if parsed.scheme != "https" or not parsed.netloc or parsed.query or parsed.fragment or parsed.username:
    parser.error("Use a public HTTPS URL without credentials, query or fragment")
p = Path(__file__).resolve().parent
metadata = '<link rel="canonical" href="' + escape(url, {'"':'&quot;'}) + '" />\n<meta property="og:url" content="' + escape(url, {'"':'&quot;'}) + '" />'
s = p.joinpath("index.html").read_text()
s = re.sub(r"<!-- SITE_URL_START -->.*?<!-- SITE_URL_END -->", lambda _: "<!-- SITE_URL_START -->\n" + metadata + "\n<!-- SITE_URL_END -->", s, flags=re.S)
p.joinpath("index.html").write_text(s)
p.joinpath("sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>' + escape(url) + '</loc></url></urlset>\n')
p.joinpath("robots.txt").write_text('User-agent: *\nAllow: /\nSitemap: ' + url + 'sitemap.xml\n')
s = p.joinpath("404.html").read_text()
s = re.sub(r'(<a id="home" href=")[^"]*(")', lambda m:m[1]+escape(url, {'"':'&quot;'})+m[2], s)
p.joinpath("404.html").write_text(s)
print("Configured:", url)
