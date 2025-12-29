# ``WKInternalsNotes/WKQuickLookPreviewController/endControl(_:)``

`QLPreviewPanel` のデータソースとデリゲート設定を解除する。

## Objective-C Declaration
```objective-c
- (void)endControl:(QLPreviewPanel *)panel;
```

## Discussion
現在の `dataSource`/`delegate` が自身であれば `nil` に戻す。

## References
- [`WKQuickLookPreviewController.h#L43`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WKQuickLookPreviewController.h#L43)
- [`WKQuickLookPreviewController.mm#L72`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WKQuickLookPreviewController.mm#L72)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
