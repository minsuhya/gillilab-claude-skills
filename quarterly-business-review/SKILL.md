---
name: quarterly-business-review
description: >
  분기별 비즈니스 검토(QBR) 보고서를 Markdown으로 생성. CSV/Excel 데이터를 분석하여
  실적 요약, KPI 대시보드, 목표 대비 진척도, 리스크/기회 분석, 다음 분기 계획을 포함한
  표준 QBR 문서를 한영 혼용으로 작성. "QBR", "분기별 검토", "quarterly review",
  "분기 보고서", "비즈니스 리뷰" 등의 키워드로 트리거.
---

# Quarterly Business Review (QBR) 스킬

CSV/Excel 데이터를 기반으로 표준 QBR Markdown 보고서를 생성한다.

## 워크플로우

1. **데이터 수집**: 사용자로부터 CSV/Excel 파일 경로를 받는다
2. **데이터 분석**: `scripts/analyze_qbr_data.py`로 핵심 지표를 추출한다
3. **보고서 생성**: 분석 결과를 QBR 템플릿에 채워 Markdown 문서를 작성한다
4. **검토 및 보완**: 사용자 피드백을 반영하여 수정한다

## 데이터 분석

데이터 파일이 제공되면 `scripts/analyze_qbr_data.py`를 실행하여 요약 통계를 생성한다.

```bash
python3 scripts/analyze_qbr_data.py <data_file> [--quarter Q1|Q2|Q3|Q4] [--year 2024]
```

스크립트가 처리하는 데이터 형식:
- `.csv`, `.tsv`: pandas로 직접 로드 (인코딩: utf-8 시도 → 실패 시 cp949/euc-kr 자동 감지)
- `.xlsx`, `.xls`: openpyxl/xlrd를 통해 로드

스크립트 출력: JSON 형태의 요약 통계 (합계, 평균, 증감률, 상위/하위 항목)

다중 시트 Excel은 첫 번째 시트를 기본으로 분석하고, 사용자에게 시트 선택을 확인한다.

데이터 파일이 없거나 스크립트 실행이 어려운 경우, 사용자가 제공한 텍스트 정보를 기반으로 보고서를 작성한다.

결측값 처리: NaN이 포함된 행은 해당 지표에서 제외하고, 보고서에 "데이터 미비 N건" 주석을 추가한다.

## 보고서 구조

QBR 템플릿의 전체 구조는 [references/qbr-template.md](references/qbr-template.md)를 참조한다.

핵심 섹션 (순서 유지):

1. **Executive Summary** - 분기 핵심 성과 3-5줄 요약
2. **KPI Dashboard** - 주요 지표 테이블 (목표 vs 실적 vs 달성률)
3. **실적 상세 분석** - 카테고리별 성과 breakdown
4. **목표 대비 진척도** - 분기 목표별 상태 (On Track / At Risk / Off Track)
5. **Risk & Opportunity** - 리스크 요인과 기회 요인
6. **Action Items** - 다음 분기 핵심 과제와 담당자
7. **Appendix** - 상세 데이터 테이블

## 작성 규칙

- **언어**: 본문은 한국어, 지표명/차트 레이블/섹션 제목은 영어 병기
- **수치 표현**: 천 단위 콤마, 퍼센트는 소수점 1자리 (예: 1,234,567원, 95.3%)
- **비교 표현**: 전분기 대비(QoQ), 전년 동기 대비(YoY) 증감률 명시
- **상태 표시**: On Track, At Risk, Off Track (색상 이모지 미사용)
- **테이블**: Markdown 테이블 사용, 숫자는 우측 정렬

## KPI 가이드

주요 KPI 정의와 계산 방법은 [references/kpi-guide.md](references/kpi-guide.md)를 참조한다.

## 사용자 상호작용

데이터가 불충분할 때 확인할 항목:
- 분기 및 연도 (예: 2024 Q4)
- 비교 기준 (전분기, 전년 동기, 목표치)
- 핵심 KPI 목록 (매출, DAU, 전환율 등)
- 특이사항이나 강조할 성과
