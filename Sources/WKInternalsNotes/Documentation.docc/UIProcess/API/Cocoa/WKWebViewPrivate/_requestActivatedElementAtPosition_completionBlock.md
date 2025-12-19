# ``WKInternalsNotes/WKWebView/_requestActivatedElementAtPosition(_:completionBlock:)``

`_requestActivatedElementAtPosition` を取得する。

## Objective-C Declaration
```objective-c
- (void)_requestActivatedElementAtPosition:(CGPoint)position completionBlock:(void (^)(_WKActivatedElementInfo *))block WK_API_AVAILABLE(ios(11.0));
```

## Discussion
`completion` に結果を返す。

## References
- [`WKWebViewPrivate.h#L740`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L740)
- [`WKWebViewIOS.mm#L4535`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/ios/WKWebViewIOS.mm#L4535)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
