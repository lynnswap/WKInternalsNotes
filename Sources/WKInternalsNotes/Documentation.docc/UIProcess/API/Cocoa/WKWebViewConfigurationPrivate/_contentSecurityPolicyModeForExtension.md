# ``WKInternalsNotes/WKWebViewConfiguration/_contentSecurityPolicyModeForExtension``

Web Extension 向け CSP モード

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setContentSecurityPolicyModeForExtension:) _WKContentSecurityPolicyModeForExtension _contentSecurityPolicyModeForExtension WK_API_AVAILABLE(macos(13.0), ios(16.0));
```

## Default Value
iOS: `_WKContentSecurityPolicyModeForExtensionNone` / macOS: `_WKContentSecurityPolicyModeForExtensionNone`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- 値を変更すると: Web Extension 向け CSP モードのモード/値として、その enum 値が使われる。

## References
- [`WKWebViewConfigurationPrivate.h#L170`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L170)
- [`WKWebViewConfiguration.mm#L1550`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L1550)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
