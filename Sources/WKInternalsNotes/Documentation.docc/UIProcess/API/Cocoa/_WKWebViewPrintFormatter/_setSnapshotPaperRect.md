# ``WKInternalsNotes/_WKWebViewPrintFormatter/_setSnapshotPaperRect(_:)``

スナップショット用の `paperRect` を設定する。

## Objective-C Declaration
```objective-c
- (void)_setSnapshotPaperRect:(CGRect)paperRect;
```

## Discussion
ページ数再計算を抑制した上で、`printPageRenderer.paperRect` と `printableRect` を指定矩形に設定する。

## References
- [`_WKWebViewPrintFormatterInternal.h#L37`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/_WKWebViewPrintFormatterInternal.h#L37)
- [`_WKWebViewPrintFormatter.mm#L138`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/_WKWebViewPrintFormatter.mm#L138)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
