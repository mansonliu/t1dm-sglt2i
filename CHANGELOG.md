# 更新記錄

格式：日期 — 改了什麼。每筆對應一次 git commit；`git log` 為完整版本史。
本檔之後每次更新內容時同步補一行（最新在上）。

---

## 2026-06-19 — 讀本校正 Wang CA 族群描述

回查 PubMed 原標題確認 Wang CA 2026（PMID 42049097）族群為「歷經**需透析的急性腎損傷（dialysis-requiring AKI, AKI-D）**並存活出院的 T1D」，先前讀本誤寫「透析後急性腎損傷」（讀成透析之後才發生 AKI，因果顛倒）。C-2 主條目改正名稱、補原文與**適用性註記（重症次族群、不可外推到一般 T1DM）**；文獻清單與第六節同步。教訓：對抗查核只驗了數字保真度（aHR 對全文 verbatim），漏掉**族群適用性**這關，此篇靠人工定稿才剔除——查核流程應補「族群/PICO 的 P 比對」前置關卡。

---

## 2026-06-19 — 網誌定稿並上 Blogger（LIVE）

網誌草稿經多輪審閱定稿、發佈：<https://hanwenliu.blogspot.com/2026/06/1-sglt2.html>，標題改為「第 1 型糖尿病用 SGLT2 抑制劑的心腎保護證據」，已加入「糖尿病」分類頁。本檔 `網誌草稿_T1DM_SGLT2i.md` 同步為發佈版。主要修訂：

- **新增「健保」章節**：心衰竭適應症（純心臟條件、未排除第 1 型）vs 慢性腎臟病適應症（排除清單第一項即第 1 型）；補仿單使用限制亦不建議第 1 型。來源為健保給付規定（chap2 §2.16／chap5）與兩份 TFDA 仿單。
- **心血管外推補元老 CVOT**：內文與結論表加 EMPA-REG OUTCOME（PMID 26378978）、DECLARE-TIMI 58（PMID 30415602），修「只列 sotagliflozin」的割裂。
- **移除 Wang CA 2026（PMID 42049097）**：TriNetX、約五成白人、且為透析後 AKI 族群，與本文臨床情境不符（內文句＋RWD 表列皆刪，RWD 改「兩篇」）。
- **引用改寫**：Danne 2019→「源自 2018 ATTD 會議的國際共識」；Peters 2020→「inTandem 1 與 2 研究」。
- **DKA 數量級**用詞：「約一個數量級，最多可達數十倍」（不誇大下限）。
- 介入性試驗表新增「主要終點」欄（血糖／心血管／腎臟）。
- Steno 1 改寫為「第 1 型第一個直接測 CV 硬終點的前瞻試驗，預計 2029 年」。
- 用語：euglycemic DKA 用英文、句首大寫（Euglycemic／Empagliflozin／Sotagliflozin）；刪鋪陳語氣與「臨床上不會使用」斷語。

---

## 2026-06-19 — 建立版本庫（內容狀態匯入）

把既有的自學讀本與網誌草稿匯入 GitHub 做版本控制。以下為匯入前、原先記在兩份 HANDOFF 的版本史，保留為記錄。

### 自學讀本（`整理_自學讀本_T1DM_SGLT2i.md`）

- **2026-06-15** 初版：讀 ADA 2026 第 9 章，收錄核心 15 篇（PMID 已 esummary 核對），寫成指引＋證據表＋利弊＋實務＋文獻清單；產出 HTML 閱讀版與全文下載清單。
- **2026-06-15** 對抗查核 54 條主張（52 confirmed／1 refuted／1 unverifiable）：修正 Li 2023 DKA 為 RR 2.79、EMA dapagliflozin 劑量為 5mg（2021-10-25 撤回）。補近期 6 篇（Oktavian／Bakhsh／Nardone／Al Ozairi／Lawton／Wang）。
- **2026-06-15** 補搜 T1DM 蛋白尿／腎臟，新增 C-2 節與 7 篇真實世界文獻（摘要等級）。
- **2026-06-16** 醫院抓回 F 區全文：6 篇逐字核對升級為全文（Caramori／Wang CA／Pandey／Abdel-Rahman／Tuttle／Steno 1）；補大型回顧 Snaith 2026，補進行中 T1D 腎臟終點試驗（ATTEMPT／SUGARNSALT／RESET1／ReCaRD）。
- **2026-06-16** ATTEMPT 正式結果已發表（Nat Med 2025），升級並校對第三／七節矛盾；新增 C-0「主要 SGLT2i 結果試驗全部排除 T1DM」分類表（13 試驗查 ClinicalTrials.gov）；第七節補 11 篇地標 CVOT/CKD/HF 試驗 PMID。共 30 篇（23 全文／7 摘要）＋11 篇 T2DM 對照。
- **2026-06-19（第二輪）** 事實校正＋論述重構：法規措辭「禁用→未核准＋警語」（FDA Inpefa §5.1 vs §4）；DKA 同維度換算；**心、腎分軸**（腎已到 RCT 級替代指標、心仍為外推）；開頭翻轉成臨床導向、法規降為文末背景。
- **2026-06-19（第三輪）** 回讀資料夾原文 PDF，校正三處擷取錯誤：
  - **RESET1**：是 semaglutide（GLP-1RA）試驗、非 sotagliflozin（先前誤標），網誌版不列入。
  - **Caramori**：單用 SGLT2i 對 UACR 亦顯著 HR 0.71（0.51–0.98）——先前「不能單獨歸因於 SGLT2i」有誤。
  - **Pandey**：SGLT2i 單用 MACE HR 0.77（未顯著）；先前把整體 CKM 組的 DKA 安全終點誤當成「併用組 MACE」。
  - Caramori 與 Pandey 資料庫都是 Optum（非 TriNetX）。

### 網誌草稿（`網誌草稿_T1DM_SGLT2i.md`）

- **v1（2026-06-19）** 從自學讀本改寫初稿。
- **v2** 格式定案：段落標題改「內容型」、文獻整理表移到文章中間、語氣中性；全文「第 1 型／第 2 型」（阿拉伯數字）、「超過濾」（非高過濾）；移除個人猶豫句，結尾收於「逐一評估的決定」。
- **v3** RESET1 抽掉（GLP-1RA 試驗）；Abdel-Rahman／Tuttle 改 inline 補入；DKA 注意事項改 `<ul>`；新增第二張真實世界資料表。補強 ATTEMPT「dip」臨床意義（Cherney 2014／Magee 2009／Moriconi 2023 三篇 esummary 核對）。
- **v4** 回讀原文 PDF 校正 Caramori／Pandey 數字與資料庫，故事更挺「腎強心弱」主軸。

> 校正教訓：RWD 的分組 HR 一定回讀原文 PDF，不可只信前輪摘要式擷取。
