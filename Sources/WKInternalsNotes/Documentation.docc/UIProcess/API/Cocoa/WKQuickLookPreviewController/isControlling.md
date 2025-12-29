# ``WKInternalsNotes/WKQuickLookPreviewController/isControlling(_:)``

自身が `QLPreviewPanel` を管理しているか判定する。

## Objective-C Declaration
```objective-c
- (BOOL)isControlling:(QLPreviewPanel *)panel;
```

## Discussion
`panel.dataSource` と `panel.delegate` がどちらも自身であれば `YES` を返す。

## References
- [`WKQuickLookPreviewController.h#L42`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WKQuickLookPreviewController.h#L42)
- [`WKQuickLookPreviewController.mm#L91`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WKQuickLookPreviewController.mm#L91)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
