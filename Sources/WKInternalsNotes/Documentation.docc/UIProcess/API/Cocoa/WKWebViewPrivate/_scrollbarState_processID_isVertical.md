# ``WKInternalsNotes/WKWebView/_scrollbarState(_:processID:isVertical:)``

`_scrollbarState` を実行する。

## Objective-C Declaration
```objective-c
- (NSString *)_scrollbarState:(unsigned long long)scrollingNodeID processID:(unsigned long long)processID isVertical:(bool)isVertical;
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`API/ios/WKWebViewPrivateForTestingIOS.h#L98`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/ios/WKWebViewPrivateForTestingIOS.h#L98)
- [`API/ios/WKWebViewTestingIOS.mm#L322`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/ios/WKWebViewTestingIOS.mm#L322)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
