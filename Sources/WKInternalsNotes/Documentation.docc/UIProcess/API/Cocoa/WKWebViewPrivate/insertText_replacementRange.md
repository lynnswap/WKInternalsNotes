# ``WKInternalsNotes/WKWebView/insertText(_:replacementRange:)``

`insertText` を実行する。

## Objective-C Declaration
```objective-c
- (void)insertText:(id)string replacementRange:(NSRange)replacementRange;
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`WKWebViewMac.h#L40`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/mac/WKWebViewMac.h#L40)
- [`WKWebViewMac.mm#L1397`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/mac/WKWebViewMac.mm#L1397)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
