# Fisheye Retro Skill

An OpenAI Codex skill that transforms any photo into a **circular fisheye lens + retro film** aesthetic.

![cover](assets/brand/cover.png)

## Style Features

- **Circular fisheye frame**: 180° barrel distortion, circular crop, natural vignette falloff
- **Retro film texture**: organic grain, color cast (warm amber / teal-green / faded magenta), light leaks, soft focus
- **Lo-fi street vibe**: raw, spontaneous, unpolished, analog feel
- **Dark matte**: solid near-black / deep charcoal surrounding the circle
- **Micro-text (on by default, can be turned off)**: a quiet line of small English text on the dark matte as a film-edge trace; user can say "no text", "Chinese text", or provide custom wording

## Installation

1. Make sure [OpenAI Codex](https://github.com/openai/codex) is installed
2. Clone this repo:
   ```bash
   git clone https://github.com/Roc8458/fisheye-retro-skill.git
   ```
3. Copy the skill into Codex's skills directory:
   ```bash
   cp -R fisheye-retro-skill/skills/fisheye-retro-v1 ~/.codex/skills/
   ```
4. Restart Codex

## Usage

Upload a photo, then type:

```
$fisheye-retro-v1
```

Or describe what you want:

```
Turn this photo into a fisheye retro film style
```

## Examples

### Example 01 · Seaside Dusk

| Source | Fisheye retro result |
|--------|---------------------|
| ![source](examples/example-01/source.jpg) | ![result](examples/example-01/result.jpg) |

## How it works

This skill is pure prompt engineering, zero code. The core logic lives in `SKILL.md`; Codex reads it and drives its built-in image generation model to apply the stylization.

## License

MIT

## 中文说明

[中文文档请见 README.zh.md](README.zh.md)
