# ``WKInternalsNotes/WKUIDelegatePrivate/_webView(_:includeSensitiveMediaDeviceDetails:)``

センシティブなメディアデバイス情報を含めるかを delegate に問い合わせる。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView includeSensitiveMediaDeviceDetails:(void (^)(BOOL includeSensitiveDetails))decisionHandler WK_API_AVAILABLE(macos(10.15), ios(13.0));
```

## Discussion
ヘッダのコメントに「この delegate はもはや呼ばれない」とある通り、UIProcess 内に呼び出しが存在しない。

## References
- [`WKUIDelegatePrivate.h#L171`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L171)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
