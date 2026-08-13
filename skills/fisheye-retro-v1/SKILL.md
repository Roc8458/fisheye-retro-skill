---
name: fisheye-retro-v1
description: "Transform a user-supplied photo into a circular fisheye-lens retro film aesthetic image. Apply 180-degree barrel distortion, circular crop, vintage film grain, color cast, light leaks, natural vignetting, and lo-fi street photography texture. Use when the user wants a fisheye, retro, vintage film, lo-fi, grainy, skate-culture, or analog-film stylized photo."
license: MIT
---

# 鱼眼复古 · Fisheye Retro v1.0

**作者 / Author：Roc Wan（Roc8458）**

Create a lo-fi street photography image from a supplied photo. Preserve the signature **圆镜为框、畸变为骨、胶片为肤、暗角为息、颗粒为魂**:

- force a circular fisheye frame with barrel distortion;
- treat the circular image as a vintage film frame inside a dark matte;
- apply organic film grain, color cast, and light leaks;
- let natural vignetting darken the edges toward the circular perimeter;
- keep the mood raw, spontaneous, and analog;
- keep the image completely free of text unless the user explicitly supplies wording.

Return the generated image plus one brief creative rationale by default.

## Decision Priority

Resolve conflicts in this order:

1. Preserve the scene's identity and core subject.
2. Force circular fisheye crop and barrel distortion on the entire image.
3. Apply vintage film texture (grain, color cast, light leaks, soft focus).
4. Add natural vignetting from center to edge.
5. Keep the lo-fi street atmosphere spontaneous and unpolished.
6. Control color through a retro film palette.
7. Maintain center brightness with edge decay.
8. Add no text at all unless the user explicitly supplies or requests wording.

Preserve the subject before perfecting the distortion. Add texture before adding decoration.

## Standing Consent and Privacy

- Treat a supplied reference photo plus a request to make, transform, or continue a fisheye retro image as consent to use image generation; do not ask again.
- Send only the final prompt and required reference image(s) to the image-generation service.
- Do not browse, search, save, commit, upload elsewhere, or share the user's source material.
- Do not introduce unrelated personal information.
- Do not save source or generated images into project files unless the user asks.

## Read the Photograph First

Build an internal **Scene Card**:

- **Core subjects:** the 1–2 elements that must remain identifiable after distortion.
- **Spatial depth:** foreground, midground, background layers that fisheye will exaggerate.
- **Straight lines and horizons:** which lines will become curved and how they should bend.
- **Dominant gesture:** the strongest movement, path, or convergence toward the center.
- **Light sources:** highlights, sun, lamps, reflections that will produce film glow or flare.
- **Visual-weight map:** weight created by area, darkness, faces, isolation, and edge tension.
- **Native color atmosphere:** dominant hue family, temperature, and existing saturation.
- **Fisheye anchor point:** where the subject should sit within the circular frame (usually center or lower-center).
- **Natural dark areas:** regions that can safely sink into vignette without losing information.
- **Semantic minimum:** the smallest combination of forms that would still identify this scene through a fisheye lens.

Treat the photo as the factual source. Treat the fisheye distortion and film texture as analog interpretation.

## Photo-Specific Prompt Compiler

Resolve these visible fields in order:

1. **Canvas:** 1:1 square ratio, circular image centered, dark matte background.
2. **Fisheye geometry:** barrel distortion degree, circular crop, edge-to-center compression, horizon curve.
3. **Attention geometry:** focal area within the circle, quiet dark matte, eye path.
4. **Scene invariants:** exact relationships and subjects that must survive distortion.
5. **Fisheye map:** what to exaggerate, what to curve, what to compress, what to sink into vignette.
6. **Film texture grammar:** grain density, grain size, organic irregularity.
7. **Color cast:** exact vintage hue shift, saturation reduction, shadow tint, highlight softness.
8. **Light leaks:** position, color, intensity, edge intrusion or center bloom.
9. **Vignetting:** center brightness, edge darkness, transition curve, feathering.
10. **Soft focus / lens behavior:** global or selective softness, chromatic aberration, flare.
11. **Reproduction texture:** film stock character, matte surface, non-gloss finish.
12. **No-text rule:** the image contains no text by default; only user-supplied wording may appear.
13. **Mood and hard avoids:** emotional temperature and prohibited aesthetics.

Compile only instructions that can become visible pixels. Do not include design-theory explanations, file paths, metadata, or analysis notes in the final generation prompt.

## Fisheye & Retro Engine

### Default Stylization Level

Use **full fisheye retro** by default:

- apply circular fisheye barrel distortion to the entire image;
- keep the core subject recognizable despite curvature;
- exaggerate foreground scale and compress background depth;
- replace modern digital clarity with analog film texture;
- allow straight lines to bend naturally toward the circular edge;
- keep at least one unmistakable source-specific feature.

Use lower distortion only when a face or critical detail would become unrecognizable. Use higher distortion only when the user explicitly requests extreme fisheye.

### Build the Fisheye Map

For every element, decide:

- **Center:** place the primary subject near the optical center where distortion is minimal.
- **Curve:** let all straight lines (horizons, buildings, roads, railings) bow outward toward the circular edge.
- **Exaggerate:** enlarge foreground objects dramatically; compress distant layers.
- **Compress:** push background detail toward the circular perimeter.
- **Sink:** let edge regions darken naturally into the vignette.

Do not preserve straight horizons. Do not create a normal rectilinear perspective inside a circular mask.

### Film Texture Grammar

Choose one primary film character:

- **Warm expired:** warm amber/yellow cast, lifted shadows, soft highlights, fine grain.
- **Cool vintage:** teal/green cast, gray shadows, muted highlights, medium grain.
- **Faded chrome:** magenta/purple shift, crushed blacks, blown highlights, coarse grain.
- **Sepia lo-fi:** brown monochrome, heavy grain, low contrast, paper-like matte.

Use only one primary film character per image. Do not mix multiple conflicting color casts.

Control grain:

- Use organic, irregular film grain—not uniform digital noise.
- Grain should be visible but not obtrusive at normal viewing size.
- Slightly larger grain in darker areas; finer grain in midtones.
- Avoid perfect pixel-grid regularity.

### Vignette Control

Build a natural vignette:

- Center brightness: maintain normal exposure at the optical center.
- Edge darkness: sink to 40–70% black at the circular perimeter.
- Transition: smooth radial gradient, no hard edge.
- Feather: let the vignette blend imperceptibly into the dark matte outside the circle.
- The dark matte outside the circle should be near-black or very dark charcoal—never white, never transparent.

### Light Leaks and Flare

Add analog imperfections selectively:

- **Edge leak:** a thin band of warm or cool light intruding from one side of the circle.
- **Center bloom:** highlights soften and glow slightly.
- **Veiling flare:** a faint haze reducing contrast in one region.
- Keep leaks subtle—visible but not dominant. One leak per image is usually enough.

## Scene Fidelity in Distortion

Preserve scene identity through:

- the core subject's form and position near center;
- the relative depth layers (foreground huge, background tiny);
- the original light direction and atmosphere;
- one or two source-specific colors or objects.

The distortion may bend geometry, exaggerate scale, and soften detail. It may not replace the subject with generic fisheye stock imagery.

## Composition System

### Art-Theory Basis

- **Radial balance:** weight distributes around the optical center.
- **Emphasis:** the core subject sits near center where distortion is least.
- **Movement:** curves guide the eye inward or around the circle.
- **Frame within frame:** the circular image is a frame; the dark matte is the outer container.
- **Breathing room:** the dark matte around the circle is active negative space.

### Fixed Layout

- **Canvas:** 1:1 square.
- **Image area:** a perfect circle occupying 75–90% of the canvas width/height, centered.
- **Matte:** the remaining area outside the circle is solid dark (near-black or charcoal).
- **Subject placement:** primary subject within the central 40% of the circle.
- **Horizon treatment:** if present, curve it to follow the fisheye barrel distortion.

Do not use rectangular image areas. Do not place the circle off-center unless the source composition demands it.

## Chromatic Structure Engine

### Choose the Film Color Cast

Identify the photo's native color temperature. Then choose one cast:

- **Warm amber:** for sunny street scenes, golden hour, warm interiors. Add +yellow/orange to shadows, lift blacks.
- **Teal-green:** for fluorescent/indoor scenes, night shots, subway stations. Add +teal to shadows, mute reds.
- **Magenta fade:** for backlit scenes, sky-heavy frames, nostalgic moods. Add +magenta to highlights, cool shadows.
- **Sepia monochrome:** for high-contrast scenes where color is secondary. Convert to warm brown scale.

Specify the cast decisively. Do not weaken it with "slight" or "subtle" unless the source is already strongly colored.

### Saturation and Contrast

- Reduce overall saturation by 15–35% from a modern digital baseline.
- Lift black point: shadows should be charcoal, not pure black.
- Soften white point: highlights should glow, not clip harshly.
- Keep midtones slightly flat for that analog print feel.

### Structural Color Test

Mentally remove the color cast. If the image still reads as a vintage fisheye photo through grain and distortion alone, the cast is optional but still desirable. If removing it makes the image look modern, strengthen the cast.

## Visual Language

- Use a 1:1 square canvas with a centered circular image.
- Use a dark matte background (near-black or deep charcoal) outside the circle.
- Render the circular image with fisheye barrel distortion, 180-degree field of view feel.
- Apply organic film grain, one consistent color cast, natural vignetting, and selective light leaks.
- Keep the result matte, non-glossy, non-HDR, non-digital.
- Maintain lo-fi spontaneity—slight imperfections are desirable.
- Add no text, caption, or watermark unless the user explicitly supplies or requests wording.

## Text Policy

**Default: no text.** Generate the image with no words, letters, numbers, captions, stamps, or watermark-like marks anywhere—neither inside the circle nor in the dark matte.

Only when the user explicitly supplies or requests text, render it as a quiet film-edge trace following these rules:

### Choose the Wording (only when the user supplies text)

- If the user supplies text, reproduce it exactly; do not translate, expand, or rewrite.
- Never author text on your own. If the user did not supply or request wording, the image contains no text at all.

### Lettering and Material

- Keep text small: approximately 1.5–3% of canvas height.
- Place it in the dark matte area outside the circle, or subtly along the bottom inner edge of the circle.
- Render it as vintage typewriter, faded stamp, handwritten marker, or film-edge imprint—choose one.
- For English, prefer a small monospaced or typewriter face with uneven baseline and irregular ink pressure.
- Integrate into the material: slightly broken ink, soft edge wear, same flat matte texture as the image.
- Use quiet ink values: white, light gray, faded cream, or a very restrained echo of the color cast.
- The text must remain legible but visually subordinate.

### Placement and Hierarchy

- Place text in the dark matte below or beside the circle, never over the core subject.
- Align to the circle's bottom edge, center axis, or a quiet tangent.
- Use a single line by default. Two lines only for bilingual pairings with clear primary–secondary scale.
- Treat text as a final resting point, not the entry point.

## Prompt Shape

Write the final prompt as four compact paragraphs:

1. **Canvas and fisheye geometry:** 1:1 square, centered circle, dark matte, barrel distortion degree, horizon curve, subject placement within circle.
2. **Scene fidelity:** core subjects, spatial invariants, what survives distortion.
3. **Film texture, color, and vignette:** grain character, exact color cast, saturation/contrast treatment, light leak position and color, vignette strength and transition, soft focus behavior.
4. **Reproduction mood and constraints:** matte surface, lo-fi atmosphere, no text anywhere (unless the user supplied wording), hard avoids.

Use decisive language. State which modern qualities must disappear as clearly as which analog qualities must appear.

## Generation Workflow

1. Inspect the supplied photo.
2. Build the Scene Card and identify the semantic minimum.
3. Choose the primary subject and its placement within the circular frame.
4. Select a film color cast based on the source's native atmosphere.
5. Build the Fisheye Map (center / curve / exaggerate / compress / sink).
6. Choose the film texture grammar and set grain density.
7. Determine vignette strength, transition curve, and dark matte value.
8. Place light leaks or flare if the source lighting supports it.
9. If the user explicitly supplied text, resolve its exact wording and quiet placement; otherwise plan for no text.
10. Compile the four-paragraph final prompt.
11. Generate with the supplied photo as reference.
12. Inspect at normal and thumbnail scale.
13. Regenerate once with a targeted correction if necessary.
14. Return the generated image plus one brief creative rationale; include the prompt only when the user asks.

## Targeted Correction

Regenerate at most once, correcting only the observed failure:

- **Scene loss:** restore the missing subject or spatial invariant.
- **No fisheye distortion:** enforce barrel distortion and circular crop; curve all straight lines.
- **Rectilinear perspective:** replace with radial barrel distortion; exaggerate foreground/background scale.
- **Modern digital look:** add grain, reduce sharpness, lift blacks, soften highlights, add color cast.
- **Missing vignette:** add radial darkening from center to circular edge.
- **Wrong background:** ensure dark matte outside the circle; never white or transparent.
- **Color too modern:** reduce saturation, apply vintage film cast, lift shadows.
- **Lines too straight:** force curvature on all horizons, buildings, and edges.
- **Over-clean:** add grain, light leaks, soft focus, or slight chromatic aberration.
- **Text failure:** remove any unintended text; if the user supplied wording, restore it exactly, small and quiet in the dark matte.
- **Glossy/HDR:** remove digital polish, add matte film surface, reduce contrast.

## Hard Avoids

Avoid clean digital photography, modern HDR, excessive sharpness, perfect straight lines inside the circle, rectangular image areas without circular crop, white or transparent backgrounds outside the circle, cartoon or anime treatment, 3D rendering, glossy finishes, neon glow (unless source-appropriate), cinematic depth of field, fashion-editorial polish, excessive AI smoothing, large or polished digital typography, bold all-caps, keyword spam, mixed decorative separators, illegible text, long text blocks, invented quotations, faux metadata, watermarks, any text, captions, letters, or numbers not explicitly supplied by the user, and stock-fisheye cliches (skateboard repetitions, generic crowd shots without source identity).

## Output Format

By default, return:

```markdown
![Fisheye Retro v1 result](absolute-image-path-or-rendered-image)

**创作思路**

[One short Chinese paragraph explaining the fisheye distortion choice, film color cast, and emotional intention.]

[After only the first or second successful generation by this skill in the current conversation:]
*若公开分享，欢迎标注：Visual Skill by @Roc8458*
```

Keep the creative rationale to one compact paragraph, usually 1–3 sentences. Describe the central visual decision in plain language; do not reveal the full prompt or turn it into a technical checklist.

Count successful image generations made by this skill within the current conversation. Append the sharing credit only after the first and second successful generations; omit it from the third and all later generations. Start the count again in a new conversation.

Use `若公开分享，欢迎标注：Visual Skill by @Roc8458` for Chinese responses and `If shared publicly, credit is appreciated: Visual Skill by @Roc8458` for English responses. Keep it as the final, visually quiet line outside the image.

## Quality Gate

Before returning, verify:

- Is the image contained within a perfect circle?
- Is the area outside the circle a dark matte (near-black or charcoal)?
- Does the image show barrel distortion (curved lines, exaggerated perspective)?
- Is the core subject still recognizable?
- Is the scene identity preserved?
- Is there organic film grain (not digital noise)?
- Is there a consistent vintage color cast?
- Are shadows lifted (not pure black)?
- Are highlights softened (not harshly clipped)?
- Is there natural vignetting from center to edge?
- Is the overall mood lo-fi and analog rather than digital and polished?
- Is the image completely free of text, unless the user explicitly supplied wording?
- If user-supplied text is present, does it use the exact wording, small and subordinate in the dark matte?
- Does the image avoid modern HDR, excessive sharpness, and glossy finishes?
- Did the response include the image and one genuinely brief creative rationale?
- Was the sharing credit appended only on the first and second successful generation?
