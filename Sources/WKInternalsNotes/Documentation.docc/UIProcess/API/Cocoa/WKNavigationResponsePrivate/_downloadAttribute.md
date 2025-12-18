# ``WKInternalsNotes/WKNavigationResponse/_downloadAttribute``

download 属性の値を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) NSString *_downloadAttribute WK_API_AVAILABLE(macos(10.15), ios(13.0));
```

## Default Value
`_navigationResponse->downloadAttribute()` を `NSString` 化した値（null の場合は nil）。

## Discussion
download 属性が null の場合は `nil`、それ以外は `NSString` に変換して返す。

## References
- [`WKNavigationResponsePrivate.h#L35`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKNavigationResponsePrivate.h#L35)
- [`WKNavigationResponse.mm#L99`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKNavigationResponse.mm#L99)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
