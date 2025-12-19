# ``WKInternalsNotes/WKWebViewConfiguration/_isValidCustomScheme(_:)``

カスタム URL スキームの妥当性を判定

## Objective-C Declaration
```objective-c
+ (BOOL)_isValidCustomScheme:(NSString *)urlScheme;
```

## Discussion
- `WKWebView` が扱うスキームは `NO`。
- スキームの canonicalize が失敗した場合は `NO`。
- それ以外は `YES`。

## References
- [`WKWebViewConfigurationInternal.h#L66`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationInternal.h#L66)
- [`WKWebViewConfiguration.mm#L593`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L593)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
