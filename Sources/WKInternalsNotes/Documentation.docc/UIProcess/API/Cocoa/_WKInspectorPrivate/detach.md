# ``WKInternalsNotes/_WKInspector/detach()``

インスペクタをドッキング解除して独立ウインドウにする。

## Objective-C Declaration
```objective-c
- (void)detach;
```

## Discussion
`WebInspectorUIProxy::detach` を呼び出し、ドッキング状態でかつインスペクタページが存在する場合に SetAttached(false) と Detached の通知を行い、プラットフォーム側で切り離す。

## References
- [`_WKInspector.h#L56`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInspector.h#L56)
- [`_WKInspector.mm#L185`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInspector.mm#L185)
- [`WebInspectorUIProxy.cpp#L354`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Inspector/WebInspectorUIProxy.cpp#L354)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
