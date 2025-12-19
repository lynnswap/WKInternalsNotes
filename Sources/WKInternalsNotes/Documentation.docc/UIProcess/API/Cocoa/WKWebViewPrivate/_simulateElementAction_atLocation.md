# ``WKInternalsNotes/WKWebView/_simulateElementAction(_:atLocation:)``

`_simulateElementAction` を実行する。

## Objective-C Declaration
```objective-c
- (void)_simulateElementAction:(_WKElementActionType)actionType atLocation:(CGPoint)location;
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`API/ios/WKWebViewPrivateForTestingIOS.h#L76`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/ios/WKWebViewPrivateForTestingIOS.h#L76)
- [`API/ios/WKWebViewTestingIOS.mm#L413`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/ios/WKWebViewTestingIOS.mm#L413)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
