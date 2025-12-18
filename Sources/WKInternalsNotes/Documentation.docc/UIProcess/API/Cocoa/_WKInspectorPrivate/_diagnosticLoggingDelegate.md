# ``WKInternalsNotes/_WKInspector/_diagnosticLoggingDelegate``

インスペクタフロントエンドの診断ログ delegate を設定し、診断ログの利用可否を Inspector に通知する。

## Objective-C Declaration
```objective-c
@property (nonatomic, weak, setter=_setDiagnosticLoggingDelegate:) id<_WKDiagnosticLoggingDelegate> _diagnosticLoggingDelegate;
```

## Default Value
`nil`

## Discussion
`_setDiagnosticLoggingDelegate:` は `inspectorWebView` を取得し、存在しない場合は何もしない。存在する場合はその `_diagnosticLoggingDelegate` を設定し、`setDiagnosticLoggingAvailable` を delegate の有無で呼び出してフロントエンドに通知する。

## References
- [`_WKInspectorPrivate.h#L33`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInspectorPrivate.h#L33)
- [`_WKInspector.mm#L208`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInspector.mm#L208)
- [`_WKInspectorTesting.mm#L48`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInspectorTesting.mm#L48)
- [`WebInspectorUIProxy.cpp#L821`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Inspector/WebInspectorUIProxy.cpp#L821)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
