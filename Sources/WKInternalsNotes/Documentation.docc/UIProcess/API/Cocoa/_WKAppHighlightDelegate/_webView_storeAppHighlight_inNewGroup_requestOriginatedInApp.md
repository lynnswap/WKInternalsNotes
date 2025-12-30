# ``WKInternalsNotes/_WKAppHighlightDelegate/_webView(_:storeAppHighlight:inNewGroup:requestOriginatedInApp:)``

アプリハイライトの保存を通知する。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView storeAppHighlight:(_WKAppHighlight *)highlight inNewGroup:(BOOL)inNewGroup requestOriginatedInApp:(BOOL)requestOriginatedInApp WK_API_AVAILABLE(macos(12.0), ios(15.0));
```

## Discussion
`WKWebView` の `_storeAppHighlight:` から呼ばれる。`_WKAppHighlight` を生成し、`inNewGroup` と `requestOriginatedInApp` を `WebCore::AppHighlight` のフラグから変換して渡す。

## References
- [`_WKAppHighlightDelegate.h#L34`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAppHighlightDelegate.h#L34)
- [`WKWebView.mm#L2134`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L2134)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
