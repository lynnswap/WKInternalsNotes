# ``WKInternalsNotes/WKWebView/_executeEditCommand(_:argument:completion:)``

`_executeEditCommand` を実行する。

## Objective-C Declaration
```objective-c
- (void)_executeEditCommand:(NSString *)command argument:(NSString *)argument completion:(void (^)(BOOL))completion WK_API_AVAILABLE(macos(10.13.4), ios(11.3));
```

## Discussion
`completion` に結果を返す。

## References
- [`API/Cocoa/WKWebViewPrivate.h#L324`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L324)
- [`API/Cocoa/WKWebView.mm#L3903`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L3903)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
