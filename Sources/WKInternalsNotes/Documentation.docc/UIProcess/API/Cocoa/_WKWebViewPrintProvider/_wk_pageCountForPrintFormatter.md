# ``WKInternalsNotes/_WKWebViewPrintProvider/_wk_pageCountForPrintFormatter(_:)``

印刷ページ数を返す。

## Objective-C Declaration
```objective-c
- (NSUInteger)_wk_pageCountForPrintFormatter:(_WKWebViewPrintFormatter *)printFormatter;
```

## Discussion
`_attributesForPrintFormatter:` を使って計算し、取得できない場合は `0` を返す。

## References
- [`_WKWebViewPrintFormatterInternal.h#L49`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/_WKWebViewPrintFormatterInternal.h#L49)
- [`WKContentView.mm#L1243`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentView.mm#L1243)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
