# ``WKInternalsNotes/WKWebView/_canUseCredentialStorage``

`_canUseCredentialStorage` の値を取得/設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setCanUseCredentialStorage:) BOOL _canUseCredentialStorage WK_API_AVAILABLE(macos(12.0), ios(15.0));
```

## Discussion
getter/setter を通じて値を取得/設定する。 setter は `_setCanUseCredentialStorage:`。

## References
- [`WKWebViewPrivate.h#L466`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L466)
- [`WKWebView.mm#L5767`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L5767)
- [`WKWebView.mm#L5767`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L5767)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
