# ``WKInternalsNotes/WKWebView/_remoteInspectionNameOverride``

`_remoteInspectionNameOverride` の値を取得/設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic, copy, setter=_setRemoteInspectionNameOverride:) NSString *_remoteInspectionNameOverride WK_API_AVAILABLE(macos(10.12), ios(10.0));
```

## Discussion
getter/setter を通じて値を取得/設定する。 setter は `_setRemoteInspectionNameOverride:`。

## References
- [`WKWebViewPrivate.h#L253`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L253)
- [`WKWebView.mm#L5253`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L5253)
- [`WKWebView.mm#L5253`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L5253)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
