from pydub import AudioSegment
import math
import openai

def split_audio(file_path, segment_length=600):
    """
    音声ファイルを分割する関数
    :param file_path: 分割したい音声ファイルのパス
    :param segment_length: 分割後の各セグメントの長さ（秒）
    :return: 分割された音声ファイルのリスト
    """
    audio = AudioSegment.from_file(file_path)
    length_audio = len(audio)
    parts = math.ceil(length_audio / (segment_length * 1000))
    audio_chunks = []

    for i in range(parts):
        start = i * segment_length * 1000
        end = (i + 1) * segment_length * 1000
        chunk = audio[start:end]
        chunk_name = f"{file_path}_part{i}.mp3"
        chunk.export(chunk_name, format="mp3")
        audio_chunks.append(chunk_name)

    return audio_chunks

def transcribe_audio(file_path, output_file):
    """
    音声ファイルを文字起こしする関数
    :param file_path: 音声ファイルのパス
    :return: 文字起こしの結果
    """
    # OpenAIクライアントの初期化
    client = openai.OpenAI(api_key="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")

    # 音声ファイルを開く
    with open(file_path, 'rb') as audio_file:
        transcription_response = client.audio.transcriptions.create(
            model="whisper-1", 
            file=audio_file
        )

    # 正しい属性を使用して結果を取得
    transcription_text = transcription_response.text

    with open(output_file, "w") as text_file:
        text_file.write(transcription_text)


# 例: 音声ファイルを10分ごとに分割し、文字起こしを行う
audio_chunks = split_audio("/Users/hosotanikai/Documents/Transcription/TechCrunch/2023:12:18/Johann Kerbrat Robinhood.mp3", 600)
# transcriptions = [transcribe_audio(chunk) for chunk in audio_chunks]

for i, chunk in enumerate(audio_chunks):
    output_file = f"/Users/hosotanikai/Documents/Transcription/TechCrunch/2023:12:18/transcription_{i}.txt"
    transcribe_audio(chunk, output_file)
