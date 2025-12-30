# ``WKInternalsNotes/_WKWebViewPrintFormatter/_waitForPrintedDocumentOrImage()``

印刷ドキュメントまたはプレビュー画像の生成を待機する。

## Objective-C Declaration
```objective-c
- (void)_waitForPrintedDocumentOrImage;
```

## Discussion
ロック下で `_printCompletionCondition` のシグナルを待機する。

## References
- [`_WKWebViewPrintFormatterInternal.h#L42`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/_WKWebViewPrintFormatterInternal.h#L42)
- [`_WKWebViewPrintFormatter.mm#L132`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/_WKWebViewPrintFormatter.mm#L132)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
