"""Grava cada palavra do app com uma voz neural (edge-tts) e embute o áudio no index.html.

Uso:  python gerar_audio.py
Requer: pip install edge-tts  (e internet na hora de gerar)
"""
import asyncio, base64, json, re, sys
from pathlib import Path

import edge_tts

VOICE = "en-US-AnaNeural"     # voz de criança; en-US-JennyNeural é a adulta amigável
HERE = Path(__file__).parent
HTML = HERE / "index.html"
CACHE = HERE / "audio"          # mp3 ficam aqui para não gerar de novo
CACHE.mkdir(exist_ok=True)

html = HTML.read_text(encoding="utf-8")

# primeira posição de cada trio ['en', 'pt', 'emoji'] dentro de DATA
data_block = html[html.index("const DATA = ["): html.index("];", html.index("const DATA = [")) + 2]
words = re.findall(r"""\[\s*(?:'([^']*)'|"([^"]*)")\s*,\s*'""", data_block)
words = [a or b for a, b in words]
words = list(dict.fromkeys(words))
vb = html[html.index("/*VERBS-START*/"): html.index("/*VERBS-END*/")]
words += re.findall(r""":\s*'([^']*)'""", vb)
words = list(dict.fromkeys(words))
print(f"{len(words)} palavras encontradas")


def safe_name(w: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", w.lower()).strip("_") or "x"


async def gen(word: str, sem: asyncio.Semaphore) -> None:
    out = CACHE / f"{safe_name(word)}.mp3"
    if out.exists() and out.stat().st_size > 0:
        return
    text = word.replace("...", "")
    async with sem:
        for attempt in range(3):
            try:
                await edge_tts.Communicate(text, VOICE, rate="-10%").save(str(out))
                print("  ok ", word)
                return
            except Exception as e:  # noqa: BLE001
                print(f"  tentativa {attempt + 1} falhou em '{word}': {e}")
                await asyncio.sleep(2)
        sys.exit(f"Não consegui gerar '{word}'")


async def main() -> None:
    sem = asyncio.Semaphore(4)
    await asyncio.gather(*(gen(w, sem) for w in words))


asyncio.run(main())

audio = {}
for w in words:
    b = (CACHE / f"{safe_name(w)}.mp3").read_bytes()
    audio[w] = "data:audio/mpeg;base64," + base64.b64encode(b).decode()

payload = json.dumps(audio, ensure_ascii=False, separators=(",", ":"))
start, end = "<!--AUDIO-START-->", "<!--AUDIO-END-->"
i, j = html.index(start), html.index(end) + len(end)
new_block = f'{start}\n<script id="audio-data" type="application/json">{payload}</script>\n{end}'
HTML.write_text(html[:i] + new_block + html[j:], encoding="utf-8")
print(f"embutido: {len(payload) / 1024:.0f} KB de áudio em {HTML.name}")
