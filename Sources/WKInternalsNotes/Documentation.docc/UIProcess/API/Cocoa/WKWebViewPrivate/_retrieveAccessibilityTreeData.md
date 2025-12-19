# ``WKInternalsNotes/WKWebView/_retrieveAccessibilityTreeData(_:)``

`_retrieveAccessibilityTreeData` を実行する。

## Objective-C Declaration
```objective-c
- (void)_retrieveAccessibilityTreeData:(void (^)(NSData *, NSError *))completionHandler;
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`WKWebViewPrivateForTestingMac.h#L54`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/mac/WKWebViewPrivateForTestingMac.h#L54)
- [`WKWebViewTestingMac.mm#L125`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/mac/WKWebViewTestingMac.mm#L125)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
