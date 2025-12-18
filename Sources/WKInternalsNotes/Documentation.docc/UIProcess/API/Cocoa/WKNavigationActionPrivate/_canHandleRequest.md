# ``WKInternalsNotes/WKNavigationAction/_canHandleRequest``

WebKit がリクエストを処理可能かどうかを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) BOOL _canHandleRequest;
```

## Default Value
`_navigationAction->canHandleRequest()` の結果。

## Discussion
API::NavigationAction の `canHandleRequest()` を返す。

## References
- [`WKNavigationActionPrivate.h#L46`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKNavigationActionPrivate.h#L46)
- [`WKNavigationAction.mm#L192`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKNavigationAction.mm#L192)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
