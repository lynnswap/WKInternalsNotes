# ``WKInternalsNotes/WKWebViewConfiguration/_invisibleAutoplayNotPermitted``

“見えない autoplay” を禁止

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setInvisibleAutoplayNotPermitted:) BOOL _invisibleAutoplayNotPermitted WK_API_AVAILABLE(macos(10.12), ios(10.0));
```

## Default Value
iOS: `NO` / macOS: `NO`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_invisibleAutoplayNotPermitted = YES`: “見えない autoplay” を禁止。
- `_invisibleAutoplayNotPermitted = NO`: “見えない autoplay” を禁止（無効）。

## Details
- 内部名は `invisibleAutoplayForbidden`

## References
- [`WKWebViewConfigurationPrivate.h#L84`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L84)
- [`WKWebViewConfiguration.mm#L997`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L997)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
