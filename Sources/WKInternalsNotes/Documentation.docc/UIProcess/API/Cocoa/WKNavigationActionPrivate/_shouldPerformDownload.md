# ``WKInternalsNotes/WKNavigationAction/_shouldPerformDownload``

ダウンロードを実行すべきかどうかを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) BOOL _shouldPerformDownload WK_API_DEPRECATED_WITH_REPLACEMENT("downloadAttribute", macos(10.15, 12.0), ios(13.0, 15.0));
```

## Default Value
`_navigationAction->shouldPerformDownload()` の結果。

## Discussion
API::NavigationAction の `shouldPerformDownload()` を返す。

## References
- [`WKNavigationActionPrivate.h#L49`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKNavigationActionPrivate.h#L49)
- [`WKNavigationAction.mm#L207`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKNavigationAction.mm#L207)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
