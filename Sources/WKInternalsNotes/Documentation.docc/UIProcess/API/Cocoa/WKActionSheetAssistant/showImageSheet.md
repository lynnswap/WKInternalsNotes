# ``WKInternalsNotes/WKActionSheetAssistant/showImageSheet()``

画像用のアクションシートを構築して表示する。

## Objective-C Declaration
```objective-c
- (void)showImageSheet;
```

## Discussion
位置情報を取得し、必要ならデリゲートから代替URLを非同期取得して要素情報を構築する。デフォルトアクションを組み立てた後にデリゲートで最終決定し、内容があればシートを生成・表示する。

## References
- [`WKActionSheetAssistant.h#L114`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKActionSheetAssistant.h#L114)
- [`WKActionSheetAssistant.mm#L383`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKActionSheetAssistant.mm#L383)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
