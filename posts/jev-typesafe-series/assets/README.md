# Jev article visuals

Eight canonical SVG diagrams were generated with Fireworks Tech Graph 1.2.0, Style 1. Each adjacent JSON file is an editable source; layout reports record strict text and showcase composition validation. Five `-mobile.svg` variants preserve the same nodes and edges in narrower layouts. PNGs were rendered with Chromium because the installed Fireworks PNG dependencies were unavailable. SVGs are the embedded canonical artifacts.

Rebuild a diagram with the installed skill's `fireworks.py validate architecture INPUT.json`, `render architecture INPUT.json OUTPUT.svg --report OUTPUT.layout.json`, and `check OUTPUT.svg` commands. Keep the source meaning and geometry gates intact.

`visuals.css` and `visuals.js` hold the editable common visual enhancements. Matching copies are embedded in the article HTML so core reading does not need an external script or build system. Interactive fixtures are fictional; controls never call an API.

## Animation limitation

No GIF was generated. The installed animator only supports twelve fixed scene contracts; these Jev workflows do not match their required roles and topology. A dry run rejected the generic overview for missing reviewed motion metadata. The exact result is retained in `../01-what-is-jev/assets/decision-loop.motion.json`. No metadata or architecture was fabricated to bypass that gate. Validated static diagrams and manual walkthroughs are the delivered alternatives. This does not claim completion of GIF animation.
