# ``WKInternalsNotes/WKNavigationResponse/_wasPrivateRelayed``

Private Relay 経由かどうかを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) BOOL _wasPrivateRelayed WK_API_AVAILABLE(macos(15.4), ios(18.4), visionos(2.4));
```

## Default Value
`_navigationResponse->response().wasPrivateRelayed()` の結果。

## Discussion
ResourceResponse の `wasPrivateRelayed()` をそのまま返す。

## References
- [`WKNavigationResponsePrivate.h#L36`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKNavigationResponsePrivate.h#L36)
- [`WKNavigationResponse.mm#L105`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKNavigationResponse.mm#L105)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
