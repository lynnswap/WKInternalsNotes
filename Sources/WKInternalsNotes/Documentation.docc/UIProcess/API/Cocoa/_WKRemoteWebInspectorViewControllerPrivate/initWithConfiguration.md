# ``WKInternalsNotes/_WKRemoteWebInspectorViewController/initWithConfiguration(_:)``

指定の `_WKInspectorConfiguration` でリモートインスペクタを初期化する。

## Objective-C Declaration
```objective-c
- (instancetype)initWithConfiguration:(_WKInspectorConfiguration *)configuration WK_API_AVAILABLE(macos(12.0));
```

## Discussion
設定を copy して保持し、RemoteWebInspectorUIProxy を生成して client を設定する。この client が後続の初期化時に configuration を供給する。

## References
- [`_WKRemoteWebInspectorViewController.h#L49`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKRemoteWebInspectorViewController.h#L49)
- [`_WKRemoteWebInspectorViewController.mm#L96`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKRemoteWebInspectorViewController.mm#L96)
- [`RemoteWebInspectorUIProxy.h`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Inspector/RemoteWebInspectorUIProxy.h)
- [`RemoteWebInspectorUIProxy.h`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Inspector/RemoteWebInspectorUIProxy.h)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
