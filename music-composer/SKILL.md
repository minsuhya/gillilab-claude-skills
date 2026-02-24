---
name: music-composer
description: >
  음악 작곡 도우미. 코드 진행, 멜로디, 곡 구조를 설계하고 ABC notation 악보,
  MIDI 파일(Python midiutil), 코드 차트를 생성한다. 초급자도 이해할 수 있도록
  음악 이론 설명을 포함. "작곡", "곡 만들어", "멜로디", "코드 진행", "compose",
  "chord progression", "음악 만들기", "노래 만들기" 등의 키워드로 트리거.
---

# Music Composer 스킬

사용자의 요청에 따라 코드 진행, 멜로디, 곡 구조를 설계하고 다양한 형식으로 출력한다.

## 워크플로우

기본값: **C Major, 4/4박자, 120 BPM, 피아노**. 사용자가 지정하지 않은 항목에 적용한다.

1. **요구사항 파악**: 분위기, 장르, 템포, 조성, 용도 확인
2. **곡 구조 설계**: 섹션 구성 (Intro-Verse-Chorus-Bridge-Outro 등)
3. **코드 진행 생성**: 조성에 맞는 코드 진행 설계
4. **멜로디 작성**: 코드 위에 멜로디 라인 구성
5. **출력 생성**: ABC 악보, MIDI 파일, 코드 차트 중 선택 출력

## 출력 형식

### 1. 코드 차트 (기본, 항상 제공)

Markdown 테이블로 섹션별 코드 진행을 표기한다.

```markdown
## 코드 차트 - "곡 제목" (C Major, BPM 120)

### Verse
| 마디 1 | 마디 2 | 마디 3 | 마디 4 |
|--------|--------|--------|--------|
| C      | Am     | F      | G      |
```

### 2. ABC Notation 악보 (요청 시)

```abc
X:1
T:곡 제목
M:4/4
L:1/8
K:C
Q:1/4=120
|: C2 E2 G2 E2 | A2 c2 e2 c2 :|
```

ABC notation 주요 규칙:
- `X:` 곡 번호, `T:` 제목, `M:` 박자, `L:` 기본 음표 길이, `K:` 조성
- 음이름: `C D E F G A B` (소문자는 한 옥타브 위: `c d e f g a b`)
- 음표 길이: `C2`(2배), `C/2`(반), `C3/2`(점음표)
- 쉼표: `z`, 마디선: `|`, 반복: `|: :|`
- 샵: `^C`, 플랫: `_B`, 내추럴: `=C`

### 3. MIDI 파일 (요청 시)

`scripts/generate_midi.py`로 생성한다. `midiutil` 패키지가 필요하다 (`pip install midiutil`).
패키지 미설치 시 ABC notation과 코드 차트만 제공하고, MIDI 생성은 건너뛴다.

```bash
python3 scripts/generate_midi.py --key C --tempo 120 --chords "C Am F G" --output song.mid
```

옵션: `--key` 조성, `--tempo` BPM, `--chords` 코드 진행 (공백 구분), `--output` 출력 파일명, `--style` 반주 스타일 (block/arpeggio/rhythm)

## 레퍼런스

- **코드/화성 이론**: [references/harmony-guide.md](references/harmony-guide.md) - 조성, 코드 구성, 진행 패턴
- **장르별 패턴**: [references/genre-patterns.md](references/genre-patterns.md) - 장르별 코드/리듬/구조

## 사용자 정보가 부족할 때 확인 항목

- **분위기**: 밝은/어두운/몽환적/에너지틱/차분한
- **템포**: 느린(60-80), 보통(90-120), 빠른(130-180)
- **조성**: 기본값 C Major
- **용도**: 감상용, BGM, 연습곡, 노래
- **악기**: 피아노, 기타, 밴드 등

기본값은 워크플로우 섹션 상단 참조

비표준 박자(5/4, 7/8 등)는 지원하되, 미크로토널 등 ABC notation으로 표현 불가한 요소는 한계를 안내한다.

## 작성 규칙

- 코드명은 영어 표기 (C, Am7, Dm7, G7)
- 설명은 한국어, 이론 용어는 한영 병기 (예: "으뜸화음(Tonic)")
- 각 섹션의 코드 진행 의도를 간단히 설명
- 초급자를 위해 결정 과정마다 이론 설명 포함
