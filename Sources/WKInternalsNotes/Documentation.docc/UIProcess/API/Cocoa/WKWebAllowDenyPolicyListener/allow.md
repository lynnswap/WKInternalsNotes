# ``WKInternalsNotes/WKWebAllowDenyPolicyListener/allow()``

許可としてコールバックを完了する。

## Objective-C Declaration
```objective-c
- (void)allow;
```

## Discussion
内部の完了ハンドラに `true` を渡して呼び出す。

## References
- [`WKWebGeolocationPolicyDecider.h#L35`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKWebGeolocationPolicyDecider.h#L35)
- [`WKGeolocationProviderIOS.mm#L257`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKGeolocationProviderIOS.mm#L257)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
