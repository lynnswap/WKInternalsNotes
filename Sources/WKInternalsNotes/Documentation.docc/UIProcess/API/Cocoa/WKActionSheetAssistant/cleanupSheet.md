# ``WKInternalsNotes/WKActionSheetAssistant/cleanupSheet()``

アクションシートの後始末と状態リセットを行う。

## Objective-C Declaration
```objective-c
- (void)cleanupSheet;
```

## Discussion
必要に応じてデリゲートへ停止通知を送り、`_interactionSheet` に `doneWithSheet:` を呼んだ上でシートと要素情報、位置情報、フラグ類を初期状態に戻す。

## References
- [`WKActionSheetAssistant.h#L119`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKActionSheetAssistant.h#L119)
- [`WKActionSheetAssistant.mm#L1110`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKActionSheetAssistant.mm#L1110)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
