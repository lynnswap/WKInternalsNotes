# ``WKInternalsNotes/WKWebViewConfigurationPrivate/_requiresUserActionForEditingControlsManager``

editing controls manager に user action を要求

## Objective-C Declaration
```objective-c
@property (nonatomic, readwrite, setter=_setRequiresUserActionForEditingControlsManager:) BOOL _requiresUserActionForEditingControlsManager WK_API_AVAILABLE(macos(10.12));
```

## Default Value
macOS: `NO`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_requiresUserActionForEditingControlsManager = YES`: editing controls manager に user action を要求。
- `_requiresUserActionForEditingControlsManager = NO`: editing controls manager に user action を要求（無効）。

## Details
- `HAVE(TOUCH_BAR)` のみ

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L130`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L130)
- [`Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L1290`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L1290)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
