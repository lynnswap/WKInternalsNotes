# ``WKInternalsNotes/WKWebView/_findInteractionEnabled``

`_findInteractionEnabled` の値を取得/設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic, readwrite, setter=_setFindInteractionEnabled:) BOOL _findInteractionEnabled WK_API_AVAILABLE(ios(16.0));
```

## Discussion
getter/setter を通じて値を取得/設定する。 setter は `_setFindInteractionEnabled:`。

## References
- [`API/Cocoa/WKWebViewPrivate.h#L677`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L677)
- [`API/ios/WKWebViewIOS.mm#L5069`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/ios/WKWebViewIOS.mm#L5069)
- [`API/ios/WKWebViewIOS.mm#L5074`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/ios/WKWebViewIOS.mm#L5074)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
