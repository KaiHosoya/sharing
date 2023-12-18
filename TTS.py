from pathlib import Path
from openai import OpenAI

client = OpenAI(api_key="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")

speech_file_path = Path(__file__).parent / "/Users/hosotanikai/Documents/TextToSpeech/CNBC/20231212.mp3"
response = client.audio.speech.create(
  model="tts-1",
  voice="alloy",
  input='''Most of today’s biggest music releases already come with a Dolby Atmos mix alongside the traditional stereo version, but Apple is apparently determined to increase the format’s adoption even further. Bloomberg is today reporting that the company is planning to give “added weighting” to songs that offer an Atmos mix; this could potentially increase the royalties that artists receive from Apple Music. Intriguingly, the report notes that “listeners wouldn’t necessarily have to play the Atmos version of a song for artists to benefit. It only matters that the song is offered in that format.”

The change in weighting hasn’t yet been announced by Apple. But with more and more artists and studios churning out spatial audio mixes like clockwork, it would make a lot of sense as the next logical step to help Atmos truly cross into the mainstream.

Tools for mixing songs in Atmos are increasingly prevalent across the industry; several weeks ago, Nilay and I visited Republic Records’ New York studio, where Ken “Duro” Ifill demonstrated the Atmos production process. A bunch of early Atmos music mixes were subpar and too spread out, but the quality on the whole has climbed substantially over the last couple of years as engineers continue to learn what works — and what doesn’t. They can still be hit or miss, but things are trending in the right direction.


Apple supports the format across its AirPods, iPhone, iPad, Mac, Apple TV, and HomePod devices. Other tech players, including Amazon and Sonos, also offer Atmos-optimized speakers, including the Echo Studio and Era 300, respectively, that are designed to showcase the format’s immersion. And spatial audio continues to be a selling point of more and more earbuds / headphones hitting the market.

Spotify, the leading subscription music service, still does not support spatial audio listening of any kind — nor has the company made good on its long-overdue promise to stream at lossless quality. But rumors have indicated that both features could appear in a new subscription tier priced above Spotify’s current Premium offering. It’s been a challenging period for Apple’s biggest competitor: last week Spotify announced mass layoffs, and the ouster of its CFO soon followed. The company has also been criticized for changes to its royalty structure.

It’s possible that Apple senses an opening amid all the upheaval, and this attempt to make Atmos more enticing to artists could help the company’s standing with artists and publishers. Of course, consumers are a different story, and Apple still hasn’t come close to matching Spotify’s big cultural moments like Spotify Wrapped.'''
)

response.stream_to_file(speech_file_path)