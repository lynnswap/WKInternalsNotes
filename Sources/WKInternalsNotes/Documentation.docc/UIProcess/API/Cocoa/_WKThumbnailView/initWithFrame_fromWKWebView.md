# ``WKInternalsNotes/_WKThumbnailView/initWithFrame(_:fromWKWebView:)``

WKWebView を元にサムネイル表示を初期化する。

## Objective-C Declaration
```objective-c
- (instancetype)initWithFrame:(NSRect)frame fromWKWebView:(WKWebView *)webView;
```

## Discussion
`initWithFrame:` で初期化したあと `WKWebView` を保持し、`_page` から `WebPageProxy` を取得する。元の `mayStartMediaWhenInWindow` と、元ビューがウィンドウ内かどうかを記録する。

## References
- [`_WKThumbnailView.h#L42`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKThumbnailView.h#L42)
- [`_WKThumbnailView.mm#L97`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKThumbnailView.mm#L97)
- [`_WKThumbnailView.mm#L102`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKThumbnailView.mm#L102)
- [`_WKThumbnailView.mm#L104`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKThumbnailView.mm#L104)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
