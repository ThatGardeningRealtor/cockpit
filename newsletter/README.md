# Newsletter

Live emails and the WordPress page at [getrealtytx.com/little-red-house-news](https://getrealtytx.com/little-red-house-news) load issue HTML from GitHub Pages and images from `raw.githubusercontent.com`. Once a file is referenced, leave it at that path. Do not rename it, and do not move it.

Older issues stay where they already are. Garden Edition Vols. 1–6 and the Weekly Newsletter Vols. 1–7 are flat files in `newsletter/`. Garden Edition Vols. 7 and 8 already live in `newsletter/vol7/` and `newsletter/vol8/`.

## One folder per issue

From Vol. 9 on, each issue gets its own folder:

```
newsletter/volN/
  TGR-Garden-Edition-VolN.html   (or the Weekly HTML, if that series returns)
  wordpress-embed-volN.html
  volN-hero.jpg
  …other images for this issue only
```

The folder holds the issue HTML, the images that belong to that issue, and the WordPress embed snippet.

Shared images that older issues already use (headshots, logos, and anything else under `newsletter/` with a live URL) stay put.

`newsletter/_archive/` is for files nothing links to. Do not point a new issue at a file in there.

## Image URL conventions

In the issue HTML, every image uses a raw GitHub URL on `main`:

```
https://raw.githubusercontent.com/ThatGardeningRealtor/cockpit/main/newsletter/volN/volN-hero.jpg
```

The HTML itself is what GitHub Pages serves, and what the WordPress iframe loads:

```
https://thatgardeningrealtor.github.io/cockpit/newsletter/volN/TGR-Garden-Edition-VolN.html
```

Name new files with lowercase letters and hyphens, and no spaces. If a filename already contains a space, encode each space as `%20` in the URL (`(` is `%28`, `)` is `%29`).

The WordPress embed is a small HTML snippet whose iframe `src` is the GitHub Pages URL above. See `vol7/wordpress-embed-vol7.html`.

## Publishing

1. Push the issue folder (`newsletter/volN/`).
2. Update `newsletter/latest.html` so the meta refresh and the script both point at the new issue HTML.
3. Add the issue to `newsletter/index.html`, linking the HTML at its real path.
