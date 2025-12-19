# ``WKInternalsNotes/WKWebView/_insertText(_:replacementRange:)``

`_insertText` を実行する。

## Objective-C Declaration
```objective-c
- (void)_insertText:(id)string replacementRange:(NSRange)replacementRange;
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`WKWebViewPrivateForTestingMac.h#L49`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/mac/WKWebViewPrivateForTestingMac.h#L49)
- [`WKWebViewTestingMac.mm#L89`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/mac/WKWebViewTestingMac.mm#L89)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
