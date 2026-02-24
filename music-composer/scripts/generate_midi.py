#!/usr/bin/env python3
"""코드 진행을 기반으로 MIDI 파일을 생성한다."""

import argparse
import sys

try:
    from midiutil import MIDIFile
except ImportError:
    print("Error: midiutil required. Install with: pip install midiutil", file=sys.stderr)
    sys.exit(1)

# 음이름 -> MIDI 번호 매핑 (4옥타브 기준)
NOTE_MAP = {
    "C": 60, "C#": 61, "Db": 61, "D": 62, "D#": 63, "Eb": 63,
    "E": 64, "F": 65, "F#": 66, "Gb": 66, "G": 67, "G#": 68,
    "Ab": 68, "A": 69, "A#": 70, "Bb": 70, "B": 71,
}

# 코드 타입 -> 루트 기준 반음 간격
CHORD_INTERVALS = {
    "":      [0, 4, 7],          # major
    "m":     [0, 3, 7],          # minor
    "7":     [0, 4, 7, 10],      # dominant 7th
    "maj7":  [0, 4, 7, 11],      # major 7th
    "m7":    [0, 3, 7, 10],      # minor 7th
    "dim":   [0, 3, 6],          # diminished
    "aug":   [0, 4, 8],          # augmented
    "sus2":  [0, 2, 7],          # suspended 2nd
    "sus4":  [0, 5, 7],          # suspended 4th
    "add9":  [0, 4, 7, 14],      # add 9th
    "m9":    [0, 3, 7, 10, 14],  # minor 9th
    "9":     [0, 4, 7, 10, 14],  # dominant 9th
    "maj9":  [0, 4, 7, 11, 14],  # major 9th
}


def parse_chord(chord_str: str) -> tuple[int, list[int]]:
    """코드 문자열을 파싱하여 (루트 MIDI 번호, 인터벌 리스트)를 반환."""
    # 루트 음 추출
    if len(chord_str) >= 2 and chord_str[1] in ("#", "b"):
        root_name = chord_str[:2]
        quality = chord_str[2:]
    else:
        root_name = chord_str[0]
        quality = chord_str[1:]

    root = NOTE_MAP.get(root_name)
    if root is None:
        raise ValueError(f"Unknown root note: {root_name}")

    intervals = CHORD_INTERVALS.get(quality)
    if intervals is None:
        raise ValueError(f"Unknown chord quality: {quality} (chord: {chord_str})")

    return root, intervals


def add_block_chord(midi, track, channel, root, intervals, time, duration, velocity=80):
    """블록 코드(동시 연주)를 추가."""
    for interval in intervals:
        midi.addNote(track, channel, root + interval, time, duration, velocity)


def add_arpeggio(midi, track, channel, root, intervals, time, duration, velocity=75):
    """아르페지오(분산 화음)를 추가."""
    note_dur = duration / len(intervals)
    for i, interval in enumerate(intervals):
        midi.addNote(track, channel, root + interval, time + i * note_dur, note_dur, velocity)


def add_rhythm(midi, track, channel, root, intervals, time, duration, velocity=80):
    """리듬 패턴(8분음표 스트럼)을 추가."""
    eighth = duration / 8
    pattern = [0, 0, 1, 0, 0, 1, 0, 1]  # 1=rest
    for i, rest in enumerate(pattern):
        if not rest:
            for interval in intervals:
                midi.addNote(track, channel, root + interval, time + i * eighth, eighth * 0.9, velocity)


def generate_midi(key: str, tempo: int, chords: list[str], output: str, style: str = "block"):
    midi = MIDIFile(1)
    midi.addTempo(0, 0, tempo)
    midi.addProgramChange(0, 0, 0, 0)  # Piano

    # 조성에 따른 옥타브 조정 (C4 기준)
    key_root = NOTE_MAP.get(key, 60)
    octave_shift = -12 if key_root >= 66 else 0  # 높은 키는 한 옥타브 내림

    style_fn = {"block": add_block_chord, "arpeggio": add_arpeggio, "rhythm": add_rhythm}.get(style, add_block_chord)

    time = 0
    beats_per_bar = 4
    for chord_str in chords:
        root, intervals = parse_chord(chord_str)
        root += octave_shift
        style_fn(midi, 0, 0, root, intervals, time, beats_per_bar)
        time += beats_per_bar

    with open(output, "wb") as f:
        midi.writeFile(f)

    print(f"MIDI file generated: {output}")
    print(f"  Key: {key}, Tempo: {tempo} BPM, Style: {style}")
    print(f"  Chords: {' -> '.join(chords)}")
    print(f"  Duration: {len(chords)} bars ({len(chords) * beats_per_bar} beats)")


def main():
    parser = argparse.ArgumentParser(description="Generate MIDI from chord progression")
    parser.add_argument("--key", default="C", help="Key signature (default: C)")
    parser.add_argument("--tempo", type=int, default=120, help="BPM (default: 120)")
    parser.add_argument("--chords", required=True, help="Chord progression (space-separated, e.g. 'C Am F G')")
    parser.add_argument("--output", default="output.mid", help="Output MIDI file path")
    parser.add_argument("--style", choices=["block", "arpeggio", "rhythm"], default="block", help="Accompaniment style")
    args = parser.parse_args()

    chord_list = args.chords.split()
    try:
        generate_midi(args.key, args.tempo, chord_list, args.output, args.style)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
