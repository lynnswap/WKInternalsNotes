# ``WKInternalsNotes/WKQuickLookPreviewController/closePanelIfNecessary()``

自身が管理する `QLPreviewPanel` を必要に応じて閉じる。

## Objective-C Declaration
```objective-c
- (void)closePanelIfNecessary;
```

## Discussion
Quick Look UI が利用できない場合や共有パネルが存在しない場合は何もしない。共有パネルが自身の `dataSource`/`delegate` を指している場合に `close` する。

## References
- [`WKQuickLookPreviewController.h#L44`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WKQuickLookPreviewController.h#L44)
- [`WKQuickLookPreviewController.mm#L82`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WKQuickLookPreviewController.mm#L82)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
