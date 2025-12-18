# ``WKInternalsNotes/WKNavigationAction/_shouldOpenExternalSchemes``

外部スキームを開くべきかどうかを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) BOOL _shouldOpenExternalSchemes WK_API_AVAILABLE(macos(10.11), ios(9.0));
```

## Default Value
`_navigationAction->shouldOpenExternalSchemes()` の結果。

## Discussion
API::NavigationAction の `shouldOpenExternalSchemes()` を返す。

## References
- [`WKNavigationActionPrivate.h#L47`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKNavigationActionPrivate.h#L47)
- [`WKNavigationAction.mm#L197`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKNavigationAction.mm#L197)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
