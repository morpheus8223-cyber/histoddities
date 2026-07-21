"""
Real license-free image sourcing for the documentary compositing pipeline.

Confirmed working sources (see analysis/thumbnail-full-audit-and-licensing.md):
- Wikimedia Commons (best general-purpose source, per-file license tags)
- Library of Congress (strong for pre-1929 US photography)
- Smithsonian Open Access (everything returned is explicitly CC0)

Every function returns the per-file license/rights string alongside the
downloaded path -- never assume "hosted on Commons" means usable, the
license tag on the specific file is what matters.
"""
import json
import os
import urllib.parse
import urllib.request

USER_AGENT = "HistOddities-Pipeline/1.0 (research/production use)"


def _get_json(url):
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))


def _download(url, out_path):
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=60) as resp:
        data = resp.read()
    with open(out_path, "wb") as f:
        f.write(data)
    return out_path


def search_wikimedia(query, limit=10):
    """Search Wikimedia Commons for images matching query. Returns list of dicts
    with title, thumb URL, and full-res descriptionurl for license verification."""
    search_url = (
        "https://commons.wikimedia.org/w/api.php?action=query&format=json"
        f"&list=search&srnamespace=6&srlimit={limit}"
        f"&srsearch={urllib.parse.quote(query)}"
    )
    data = _get_json(search_url)
    results = []
    for item in data.get("query", {}).get("search", []):
        title = item["title"]  # e.g. "File:BostonMolassesDisaster.jpg"
        info_url = (
            "https://commons.wikimedia.org/w/api.php?action=query&format=json"
            "&prop=imageinfo&iiprop=url|extmetadata"
            f"&titles={urllib.parse.quote(title)}"
        )
        info = _get_json(info_url)
        pages = info.get("query", {}).get("pages", {})
        for _, page in pages.items():
            imageinfo = page.get("imageinfo", [])
            if not imageinfo:
                continue
            ii = imageinfo[0]
            meta = ii.get("extmetadata", {})
            license_short = meta.get("LicenseShortName", {}).get("value", "unknown")
            usage_terms = meta.get("UsageTerms", {}).get("value", "unknown")
            results.append({
                "title": title,
                "url": ii.get("url"),
                "descriptionurl": ii.get("descriptionurl"),
                "license": license_short,
                "usage_terms": usage_terms,
                "credit": meta.get("Credit", {}).get("value", ""),
                "artist": meta.get("Artist", {}).get("value", ""),
            })
    return results


def download_wikimedia_file(result, out_dir):
    """Download a single result dict from search_wikimedia() and write a
    sidecar .license.txt next to it recording the exact terms found."""
    os.makedirs(out_dir, exist_ok=True)
    fname = result["title"].replace("File:", "").replace(" ", "_")
    out_path = os.path.join(out_dir, fname)
    _download(result["url"], out_path)
    license_path = out_path + ".license.txt"
    with open(license_path, "w") as f:
        f.write(f"Source: {result['descriptionurl']}\n")
        f.write(f"License: {result['license']}\n")
        f.write(f"Usage terms: {result['usage_terms']}\n")
        f.write(f"Credit: {result['credit']}\n")
        f.write(f"Artist: {result['artist']}\n")
    return out_path, license_path


def search_smithsonian(query, api_key, limit=10):
    """Smithsonian Open Access -- everything returned is CC0, but api_key is
    required (get one at api.data.gov). Kept here for parity; Wikimedia is
    the default first stop since it needs no key."""
    url = (
        "https://api.si.edu/openaccess/api/v1.0/search"
        f"?q={urllib.parse.quote(query)}&rows={limit}&api_key={api_key}"
    )
    return _get_json(url)


if __name__ == "__main__":
    import sys
    query = sys.argv[1] if len(sys.argv) > 1 else "Boston Molasses Flood 1919"
    for r in search_wikimedia(query, limit=5):
        print(r["title"], "|", r["license"], "|", r["url"])
