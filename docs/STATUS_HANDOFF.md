# STATUS_HANDOFF — DataForge Mini Research 04 (2026-10-25)

## Repository and phase
- Repo: https://github.com/rikkurea-boop/dataforge-mini — private.
- Docs branch: `docs/project-charter-ai-handoff`, open PR #1 https://github.com/rikkurea-boop/dataforge-mini/pull/1; main remains at initial README as verified at R04 start.
- R04 modified documentation **only**; no source `.py`, dataset `.csv`, requirement file, tests, PDF or video created. No app run or pytest pass.
- No changes to Data-Forge origin repository. No PR merge or visibility changes.

## Status (7 research + 1 final)
| Stage | Status | Output |
|---|---|---|
| R01 | DONE | Instructor requirements, self-assessment 3+2+2+1+2 |
| R02 | DONE | One-page MVP, one synthetic 12-row dataset spec, three Matplotlib charts |
| R03 | DONE | 3 planned Python modules, 5 data/3 chart contracts |
| R04 | **DONE — SPEC/MATH QA** | Independent oracle, ddof0, missing/infinity/group/duplicates/chart logic and OR-01..OR-15 |
| R05 | **NEXT** | QA test case design, dependency/runtime policy, errors/fresh clone |
| R06 | NOT STARTED | PDF report 15–20 pages, YouTube demo outline, self-assessment evidence |
| R07 | NOT STARTED | AI handoff/rules/implementation work prompts |
| FINAL | NOT STARTED | Cross-review and optional READY FOR IMPLEMENTATION |
| P0–P4 | **BLOCKED** | Only after user's explicit implementation instruction |

## What R04 checked
- Read all 8 GitHub branch files and verified current PR state.
- Manually/reproducibly recalculated CSV in PROJECT_SPEC §5 in temporary pandas 2.2.3/NumPy 2.3.5, NOT app code.
- Raw: 12x4, 2 exact duplicates, 2 missing; cleaned: 10x4, fill medians `gio_hoc=4`, `diem=8`. Mean grade7.8, group A8/B7.6, score>=8 for 6 rows, mean hours4.4.
- Exact population variance 1.56, std=sqrt(1.56)=1.24899959968 (`ddof=0`), sample std=1.31656117721 solely for comparison.
- Histogram 5 equal bins [2,2,3,2,1]; group bar Y from 0; scatter raw/clean 10 complete pairs each.
- Locked all-NA and singleton numeric handling, missing group key omission, no artificial zero bar, infinity rejection, imputation-induced duplicate and no second dedup pass.
- R04 future checks **OR-01..OR-15** detailed at `PROJECT_SPEC.md §11`, docs references recorded at `docs/REQUIREMENTS.md §11`.
- Claims are research and numerical expected values, **not tests passing in DataForge Mini**.

## Still unknown and next
- Teacher deadline, video duration, PPT requirement — UNKNOWN.
- R05: choose Python/pip compatibility, test cases based on OR-01..15, dataset loading errors, no-number/file-empty failure, plot verification, fresh environment; **only update docs, no test/app file yet**.
- R06: PDF/YouTube/self-assessment plan.
- User will authorize implementation only after all 7 research turns and FINAL review.

## Metadata
- Date 2026-10-25; branch `docs/project-charter-ai-handoff`, PR #1.
- Current exact SHA: read from PR head (the branch may continue to receive commits).
- Files changed R04: PROJECT_SPEC.md, docs/PLAN.md, docs/REQUIREMENTS.md, RULEBOOK.md, docs/STATUS_HANDOFF.md, README.md.
