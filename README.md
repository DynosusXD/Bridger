# Bridger

Short script which bridges language gap between two people connected by just the screen, internet, and a fcked sleep schedule.

## the story

I had a friend who didn't know English, and I didn't know Vietnamese. Texting back and forth through Google Translate felt clunky, lost the tone half the time, and honestly killed the vibe of a conversation. So I made Bridger.

v1 was hardcoded to just Vietnamese. This is v2 — now you pick the language once at the start, and it figures out the rest.

## what it does

This isn't your generic word-for-word translator. It uses AI to actually preserve tone and the core idea behind what you're saying, not just swap words around.

- Pick a language once when you start the script
- After that, it auto-detects direction — type in English, it translates to your chosen language; type in your chosen language, it translates to English
- No need to flip a "from/to" setting every message, it just understands
- Type `0` to exit

## setup

You'll need a Gemini API key. Get one from [Google AI Studio](https://aistudio.google.com/apikey).

```bash
pip install google-genai
```

Then either:

**Option A — paste it directly in the script** (quick and dirty)

Replace `YourGeminiAPI` in `Bridger.py` with your actual key:

```python
client = genai.Client(api_key="your-actual-key-here")
```

**Option B — use an environment variable** (cleaner, recommended)

Set the `GEMINI_API_KEY` environment variable:

```bash
export GEMINI_API_KEY="your-actual-key-here"
```

Then drop the `api_key` argument entirely — the client picks it up automatically:

```python
client = genai.Client()
```

## usage

```bash
python Bridger.py
```

```
Enter Language: German
Enter Text: How was your day?
Wie war dein Tag?
Enter Text: Mir geht's gut, danke!
I'm doing well, thanks!
Enter Text: 0
```

That's it. One language picked, both directions covered.
