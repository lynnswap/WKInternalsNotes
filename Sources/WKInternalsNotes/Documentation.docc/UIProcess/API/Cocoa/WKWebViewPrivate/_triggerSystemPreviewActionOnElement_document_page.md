# ``WKInternalsNotes/WKWebView/_triggerSystemPreviewActionOnElement(_:document:page:)``

`_triggerSystemPreviewActionOnElement` を実行する。

## Objective-C Declaration
```objective-c
- (void)_triggerSystemPreviewActionOnElement:(uint64_t)elementID document:(NSString*)documentID page:(uint64_t)pageID;
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`WKWebViewPrivateForTestingIOS.h#L82`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/ios/WKWebViewPrivateForTestingIOS.h#L82)
- [`WKWebViewTestingIOS.mm#L428`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/ios/WKWebViewTestingIOS.mm#L428)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
