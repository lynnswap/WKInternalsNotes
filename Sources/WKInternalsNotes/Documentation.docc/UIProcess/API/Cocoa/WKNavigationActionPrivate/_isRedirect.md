# ``WKInternalsNotes/WKNavigationAction/_isRedirect``

リダイレクトかどうかを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) BOOL _isRedirect WK_API_AVAILABLE(macos(10.13), ios(11.0));
```

## Default Value
`_navigationAction->isRedirect()` の結果。

## Discussion
API::NavigationAction の `isRedirect()` を返す。

## References
- [`WKNavigationActionPrivate.h#L62`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKNavigationActionPrivate.h#L62)
- [`WKNavigationAction.mm#L232`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKNavigationAction.mm#L232)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
