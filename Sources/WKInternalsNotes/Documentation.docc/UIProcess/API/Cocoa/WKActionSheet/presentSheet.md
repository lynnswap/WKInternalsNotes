# ``WKInternalsNotes/WKActionSheet/presentSheet(_:)``

指定スタイルでアクションシートを表示する。

## Objective-C Declaration
```objective-c
- (BOOL)presentSheet:(WKActionSheetPresentationStyle)style;
```

## Discussion
iPad 系では表示直前に `presentationRect` を計算し、空なら `NO` を返す。`_currentPresentationStyle` を設定して `presentSheetFromRect:` を呼び出す。

## References
- [`WKActionSheet.h#L45`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKActionSheet.h#L45)
- [`WKActionSheet.mm#L81`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKActionSheet.mm#L81)
- [`WKActionSheet.mm#L87`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKActionSheet.mm#L87)
- [`WKActionSheet.mm#L93`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKActionSheet.mm#L93)
- [`WKActionSheet.mm#L94`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKActionSheet.mm#L94)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
