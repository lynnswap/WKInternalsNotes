# ``WKInternalsNotes/WKNavigationDelegatePrivate/_webView(_:didBlockInsecurePluginVersionWithInfo:)``

安全でないプラグインバージョンのブロックを通知する。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView didBlockInsecurePluginVersionWithInfo:(NSDictionary *)info WK_API_AVAILABLE(macos(10.14));
```

## Discussion
WKNavigationDelegatePrivate で宣言されているが、UIProcess 内の呼び出しは現行ソースでは見当たらない。

## References
- [`WKNavigationDelegatePrivate.h#L99`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKNavigationDelegatePrivate.h#L99)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
