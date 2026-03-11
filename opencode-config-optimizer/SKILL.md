---
name: opencode-config-optimizer
description: "OpenCode/oh-my-opencode 추론 강도 및 속도/비용 프로파일을 일관되게 적용하는 운영 스킬. '설정 최적화 적용', 'reasoning profile', 'opencode profile', '추론 강도 매핑' 키워드에서 사용."
---

# OpenCode Config Optimizer

OpenCode/oh-my-opencode/Claude 설정을 반복 가능하게 최적화한다.

## Scope

- `~/.config/opencode/opencode.json`
- `~/.config/opencode/oh-my-opencode.json`
- `~/.claude/settings.json`

## Profiles

### 1) `fast`

- 목적: 응답속도/비용 최적화
- 적용:
  - `opencode.provider.openai.options.reasoningEffort = low`
  - `claude.alwaysThinkingEnabled = false`
  - categories:
    - `quick = low`
    - `unspecified-low = low`
    - `unspecified-high = medium`
    - `ultrabrain = high`
  - agents:
    - `plan = medium`
    - `hephaestus = medium`
    - `oracle = high`
    - `librarian = low`

### 2) `balanced`

- 목적: 품질/비용 균형 (권장 기본)
- 적용:
  - `opencode.provider.openai.options.reasoningEffort = low`
  - `claude.alwaysThinkingEnabled = false`
  - categories:
    - `quick = low`
    - `unspecified-low = medium`
    - `unspecified-high = high`
    - `ultrabrain = xhigh`
  - agents:
    - `plan = high`
    - `hephaestus = high`
    - `oracle = xhigh`
    - `librarian = low`

### 3) `deep`

- 목적: 복잡 문제 해결/아키텍처/보안 검토
- 적용:
  - `opencode.provider.openai.options.reasoningEffort = high`
  - `claude.alwaysThinkingEnabled = true`
  - categories:
    - `quick = medium`
    - `unspecified-low = high`
    - `unspecified-high = xhigh`
    - `ultrabrain = xhigh`
  - agents:
    - `plan = xhigh`
    - `hephaestus = xhigh`
    - `oracle = xhigh`
    - `librarian = medium`

## Workflow

1. 백업 파일 생성 (`*.bak.profile-<timestamp>`)
2. 프로파일 적용
3. JSON 파싱 검증 (`python -m json.tool`)
4. 변경 diff 요약 출력

## Command

스킬 번들 스크립트 사용:

```bash
~/.claude/skills/opencode-config-optimizer/scripts/opencode-reasoning-profile balanced
```

## Safety

- JSON 파싱 실패 시 즉시 중단
- 미존재 key는 생성하지 말고 경고 출력 후 스킵
- 사용자가 요청하지 않은 provider/model 삭제 금지
