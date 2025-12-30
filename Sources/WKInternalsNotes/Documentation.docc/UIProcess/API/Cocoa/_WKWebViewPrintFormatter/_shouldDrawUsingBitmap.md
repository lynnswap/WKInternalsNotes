# ``WKInternalsNotes/_WKWebViewPrintFormatter/_shouldDrawUsingBitmap()``

ビットマップ描画を使うか判定する。

## Objective-C Declaration
```objective-c
- (BOOL)_shouldDrawUsingBitmap;
```

## Discussion
`snapshotFirstPage` が `YES`、印刷プロバイダが `_wk_requestImageForPrintFormatter:` に未対応、または `requestedRenderingQuality` が `UIPrintRenderingQualityBest` の場合は `NO`。それ以外は `YES` を返す。

## References
- [`_WKWebViewPrintFormatterInternal.h#L36`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/_WKWebViewPrintFormatterInternal.h#L36)
- [`_WKWebViewPrintFormatter.mm#L76`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/_WKWebViewPrintFormatter.mm#L76)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
