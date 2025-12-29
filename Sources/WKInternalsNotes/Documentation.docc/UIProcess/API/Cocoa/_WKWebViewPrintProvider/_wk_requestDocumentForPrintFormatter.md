# ``WKInternalsNotes/_WKWebViewPrintProvider/_wk_requestDocumentForPrintFormatter(_:)``

印刷用ドキュメント生成を要求する。

## Objective-C Declaration
```objective-c
- (void)_wk_requestDocumentForPrintFormatter:(_WKWebViewPrintFormatter *)printFormatter;
```

## Discussion
属性を計算し、必要ならバックグラウンド印刷の追跡に追加した上でPDF生成を開始し、完了待ちを行う。

## References
- [`_WKWebViewPrintFormatterInternal.h#L50`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/_WKWebViewPrintFormatterInternal.h#L50)
- [`WKContentView.mm#L1343`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentView.mm#L1343)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
