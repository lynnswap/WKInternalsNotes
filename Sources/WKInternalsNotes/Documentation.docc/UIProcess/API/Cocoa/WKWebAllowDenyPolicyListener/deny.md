# ``WKInternalsNotes/WKWebAllowDenyPolicyListener/deny()``

拒否としてコールバックを完了する。

## Objective-C Declaration
```objective-c
- (void)deny;
```

## Discussion
内部の完了ハンドラに `false` を渡して呼び出す。

## References
- [`WKWebGeolocationPolicyDecider.h#L36`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKWebGeolocationPolicyDecider.h#L36)
- [`WKGeolocationProviderIOS.mm#L262`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKGeolocationProviderIOS.mm#L262)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
