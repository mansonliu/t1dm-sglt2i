# 第 1 型糖尿病使用 SGLT2 抑制劑：心腎保護的證據整理

依 **2026 ADA 指引**＋PubMed 原始文獻，整理「第 1 型糖尿病（T1DM）使用 SGLT2 抑制劑」的指引立場、臨床證據（心腎好處）、利與弊。供萬芳醫院內分泌科自學參考，並改寫為衛教網誌。

## 一句話主軸

SGLT2i 在第 1 型糖尿病的取捨是 **不對稱** 的：

| 軸 | 證據強度 | 現況 |
|---|---|---|
| **腎臟保護** | 中等 | 已到 RCT 級替代指標（ATTEMPT 實測 GFR，減輕超過濾）；仍缺蛋白尿／硬結局 RCT |
| **心血管保護** | 低 | 無第 1 型 CV RCT，全靠第 2 型外推＋真實世界 SGLT2i 單用 MACE 未達顯著 |
| **DKA 風險** | 高（確定） | 確定升高（約 4%、未用者 5–17 倍） |

想要的好處（尤其心血管）仍是替代指標／外推等級、不確定；最確定的後果（DKA）卻確定升高。

## 檔案

| 檔案 | 內容 |
|---|---|
| [`整理_自學讀本_T1DM_SGLT2i.md`](整理_自學讀本_T1DM_SGLT2i.md) | **主成品**。完整自學讀本：指引、證據表、利弊、實務、文獻清單（含查證等級與對抗查核註記） |
| [`網誌草稿_T1DM_SGLT2i.md`](網誌草稿_T1DM_SGLT2i.md) | 衛教網誌草稿的 markdown 版（供閱讀／版本追蹤） |
| [`CHANGELOG.md`](CHANGELOG.md) | 每次更新的版本記錄 |

文獻清單（PMID + PubMed/試驗登錄連結）在自學讀本第七節。

## 版本控制與檔案慣例

- **版本庫只放文字。** 期刊全文 PDF 有版權，由 `.gitignore` 排除，永遠不進 repo；引用一律走 PMID/DOI 連結。
- **這個 repo 是 markdown 的真實來源。** 之後更新內容請改這裡的 `.md`，再 commit，`git log` 即完整版本史。
- **產出物留在 OneDrive：**
  - 上 Blogger 的成品 HTML（含 `.t1sg-article` CSS）：`~/OneDrive/Blog and FB/_drafts/20260619 第一型糖尿病 SGLT2 抑制劑心腎保護.html`
  - 自學讀本的 HTML 閱讀版、全文 PDF、下載清單：`~/OneDrive/Medicine/01 Diabetes Melitus/T1DM SGLT2i 文獻/`
- repo 刻意 **不放在 OneDrive 內**——OneDrive 同步會在 git 操作中途搬動 `.git`，跨機器易弄壞版本庫。

## 重要查證慣例

- PubMed 驗證一律走 esummary JSON，不信頁面摘要或「已驗證」標記。
- 寫前先 extract-with-quote，把數字釘回原文句子；RWD 的分組 HR 一定回讀原文 PDF（見 CHANGELOG v4 校正）。
- 藥物學名用英文，不音譯；單位用台灣慣例。

> 內容定位仍是「自學讀本＋網誌草稿」，網誌尚未上 Blogger。詳細交班見 OneDrive 兩份 HANDOFF。
