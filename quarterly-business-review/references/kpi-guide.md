# KPI Guide

QBR에서 자주 사용되는 KPI 정의와 계산 방법.

## Financial KPIs

| KPI | 정의 | 계산식 |
|-----|------|--------|
| Revenue | 총 매출 | 총 판매액 합계 |
| MRR | Monthly Recurring Revenue | 월간 반복 매출 합계 |
| ARR | Annual Recurring Revenue | MRR x 12 |
| Gross Margin | 매출 총이익률 | (매출 - 매출원가) / 매출 x 100 |
| Operating Margin | 영업이익률 | 영업이익 / 매출 x 100 |
| Net Margin | 순이익률 | 순이익 / 매출 x 100 |
| EBITDA | 세전영업이익 | 영업이익 + 감가상각비 |
| Burn Rate | 월간 현금 소진율 | 월초 현금 - 월말 현금 |
| Runway | 잔여 운영 기간 | 보유 현금 / Burn Rate |
| CAC | Customer Acquisition Cost | 마케팅+영업 비용 / 신규 고객 수 |
| LTV | Customer Lifetime Value | ARPU x 평균 고객 유지 기간 |
| LTV/CAC Ratio | 고객 가치 대비 획득 비용 | LTV / CAC (3.0 이상 양호) |

## Growth KPIs

| KPI | 정의 | 계산식 |
|-----|------|--------|
| QoQ Growth | 전분기 대비 성장률 | (당분기 - 전분기) / 전분기 x 100 |
| YoY Growth | 전년 동기 대비 성장률 | (당분기 - 전년 동기) / 전년 동기 x 100 |
| CAGR | 연평균 성장률 | (최종값/초기값)^(1/기간) - 1 |
| Net Revenue Retention | 순 매출 유지율 | (기존고객 당기매출) / (기존고객 전기매출) x 100 |

## Product / Operations KPIs

| KPI | 정의 | 계산식 |
|-----|------|--------|
| DAU / MAU | 일간/월간 활성 사용자 | 기간 내 고유 활성 사용자 수 |
| DAU/MAU Ratio | 사용자 점착도 | DAU / MAU (0.2 이상 양호) |
| Churn Rate | 이탈률 | 이탈 고객 / 기초 고객 x 100 |
| Retention Rate | 유지율 | 1 - Churn Rate |
| Conversion Rate | 전환율 | 전환 수 / 방문자(또는 리드) 수 x 100 |
| ARPU | Average Revenue Per User | 총 매출 / 활성 사용자 수 |
| NPS | Net Promoter Score | 추천자(%) - 비추천자(%) |
| SLA Compliance | SLA 준수율 | SLA 충족 건수 / 전체 건수 x 100 |

## 비교 표현 규칙

- **QoQ**: 전분기 대비 → `(Q_current - Q_previous) / Q_previous x 100`
- **YoY**: 전년 동기 대비 → `(Q_current - Q_same_last_year) / Q_same_last_year x 100`
- 양수는 `+`, 음수는 `-`로 표시 (예: +12.5%, -3.2%)
- 목표 달성률: `실적 / 목표 x 100` (예: 95.3%)
