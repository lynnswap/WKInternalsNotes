# ``WKInternalsNotes/_WKRemoteWebInspectorViewController/configuration``

リモートインスペクタに適用する `_WKInspectorConfiguration` を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, copy) _WKInspectorConfiguration *configuration WK_API_AVAILABLE(macos(12.0));
```

## Default Value
`initWithConfiguration:` で渡した設定の copy。

## Discussion
`initWithConfiguration:` で `_configuration = [configuration copy]` として保持し、`configurationForRemoteInspector` が `_apiObject` を返して RemoteWebInspectorUIProxy に渡す。

## References
- [`_WKRemoteWebInspectorViewController.h#L47`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKRemoteWebInspectorViewController.h#L47)
- [`_WKRemoteWebInspectorViewController.mm#L80`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKRemoteWebInspectorViewController.mm#L80)
- [`_WKRemoteWebInspectorViewController.mm#L80`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKRemoteWebInspectorViewController.mm#L80)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
