# ``WKInternalsNotes/WKNavigationResponse/_isFromNetwork``

ネットワーク由来のレスポンスかどうかを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) BOOL _isFromNetwork WK_API_AVAILABLE(macos(15.4), ios(18.4), visionos(2.4));
```

## Default Value
`response().source() == WebCore::ResourceResponseBase::Source::Network` の結果。

## Discussion
ResourceResponse の source が Network かどうかを判定して返す。

## References
- [`WKNavigationResponsePrivate.h#L38`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKNavigationResponsePrivate.h#L38)
- [`WKNavigationResponse.mm#L115`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKNavigationResponse.mm#L115)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
