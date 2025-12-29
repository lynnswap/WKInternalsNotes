# ``WKInternalsNotes/WKQuickLookPreviewController/beginControl(_:)``

`QLPreviewPanel` のデータソースとデリゲートを設定する。

## Objective-C Declaration
```objective-c
- (void)beginControl:(QLPreviewPanel *)panel;
```

## Discussion
`panel.dataSource` と `panel.delegate` を自身に設定する。

## References
- [`WKQuickLookPreviewController.h#L41`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WKQuickLookPreviewController.h#L41)
- [`WKQuickLookPreviewController.mm#L66`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WKQuickLookPreviewController.mm#L66)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
