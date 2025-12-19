# ``WKInternalsNotes/WKWebView/_diagnosticLoggingDelegate``

`_diagnosticLoggingDelegate` の値を取得/設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic, weak, setter=_setDiagnosticLoggingDelegate:) id <_WKDiagnosticLoggingDelegate> _diagnosticLoggingDelegate WK_API_AVAILABLE(macos(10.11), ios(9.0));
```

## Discussion
getter/setter を通じて値を取得/設定する。 setter は `_setDiagnosticLoggingDelegate:`。

## References
- [`API/Cocoa/WKWebViewPrivate.h#L387`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L387)
- [`API/Cocoa/WKWebView.mm#L5638`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L5638)
- [`API/Cocoa/WKWebView.mm#L5647`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L5647)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
