# ``WKInternalsNotes/WKWebViewConfiguration/_allowsJavaScriptMarkup``

JavaScript 由来の markup を許可

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setAllowsJavaScriptMarkup:) BOOL _allowsJavaScriptMarkup WK_API_AVAILABLE(macos(10.12), ios(10.0));
```

## Default Value
iOS: `YES` / macOS: `YES`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_allowsJavaScriptMarkup = YES`: JavaScript 由来の markup を許可。
- `_allowsJavaScriptMarkup = NO`: JavaScript 由来の markup を許可（無効）。

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L77`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L77)
- [`Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L755`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L755)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
