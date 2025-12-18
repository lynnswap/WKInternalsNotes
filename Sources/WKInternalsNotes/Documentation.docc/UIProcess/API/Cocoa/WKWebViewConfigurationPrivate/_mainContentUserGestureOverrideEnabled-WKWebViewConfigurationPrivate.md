# ``WKInternalsNotes/WKWebViewConfiguration/_mainContentUserGestureOverrideEnabled``

main content の user gesture override

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setMainContentUserGestureOverrideEnabled:) BOOL _mainContentUserGestureOverrideEnabled WK_API_AVAILABLE(macos(10.12), ios(10.0));
```

## Default Value
iOS: `NO` / macOS: `NO`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_mainContentUserGestureOverrideEnabled = YES`: main content の user gesture override。
- `_mainContentUserGestureOverrideEnabled = NO`: main content の user gesture override（無効）。

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L83`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L83)
- [`Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L1199`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L1199)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
