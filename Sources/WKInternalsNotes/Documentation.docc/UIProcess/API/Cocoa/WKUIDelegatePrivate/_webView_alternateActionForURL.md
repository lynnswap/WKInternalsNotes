# ``WKInternalsNotes/WKUIDelegatePrivate/_webView(_:alternateActionForURL:)``

URL に対する代替アクション通知用の delegate フック（UIProcess 内の呼び出しは見当たらない）。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView alternateActionForURL:(NSURL *)url WK_API_AVAILABLE(ios(10.0));
```

## Discussion
UIProcess 配下の `.m/.mm` では呼び出しが見当たらず、宣言のみ確認できる。

## References
- [`WKUIDelegatePrivate.h#L237`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L237)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
