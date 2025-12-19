# ``WKInternalsNotes/WKWebView/_inspectorAttachmentView``

`_inspectorAttachmentView` の値を取得/設定する。

## Objective-C Declaration
```objective-c
@property (strong, nonatomic, setter=_setInspectorAttachmentView:) NSView *_inspectorAttachmentView WK_API_AVAILABLE(macos(10.13.4));
```

## Discussion
getter/setter を通じて値を取得/設定する。 setter は `_setInspectorAttachmentView:`。

## References
- [`WKWebViewPrivate.h#L863`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L863)
- [`WKWebViewMac.mm#L1811`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/mac/WKWebViewMac.mm#L1811)
- [`WKWebViewMac.mm#L1811`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/mac/WKWebViewMac.mm#L1811)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
