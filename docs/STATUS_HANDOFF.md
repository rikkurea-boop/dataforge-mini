# STATUS_HANDOFF — DataForge Mini Research 05 (2026-10-25)

## Repo and permission gate
- Repo: https://github.com/rikkurea-boop/dataforge-mini — private.
- Docs branch: `docs/project-charter-ai-handoff` within open PR #1 https://github.com/rikkurea-boop/dataforge-mini/pull/1; `main` still initial README at start of R05.
- Research-only phase: zero app source, test code, dataset CSV, requirements, report PDF or YouTube video created. No installed app/runtime tests or pytest result. No change to original Data-Forge repo.
- User requires **7 research sessions + FINAL** completed AND new explicit user authorization before implementation P0–P4.

## Stage status
| Stage | State | Outcome |
|---|---|---|
| R01 | DONE | Teacher F01–F06, link to code/video, PDF 15–20 pages <=100MB, self-assessment 3+2+2+1+2 |
| R02 | DONE | Constrained CSV→Pandas→NumPy→Matplotlib MVP; 12→10 sample oracle |
| R03 | DONE | 3 Python app files planned, 5 analysis + 3 charts functions |
| R04 | DONE | Math/stat/chart correctness; OR-01..15, population std ddof0 |
| R05 | **DONE — QA DESIGN ONLY** | Python3.13 target; PyPI/current API review; OR-01..15 test designs, IO-01..10, UI-01..06; venv + acceptance gates |
| R06 | **NEXT** | PDF report outline 15–20 pages, YouTube demo storyboard, evidence artifacts and self-assessment |
| R07 | NOT STARTED | AI handoff rules/tasks/code prompts |
| FINAL | NOT STARTED | Cross-review, READY FOR IMPLEMENTATION only if clean |
| P0–P4 | **BLOCKED** | Only after owner explicitly requests coding |

## Specific R05 findings
- Latest Python is NOT automatically target: prefer CPython 3.13 stable classroom runtime. PyPI metadata for current NumPy, pandas, Matplotlib, Streamlit and pytest assessed; **no combined installation verified**. Exact pinned versions must be selected and smoke-tested in P0.
- Important bug class: Pandas 3.x infers string dtype `str` rather than `object`; app must still discover `lop` and group bar.
- Strong separation between developer QA and course deliverables: Python scripts and tests are NOT yet created.
- Bound project CSV uploader to <=2MiB; the 100MB form limit applies only to report PDF.
- Planned Windows/macOS/Linux venv commands, `pip check`, version log, unit/figure test vs manual Streamlit GUI smoke.
- Tests: OR-01..15 from R04 mapped to precise assertions; IO-01..10 for empty/corrupt/encoding/oversized/header/export; UI-01..06 for app transitions; full descriptions at `PROJECT_SPEC.md §12`.
- No claim that all malformed CSV are detected by Pandas; short rows can become NA. No app deployment, browser automation, login, ML or DB added.
- README/Rules/Spec/Plan/Requirements/Handoff updated, PR remains unmerged (recheck state at start of R06).

## Important unresolved items
- R06: detailed page-level PDF plan, demo video flow, screenshots/evidence, self-assessment template; URLs tested only at submission.
- Teacher deadline, video duration and any PPT requirement not visible in screenshots remain UNKNOWN.
- R07: concise AI bootstrap/checklist; FINAL cross-document inconsistencies and release decision.

## Next task (only one)
**R06 — research deliverable planning only:** 15–20 page PDF outline, YouTube demo storyboard and shot list, self-review draft framework grounded in five criteria; verify precise form constraints from REQUIREMENTS without inventing rubric. No creation of final PDF/YouTube video yet.

## Handoff metadata
- Date 2026-10-25; docs branch `docs/project-charter-ai-handoff`, PR #1.
- Latest R05 commit SHA: read branch PR head; don't copy stale SHA forward.
- Files modified R05: PROJECT_SPEC.md, docs/PLAN.md, docs/REQUIREMENTS.md, RULEBOOK.md, docs/STATUS_HANDOFF.md, README.md.
- QA test plan completed, not software tests passed.
