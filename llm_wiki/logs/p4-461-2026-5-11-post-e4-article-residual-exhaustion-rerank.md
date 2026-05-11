# P4-461 Post-E4 Article Residual Exhaustion Rerank

Date: 2026-05-11
Parent surfaces:

- `logs/p4-325-2026-5-8-pcb-ziliao-per-pdf-coverage-index.md`
- `logs/p4-309-2026-5-8-pcb-ziliao-full-corpus-learning-and-usage-master-plan.md`
- `logs/p4-458-2026-5-11-e7-residual-route-reaudit-and-no-write-closeout.md`
- `logs/p4-459-2026-5-11-pcb-ziliao-continuation-rerank-and-tracker-correction.md`
- `logs/p4-460-2026-5-11-e4-mark-fiducial-route-reaudit-and-no-write-closeout.md`

Execution mode: `controller_owned_no_write_rerank`

## Purpose

Correct the continuation priority again after `P4-460`.

`P4-459` was accurate when the repo still had a plausible article-side rerank space.
After the `E4 Mark` re-audit, that broad article-side continuation wording is now too loose.

This pass does not land new `facts/`, `wiki/`, or `sources/registry/`.
It only refreshes the restart instruction so future AI does not keep treating article-side narrow recovery as an open-ended default class.

## Rechecked Surfaces

1. `P4-325` per-PDF states after `P4-460`
2. the `E7` no-write re-audit from `P4-458`
3. the `E4 Mark` no-write re-audit from `P4-460`
4. the continuation wording added by `P4-459`

## Findings

### 1. The article-side residual set is now much narrower than `P4-459` implies

Current `P4-325` non-`official_fact-backed` article rows are now only:

- `PCB板的Mark点设计对SMT重要性.pdf`
- `简单好用！再也不用担心PCB图形对齐问题.pdf`
- `华秋DFM可视化BOM交互焊接工具，SMT工厂、PCB工程师的福音来了！.pdf`
- `华秋DFM携带DFA全网重磅上线！新功能极速体验，一睹为快.pdf`
- `华秋干货铺：PCB设计避坑指南（图文结合、视频演示，荐读！）.pdf`

That means the broad article-side rerank space is no longer a general pool across controller-routed PDFs.

### 2. All five of those current article residual rows are already re-audited closed at the present authority layer

- `P4-460` re-audited `PCB板的Mark点设计对SMT重要性.pdf` and kept it route-only.
- `P4-458` re-audited the current `E7` residual set and kept:
  - `简单好用！再也不用担心PCB图形对齐问题.pdf` at route-only
  - the three branded-tool PDFs at hold-only

So the current article-side residual set is not merely `unfinished`.
It is already `rechecked and blocked without stronger authority`.

### 3. The default continuation class must now be narrowed

- future AI should no longer read `prefer article-side narrow recovery` as a broad default over the current corpus
- article-side reopening is now justified only by genuinely new authority for the already re-audited residual set
- outside that trigger, the next reopen-worthy continuation class shifts back to non-article residual authority gaps such as package / handbook residuals, again only when materially stronger owner or standards-adjacent support appears

## Audit Result

- no new article-side authority lane was admitted
- no per-PDF status changed
- tracker wording required refresh because the old restart priority had become too broad

## What This Pass Fixes

- future AI should not keep reopening the article corpus as if many controller-routed single-PDF raises were still obviously available
- the repo now records a more accurate restart posture: article residuals are currently specific and already re-audited, not broadly open-ended
- the remaining continuation pressure is clearer and more honest

## Recommended Next Action

If `/goal` continues from here:

1. treat current article-side residuals as closed unless new authority appears for the already re-audited `E4 Mark` or `E7` set
2. do not keep using `article-side narrow recovery` as a generic default restart class
3. outside new article authority, reopen non-article residual authority gaps only when a materially stronger owner or standards-adjacent source appears
