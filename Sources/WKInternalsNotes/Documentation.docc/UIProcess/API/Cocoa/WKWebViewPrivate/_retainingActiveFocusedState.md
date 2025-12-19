# ``WKInternalsNotes/WKWebView/_retainingActiveFocusedState``

`_retainingActiveFocusedState` の値を取得する。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, getter=_isRetainingActiveFocusedState) BOOL _retainingActiveFocusedState;
```

## Discussion
読み取り専用のため setter は持たない。 getter は `_isRetainingActiveFocusedState`。

## References
- [`WKWebViewIOS.h#L208`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/ios/WKWebViewIOS.h#L208)
- [`WKWebViewIOS.mm`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/ios/WKWebViewIOS.mm)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
