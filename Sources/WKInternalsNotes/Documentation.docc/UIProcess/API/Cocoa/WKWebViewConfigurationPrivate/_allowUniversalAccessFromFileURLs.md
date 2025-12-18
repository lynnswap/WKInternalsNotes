# ``WKInternalsNotes/WKWebViewConfiguration/_allowUniversalAccessFromFileURLs``

`file://` からのユニバーサルアクセスを許可

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setAllowUniversalAccessFromFileURLs:) BOOL _allowUniversalAccessFromFileURLs WK_API_AVAILABLE(macos(10.12), ios(10.0));
```

## Default Value
iOS: `NO` / macOS: `NO`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_allowUniversalAccessFromFileURLs = YES`: `file://` からのユニバーサルアクセスを許可。
- `_allowUniversalAccessFromFileURLs = NO`: `file://` からのユニバーサルアクセスを許可（無効）。

## References
- [`WKWebViewConfigurationPrivate.h#L80`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L80)
- [`WKWebViewConfiguration.mm#L339`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L339)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
