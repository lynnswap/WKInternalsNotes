# ``WKInternalsNotes/WKWebView/_textFragmentDirectiveFromSelectionWithCompletionHandler(_:)``

`_textFragmentDirectiveFromSelectionWithCompletionHandler` を実行する。

## Objective-C Declaration
```objective-c
- (void)_textFragmentDirectiveFromSelectionWithCompletionHandler:(void(^)(NSURL *))completionHandler WK_API_AVAILABLE(macos(26.0), ios(26.0), visionos(26.0));
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`WKWebViewPrivate.h#L477`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L477)
- [`WKWebView.mm#L4544`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L4544)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
