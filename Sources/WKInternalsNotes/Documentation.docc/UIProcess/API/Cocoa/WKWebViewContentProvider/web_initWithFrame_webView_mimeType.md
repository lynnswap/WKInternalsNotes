# ``WKInternalsNotes/WKWebViewContentProvider/web_initWithFrame(_:webView:mimeType:)``

コンテンツプロバイダ用ビューを初期化する。

## Objective-C Declaration
```objective-c
- (instancetype)web_initWithFrame:(CGRect)frame webView:(WKWebView *)webView mimeType:(NSString *)mimeType;
```

## Discussion
`WKUSDPreviewView` では背景色を設定し、`webView` と `mimeType` を保持した上で `scrollView` の最小/最大ズームを 1 に固定する。

## References
- [`WKWebViewContentProvider.h#L41`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/WKWebViewContentProvider.h#L41)
- [`WKUSDPreviewView.mm#L73`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKUSDPreviewView.mm#L73)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
