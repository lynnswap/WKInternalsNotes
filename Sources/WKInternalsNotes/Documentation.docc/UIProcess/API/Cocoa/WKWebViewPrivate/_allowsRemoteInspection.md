# ``WKInternalsNotes/WKWebView/_allowsRemoteInspection``

`_allowsRemoteInspection` の値を取得/設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setAllowsRemoteInspection:) BOOL _allowsRemoteInspection WK_API_DEPRECATED_WITH_REPLACEMENT("inspectable", macos(10.10, 13.3), ios(8.0, 16.4));
```

## Discussion
getter/setter を通じて値を取得/設定する。 setter は `_setAllowsRemoteInspection:`。

## References
- [`API/Cocoa/WKWebViewPrivate.h#L252`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L252)
- [`API/Cocoa/WKWebView.mm#L5243`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L5243)
- [`API/Cocoa/WKWebView.mm#L5248`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L5248)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
