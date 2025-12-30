# ``WKInternalsNotes/_WKWebViewPrintFormatter/_setPrintedDocument(_:)``

印刷用 PDF ドキュメントを設定する。

## Objective-C Declaration
```objective-c
- (void)_setPrintedDocument:(CGPDFDocumentRef)printedDocument;
```

## Discussion
メインスレッド必須の場合はそのまま代入し、そうでない場合はロック下で設定して待機中のスレッドへ通知する。

## References
- [`_WKWebViewPrintFormatterInternal.h#L38`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/_WKWebViewPrintFormatterInternal.h#L38)
- [`_WKWebViewPrintFormatter.mm#L99`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/_WKWebViewPrintFormatter.mm#L99)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
