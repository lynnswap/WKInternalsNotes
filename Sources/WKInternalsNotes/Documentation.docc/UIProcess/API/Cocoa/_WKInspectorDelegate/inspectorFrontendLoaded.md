# ``WKInternalsNotes/_WKInspectorDelegate/inspectorFrontendLoaded(_:)``

Inspector UI のロード完了通知を受ける。

## Objective-C Declaration
```objective-c
- (void)inspectorFrontendLoaded:(_WKInspector *)inspector;
```

## Discussion
`InspectorClient::frontendLoaded` から delegate が応答可能な場合に呼ばれる。

## References
- [`_WKInspectorDelegate.h#L44`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInspectorDelegate.h#L44)
- [`_WKInspector.mm#L74`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInspector.mm#L74)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
