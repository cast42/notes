---
title: "Better Typography — raw skill files"
date: 2026-08-29
timestamp: 2026-08-29
type: source
topics:
  - app_design
tags:
  - typography
  - web-design
  - css
resource: "https://ui-skills.com/skills/jakubkrehel/better-typography"
description: "Raw capture of the Better Typography skill and its supporting reference files."
source_url: "https://www.ui-skills.com/skills/jakubkrehel/better-typography"
canonical_url: "https://ui-skills.com/skills/jakubkrehel/better-typography"
author: Jakub Krehel
handle: jakubkrehel
created_at: 2026-08-29
content_hash: 1a8793941af9590c7392a68ac01d841fe4e88c8e4404b64c926e8a570ec41fec
extracted_at: "2026-09-02T08:45:21"
extractor: ui-skills-page+raw-github
---

# Raw content

Source: https://ui-skills.com/skills/jakubkrehel/better-typography


===== SKILL.md =====

---
name: better-typography
description: Focuses on type scale, spacing, sizing, variable fonts, OpenType features, wrapping, truncation and other details that make typography feel great across your product.
---

# Typography

Typography is mostly restraint: a sensible scale, comfortable spacing, enough contrast. A label, a table cell, a marketing headline and an article paragraph do not share one set of rules.

When reviewing, read the rendered page instead of scanning the code. Bad wrapping, widows and truncation only show up at real content lengths.

Write every fix in the project's styling system, and use the exact values below rather than familiar-looking equivalents. The [cheat sheet](https://github.com/jakubkrehel/skills/blob/main/skills/better-typography/css-cheat-sheet.md) maps each declaration to its Tailwind equivalent.

The words themselves belong to `better-writing`. Semantic heading structure belongs to `better-accessibility`. Spatial RTL layout and logical properties belong to `better-layout`. Contrast measurement belongs to `better-colors`. This skill owns how text renders, wraps and behaves in mixed-direction content.

## Serve the right format

Use `.woff2` on the web, for Brotli compression and broad support. `.woff` is a fallback for very old browsers. `.ttf` and `.otf` are desktop formats with no web compression. How the files load is the project's concern.

## Properties over raw tags

When a CSS property exists, use it. `font-weight: 650` instead of `font-variation-settings: "wght" 650`. `font-optical-sizing: auto` instead of `"opsz"`. `font-variant-numeric: tabular-nums` instead of `font-feature-settings: "tnum" 1`.

Properties keep working when a non-variable fallback renders. Reserve raw tags for custom axes (`"GRAD" 80`) and niche features (`"ss01" 1`) with no property of their own. Axes and feature tags are listed in [variable-fonts-and-opentype.md](https://github.com/jakubkrehel/skills/blob/main/skills/better-typography/variable-fonts-and-opentype.md).

## Load intended weights and styles

Browsers synthesize a weight or style the active family doesn't provide, distorting the real face. Load the faces the design uses.

`font-synthesis: none` turns synthesis off, but it erases emphasis rather than reporting it. Set it only after checking every required bold, italic, small-cap, superscript and subscript form stays distinct across the fallback stack.

## Fewer fonts, sizes and weights

Rarely use more than three fonts. Weight and size define hierarchy; overusing them hurts readability fast. Pair for contrast, not similarity: a serif headline over a sans body reads as deliberate, two near-identical sans-serifs read as a mistake.

Below `18px`, stay at weight `400` or heavier. Weights under `300` are display-only at `28px`+; they disappear at text sizes. Pairing guidance is in [choosing-fonts.md](https://github.com/jakubkrehel/skills/blob/main/skills/better-typography/choosing-fonts.md).

## Use a type scale with semantic names

Define a small set of sizes and deviate from it as little as possible. Hard-coded sizes with no system behind them break down at scale.

Solo, default names like `text-sm` are fine when the usage rules are clear. On a team, name sizes by use (`text-body-sm`) so the rules survive other people. Scale construction is in [spacing-and-sizing.md](https://github.com/jakubkrehel/skills/blob/main/skills/better-typography/spacing-and-sizing.md).

## Heading sizes descend with level

Map heading levels to descending steps of the type scale, so a visually subordinate heading never overpowers its parent. Adjacent levels may share a size toward the small end of the scale, as long as weight or spacing keeps them distinct. The semantic element is `better-accessibility`'s; this skill sets only the visual treatment.

## Line-height by role

Headings tighter, around `1.1`. Body copy `1.5` to `1.6`. Prefer unitless values, so line-height scales with the font size; a fixed `24px` does not.

Tight line-height is for short text. Anything that wraps to three or more lines needs at least `1.4`, even in a height-constrained row.

## Letter-spacing by size

Large headings often look better with slightly negative letter-spacing. Small uppercase labels need a little positive letter-spacing, or the letters feel crowded. Body copy at reading sizes needs neither.

## Cap the measure

Long lines make it hard for the eye to find the next one. Cap long-form text around 60–75 characters per line. Any unit works, as long as a cap exists and the line length lands in range. See [unit choices and the pixel equivalents](https://github.com/jakubkrehel/skills/blob/main/skills/better-typography/wrapping-and-punctuation.md#measure-line-length).

## Wrap deliberately

Four declarations, four jobs:

- `text-wrap: balance` distributes text evenly across lines. Use it on headings.
- `text-wrap: pretty` stops a single short word landing on the final line. Use it on descriptions.
- `overflow-wrap: break-word` where a long word, link, or ID could escape the container.
- `white-space: nowrap` on labels and badges where a line break looks broken.

Skip `balance` and `pretty` in long-form text.

## Tabular numbers on changing values

Digits have different widths by default, so timers, counters and prices shift the layout as they update. Apply `font-variant-numeric: tabular-nums` to any value that changes.

## Truncate without losing content

For a single line, `text-overflow: ellipsis` with `overflow: hidden` and `white-space: nowrap`. For several, `line-clamp`. Truncation hides content. When the missing text matters, keep the full value reachable in a tooltip or an expanded view.

## Write copy naturally, style with CSS

Store text in natural case and control presentation with `text-transform`, so a redesign never means rewriting copy.

Use smart punctuation in rendered text:

- Curly quotes in prose, straight quotes in code.
- An en dash for ranges: `2010–2020`.
- The single ellipsis character, not three periods.
- `&nbsp;` to hold `16 px` together across a line break.
- `&shy;` to say where a long word may break.

## Underlines from the font

Default underlines sit wherever the browser decides. Pull position and thickness from the font's own metrics with `text-underline-position: from-font` and `text-decoration-thickness: from-font`. Tune by hand with `text-decoration-thickness`, `text-underline-offset` and `text-decoration-skip-ink`.

`text-decoration-style` draws the line dotted, dashed, or wavy. A dotted underline is a common hint that a word carries extra information, such as an abbreviation or a defined term.

Color is the only part of a real underline that animates reliably. So unless the only thing animating is the color, build the underline as a separate element rather than using `text-decoration`.

## Inputs at 16px on mobile

iOS Safari zooms the whole page when an input's text is smaller than `16px`. Two fixes hold the size at `16px` and look different, so ask which one the design wants:

- Size the input up on mobile (`text-base sm:text-sm`). Changes how it looks on small screens.
- Keep `font-size: 16px` and render the intended size with `transform: scale()`, compensating width and `line-height`. Identical at every viewport, more code to maintain.

Both recipes are in [details-and-accessibility.md](https://github.com/jakubkrehel/skills/blob/main/skills/better-typography/details-and-accessibility.md).

## Size and contrast floors

Start long-form body text at `16px`, the browser default. Move off it only for a reason you can name: the typeface runs small, the measure is narrow, or the product is a dense professional tool.

UI text can go smaller. `14px` is a useful starting point for inputs and menus, `13px` for captions and rarely below `12px`. Inputs still need `16px` on mobile.

When text looks low-contrast, use `better-colors` to measure the rendered pair and `better-accessibility` to classify the requirement. Leave the colors alone unless asked.

## Font smoothing on the root

On macOS, text renders heavier than intended. Apply `-webkit-font-smoothing: antialiased` and `-moz-osx-font-smoothing: grayscale` once on the root layout, never per component. Tailwind's `antialiased` covers both.

## Language and bidi behavior

Set `lang` so browsers and assistive technology pick the right pronunciation, quotes and hyphenation. Set `dir` at the document or at the content boundary where direction changes. Preserve digit order, and use `<bdi>` to isolate a mixed-direction value. Spatial mirroring and logical CSS properties belong to `better-layout`.

## Keep useful text selectable

Keep text selectable by default. `::selection` can carry brand into the reading experience, as long as the selected combination stays legible.

`user-select: none` belongs on a draggable or gesture-driven surface where accidental selection interferes. Never across the interface and never because a button label can be highlighted.

## Before you finish

| Mistake | Fix |
| --- | --- |
| Synthesized face differs from the design | Load the real face; disable only the verified synthesis mode |
| Child heading visually overpowers its parent | Map that section's hierarchy to descending scale steps |
| Heading element picked for its default size | Choose semantics first, then set the size in CSS |
| Orphan on the last line of a paragraph | `text-wrap: pretty` |
| Lopsided two-line heading | `text-wrap: balance` |
| Justified text in an interface | `text-align: start`; reserve justify for specific editorial layouts |
| Underline cuts through descenders | `text-decoration-skip-ink: auto`, `from-font` metrics |
| Mixed-direction value renders in the wrong order | Correct `lang`/`dir`; isolate the value with `<bdi>` |
| Selection disabled across application chrome | Restore it; suppress only where it conflicts with a drag or gesture |
| Extra-info hint with no visual cue | Dotted underline via `text-decoration-style: dotted` |
| Thin/Light weight on `14px` UI text | Weight `400`+ below `18px`; thin weights are display-only |
| `leading-none` on a three-line card description | At least `1.4` on any text that wraps to 3+ lines |

## Reporting

**Severity.** `HIGH` makes text unreadable or truncates content with no way to recover it. `MEDIUM` breaks the type system or the heading hierarchy. `LOW` is isolated polish.

**Verification.** Without a browser: computed size and weight for each heading level, checked descending; declared line-height and measure; truncation rules against realistic string lengths. With one: resize the viewport to catch wrapping, widows and truncation at real content lengths. Report every check you could not run as `Not verified`.

**Format.** Group findings under the principle each violates, ordered by severity, one row per root cause listing every location it appears in:

| Severity | Location | Before | After | Why |
| --- | --- | --- | --- | --- |

`Location` is `path/to/file:line`. `Why` names the principle and the user impact.

End with `Block` when any `HIGH` remains, `Approve` otherwise, leaving the rest in the table as work to do. Never `Approve` coverage you did not inspect. With nothing to report, state "No actionable typography findings" and report verification.

===== choosing-fonts.md =====

# Choosing fonts

Choosing a typeface, the right file format and why fonts look the way they do.

## Choosing a typeface

Font families set the tone before the specific font does.

| Category | Traits | Use for |
| --- | --- | --- |
| Serif | Small strokes at the ends of letters guide the eye along a line | Long passages, editorial reading |
| Sans-serif | Clean, even shapes that stay crisp at small sizes | Default for most interfaces (Helvetica, Inter, Geist) |
| Monospace | Every glyph the same width so columns line up | Code, tables, tabular data |
| Display | Drawn for large headlines | Marketing headlines, hero text |
| Script | Mimics handwriting | Rare, decorative moments |

CSS exposes `cursive` and `fantasy` keywords for the last two categories.

"Display" in a font's name does not make it a display font. SF Pro and Heldane ship a `Display` variant for large sizes and a `Text` variant for small ones. Use the variant matching the size you are setting.

### Rules

- Fewer fonts is usually better. Rarely use more than three. Marketing pages can be more expressive than apps.
- The same applies to sizes and weights. They define hierarchy, and overusing them hurts readability fast.
- Pair for contrast, not similarity. A serif headline over a sans body reads as a deliberate display and reading split; two near-identical sans-serifs read as a mistake.
- Thin weights are display-only. Below `18px` stay at weight `400`+, because Ultralight, Thin and Light (`100`–`300`) strokes disappear at text sizes and on low-DPI screens. Reserve them for `28px`+ display text, and check even there that they hold against the background.

## Font family scope

Applying or reviewing typography never requires a new typeface. Use the product's type system unless the task asks for a type change, and never introduce a paid or proprietary face to satisfy a checklist. Rendering details such as font smoothing, wrapping and tabular numbers do not override the project's font family.

When a type change is asked for, two routes. The system stack gives a native macOS and iOS feel. A commercial face such as Helvetica Now is a brand decision and still needs a fallback stack.

```css
/* System-native macOS/iOS feel */
html {
  font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
}

/* Commercial brand face with safe fallbacks */
html {
  font-family: "Helvetica Now", "Helvetica Neue", Arial, sans-serif;
}
```

## Formats

| Format | Notes |
| --- | --- |
| `.woff2` | Brotli compression, broadly supported. Use this on the web. |
| `.woff` | Older compression. Fallback only for very old browsers. |
| `.ttf` / `.otf` | Raw formats, no web compression, larger files. Desktop only unless there is no other option. |

## Anatomy of a typeface

| Term | Meaning |
| --- | --- |
| x-height | Height of a lowercase `x` |
| Cap height | Height of uppercase letters |
| Baseline | The invisible line letters sit on |
| Ascender | Part of a letter rising above the x-height |
| Descender | Part dropping below the baseline |

These measurements are why two fonts at the same `font-size` look like different sizes. A large x-height looks bigger.

===== spacing-and-sizing.md =====

# Spacing and sizing

A sensible scale and comfortable spacing do more for typography than any effect.

## Units

| Unit | Behavior |
| --- | --- |
| `px` | Fixed |
| `em` | Scales with the current font size |
| `rem` | Scales with the root font size |
| `%` on `font-size` | Relative to the parent's font size, behaves like `em` |

## Type scale

A small set of sizes used across a product, deviated from as little as possible. Hard-coding sizes with no system behind them breaks down at scale.

```css
:root {
  --text-sm: 0.875rem;
  --text-base: 1rem;
  --text-lg: 1.125rem;
  --text-xl: 1.5rem;
  --text-2xl: 2rem;
}
```

Pick an existing scale or define one. Tailwind's (`text-xs` through `text-9xl`, each class pairing a size with a matching line height) is a solid ready-made choice.

Solo, the default names work fine given clear rules for where each size is used. On a team, name sizes semantically. `text-sm` tells you the size but not the use, where `text-body-sm` carries both.

A role-based scale pairs each size with its line-height and weight, making a role one decision instead of three. A starting point for a product interface:

| Role | Size | Line-height | Weight |
| --- | --- | --- | --- |
| Display | `2.25rem` (36px) | `1.1` | `600` |
| Title | `1.5rem` (24px) | `1.2` | `600` |
| Heading | `1.125rem` (18px) | `1.3` | `600` |
| Body | `1rem` (16px) | `1.5` | `400` |
| Caption | `0.8125rem` (13px) | `1.4` | `400` |

Emphasis within a role is one weight step up (`400` → `500`), not a size change.

## Heading hierarchy

Assign each heading level to a descending step of the scale, so hierarchy comes from the scale instead of one-off sizes:

```css
h1 { font-size: var(--text-2xl); }
h2 { font-size: var(--text-xl); }
h3 { font-size: var(--text-lg); }
```

In Tailwind the same mapping is utility classes per level (`text-2xl`, `text-xl`, `text-lg`), centralized in a component or `@layer base` rather than repeated inline.

When reviewing, compare the computed size of headings within each semantic section. A child rendering more prominently than its parent breaks the hierarchy. Deep levels may share a size where the scale runs out of comfortable steps, as long as weight or letter-spacing keeps them distinct. A heading is never smaller than body text unless it is deliberately a label-style overline.

Heading semantics and outline quality belong to `better-accessibility`. Pick the element from the document structure, then use this skill to make that structure visually legible. Never pick a heading element for its browser-default size.

## Kerning and letter-spacing

- **Kerning** adjusts specific pairs such as `AV` or `Ye`. It is built into the font and applied automatically. Switch it off only deliberately, with `font-kerning: none`.
- **`letter-spacing`** adds the same space between every character.

```css
/* Good */
.display-heading {
  letter-spacing: -0.02em;
}

.uppercase-label {
  text-transform: uppercase;
  letter-spacing: 0.05em;
}
```

## Line-height

| Text | Value |
| --- | --- |
| Headings | ~`1.1` |
| Body copy | `1.5`–`1.6` |

Tailwind's `leading-snug`, `leading-normal` and `leading-relaxed` are sensible defaults that rarely need overriding. A tightly-leaded paragraph is harder to read than a taller row is to fit.

```css
/* Bad: card description at heading leading */
.card-description { line-height: 1.1; }

/* Good: it wraps to 3 lines, so it reads as body text */
.card-description { line-height: 1.4; }
```

## Text trimming with text-box

Fonts reserve space above and below the letters, which is why text sits slightly too low in buttons and badges. `text-box` trims it. Two parts: which edges to trim (`trim-both`, `trim-start`, `trim-end`) and where:

| Keyword | Trims at |
| --- | --- |
| `cap` | The cap height (top) |
| `alphabetic` | The baseline (bottom) |
| `text` | The font's own text edge, keeping room for descenders |

```css
/* trim top and bottom */
.badge {
  text-box: trim-both cap alphabetic;
}

/* trim only the top */
.heading {
  text-box: trim-start cap;
}

/* trim only the bottom */
.label {
  text-box: trim-end alphabetic;
}
```

Supported in Chromium (133+) and Safari (18.2+), not yet Firefox. Treat it as progressive enhancement, where unsupported browsers keep the default leading.

===== variable-fonts-and-opentype.md =====

# Variable fonts and OpenType

What a font file can do beyond drawing letters and how to reach those abilities from CSS.

## Static vs variable

- **Static font:** one weight and one style per file. Regular, medium and bold is three files.
- **Variable font:** a whole range in one file. Any value in it works, such as `font-weight: 589`.

A variable font is not automatically better. At one or two weights, static files can be smaller. At several weights, optical sizes, or custom axes, a variable font usually wins.

## Load intended weights and styles

Use a weight or style the active family does not provide and the browser may synthesize it, so load the faces the design uses. `none` disables weight, style, small-cap, superscript and subscript synthesis together and can erase distinctions when the real face is unavailable. Verify the whole fallback stack and every emphasis state before setting it.

```css
.brand-wordmark {
  /* Safe only after this isolated treatment is verified */
  font-synthesis: none;
}
```

For body and interface text, keep synthesis enabled unless a verified font setup supplies every requested form. If only one mode is unwanted, use the specific longhand (`font-synthesis-weight`, `font-synthesis-style` and related properties) instead of the blanket shorthand.

## Axes

Variable-font controls, each with a four-letter tag. A font supports only the axes its designer included.

| Axis | Tag | Controls |
| --- | --- | --- |
| Weight | `wght` | Stroke thickness (like `font-weight`) |
| Optical size | `opsz` | Details and spacing tuned for the display size |
| Width | `wdth` | Glyph width |
| Slant | `slnt` | Slant angle |
| Custom | e.g. `GRAD` (Roboto Flex) | Whatever the designer built |

Inter's variable file exposes only `wght` and `opsz`.

Optical sizes predate variable fonts, and many families still ship them as separate files. Heldane Text is sturdier and more spaced for reading sizes, Heldane Display finer for large ones.

## Properties over axis tags

When a property exists, use it. `font-weight` keeps working when a non-variable fallback renders, where `font-variation-settings` silently does nothing. Save raw tags for custom axes with no property of their own:

```css
/* Good: common axes use the properties */
.heading {
  font-weight: 650;
  font-optical-sizing: auto;
}

/* Good: custom axis with no property of its own */
.heading-grade {
  font-variation-settings: "GRAD" 80;
}

/* Bad: weight via raw tag breaks on fallback fonts */
.heading {
  font-variation-settings: "wght" 650;
}
```

## OpenType features

OpenType is the standard behind almost every modern font. Features are extra built-in options and, unlike axes, work the same on static and variable fonts. A font ships only the features its designer included.

| Tag | Feature |
| --- | --- |
| `tnum` | Tabular numbers: every digit the same width |
| `zero` | Slashed zero: `0` distinct from `O` |
| `liga` | Ligatures: joins pairs like "fi" into one shape |
| `ss01`–`ss20` | Stylistic sets (numbered slots) |
| `cv01`–`cv99` | Character variants (numbered slots) |

Same rule as axes. Prefer the `font-variant-*` properties and reserve `font-feature-settings` for tags with no property:

```css
/* Good: common features use the properties */
.price {
  font-variant-numeric: tabular-nums;
}

/* Good: slashed zero via the property too */
.id {
  font-variant-numeric: slashed-zero;
}

/* Good: niche feature with no property of its own */
.logo {
  font-feature-settings: "ss01" 1;
}
```

Tabular numbers matter for changing values. Without them each digit has a different width and the layout shifts as values update.

## Small caps, superscripts, subscripts

- **Small capitals:** uppercase letters drawn at a smaller size. Enable real ones with `font-variant-caps`.
- **Superscripts** sit above the normal line, the 2 in x², and **subscripts** below it, as in H₂O. Enable proper glyphs with `font-variant-position`.

Both require the font to include the glyphs.

## Stylistic sets and character variants

`ss01` = stylistic set, slot 01. `cv11` = character variant, slot 11. What each slot does differs font to font, which is why they are numbered, not named. Check the font's docs. In Inter, `ss01` switches to open digits and `cv11` swaps in a single-story `a`.

===== wrapping-and-punctuation.md =====

# Wrapping and punctuation

Where lines start, where they end, where they break and which characters they use.

## Measure (line length)

Long lines make it harder for the eye to find the start of the next. For long-form text, aim for 60–75 characters per line.

Any unit works. `65ch` measures characters directly, one `ch` being the width of the `0` in the current font, and a pixel or rem cap is just as good. At a `16px` body size the 60–75 character range lands roughly between `560px` and `680px` depending on the font, so Tailwind's `max-w-xl` (`576px`) and `max-w-2xl` (`672px`) both fit. What matters is that a cap exists and the line length sits in range. Recheck it if the body font size changes.

## Alignment

`text-align` controls where each line starts and ends. `justify` stretches spaces until both edges line up, which works in specific editorial layouts and nowhere else in an interface.

## Wrapping

| Property | Use |
| --- | --- |
| `text-wrap: balance` | Distributes text evenly across multiple lines |
| `text-wrap: pretty` | Avoids leaving a single short word on the final line |
| `overflow-wrap: break-word` | Lets long words, links and IDs break before escaping the container |
| `white-space: nowrap` | Keeps labels and badges on one line where a break looks broken |

Use `balance` on headings and `pretty` on descriptions. Skip both in long-form text, because browsers ignore `balance` past a few lines anyway, and evening out a whole paragraph wastes space and makes it harder to read.

## Truncation

- Single line: `text-overflow: ellipsis`, which needs `overflow: hidden` and `white-space: nowrap`.
- Multiple lines: `line-clamp` allows any number of lines before the ellipsis.

Truncation hides content. Where the missing text matters, make the full value available in a tooltip or an expanded view.

## Case

`text-transform` changes how case appears without changing the underlying text. Write copy naturally and control presentation with CSS, so a redesign never means rewriting copy.

## Smart punctuation

Keyboard characters are not always the best characters:

| Instead of | Use |
| --- | --- |
| Straight quotes `"..."` | Curly quotes that curve around the text (keep straight quotes in code) |
| Hyphen in ranges | En dash: `2010–2020` |
| Two hyphens for an aside | Em dash character |
| Three periods `...` | The single ellipsis character `…` |
| Regular space in `16 px` | `&nbsp;` so the value never breaks apart |
| Uncontrolled word breaks | `&shy;` to mark where a word may break |

## Internationalization

Two refinements for mixed-direction text:

- **Long paragraphs align by their own language.** A one- or two-line snippet follows the surrounding UI's direction. A paragraph of three or more lines aligns to its own script instead, so an English paragraph stays start-aligned LTR even inside an RTL interface. `text-align: start` with the correct `lang`/`dir` on the paragraph element handles this.
- **Never reverse digits.** Numbers keep their order in every direction, so a phone number or "541" reads identically in RTL. Browsers handle this through the Unicode bidi algorithm. Never fight it with manual reordering, and wrap mixed number and text values in `<bdi>` where adjacent RTL text disturbs them.

===== details-and-accessibility.md =====

# Details and accessibility

Underlines, selection, forms, decorative text and the floors that keep everything readable.

## Underlines

Default underline position is browser-determined, sometimes too close, sometimes cutting through descenders, sometimes too thin. Pull position and thickness from the font's own metrics:

```css
a {
  text-underline-position: from-font;
  text-decoration-thickness: from-font;
}
```

A dotted underline on an abbreviation:

```css
abbr {
  text-decoration: underline dotted;
}
```

Or tune manually:

```css
a {
  text-decoration-thickness: 1px;
  text-underline-offset: 3px;
  text-decoration-skip-ink: auto;
  text-decoration-color: var(--color-gray-1000);
  transition: text-decoration-color 200ms ease-out;
}

a:hover {
  text-decoration-color: var(--color-gray-1200);
}
```

Animate the custom element however the effect requires.

## Selection

- `::target-text` styles the phrase a shared link scrolls to.
- The Custom Highlight API styles ranges you pick yourself, like search matches, without extra markup.

## Forms and editable text

- `::placeholder` styles the hint in an empty field.
- `caret-color` colors the blinking insertion bar. Color is about as far as caret styling goes; a fully custom caret is hard to build and rarely worth it.

### iOS input zoom

This is an accessibility feature: `16px` is the web default, and Safari treats smaller as too hard to read while typing.

The two fixes differ in what they do to the design, not in correctness.

**Size up on mobile.** The input renders at `16px` on small screens and drops to the design size from the `sm` breakpoint up. Nothing to compensate, but the mobile input no longer matches the desktop one.

```tsx
<input className="text-base sm:text-sm" type="email" />
```

**Scale the text down.** Keep `font-size` at `16px` so Safari never zooms, then render at the intended size with a transform. The design survives at every viewport, at the cost of two compensating calcs. Widen the element by the inverse of the scale so it still fills its container once shrunk, and divide `line-height` by the same factor so the intended leading survives. `origin-left` pins the text to the start edge, `origin-right` under RTL. Above the breakpoint, drop the transform and set the real size.

```tsx
// 13px rendered from a 16px font-size: 13 / 16 = 0.8125
<div className="flex h-10 items-center rounded-[10px] bg-gray-300 px-2.5">
  <input
    className="h-full w-[calc(100%/0.8125)] origin-left scale-[0.8125] bg-transparent text-base leading-[calc(1.125/0.8125)] outline-none sm:w-full sm:scale-100 sm:text-[13px]"
    type="email"
  />
</div>
```

The transform shrinks the whole box, not only the glyphs, so let a wrapper draw the field's surface and keep the input transparent. A background, border, or ring on the scaled element shrinks with the text and misses the intended hit area.

## Decorative text

| Property | Effect |
| --- | --- |
| `::first-letter` | Drop cap, widely supported |
| `::first-line` | Styles only the first line |
| `initial-letter` | Sizes the drop cap; limited support, no Firefox yet |
| `background-clip: text` | Clips a background or gradient to the letter shapes |
| `-webkit-text-stroke` | Outlines the letters; works across modern browsers despite the prefix |
| `text-shadow` | Like `box-shadow` but follows the character shapes |

A text stroke drawing lines inside the letters is the font. The stroke traces every contour, and variable fonts usually keep overlapping shapes unmerged. Static fonts do not have this issue.

## Sizes

Typography must survive the reader changing it: zoom, a larger browser font size, an overridden line height or letter spacing.

| Text | Size |
| --- | --- |
| Long-form body starting point | Around `16px`, verified in the actual typeface and measure |
| Inputs and menus starting point | Around `14px` |
| Captions | `13px` |
| Floor | Rarely below `12px` |

## Font smoothing

Tailwind's `antialiased` sets both properties:

```css
html {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
```

```tsx
<html lang="en">
  <body class="font-sans antialiased">
    <main>{children}</main>
  </body>
</html>
```

===== css-cheat-sheet.md =====

# CSS cheat sheet

One-line lookup for every typography CSS declaration covered by this skill, with the Tailwind 4 equivalent. Where no utility exists, the arbitrary-value form is shown. Pick the column that matches the project: the declaration in plain CSS, CSS Modules, styled-components or StyleX codebases, the utility in Tailwind codebases.

## Font

| Declaration | What it does | Tailwind |
| --- | --- | --- |
| `font-family: sans-serif` | The sans family | `font-sans` |
| `font-family: serif` | The serif family | `font-serif` |
| `font-family: monospace` | The monospace family | `font-mono` |
| `font-size` | Size from the type scale | `text-*` |
| `font-weight` | Any value from 1 to 1000 | `font-*` |
| `font-style: italic` | Switch to italic style | `italic` |
| `-webkit-font-smoothing` + `-moz-osx-font-smoothing` | Smooth macOS font rendering; apply once at the root | `antialiased` |
| `font-synthesis: none` | Disable all synthesized forms after verifying fallbacks and emphasis | `[font-synthesis:none]` |
| `font-feature-settings` | Toggle OpenType features | `[font-feature-settings:"ss01"]` |
| `font-variation-settings` | Tune variable font axes | `[font-variation-settings:"GRAD"_80]` |
| `font-optical-sizing` | Adjust details per size | `[font-optical-sizing:auto]` |
| `font-variant-caps` | Real small capitals | `[font-variant-caps:small-caps]` |
| `font-variant-position` | Real super and subscripts | `[font-variant-position:super]` |
| `font-variant-numeric: tabular-nums` | Equal-width digits | `tabular-nums` |
| `font-variant-numeric: slashed-zero` | Tell 0 from O | `slashed-zero` |

## Spacing and layout

| Declaration | What it does | Tailwind |
| --- | --- | --- |
| `letter-spacing` | Space between letters | `tracking-*` |
| `line-height` | Space between lines | `leading-*` |
| `font-kerning` | Kerning on or off | `[font-kerning:none]` |
| `text-box: trim-both` | Trim space above and below | `[text-box:trim-both_cap_alphabetic]` |
| `max-width` on text columns | Cap at ~60–75 characters per line | `max-w-xl` / `max-w-2xl` / `max-w-[65ch]` |
| `text-align` | Where lines start and end | `text-start` / `text-center` |

## Wrapping and overflow

| Declaration | What it does | Tailwind |
| --- | --- | --- |
| `text-wrap: balance` | Even out heading lines | `text-balance` |
| `text-wrap: pretty` | Avoid orphaned words | `text-pretty` |
| `text-overflow: ellipsis` | Ellipsis for clipped text | `truncate` |
| `line-clamp` | Cut off after N lines | `line-clamp-*` |
| `overflow-wrap: break-word` | Break long strings | `break-words` |
| `white-space: nowrap` | Stop wrapping | `whitespace-nowrap` |
| `text-transform` | Change the casing | `uppercase` / `capitalize` |

## Decoration and interaction

| Declaration | What it does | Tailwind |
| --- | --- | --- |
| `text-decoration-line: underline` | Draw an underline | `underline` |
| `text-decoration-color` | Underline color | `decoration-*` |
| `text-decoration-thickness` | Underline thickness | `decoration-1` / `decoration-2` |
| `text-underline-offset` | Push the line down | `underline-offset-*` |
| `text-underline-position: from-font` | Underline position from the font | `[text-underline-position:from-font]` |
| `text-decoration-style` | Dotted, dashed or wavy | `decoration-dotted` / `decoration-wavy` |
| `text-decoration-thickness: from-font` | Underline set by the font | `decoration-from-font` |
| `text-decoration-skip-ink` | Gaps around descenders | `[text-decoration-skip-ink:auto]` |
| `caret-color` | Tint the text cursor | `caret-*` |
| `user-select: none` | Suppress selection on a verified drag/gesture conflict only | `select-none` |
| `text-shadow` | Shadow behind the letters | `text-shadow-*` |
| `-webkit-text-stroke` | Outline the letters | `[-webkit-text-stroke:1px_black]` |
| `background-clip: text` | Clip a background to the letters | `bg-clip-text` |
| `initial-letter` | Size a drop cap | `[initial-letter:3]` |
