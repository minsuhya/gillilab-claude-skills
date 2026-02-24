# 화성 가이드 (Harmony Guide)

초급자를 위한 코드 구성과 진행 패턴 레퍼런스.

## 음계와 조성 (Key & Scale)

### Major Scale (장음계)

전전반전전전반 (W W H W W H) 간격으로 구성.

| 조성 | 음계 | 조표 |
|------|------|------|
| C Major | C D E F G A B | 없음 |
| G Major | G A B C D E F# | #1 |
| D Major | D E F# G A B C# | #2 |
| F Major | F G A Bb C D E | b1 |
| Bb Major | Bb C D Eb F G A | b2 |
| A Major | A B C# D E F# G# | #3 |
| Eb Major | Eb F G Ab Bb C D | b3 |

### Minor Scale (단음계)

자연단음계: 전반전전반전전 (W H W W H W W)

| 조성 | 음계 | 관계 장조 |
|------|------|-----------|
| Am | A B C D E F G | C Major |
| Em | E F# G A B C D | G Major |
| Dm | D E F G A Bb C | F Major |
| Bm | B C# D E F# G A | D Major |

## 다이어토닉 코드 (Diatonic Chords)

음계 위에 3도씩 쌓아 만드는 자연스러운 코드.

### Major Key 다이어토닉 (C Major 예시)

| 도수 | 코드 | 기능 | 한국어 |
|------|------|------|--------|
| I | C | Tonic | 으뜸화음 |
| ii | Dm | Subdominant | 윗으뜸화음 |
| iii | Em | Tonic (대리) | 중간음화음 |
| IV | F | Subdominant | 버금딸림화음 |
| V | G | Dominant | 딸림화음 |
| vi | Am | Tonic (대리) | 나란한화음 |
| vii° | Bdim | Dominant (대리) | 이끎음화음 |

### Minor Key 다이어토닉 (Am 예시)

| 도수 | 코드 | 기능 |
|------|------|------|
| i | Am | Tonic |
| ii° | Bdim | Subdominant |
| III | C | Tonic (대리) |
| iv | Dm | Subdominant |
| v/V | Em/E | Dominant |
| VI | F | Subdominant (대리) |
| VII | G | Dominant (대리) |

## 자주 쓰는 코드 진행

### Major Key 진행

| 이름 | 도수 | C Major 예시 | 분위기 |
|------|------|--------------|--------|
| Pop Progression | I-V-vi-IV | C-G-Am-F | 밝고 대중적 |
| 50s Progression | I-vi-IV-V | C-Am-F-G | 클래식 팝 |
| Canon Progression | I-V-vi-iii-IV-I-IV-V | C-G-Am-Em-F-C-F-G | 웅장, 감동 |
| Folk | I-IV-V-I | C-F-G-C | 단순, 밝음 |
| Axis | vi-IV-I-V | Am-F-C-G | 감성적 |
| Royal Road | IV-V-iii-vi | F-G-Em-Am | J-pop 감성 |

### Minor Key 진행

| 이름 | 도수 | Am 예시 | 분위기 |
|------|------|---------|--------|
| Natural Minor | i-VII-VI-VII | Am-G-F-G | 어둡고 서정 |
| Andalusian | i-VII-VI-V | Am-G-F-E | 비장, 플라멩코 |
| Minor Pop | i-VI-III-VII | Am-F-C-G | 어둡지만 팝 |
| Dramatic | i-iv-V-i | Am-Dm-E-Am | 긴장-해결 |

## 7th 코드 확장

기본 3화음에 7도를 추가하여 풍성한 사운드를 만든다.

| 기본 코드 | 7th 확장 | 사운드 특성 |
|-----------|----------|-------------|
| C (I) | Cmaj7 | 부드럽고 재즈적 |
| Dm (ii) | Dm7 | 따뜻한 마이너 |
| G (V) | G7 | 강한 해결감 |
| Am (vi) | Am7 | 감성적 |

## 전조 (Modulation) 기초

| 유형 | 설명 | 예시 |
|------|------|------|
| 근친조 전조 | 조표 1개 차이 조로 이동 | C → G, C → F |
| 관계조 전조 | 장조 ↔ 관계단조 | C → Am |
| 반음 올림 전조 | 반음 위로 전조 (클라이맥스) | C → Db |
| 딸림음 전조 | V도를 새 조의 I도로 | C → G (G를 새 으뜸음) |
