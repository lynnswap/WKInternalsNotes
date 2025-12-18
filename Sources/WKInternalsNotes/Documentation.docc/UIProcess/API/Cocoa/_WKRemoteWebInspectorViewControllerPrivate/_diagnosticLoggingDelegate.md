# ``WKInternalsNotes/_WKRemoteWebInspectorViewController/_diagnosticLoggingDelegate``

リモートインスペクタの WebView に診断ログ delegate を設定し、診断ログの利用可否を通知する。

## Objective-C Declaration
```objective-c
@property (nonatomic, weak, setter=_setDiagnosticLoggingDelegate:) id<_WKDiagnosticLoggingDelegate> _diagnosticLoggingDelegate;
```

## Default Value
`nil`

## Discussion
`_setDiagnosticLoggingDelegate:` は `self.webView._diagnosticLoggingDelegate` を更新し、`setDiagnosticLoggingAvailable` を delegate の有無で呼び出す。`webView` が未生成の場合は `nil` への送信となるため実質的に無効化される。

## References
- [`_WKRemoteWebInspectorViewControllerPrivate.h#L37`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKRemoteWebInspectorViewControllerPrivate.h#L37)
- [`_WKRemoteWebInspectorViewController.mm#L165`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKRemoteWebInspectorViewController.mm#L165)
- [`RemoteWebInspectorUIProxy.h#L95`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Inspector/RemoteWebInspectorUIProxy.h#L95)
- [`RemoteWebInspectorUIProxy.cpp#L78`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Inspector/RemoteWebInspectorUIProxy.cpp#L78)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
