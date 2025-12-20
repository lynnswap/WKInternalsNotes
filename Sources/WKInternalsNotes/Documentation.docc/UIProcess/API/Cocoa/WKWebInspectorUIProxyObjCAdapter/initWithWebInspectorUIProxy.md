# ``WKInternalsNotes/WKWebInspectorUIProxyObjCAdapter/initWithWebInspectorUIProxy(_:)``

WebInspector UIProxy に紐づく adapter を初期化する。

## Objective-C Declaration
```objective-c
- (instancetype)initWithWebInspectorUIProxy:(WebKit::WebInspectorUIProxy*)inspectorProxy;
```

## Discussion
`inspectorProxy` を弱参照として保持し、循環参照を避ける。

## References
- [`WKInspectorPrivateMac.h#L43`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/C/mac/WKInspectorPrivateMac.h#L43)
- [`WebInspectorUIProxyMac.mm#L99`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Inspector/mac/WebInspectorUIProxyMac.mm#L99)
- [`WebInspectorUIProxyMac.mm#L106`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Inspector/mac/WebInspectorUIProxyMac.mm#L106)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
