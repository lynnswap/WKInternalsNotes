# ``WKInternalsNotes/WKContentView/_webViewDestroyed()``

`WKWebView` の破棄に伴う後処理を行う。

## Objective-C Declaration
```objective-c
- (void)_webViewDestroyed;
```

## Discussion
保持している `_webView` を `nil` にする。

## References
- [`WKContentView.h#L92`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentView.h#L92)
- [`WKContentView.mm#L878`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentView.mm#L878)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
