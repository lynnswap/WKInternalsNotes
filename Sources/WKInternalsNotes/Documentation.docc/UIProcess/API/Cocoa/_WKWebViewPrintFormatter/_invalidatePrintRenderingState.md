# ``WKInternalsNotes/_WKWebViewPrintFormatter/_invalidatePrintRenderingState()``

印刷レンダリング状態を無効化する。

## Objective-C Declaration
```objective-c
- (void)_invalidatePrintRenderingState;
```

## Discussion
`_setPrintPreviewImage:` と `_setPrintedDocument:` に `nullptr` を渡し、キャッシュされた結果をクリアする。

## References
- [`_WKWebViewPrintFormatterInternal.h#L40`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/_WKWebViewPrintFormatterInternal.h#L40)
- [`_WKWebViewPrintFormatter.mm#L146`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/_WKWebViewPrintFormatter.mm#L146)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
