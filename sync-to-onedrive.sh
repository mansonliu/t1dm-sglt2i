#!/usr/bin/env bash
# 以 repo 為準，把版本控制的 markdown 推回 OneDrive 對應檔。
# repo 是真實來源；OneDrive 端的 .md 由本腳本覆蓋。
# 用法：bash sync-to-onedrive.sh        （預覽差異後確認才覆蓋）
#       bash sync-to-onedrive.sh -y     （不問直接覆蓋）
set -euo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# 對應表：repo 檔 → OneDrive 目標。HTML 成品不在此（OneDrive-only，手動維護）。
SRC_SELFSTUDY="$REPO_DIR/整理_自學讀本_T1DM_SGLT2i.md"
DST_SELFSTUDY="$HOME/OneDrive/Medicine/01 Diabetes Melitus/T1DM SGLT2i 文獻/00_整理_T1DM使用SGLT2抑制劑.md"

AUTO=0
[ "${1:-}" = "-y" ] && AUTO=1

sync_one() {
  local src="$1" dst="$2"
  if [ ! -f "$src" ]; then echo "⚠ 來源不存在，跳過：$src"; return; fi
  if [ ! -d "$(dirname "$dst")" ]; then echo "⚠ 目標資料夾不存在（OneDrive 未掛載？），跳過：$dst"; return; fi
  if [ -f "$dst" ] && cmp -s "$src" "$dst"; then
    echo "✓ 已一致，無需更新：$(basename "$dst")"
    return
  fi
  echo "── 將覆蓋：$dst"
  if [ -f "$dst" ]; then
    echo "   差異（OneDrive 現況 → repo 版本，僅統計）："
    diff <(cat "$dst") <(cat "$src") | grep -c '^[<>]' | sed 's/^/   變動行數約 /' || true
  else
    echo "   （OneDrive 端尚無此檔，將新建）"
  fi
  if [ "$AUTO" -ne 1 ]; then
    read -r -p "   確認覆蓋？[y/N] " ans
    [ "$ans" = "y" ] || [ "$ans" = "Y" ] || { echo "   略過。"; return; }
  fi
  cp "$src" "$dst"
  echo "✓ 已同步：$(basename "$dst")"
}

echo "repo：$REPO_DIR"
sync_one "$SRC_SELFSTUDY" "$DST_SELFSTUDY"
echo "完成。（網誌 HTML 成品為 OneDrive-only，不由本腳本同步）"
