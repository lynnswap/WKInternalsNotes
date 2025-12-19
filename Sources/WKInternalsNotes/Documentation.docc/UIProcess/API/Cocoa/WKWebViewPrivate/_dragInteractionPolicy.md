# ``WKInternalsNotes/WKWebView/_dragInteractionPolicy``

`_dragInteractionPolicy` の値を取得/設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setDragInteractionPolicy:) _WKDragInteractionPolicy _dragInteractionPolicy WK_API_AVAILABLE(ios(11.0));
```

## Discussion
getter/setter を通じて値を取得/設定する。 setter は `_setDragInteractionPolicy:`。

## References
- [`API/Cocoa/WKWebViewPrivate.h#L721`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L721)
- [`API/ios/WKWebViewIOS.mm#L4436`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/ios/WKWebViewIOS.mm#L4436)
- [`API/ios/WKWebViewIOS.mm#L4441`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/ios/WKWebViewIOS.mm#L4441)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
