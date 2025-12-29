# ``WKInternalsNotes/_WKWebViewPrintProvider/_wk_requestImageForPrintFormatter(_:)``

印刷用プレビュー画像の生成を要求する。

## Objective-C Declaration
```objective-c
- (void)_wk_requestImageForPrintFormatter:(_WKWebViewPrintFormatter *)printFormatter;
```

## Discussion
属性を計算し、必要ならバックグラウンド印刷の追跡に追加した上で画像生成を開始し、完了待ちを行う。

## References
- [`_WKWebViewPrintFormatterInternal.h#L53`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/_WKWebViewPrintFormatterInternal.h#L53)
- [`WKContentView.mm#L1387`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentView.mm#L1387)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
