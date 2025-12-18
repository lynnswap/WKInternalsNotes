# ``WKInternalsNotes/WKURLSchemeTaskPrivate/_requestOnlyIfCached``

このタスクがキャッシュのみで応答すべきかを示す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) BOOL _requestOnlyIfCached WK_API_AVAILABLE(macos(10.15), ios(13.0));
```

## Default Value
リクエストの `cachePolicy` が `NSURLRequestReturnCacheDataDontLoad` の場合は `YES`、それ以外は `NO`。

## Discussion
`nsRequest().cachePolicy` を確認して算出する。

## References
- [`WKURLSchemeTaskPrivate.h#L49`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKURLSchemeTaskPrivate.h#L49)
- [`WKURLSchemeTask.mm#L101`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKURLSchemeTask.mm#L101)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
