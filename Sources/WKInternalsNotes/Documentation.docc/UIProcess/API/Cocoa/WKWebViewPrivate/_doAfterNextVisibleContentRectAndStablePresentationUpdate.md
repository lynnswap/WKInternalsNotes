# ``WKInternalsNotes/WKWebView/_doAfterNextVisibleContentRectAndStablePresentationUpdate(_:)``

`_doAfterNextVisibleContentRectAndStablePresentationUpdate` を実行する。

## Objective-C Declaration
```objective-c
- (void)_doAfterNextVisibleContentRectAndStablePresentationUpdate:(void (^)(void))updateBlock;
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`WKWebViewPrivateForTestingIOS.h#L96`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/ios/WKWebViewPrivateForTestingIOS.h#L96)
- [`WKWebViewTestingIOS.mm#L473`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/ios/WKWebViewTestingIOS.mm#L473)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
