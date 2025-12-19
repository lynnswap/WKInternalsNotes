# ``WKInternalsNotes/WKWebView/_activeMenu``

`_activeMenu` の値を取得する。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) NSMenu *_activeMenu;
```

## Discussion
読み取り専用のため setter は持たない。

## References
- [`WKWebViewPrivateForTestingMac.h#L38`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/mac/WKWebViewPrivateForTestingMac.h#L38)
- [`WKWebViewTestingMac.mm#L116`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/mac/WKWebViewTestingMac.mm#L116)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
