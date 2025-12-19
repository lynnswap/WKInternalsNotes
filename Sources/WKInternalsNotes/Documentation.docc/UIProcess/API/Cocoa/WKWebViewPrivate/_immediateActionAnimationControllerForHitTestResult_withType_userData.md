# ``WKInternalsNotes/WKWebView/_immediateActionAnimationControllerForHitTestResult(_:withType:userData:)``

`_immediateActionAnimationControllerForHitTestResult` を実行する。

## Objective-C Declaration
```objective-c
- (id)_immediateActionAnimationControllerForHitTestResult:(_WKHitTestResult *)hitTestResult withType:(_WKImmediateActionType)type userData:(id<NSSecureCoding>)userData;
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`WKWebViewPrivate.h#L902`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L902)
- [`WKWebViewMac.mm#L1291`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/mac/WKWebViewMac.mm#L1291)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
