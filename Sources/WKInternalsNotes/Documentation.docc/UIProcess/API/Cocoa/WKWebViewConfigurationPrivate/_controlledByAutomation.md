# ``WKInternalsNotes/WKWebViewConfigurationPrivate/_controlledByAutomation``

自動化（テスト）制御フラグ

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setControlledByAutomation:, getter=_isControlledByAutomation) BOOL _controlledByAutomation WK_API_AVAILABLE(macos(10.12.4), ios(10.3));
```

## Default Value
iOS: `NO` / macOS: `NO`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_controlledByAutomation = YES`: 自動化（テスト）制御フラグ。
- `_controlledByAutomation = NO`: 自動化（テスト）制御フラグ（無効）。

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L92`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L92)
- [`Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
