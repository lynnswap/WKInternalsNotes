# ``WKInternalsNotes/WKNavigationAction/_shouldOpenAppLinks``

App Links を開くべきかどうかを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) BOOL _shouldOpenAppLinks WK_API_AVAILABLE(macos(10.11), ios(9.0));
```

## Default Value
`_navigationAction->shouldOpenAppLinks()` の結果。

## Discussion
API::NavigationAction の `shouldOpenAppLinks()` を返す。

## References
- [`WKNavigationActionPrivate.h#L48`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKNavigationActionPrivate.h#L48)
- [`WKNavigationAction.mm#L202`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKNavigationAction.mm#L202)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
