#!/bin/sh
set -e

# กำหนดค่าเริ่มต้น หรือรับผ่าน Environment Variable / Argument
REPO="${REPO:-${1:-"your-org/icon-engine"}}"
BIN_NAME="${BIN_NAME:-${2:-"icon-cli"}}"
INSTALL_DIR="${INSTALL_DIR:-"/usr/local/bin"}"

# ตรวจจับระบบปฏิบัติการ
OS="$(uname -s)"
case "$OS" in
  Linux*)  TARGET_OS="unknown-linux-gnu" ;;
  Darwin*) TARGET_OS="apple-darwin" ;;
  *)       echo "❌ Unsupported OS: $OS" && exit 1 ;;
esac

# ตรวจจับสถาปัตยกรรม CPU
ARCH="$(uname -m)"
case "$ARCH" in
  x86_64*)  TARGET_ARCH="x86_64" ;;
  aarch64*) TARGET_ARCH="aarch64" ;;
  arm64*)   TARGET_ARCH="aarch64" ;;
  *)        echo "❌ Unsupported Architecture: $ARCH" && exit 1 ;;
esac

TARGET="${TARGET_ARCH}-${TARGET_OS}"
echo "🚀 Installing ${BIN_NAME} for ${TARGET} from ${REPO}..."

# ดึง Tag ล่าสุดจาก GitHub Releases API
LATEST_TAG=$(curl -s "https://api.github.com/repos/${REPO}/releases/latest" | grep '"tag_name":' | sed -E 's/.*"([^"]+)".*/\1/')

if [ -z "$LATEST_TAG" ]; then
  echo "❌ Error: Could not determine latest release tag for ${REPO}"
  exit 1
fi

DOWNLOAD_URL="https://github.com/${REPO}/releases/download/${LATEST_TAG}/${BIN_NAME}-${TARGET}.tar.gz"
TMP_DIR="$(mktemp -d)"

echo "📦 Downloading ${DOWNLOAD_URL}..."
curl -fsSL "$DOWNLOAD_URL" -o "${TMP_DIR}/${BIN_NAME}.tar.gz"

echo "📂 Extracting binary..."
tar -xzf "${TMP_DIR}/${BIN_NAME}.tar.gz" -C "$TMP_DIR"

# ตรวจสอบสิทธิ์การติดตั้ง (หากไม่มีสิทธิ์ root ให้ลง ~/.local/bin แทน)
if [ ! -w "$INSTALL_DIR" ]; then
  INSTALL_DIR="${HOME}/.local/bin"
  mkdir -p "$INSTALL_DIR"
  echo "⚠️ Warning: No write access to /usr/local/bin. Installing to ${INSTALL_DIR} instead."
fi

mv "${TMP_DIR}/${BIN_NAME}" "${INSTALL_DIR}/${BIN_NAME}"
chmod +x "${INSTALL_DIR}/${BIN_NAME}"
rm -rf "$TMP_DIR"

echo "✅ Successfully installed ${BIN_NAME} (${LATEST_TAG}) to ${INSTALL_DIR}/${BIN_NAME}"
