# ``WKInternalsNotes/_WKWebViewPrintFormatter/_setPrintPreviewImage(_:)``

印刷プレビュー画像を設定する。

## Objective-C Declaration
```objective-c
- (void)_setPrintPreviewImage:(CGImageRef)printPreviewImage;
```

## Discussion
メインスレッド必須の場合はそのまま代入し、そうでない場合はロック下で設定して待機中のスレッドへ通知する。

## References
- [`_WKWebViewPrintFormatterInternal.h#L39`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/_WKWebViewPrintFormatterInternal.h#L39)
- [`_WKWebViewPrintFormatter.mm#L120`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/_WKWebViewPrintFormatter.mm#L120)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
