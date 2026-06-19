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
| [`網誌草稿_T1DM_SGLT2i.md`](網誌草稿_T1DM_SGLT2i.md) | 衛教網誌的 markdown **鏡像**（供閱讀／版本追蹤）。**由 `blog-html-to-md.py` 從成品 HTML 自動轉出，請勿手動改。** |
| [`blog-html-to-md.py`](blog-html-to-md.py) | 把 OneDrive 的網誌成品 HTML 轉成上面的 md 鏡像（網誌以 HTML 為真實來源） |
| [`sync-to-onedrive.sh`](sync-to-onedrive.sh) | 把文獻整理 md 從 repo 單向推回 OneDrive |
| [`CHANGELOG.md`](CHANGELOG.md) | 每次更新的版本記錄 |

文獻清單（PMID + PubMed/試驗登錄連結）在自學讀本第七節。

## 版本控制與檔案慣例

- **版本庫只放文字。** 期刊全文 PDF 有版權，由 `.gitignore` 排除，永遠不進 repo；引用一律走 PMID/DOI 連結。
- **兩種真實來源，分開處理（這是同步的關鍵，先前曾因混淆而脫鉤）：**
  - **文獻整理（自學讀本）→ repo 的 `整理_自學讀本_*.md` 為真實來源。** 改它 → commit → `sync-to-onedrive.sh` 推回 OneDrive。其 OneDrive `.html` 是手動衍生的閱讀版。
  - **網誌 → OneDrive 的成品 `*.html` 為真實來源**（你在那裡微調表格／欄寬、上 Blogger）。改完／發佈後跑 `blog-html-to-md.py` 重生成 repo 的 `網誌草稿_*.md` 鏡像，再 commit。**不要手動改網誌 md**，會被下次轉出覆蓋。
- **文獻整理改完：commit，再單向推回 OneDrive**：
  ```
  cd ~/t1dm-sglt2i
  # 改 整理_自學讀本_*.md、補一行 CHANGELOG
  git add -A && git commit -m "校正 XX" && git push
  bash sync-to-onedrive.sh        # 預覽差異後確認覆蓋；加 -y 直接覆蓋
  ```
- **網誌改完／發佈後：把成品 HTML 轉回 md 鏡像再 commit**：
  ```
  cd ~/t1dm-sglt2i
  python3 blog-html-to-md.py \
    --html "$HOME/OneDrive/Blog and FB/_drafts/_archive/20260619 第一型糖尿病 SGLT2 抑制劑心腎保護.html" \
    --out 網誌草稿_T1DM_SGLT2i.md \
    --url https://hanwenliu.blogspot.com/2026/06/1-sglt2.html
  git add -A && git commit -m "網誌：同步 md 鏡像" && git push
  ```
- **產出物留在 OneDrive：**
  - 上 Blogger 的成品 HTML（含 `.t1sg-article` CSS）：`~/OneDrive/Blog and FB/_drafts/20260619 第一型糖尿病 SGLT2 抑制劑心腎保護.html`。HTML 為 OneDrive-only、手動維護，從 OneDrive 開啟即可預覽，不上 git、不做 GitHub Pages。
  - 自學讀本的 HTML 閱讀版、全文 PDF、下載清單：`~/OneDrive/Medicine/01 Diabetes Melitus/T1DM SGLT2i 文獻/`
- repo 刻意 **不放在 OneDrive 內**——OneDrive 同步會在 git 操作中途搬動 `.git`，跨機器易弄壞版本庫。

## 重要查證慣例

- PubMed 驗證一律走 esummary JSON，不信頁面摘要或「已驗證」標記。
- 寫前先 extract-with-quote，把數字釘回原文句子；RWD 的分組 HR 一定回讀原文 PDF（見 CHANGELOG v4 校正）。
- 藥物學名用英文，不音譯；單位用台灣慣例。

> 網誌已上 Blogger（LIVE，2026-06-19）：<https://hanwenliu.blogspot.com/2026/06/1-sglt2.html>，標題「第 1 型糖尿病用 SGLT2 抑制劑的心腎保護證據」，並已加入「糖尿病」分類頁。詳細交班見 OneDrive `_drafts/_archive/` 的 HANDOFF。
